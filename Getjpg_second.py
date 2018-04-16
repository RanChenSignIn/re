#coding:utf-8
import re
import urllib
import sys
import os

# reload(sys)

def getHtml(url):  #定义一个函数，传递网址
    page = urllib.urlopen(url) #打开一个URL地址
    html = page.read()          #读取URL上的数据#
    return html

def getImg(html,x):
    reg=r'src="(http://img.*?\.jpg)"pic_ext'
    imgre=re.compile(reg)
    imList=re.finditer(reg,html)

    print(imList)
    for i in imList:
        print(i)
        # print x
        urllib.urlretrieve(i,'%s.jpg'%x) #下载地址为i的图片，并用x.jpg命名
        x+=1
    return x


if os.path.exists("F:/images_second") == False:
    os.mkdir("F:/images_second")


x=1
url="http://tieba.baidu.com/p/3466236659?pn=5"
for k in range(1,28):
    ul=url+str(k)
    # print ul
    html = getHtml(ul)
    #print html
    x=getImg(html,x)