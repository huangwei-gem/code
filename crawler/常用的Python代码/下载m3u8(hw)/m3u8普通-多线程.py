import requests
import os
import threading


class Downloader(threading.Thread):
    def __init__(self, url, ts_url, file_path):
        threading.Thread.__init__(self)
        self.url = url
        self.ts_url = ts_url
        self.file_path = file_path

    def run(self):
        r = requests.get(self.ts_url, stream=True)
        if r.status_code == 200:
            with open(self.file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)


def download_m3u8_video(url, file_path):
    r = requests.get(url)
    if r.status_code != 200:
        print('m3u8视频下载链接无效')
        return False

    m3u8_list = r.text.split('\n')
    m3u8_list = [i for i in m3u8_list if i and i[0] != '#']

    ts_list = []
    for ts_url in m3u8_list:
        ts_url = url.rsplit('/', 1)[0] + '/' + ts_url
        ts_list.append(ts_url)

    threads = []
    for i, ts_url in enumerate(ts_list):
        ts_file_path = file_path.rsplit('.', 1)[0] + f'_{i}.ts'
        thread = Downloader(url, ts_url, ts_file_path)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print('m3u8视频下载完成')
    return True


def convert_ts_to_mp4(ts_file_path, mp4_file_path):
    os.system(f'ffmpeg -i {ts_file_path} -c copy {mp4_file_path}')


if __name__ == '__main__':
    url = '输入m3u8流媒体播放列表文件下载链接'
    ts_file_path = '输入ts文件保存路径'
    mp4_file_path = '输入mp4文件保存路径'

    download_m3u8_video(url, ts_file_path)
    convert_ts_to_mp4(ts_file_path, mp4_file_path)