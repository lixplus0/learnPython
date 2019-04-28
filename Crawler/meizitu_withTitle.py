# coding=utf-8
import os
import requests
import bs4
from bs4 import BeautifulSoup
import re

# 以标题来命名
# 按月收藏
# 给请求指定一个请求头来模拟chrome浏览器
global headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}

global html_codes
html_codes = 'utf8'

# 创建文件夹
def createFile(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    os.chdir(file_path)

def res_solve(page):
# 获取经过BS4处理后的网页
    global headers
    global html_codes
    try:
        res_sub = requests.get(page, headers=headers)
        res_sub.encoding = html_codes
        soup_sub = BeautifulSoup(res_sub.text, 'html.parser')
        return soup_sub
    except:
        return None

def download_pics(img, file_name):
# 保存图片
    if not os.path.exists(file_name):
        try:
            f = open(file_name, 'ab')
            f.write(img.content)
            f.close()
        except:
            print('图片保存出错')
    # else:
    #     print('skip ' + file_name)

# 下载文件
def downloadFile(href, fileTitle,count):
    global headers

    # print('套图地址：' + href)
    soup_sub_1 = res_solve(href)

    try:
        # 获取套图的最大数量
        pic_max = soup_sub_1.find('div', class_='pagenavi').find_all('span')[-2].text

        # 获取文件名相关数据
        pic_meta = soup_sub_1.find('div', class_='main-meta')
        pic_pubdate = pic_meta.find_all('span')[1].text.split(' ')[1].split('-')[2]

        print("当前下载第 %s 组套图，共有 %s 张。\n" % (count, pic_max))

        for j in range(1, int(pic_max)+1):
            href_sub = href + '/' + str(j)
            soup_sub_2 = res_solve(href_sub)
            img = soup_sub_2.find('div', class_='main-image').find('img')
            if isinstance(img, bs4.element.Tag):
                # 提取src
                url = img.attrs['src']

                # 定义文件名
                array = url.split('.')
                file_name = pic_pubdate + '日_' + fileTitle + '_' + format(str(j), '0>2s') + '.' + array[len(array)-1]

                # 防盗链加入Referer
                headers = {'Referer': href}
                img = requests.get(url, headers=headers)

            # 调用下载函数
            download_pics(img, file_name)

    except Exception as e:
        print(e)
       
class BreakAll(Exception):
    pass

if __name__ == "__main__":
    # 爬图地址
    mziTulist = ['https://www.mzitu.com/all/', 'https://www.mzitu.com/old/']

    # 最新的有多少期？
    new_pics = 77
    # 定义存储位置
    save_path = 'D:\\MyFiles\\Downloads\\Pictures\\mzitu'
    createFile(save_path)
    try:
        for mziTu in mziTulist:
            res = requests.get(mziTu, headers=headers)
            # 使用自带的html.parser解析
            soup = BeautifulSoup(res.text, 'html.parser')
            soup = soup.find('div', class_='all')
            all_years = soup.find_all('div', class_='year')
            all_archives = soup.find_all('ul', class_='archives')
            count = 0
            for i in range(0, len(all_years)):
                year = all_years[i].text
                print('\n' + year)
                all_months = all_archives[i].find_all('li')
                for m in range(0, len(all_months)):
                    month = all_months[m].find('p', class_='month').find('em').text
                    print(month)
                    YMfolder = year + month
                    createFile(save_path + '\\' + YMfolder)
                    all_a = all_months[m].find_all('a', target='_blank')
                    for a in all_a:
                        if new_pics == 0:
                            raise BreakAll
                        count += 1
                        # # 断点
                        # if count < 75:
                        #     continue
                        href = a.attrs['href']
                        fileTitle = re.sub('[\/:*?"<>|]', ' ', a.text)
                        # print(fileTitle)
                        downloadFile(href, fileTitle, count)
                        new_pics -= 1
    except BreakAll:
        pass