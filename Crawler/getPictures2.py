# -*- coding:utf-8 -*-
from urllib import request
import re
import os


def get_html(url):
    page = request.urlopen(url)
    html_code = page.read().decode("gbk")
    return html_code
    # page_file = open('D:\\1.txt','w',encoding='utf-8')
    # page_file.write(html_code)
    # page_file.close()


def get_Filesurl(html):
    # filere = re.compile(r'gdp.alicdn.com.*?jpg')
    filere = re.compile(r'img.alicdn.com/bao/uploaded/.*?jpg')
    filelist = filere.findall(html)
    return filelist


def downFile(url, dirnum):
    dirpath = r"D:\\MyFiles\Downloads\\Pictures\\Pic%s\\" % (dirnum)
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
    html = url
    filelist = get_Filesurl(html)
    filenum = 1
    for fileurl in filelist:
        path = dirpath + r"%s.jpg" % (filenum)
        request.urlretrieve("https://"+fileurl, path)
        filenum += 1


f = open('D:\\url.txt', 'r', encoding='utf-8')
url = f.read()
f.close()
dirnum = 10
downFile(url, dirnum)
