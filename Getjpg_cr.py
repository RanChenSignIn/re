#coding:utf-8
import re
import urllib.request
import os

def getHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    return html

def getImg(html):
    imglist = re.findall('img class="BDE_Image" src="(http.*?)"', html)
    return imglist


url_all="http://tieba.baidu.com/p/4244241086?pn="

if os.path.exists("F:/images_cr_zhaolilying") == False:
    os.mkdir("F:/images_cr_zhaolilying")
count = 0
for k in range(1,10):
    url=url_all+str(k)
    html = getHtml(url)#.decode("utf-8")
    imagesUrl = getImg(html)

    for url in imagesUrl:
        print(url)
        if (url.find('.') == 1):
            name = url[url.find('.', len(url) - 5):]#图片的后缀，
            url_sigle = urllib.request.urlopen(url)
            f = open("F:/images_cr_zhaolilying/" + str(count)+name, 'wb')#将读的图片写进文件里面，
            f.write(url_sigle.read())
            f.flush()#刷新内部缓冲区
            f.close()#
            count += 1