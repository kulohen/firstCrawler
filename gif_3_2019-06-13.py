import requests
from bs4 import BeautifulSoup
import os
import time
import _thread
import threading
import saveFile

time_1=time.time()

countThread=0 #设置在运行的线程数，计数
TotalThread=16 #设置总数8个线程


def threadCraw(i, countThread):
    countThread += 1

    cur_url = url + str(i) + '.html'
    cur_page = requests.get(cur_url, header)

    soap = BeautifulSoup(cur_page.text, "html.parser")

    try:
        pic_src = soap.find('div', 'listgif-giftu content_pic').find('img')['src']
        pic_name = pic_src.split('/')[-1]
        #svf = saveFile.
        saveFile.saveIMG(pic_name, requests.get(pic_src, headers=header).content)
        print(str(i) + ' download!')
    except Exception:
        print(str(i) + ' fail!')

    countThread -= 1


class MyThread(threading.Thread):

    def __init__(self, i,countThread):
        threading.Thread.__init__(self)
        self.i = i
        self.countThread = countThread

    def run(self):
        threadCraw(self.i,self.countThread)

# 爬取目标
url = 'http://www.gaoxiaogif.com/meinvgif/'
# 这个网站从10编号开始

parser = 'html.parser'
cur_path = os.getcwd() + '/download'+'/'+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
if os.path.exists(cur_path):
    print('directory exist!')
else:
    os.mkdir(cur_path)


header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'}
# 爬取的预览页面数量
#这个网站从10编号开始
init_page = 1111
preview_page_cnt = 1133

# main_page= requests.get(url,headers=header)
main_page= requests.get(url)
# print(main_page.text)

os.chdir(cur_path)  # 进入目录，开始下载



# 开始写
threads = []

for i in range(init_page,preview_page_cnt):

    t1= MyThread(i,countThread)
    t1.start()
    threads.append(t1)
    #print(i)

for t in threads:
    t.join()

os.chdir(cur_path)  # 完成下载，退出目录
print('耗时 '+str(time.time()-time_1)+'秒')