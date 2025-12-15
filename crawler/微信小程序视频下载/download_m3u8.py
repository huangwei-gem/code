import os,shutil,time,requests
from Crypto.Cipher import AES
from fake_useragent import UserAgent
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
import urllib3

# 禁用 InsecureRequestWarning 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

video_download_path = './m3u8Download'
save_mp4_path = './m3u8Download/testVideo'
save_temporary_ts_path = './m3u8Download/temporary_ts'

# 确保所有必需的目录都存在
os.makedirs(video_download_path, exist_ok=True)
os.makedirs(save_mp4_path, exist_ok=True)
os.makedirs(save_temporary_ts_path, exist_ok=True)

# 定义一个确保目录存在的函数
def ensure_directories():
    """确保所有必需的目录都存在"""
    os.makedirs(video_download_path, exist_ok=True)
    os.makedirs(save_mp4_path, exist_ok=True)
    os.makedirs(save_temporary_ts_path, exist_ok=True)

#先定义一个发送请求方法，方便后面的重复调用
def send_request(url):
    headers = {
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Origin': 'https://appryrtssf74394.h5.xet.citv.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://appryrtssf74394.h5.xet.citv.cn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
        'accept': '*/*, application/vnd.t1c.int-18393',
        'accept-language': 'zh-CN,zh;q=0.9',
        'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    try:
        # 添加verify=False以避免SSL证书问题，实际生产环境中应谨慎使用
        response = requests.get(url=url, headers=headers, timeout=30, verify=False)
        if response.status_code == 200:
            return response
        else:
            print(f'响应异常！状态码: {response.status_code}')
            return None
    except Exception as e:
        print('链接请求异常！！！')
        print(e)
        return None
#这里先发送m3u8链接请求，得到返回的响应数据
def get_m3u8_response_data(m3u8_url):
    response = send_request(m3u8_url)
    if response:
        return response.text
    else:
        raise Exception("无法获取m3u8数据")

#然后对得到的m3u8数据进行解析，得到每一个ts_url链接，和视频的时长，有加密则提取出
def parse_m3u8_data(m3u8_url):
    m3u8_data = get_m3u8_response_data(m3u8_url)
    each_line_list = m3u8_data.strip('\n').split('\n') #对m3u8里面的内容提取出每一行数据
    all_ts_list = []
    video_time = []
    AES_decode_data = None
    base_url = '/'.join(m3u8_url.split('/')[:-1]) + '/'
    
    if '#EXTM3U' in m3u8_data:  # 修改判断条件，检查整个数据而不是列表
        for i in range(len(each_line_list)):
            line = each_line_list[i]
            if '#EXT-X-KEY' in line: #判断是否加密
                encryption_method,key_url, iv = parse_AES_encryption(line)
                print('加密方法：',encryption_method)
                # 处理相对路径和绝对路径
                if not key_url.startswith('http'):
                    key_url = urljoin(base_url, key_url)
                AES_decode_data = AES_decode(key_url,iv)
            # 检查是否是.ts片段行
            if not line.startswith('#') and (line.endswith('.ts') or '.ts?' in line):
                # 处理相对路径和绝对路径
                if line.startswith('http'):
                    each_ts_url = line
                else:
                    each_ts_url = urljoin(base_url, line)
                all_ts_list.append(each_ts_url)
            if line.startswith('#EXTINF'):
                time_ = float(line.strip().split(':')[1][:-1])
                video_time.append(time_)
    print('视频时长约为：{:.2f}分钟'.format(sum(video_time) / 60))
    print(f'找到 {len(all_ts_list)} 个视频片段')
    return all_ts_list,AES_decode_data
#再对每一个ts_url链接发送请求（用线程池）
def get_each_ts_response_data(m3u8_url):
    print('开始下载视频……')
    all_ts_list,AES_decode_data = parse_m3u8_data(m3u8_url)
    ###初始化一个线程池，并设置最大线程数为30
    success_count = 0
    with ThreadPoolExecutor(max_workers=10) as executor:  # 减少线程数以避免服务器压力过大
        futures = []
        for i,ts_url in enumerate(all_ts_list):
            future = executor.submit(download_ts, i, ts_url, AES_decode_data)
            futures.append(future)
        
        # 等待所有任务完成并统计成功数量
        for future in futures:
            if future.result():
                success_count += 1
                
    print(f'视频下载结束！成功下载 {success_count}/{len(all_ts_list)} 个片段')
    return success_count > 0
#下载并保存ts
def download_ts(i, ts_url, AES_decode_data):
    try:
        # 确保目录存在
        ensure_directories()
        
        response = send_request(ts_url)
        if response is None:
            print(f'{i}.ts下载失败！')
            return False
            
        ts_data = response.content
        if AES_decode_data:
            ts_data = AES_decode_data.decrypt(ts_data)
            
        with open(f'{save_temporary_ts_path}/{i}.ts', mode='wb+') as f:
            f.write(ts_data)
            # print(f'{i}.ts下载完成！')
        return True
    except Exception as e:
        print(f'{i}.ts下载出现异常：{e}')
        return False
#解析加密内容
def parse_AES_encryption(key_content):
    if 'IV' in key_content or 'iv' in key_content:
        parse_result = key_content.split('=')
        # 获取加密方法
        encryption_method = parse_result[1].split(',')[0]
        parts = key_content.split(',')
        # 获取密钥链接
        uri_part = [part for part in parts if 'URI=' in part][0]
        key_url = uri_part.split('"')[1]
        # 获取 IV 值
        iv_part = [part for part in parts if 'IV=' in part]
        iv_hex = iv_part[0].split('=')[1]  # 获取 IV 的十六进制值
        # 移除 "0x" 前缀
        iv_value = iv_hex[2:] if iv_hex.startswith('0x') else iv_hex
    else:
        parse_result = key_content.split('=')
        encryption_method = parse_result[1].split(',')[0]
        key_url = parse_result[2].split('"')[1]
        iv_value = None
    return encryption_method, key_url, iv_value

#AES解密
def AES_decode(key_url,iv):
    print("key_url：", key_url)
    print("iv：",iv)
    response = send_request(key_url)
    if response is None:
        raise Exception("无法获取解密密钥")
        
    key = response.content
    # 处理 IV
    if iv:
        # 如果 IV 是十六进制字符串，转换为字节
        if isinstance(iv, str):
            # 移除可能的 "0x" 前缀
            if iv.startswith('0x'):
                iv = iv[2:]
            # 将十六进制字符串转换为字节
            iv_bytes = bytes.fromhex(iv)
        else:
            iv_bytes = iv
        AES_decode_data = AES.new(key, AES.MODE_CBC, iv_bytes)
    else:
        # 默认 IV 设置为16个字节的零
        AES_decode_data = AES.new(key, AES.MODE_CBC, bytes(16))
    return AES_decode_data
#最后合并所有的ts文件
def merge_all_ts_file(chapter_title=None):
    print('开始合并视频……')
    if not os.path.exists(save_temporary_ts_path):
        print('临时目录不存在，无法合并视频')
        return False
        
    ts_file_list = os.listdir(save_temporary_ts_path)
    if not ts_file_list:
        print('没有找到任何ts文件')
        return False
        
    ts_file_list.sort(key=lambda x: int(x.split('.')[0]))
    
    # 使用章节标题作为文件名，如果没有提供则使用默认名称
    filename = chapter_title if chapter_title else 'video'
    # 确保文件名合法，去除可能存在的非法字符
    filename = "".join(c for c in filename if c.isalnum() or c in (' ','_','-')).rstrip()
    # 保证文件名不为空
    if not filename:
        filename = 'video'
    
    with open(f'{save_mp4_path}/{filename}.mp4', 'wb+') as fw:
        for i in range(len(ts_file_list)):
            file_path = os.path.join(save_temporary_ts_path, ts_file_list[i])
            if os.path.exists(file_path):
                with open(file_path, 'rb') as fr:
                    fw.write(fr.read())
    shutil.rmtree(save_temporary_ts_path) #删除所有的ts文件
    print(f'视频合并完成！已保存为 {filename}.mp4')
    return True

def begin(m3u8_url, chapter_title=None):
    # 确保所有必需的目录都存在
    ensure_directories()
    if get_each_ts_response_data(m3u8_url):
        merge_all_ts_file(chapter_title)

def download_video(m3u8_url,chapter_title):
    start_time = time.time()
    ###m3u8_url链接自己找哈！
    # m3u8_url = 'https://v-vod-k.xiaoeknow.com/a8307e36f7a64aeeae086cc157bb356b/appryrtssf74394/video/b_u_ckscv9mps1bshnl3nsrg/lub6sbks01rr/drm/main.m3u8'
    # m3u8_url='https://v-vod-k.xiaoeknow.com/a8307e36f7a64aeeae086cc157bb356b/appryrtssf74394/video/b_u_ckscv9mps1bshnl3nsrg/lub6sbks0nj5/drm/main.m3u8?sign=490ef725d711f2cc62de7c9cafe89127&t=693dc20f&us=tHiWcPOYeE'
    begin(m3u8_url,chapter_title)
    end_time = time.time()
    print(f'总共耗时：{end_time-start_time}秒')


# if __name__ == '__main__':
#     main()