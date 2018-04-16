#coding=utf-8
import urllib
import re

def getHtml(url):  #定义一个函数，传递网址
    page = urllib.urlopen(url) #打开一个URL地址
    html = page.read()          #读取URL上的数据#
    return html


# def GetImg(html):       #建立一个函数，筛选网址数据中的目标数据，
#     reg = r'src="(.+?\.jpg)" pic_ext'    #网址数据中目标数据的，数据格式
#     imgre = re.compile(reg)             #re.compile,把正则表达式编译成一个正则表达式对象
#     imglist = re.findall(imgre, html)   #读取html 中包含 imgre（正则表达式）的数据
#     return imglist

def GetImg(html):       ##建立一个函数，筛选网址数据中的目标数据，并对目标数据进行保存
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0       #计数，遍历一个，次数加一，同时对数据重命名
    for imgurl in imglist:                              #for循环对获取图片连接进行遍历
        urllib.urlretrieve(imgurl,'%s.jpg' % x)         #直接将远程数据下载到本地，并重命名，保存的位置默认为程序的存放目录。
        x+=1
        return imglist

html = getHtml("http://tieba.baidu.com/p/5383526885?red_tag=f1563613387")

print GetImg(html)