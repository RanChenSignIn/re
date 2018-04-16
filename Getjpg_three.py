# coding=utf-8
import urllib.request
import re
import os


# Urllib 模块提供了读取web页面数据的接口，我们可以像读取本地文件一样读取www和ftp上的数据
def getHtml(url):
    page = urllib.request.urlopen(url)      #urlopen 方法用来打开一个url
    html = page.read()          #read方法 用于读取Url上的数据
    return html

def getImg(html):
    imglist = re.findall('src="(http.*?)"', html)  #.*?:三个符号可以匹配任意多个任意符号
    return imglist

html = getHtml("https://www.zhihu.com/question/34378366").decode("utf-8")
imagesUrl = getImg(html)

if os.path.exists("F:\Python_Data_Code\Re_cr_实习\Re_cr\images") == False:
    os.mkdir("F:\Python_Data_Code\Re_cr_实习\Re_cr\images")

count = 0
for url in imagesUrl:
    print(url)
    if (url.find('.') != -1):
        name = url[url.find('.', len(url) - 5):]
        bytes = urllib.request.urlopen(url)
        f = open("F:\Python_Data_Code\Re_cr_实习\Re_cr\images\\" + str(count) + name, 'wb')
        f.write(bytes.read())
        f.flush()
        f.close()
        count += 1