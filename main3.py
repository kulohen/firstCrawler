
#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

# 爬取目标
url = 'http://www.mzitu.com/page/'
# 设置报头，Http协议

parser='html.parser'

header = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'}
# 爬取的预览页面数量
preview_page_cnt = 2
for cur_page in range(1, int(preview_page_cnt)+1):
    cur_url = url + str(cur_page)
    cur_page = requests.get(cur_url, headers = header)
    # 解析网页
    soup = BeautifulSoup(cur_page.text, parser)
    # 图片入口和文字入口取一个即可
    preview_link_list = soup.find(id='pins').find_all('a', target='_blank')[1::2]
    for link in preview_link_list:
        link = link['href']
        soup = BeautifulSoup(requests.get(link).text, parser)
        # 获取图片数量
        pic_cnt = soup.find('div', class_='pagenavi').find_all('a')[4].get_text()
        # 遍历获取每页图片的地址
        for pic_index in range(1, int(pic_cnt)+1):
            pic_link = link + '/' + str(pic_index)
            cur_page = requests.get(pic_link, headers = header)
            soup = BeautifulSoup(cur_page.text, parser)
            pic_src = soup.find('div', 'main-image').find('img')['src']
            print(pic_src)