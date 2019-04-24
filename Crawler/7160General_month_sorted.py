# coding=utf-8
import os
import time
import re
import requests
from bs4 import BeautifulSoup


class BeautifulPicture():
    def __init__(self):     # 类的初始化操作
        # 给请求指定一个请求头来模拟chrome浏览器
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
        self.catalog_min = 1    # 目录页起始页码
        self.catalog_max = 1    # 目录页结束页码
        self.order_flag = 1    # 正序1，其他数字倒序
        self.pic_website = 'https://www.7160.com'
        self.html_codes = 'gbk'    # 设置网页编码

        ticks = time.localtime()
        self.date = time.strftime("%Y", ticks) + '年' + \
            time.strftime("%m", ticks) + '月'

        self.catlog_url = ''    # 爬图地址，目录页首页
        self.catlog_nameCN = ''
        self.catlog_pre = ''
        self.save_path = ''

    def set_value(self, catlog_urlsuffix, catlog_nameCN, catlog_pre, save_path):
        self.catlog_url = self.pic_website + catlog_urlsuffix    # 爬图地址，目录页首页
        self.catlog_nameCN = catlog_nameCN
        self.catlog_pre = catlog_pre
        self.save_path = save_path    # 定义存储位置，注意末尾

    def catalogs_urlsolve(self, catalog_no):
        '''获取每个目录页的URL地址'''
        url = self.catlog_url + self.catlog_pre + str(catalog_no) + '.html'
        return url

    def find_img_from_BS(self, soup):
        '''返回soup中的img_tag'''
        return soup.find('div', class_=['picsbox', 'picsboxcenter']).find('img')

    def a_resolve(self, catalog_no):
        '''解析page的url地址，返回img的所有a的list'''
        catalog_url = self.catalogs_urlsolve(catalog_no)
        catalog_soup = self.res_solve(catalog_url)
        # 找到当前目录页每一个page内页的a,并存入all_a列表
        page_all = catalog_soup.find(
            'div', class_='news_bom-left').find_all('div', class_='new-img')
        if page_all == []:    # 7160网站里有些用ul标签
            page_all = catalog_soup.find(
                'div', class_='news_bom-left').find_all('ul', class_='new-img')
        all_a = []
        for page_cols in page_all:
            try:
                all_a += page_cols.find_all('a', target='_blank')
            except Exception as e:
                print(e)
        return all_a

    def get_imgnum(self, soup_sub):
        '''获取套图的最大数量'''
        pic_max = soup_sub.find('div', class_='itempage').find_all('a')[
            0].text.replace('共', '').replace('页: ', '')
        pic_max = int(pic_max)
        return pic_max

    def get_imgname(self, soup_sub):
        '''获取文件名相关数据'''
        pic_title = soup_sub.find('div', class_='picmainer').find('h1').text
        return pic_title

    def get_imgdate(self, soup_sub):
        '''获取该组图片的创建年月'''
        date = soup_sub.find('p', class_='pleft').find(
            'span').find('i').next.strip()
        date_list = date.split('-')
        pic_date = date_list[0] + '年' + date_list[1] + '月'
        return pic_date

    # -----------------------------------------------------------------------
    # 以下为通用方法，一般无需更改

    def create_folder(self, file_path):
        '''创建文件夹函数'''
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        os.chdir(file_path)

    def res_solve(self, page):
        '''获取经过BS4处理后的网页对象，无法获取则返回None'''
        try:
            res_sub = requests.get(page, headers=self.headers)
            res_sub.encoding = self.html_codes
            soup_sub = BeautifulSoup(res_sub.text, 'html.parser')
            return soup_sub
        except:
            return None

    def img_avoidthief(self, href, img_url):
        '''防盗链，返回图片的response'''
        headers2 = self.headers.copy()
        headers2.update({'Referer': href})
        img = requests.get(img_url, headers=headers2)
        return img

    def save_img(self, img, file_name):
        '''保存图片'''
        try:
            f = open(file_name, 'ab')
            f.write(img.content)
            f.close()
        except:
            print('图片保存出错')

    def catalog_range(self):
        '''定位搜寻目录的范围'''
        if self.order_flag == 1:
            catalog_range = range(self.catalog_min, self.catalog_max + 1)
        else:
            catalog_range = range(self.catalog_max, self.catalog_min-1, -1)
        return catalog_range

    # -----------------------------------------------------------------------
    # 以下为主方法
    def get_pic(self):
        '''获取图片的主方法'''
        self.create_folder(self.save_path)    # 创建根目录文件夹

        file_path = self.save_path + self.date
        self.create_folder(file_path)    # 创建一个当前年月的目录

        for catalog_num in self.catalog_range():

            all_a = self.a_resolve(catalog_num)    # 解析目录页的所有a，即每个page的入口a

            count = 0    # 内页的图片计数
            for a in all_a:
                print('\n\n' + self.catlog_nameCN + '，目录页第 %s 页' % catalog_num)
                count += 1

                try:
                    # page第一页，注意此处的格式，与网页代码核对
                    href = self.pic_website + a.attrs['href']

                    soup_sub_1 = self.res_solve(href)    # BS4处理后的page第一页

                    pic_date = self.get_imgdate(soup_sub_1)
                    if self.date != pic_date:
                        self.date = pic_date
                        file_path = self.save_path + self.date
                        self.create_folder(file_path)    # 创建目录

                    pic_max = self.get_imgnum(soup_sub_1)
                    pic_title = self.get_imgname(soup_sub_1)
                    print("内页第 %s 页，共 %s 张图，存放于 %s 中。" %
                          (count, pic_max, self.date))

                    # 利用第一页img的文件后缀，获取文件类型
                    img1_tag = self.find_img_from_BS(soup_sub_1)
                    img1_url = img1_tag.attrs['src']
                    file_type = '.' + img1_url.split('.')[-1]

                    for j in range(1, pic_max+1):
                        file_name = pic_title + '_' + \
                            format(str(j), '0>2s') + file_type
                        file_name = re.sub(
                            r'[\\/:*?"<>|\r\n]+', ' ', file_name)    # 去掉特殊字符
                        if not os.path.exists(file_name):
                            if j == 1:
                                img_url = img1_url
                            else:
                                # list_href = list(href)
                                # list_href.insert(-5,'_'+str(j))
                                # href_sub = ''.join(list_href)
                                href_sub = href + 'index_' + str(j) + '.html'

                                soup_sub_2 = self.res_solve(href_sub)
                                img_tag = self.find_img_from_BS(soup_sub_2)
                                img_url = img_tag.attrs['src']    # 提取src

                            img = self.img_avoidthief(href, img_url)    # 防盗链
                            print('\r正在下载...  ', end=" ")

                            self.save_img(img, file_name)    # 调用下载函数
                        else:
                            print('\r跳过文件...  ', end=" ")
                except Exception as e:
                    print(e)


if __name__ == "__main__":
    catlog_urlsuffix_list = ['/rentiyishu/', '/xingganmeinv/', '/xingganmote/', '/zhenrenxiu/']
    catlog_nameCN_list = ['人体艺术', '性感美女', '性感模特', '真人秀']
    catlog_pre_list = ['list_1_', 'list_3_', 'list_4_', 'list_11_']
    save_path_list = list(
        map(lambda x: 'D:/MyFiles/Downloads/Pictures/' + x, catlog_urlsuffix_list))

    url_max = len(catlog_urlsuffix_list)

    for j in range(0, url_max):    # 下载全部请使用range(0, url_max)
        catlog_urlsuffix = catlog_urlsuffix_list[j]
        catlog_nameCN = catlog_nameCN_list[j]
        catlog_pre = catlog_pre_list[j]
        save_path = save_path_list[j]
        PIC_CRAWER = BeautifulPicture()  # 创建类的实例
        PIC_CRAWER.set_value(
            catlog_urlsuffix, catlog_nameCN, catlog_pre, save_path)    # 设置类中的值
        PIC_CRAWER.get_pic()  # 执行类中的方法
