import re
import asyncio
import aiohttp
import aiofiles

urlist = [f'https://music.163.com/discover/playlist/?order=hot&cat=全部&limit=35&offset={str((n-1)*35)}' for n in range(1,20)]


cookies = {
    'Qs_lvt_382223': '1726643116',
    'Qs_pv_382223': '2610020288482423000',
    '_ga': 'GA1.1.1674354346.1726643117',
    '_clck': 'f2kdag%7C2%7Cfpa%7C0%7C1722',
    '_ga_C6TGHFPQ1H': 'GS1.1.1726643116.1.1.1726643187.0.0.0',
    'NMTID': '00OOtMeceIc8KlyoEI_hL3LcdpJ0ngAAAGVKzndFg',
    '_iuqxldmzr_': '32',
    '_ntes_nnid': 'e34a15fc20b9518b86d812cb14919b19,1740186966482',
    '_ntes_nuid': 'e34a15fc20b9518b86d812cb14919b19',
    'WEVNSM': '1.0.0',
    'WNMCID': 'gwmqym.1740186966650.01.0',
    'ntes_utid': 'tid._.Hfrt%252BaWPGzRFAgARAVeEhCDhjGZvFexK._.0',
    'WM_TID': 'uWADy2Zbm%2FtERREUABeQFBrQXrd%2BA5YI',
    'sDeviceId': 'YD-SMmxvc6YwMFAEkAFQUaVPWeVtVEjGmtT',
    'JSESSIONID-WYYY': 'n8JWuml2ZCjDq7lyMMnCpZh43dD96WE90rdslc1V%2Fs5ekyPttrFr8NrFxHD1kp9u%2BFnelcI1fPosZdmH7sBmF%2B%2BnK2Y34AnnA4lfrwTACnDOQAK%5CpiYmpEny3uMM%2BGwb4UthqgkYIQU0SDPwNeySAm%2B%2BTNXqniHmR8aQKDXi%2B2%2B936%2BY%3A1740621689422',
    'WM_NI': '%2B%2BxbI%2BP1BPZPBVkB27VbMX0FHmA%2FCSOcUIl6St5z%2BWu2q6hAgkcnuSRwvZnFGGza8YxwJ0nkGreyQkoOgJi2e%2Bbksnv2Eg6NIRTJkZJJrcjmryQNFDxUflwCaKFp5yaMc0Y%3D',
    'WM_NIKE': '9ca17ae2e6ffcda170e2e6ee83c964aaaf8b86d15e8f968aa2d15f969b9a83cb47f18ea2a3c77eb0bc8db1c42af0fea7c3b92ae9f5b883cc2194ef8eb1d95c828aa5a3b13d96be83b9b34e8cb38fd0c2598dbd9baaef3e91acfb9baa5db7eebfd7eb4ba5b5ad8ff85992a9babbed4e8599b682bb53bca986d1ed6185aeab9ad461ad91a9abec3aa7f5ae8cf266b6ee8b88b5468b8e9cabea528a96be84e967b2a79fafc550bc8baa8df649a3958a91b873a393add1dc37e2a3',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'priority': 'u=0, i',
    'referer': 'https://music.163.com/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
    'cookie': 'Qs_lvt_382223=1726643116; Qs_pv_382223=2610020288482423000; _ga=GA1.1.1674354346.1726643117; _clck=f2kdag%7C2%7Cfpa%7C0%7C1722; _ga_C6TGHFPQ1H=GS1.1.1726643116.1.1.1726643187.0.0.0; NMTID=00OOtMeceIc8KlyoEI_hL3LcdpJ0ngAAAGVKzndFg; _iuqxldmzr_=32; _ntes_nnid=e34a15fc20b9518b86d812cb14919b19,1740186966482; _ntes_nuid=e34a15fc20b9518b86d812cb14919b19; WEVNSM=1.0.0; WNMCID=gwmqym.1740186966650.01.0; ntes_utid=tid._.Hfrt%252BaWPGzRFAgARAVeEhCDhjGZvFexK._.0; WM_TID=uWADy2Zbm%2FtERREUABeQFBrQXrd%2BA5YI; sDeviceId=YD-SMmxvc6YwMFAEkAFQUaVPWeVtVEjGmtT; JSESSIONID-WYYY=n8JWuml2ZCjDq7lyMMnCpZh43dD96WE90rdslc1V%2Fs5ekyPttrFr8NrFxHD1kp9u%2BFnelcI1fPosZdmH7sBmF%2B%2BnK2Y34AnnA4lfrwTACnDOQAK%5CpiYmpEny3uMM%2BGwb4UthqgkYIQU0SDPwNeySAm%2B%2BTNXqniHmR8aQKDXi%2B2%2B936%2BY%3A1740621689422; WM_NI=%2B%2BxbI%2BP1BPZPBVkB27VbMX0FHmA%2FCSOcUIl6St5z%2BWu2q6hAgkcnuSRwvZnFGGza8YxwJ0nkGreyQkoOgJi2e%2Bbksnv2Eg6NIRTJkZJJrcjmryQNFDxUflwCaKFp5yaMc0Y%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee83c964aaaf8b86d15e8f968aa2d15f969b9a83cb47f18ea2a3c77eb0bc8db1c42af0fea7c3b92ae9f5b883cc2194ef8eb1d95c828aa5a3b13d96be83b9b34e8cb38fd0c2598dbd9baaef3e91acfb9baa5db7eebfd7eb4ba5b5ad8ff85992a9babbed4e8599b682bb53bca986d1ed6185aeab9ad461ad91a9abec3aa7f5ae8cf266b6ee8b88b5468b8e9cabea528a96be84e967b2a79fafc550bc8baa8df649a3958a91b873a393add1dc37e2a3',
}

params = {
    'order': 'hot',
    'cat': '全部',
    'limit': '35',
    'offset': '35',
}



async def fetch(session,url):
    # print("发送请求::",url)
    async with session.get(url,cookies=cookies,headers=headers) as response:
        async with aiofiles.open('music_href','a') as f:
            text = await response.text()
            music_href_list = re.findall('<a title="(.*?)" href="(.*?)" class="msk',text)
            # print(len(music_href_list))
            # https://music.163.com/#/playlist?id=12937122744
            # /playlist?id=534733414
            for music_href in music_href_list:
                music_href = list(music_href)
                music_href[1] = 'https://music.163.com/#'+music_href[1]
                music_href_str = ' \\ '.join(music_href)+'\n'
                await f.write(music_href_str)

# with open('music_list','w') as f:
#     f.write(response.text)

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch(session,url)) for url in urlist]
        await asyncio.wait(tasks)


if __name__ == '__main__':
    # print(urlist)
    #href="/playlist?id=12646326771" class="msk
    # <a title="韩流教科书｜一秒沦陷宿命感极强的韩流" href="/playlist?id=13015254350" class="msk"></a>
    # music_href_list = re.findall('<a title="(.*?)" href="(.*?)" class="msk',response.text)
    # print(music_href_list)
    asyncio.run(main())