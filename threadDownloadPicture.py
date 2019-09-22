import requests
from bs4 import BeautifulSoup
import os
import time
import threading
import saveFile

time_1 = time.time()

# 设置在运行的线程数，计数
countThread = 0

# 设置总数8个线程
TotalThread = 16
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'}


def threadCraw(i, countThread):
    countThread += 1

    # 获取图片，并保存图片的代码

    countThread -= 1


class MyThread(threading.Thread):

    def __init__(self, i, countThread):
        threading.Thread.__init__(self)
        self.i = i
        self.countThread = countThread

    def run(self):
        threadCraw(self.i, self.countThread)
