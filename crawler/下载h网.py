from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import requests
import json
import urllib3
import time
import re
import os
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def sanitize_filename(filename):
    """
    清理文件名，移除Windows系统不允许的字符
    :param filename: 原始文件名
    :return: 清理后的文件名
    """
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename.strip()


def extract_chinese(filename):
    """
    从文件名中提取中文字符
    :param filename: 原始文件名
    :return: 只包含中文的文件名
    """
    import re
    chinese_pattern = re.compile(r'[\u4e00-\u9fff]+')
    chinese_chars = chinese_pattern.findall(filename)
    if chinese_chars:
        return ''.join(chinese_chars)
    return None



def aes_ecb_encrypt(plaintext: str, hex_key: str) -> str:
    """
    AES-128-ECB 加密（PKCS7填充），输出Base64编码密文
    :param plaintext: 待加密的明文（字符串）
    :param hex_key: Hex格式的密钥（128位，对应32个Hex字符）
    :return: 加密后的密文（Base64字符串）
    """
    # 1. Hex密钥转字节（128位密钥 → 16字节）
    key = bytes.fromhex(hex_key)
    # 2. 明文转字节（UTF-8编码）
    data = plaintext.encode("utf-8")
    # 3. 创建AES-ECB加密器
    cipher = AES.new(key, AES.MODE_ECB)
    # 4. PKCS7填充（块大小固定为AES块大小16字节）
    padded_data = pad(data, AES.block_size, style="pkcs7")
    # 5. 加密并返回Base64编码的密文
    ciphertext = cipher.encrypt(padded_data)
    return base64.b64encode(ciphertext).decode("utf-8")


def aes_ecb_decrypt(ciphertext_b64: str, hex_key: str) -> str:
    """
    AES-128-ECB 解密（PKCS7填充），输入Base64编码密文
    :param ciphertext_b64: 待解密的密文（Base64字符串）
    :param hex_key: Hex格式的密钥（128位，对应32个Hex字符）
    :return: 解密后的明文（字符串）
    """
    # 1. Hex密钥转字节
    key = bytes.fromhex(hex_key)
    # 2. Base64密文转字节
    ciphertext = base64.b64decode(ciphertext_b64)
    # 3. 创建AES-ECB解密器
    cipher = AES.new(key, AES.MODE_ECB)
    # 4. 解密得到带填充的明文
    padded_plaintext = cipher.decrypt(ciphertext)
    # 5. 移除PKCS7填充并转字符串
    plaintext = unpad(padded_plaintext, AES.block_size, style="pkcs7")
    return plaintext.decode("utf-8")


"""
AES-128-ECB 加密（PKCS7填充），输出Base64编码密文
:param plaintext: 待加密的明文（字符串）
:param hex_key: Hex格式的密钥（128位，对应32个Hex字符）
:return: 加密后的密文（Base64字符串）
"""
# ------------------- 测试用例 -------------------
if __name__ == "__main__":
    for i in range(100):
        # 截图中的Hex密钥
        hex_key = "5a7439576a45366350624c6b51325668"
        token = '36361c19b8822f2acc88eeecf6bfb41b_6773666'
        original_str = '{"deviceId":"7f7c852f-dab2-40c2-9671-1aaa7581","token":"bbc02078c7310e25ee0b91cee7224422_4755159","data":{"page":1,"page_size":10,"position":"normal"}}'
        # 1. 把字符串解析成Python字典
        data_dict = json.loads(original_str)

        # 2. 替换token值（直接修改字典的key）
        new_token = token  # 替换成你想要的token
        data_dict["token"] = new_token
        data_dict["data"]['page'] = i

        # 4. 把修改后的字典转回JSON字符串
        new_str = json.dumps(data_dict)
        # 加密
        ciphertext = aes_ecb_encrypt(new_str, hex_key)
        print(f"加密后的密文（Hex）: {ciphertext}")


        headers = {
            'Host': 'api.82d0616f.com',
            'Connection': 'keep-alive',
            # 'Content-Length': '216',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="140", "Edge";v="140"',
            'sec-ch-ua-mobile': '?1',
            'DeviceType': 'h5',
            'Time': '2026-01-20 14:38:10',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Mobile Safari/537.36 EdgA/140.0.0.0',
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'text/plain',
            'Version': '3.0',
            'Origin': 'https://api.82d0616f.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            # 'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

        data = ciphertext

        response = requests.post('https://api.82d0616f.com/putanginamo/movie/favorite', headers=headers, data=data,verify=False)
        print(response.text)
        # 解密
        decrypted_text = aes_ecb_decrypt(response.text, hex_key)
        print(f"解密后的明文: {decrypted_text}")
        dict_data = json.loads(decrypted_text)
        id_list = []
        for item in dict_data['data']:
            id = item['id']
            id_list.append(id)
        print(id_list)
        
        failed_files = []
        
        for id in id_list:
            data = '{"deviceId":"7f7c852f-dab2-40c2-9671-1aaa7581","token":"cb89a53a88b16f247e2b8c5f15f9fd28_4755159","data":{"id":"fa7a6c7f4a80bcf6"}}'
            # 1. 把字符串解析成Python字典
            data_dict = json.loads(data)

            # 2. 替换token值（直接修改字典的key）
            new_token = token  # 替换成你想要的token
            data_dict["token"] = new_token

            # 3. 替换data里的id值（嵌套字典，先取data再改id）
            new_id = id       # 替换成你想要的id
            data_dict["data"]["id"] = new_id

            # 4. 把修改后的字典转回JSON字符串
            new_str = json.dumps(data_dict)
            data = aes_ecb_encrypt(new_str, hex_key)
            response = requests.post('https://api.82d0616f.com/putanginamo/movie/detail', headers=headers, data=data,verify=False)
            json_data = aes_ecb_decrypt(response.text, hex_key)
            json_data = json.loads(json_data)
            id = json_data['data']['id']
            name = json_data['data']['name']
            m3u8_url = json_data['data']['play_links'][0]['m3u8_url']
            print(id,name,m3u8_url)
            
            # 创建目录（如果不存在）
            os.makedirs('m3u8_fils', exist_ok=True)
            
            m3u8_text = requests.get(m3u8_url,headers=headers,verify=False).text
            
            # 尝试保存文件，处理各种文件名问题
            saved = False
            filename_attempts = [
                name,
                sanitize_filename(name),
                extract_chinese(name)
            ]
            
            for filename in filename_attempts:
                if filename:
                    try:
                        with open(f'm3u8_fils/{filename}.m3u8', 'w', encoding='utf-8') as f:
                            f.write(m3u8_text)
                        print(f"成功保存: {filename}.m3u8")
                        saved = True
                        break
                    except (FileNotFoundError, OSError) as e:
                        continue
            
            if not saved:
                print(f"保存失败: {name}")
                failed_files.append({
                    'name': name,
                    'm3u8_url': m3u8_url,
                    'error': '无法创建有效文件名'
                })
        
        # 输出失败的文件列表
        if failed_files:
            print("\n" + "="*60)
            print("以下文件保存失败:")
            for failed in failed_files:
                print(f"名称: {failed['name']}")
                print(f"链接: {failed['m3u8_url']}")
                print(f"错误: {failed['error']}")
                print("-" * 60)
        



        