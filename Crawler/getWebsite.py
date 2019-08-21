# coding=utf-8
import os
import time
import re
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    WEBSITE = 'https://think.lenovo.com.cn/support/driver/newdriversdownlist.aspx?categoryid=3110338&CODEName=20KH&SearchType=1&wherePage=1&SearchNodeCC=&needmt=20KH'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
    html_codes = 'utf8'

    try:
        res_sub = requests.get(WEBSITE, headers=headers)
        res_sub.encoding = html_codes
        soup_sub = BeautifulSoup(res_sub.text, 'html.parser')
        print(res_sub.text)
    except:
        print('error')