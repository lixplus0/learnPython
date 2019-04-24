# coding=utf-8

import time
import os

ticks = time.localtime()
date = time.strftime("%Y",ticks) + '年' + time.strftime("%m",ticks) + '月'
print(date)
os.makedirs('D:\\1\\')