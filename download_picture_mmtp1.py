import os
import time
import threading
import saveFile

time_1=time.time()

countThread=0  # 设置在运行的线程数，计数
TotalThread=500  #设置线程总数
# 爬取目标
# url = 'https://mmtp1.com/fulitu/zipai/240/01.jpg'
url = 'https://mmtp1.com/fulitu/katong/'



class MyThread(threading.Thread):
    def __init__(self, i,j):
        threading.Thread.__init__(self)
        self.i = i
        self.j = j

    def run(self):
        # countThread += 1

        # i是网页编号，所以遍历去调用下载函数
        # 1、弄出每个图片的地址

        if j < 10:
            pic_tmp_name = '0' + str(j)
        else:
            pic_tmp_name = str(j)
        pic_src = url + str(i) + '/' + pic_tmp_name + '.jpg'
        pic_name = str(i) + '_' + pic_tmp_name + '.jpg'

        saveFile.get_picture(pic_src, pic_name)

        # countThread -= 1


# 创建下载的文件夹
cur_path = os.getcwd() + '/download'+'/'+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
if os.path.exists(cur_path):
    print('directory exist!')
else:
    os.mkdir(cur_path)

os.chdir(cur_path)  # 进入目录，开始下载

#这个网站从1编号开始
init_page = 1
preview_page_cnt = 300

#图片从01编号开始到99最多
init_page_2 = 1
preview_page_cnt_2 = 99

# 开始多线程
threads = []

for i in range(init_page,preview_page_cnt):
    for j in range(init_page_2 ,preview_page_cnt_2):
        # countThread += 1
        t1= MyThread(i, j)
        while len(threading.enumerate()) > TotalThread:
            time.sleep(0.1)
        t1.start()
        threads.append(t1)
        # countThread -= 1


for t in threads:
    t.join()

os.chdir(cur_path)  # 完成下载，退出目录
print('耗时 '+str(time.time()-time_1)+'秒')