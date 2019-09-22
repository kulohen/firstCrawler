# by王毅 分离保存文件的代码
import requests

header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'}


def save_img(pic_name, pic_src):
    f = open(pic_name, 'wb')
    f.write(pic_src)
    f.close()


def get_picture(pic_src, pic_name):
    try:
        # get_pic_temp = requests.get(pic_src, headers=header).content
        get_pic_temp = requests.get(pic_src, headers=header)
        if get_pic_temp.status_code == 200:
            save_img(pic_name, get_pic_temp.content)
            print(pic_name + ' download!')
#        if get_pic_temp.status_code == 404:
#            print(pic_name + ' 404!')
#        else:
#            save_img(pic_name, get_pic_temp.content)
#            print(pic_name + ' download!')

    except Exception:
        print(pic_name + ' fail!')
