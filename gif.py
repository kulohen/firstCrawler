import requests
from bs4 import BeautifulSoup
import os
import time

time_1=time.time()

# 爬取目标
url = 'http://www.gaoxiaogif.com/meinvgif/'
# 这个网站从10编号开始

parser = 'html.parser'
cur_path = os.getcwd() + '/download'

header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'}
# 爬取的预览页面数量
#这个网站从10编号开始
init_page = 500
preview_page_cnt = 9999

# main_page= requests.get(url,headers=header)
main_page= requests.get(url)
# print(main_page.text)

os.chdir(cur_path)  # 进入目录，开始下载


# 开始写
for i in range(init_page,preview_page_cnt):

    cur_url = url+str(i)+ '.html'
    # 写上页面了。如 www.xxx.com/1234
    cur_page = requests.get(cur_url,header)
    # print(cur_page.text)
    # 现在去找图片
    soap = BeautifulSoup(cur_page.text, "html.parser")
    # p rint('下载' + dir_name + '...')
    # 遍历获取每页图片的地址
    #if soap.can_be_empty_element
    #   continue
    try:
        pic_src = soap.find('div', 'listgif-giftu content_pic').find('img')['src']
        pic_name = pic_src.split('/')[-1]
        # 文件读写部分
        f = open(pic_name, 'wb')
        f.write(requests.get(pic_src, headers=header).content)
        f.close()
        print(str(i) + ' download!')
    except Exception:
        print(str(i) + ' fail!')
        continue

os.chdir(cur_path)  # 完成下载，退出目录
print(time.time()-time_1)