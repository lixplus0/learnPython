# -*- encoding: utf-8 -*-
import os
import os.path
import shutil


#find temperature
def temp(list):             
    i = 0;                              #标记第几个char
    for char in list:
        i += 1
        if char == '\t':                #找tab标记
            break
    i0 = i                              #此处的值为tab后的第一个char
    while (list[i] != 'E'):             #找E所在char位置
        i += 1
    num = float(list[i0:i-1])           #E前面的数字
    num = num * (10 **float(list[i+2])) #加上E后面的数字
    return num                          #返回温度大小数值

#遍历所有文件
def findfile(rootdir):
    filelist = []
    for parent,dirnames,filenames in os.walk(rootdir):  #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for filename in filenames:
            filelist.append(filename) #输出文件路径信息,添加到filelist列表
    return filelist     #返回文件列表
    

dir = 'D:\\PLD\\GdYMn2O5\\Data\\Polarization_Dielectric\\未热压-重新测试' #请修改此处文件夹，末尾不可加斜杠
newdir = dir + '\\update'
if os.path.exists(newdir):
    shutil.rmtree(newdir) #删除update文件夹

filelist = findfile(dir)
os.mkdir(newdir)
n = 0
for file in filelist:
    n += 1
    f = open(dir + '\\' + file)         #打开旧文件
    f1 = open(newdir + '\\' + file,'w') #创建新文件
    try:
        fline = f.readlines()           #读取所有行并作为list
        f1.write(fline[0])
        for line in fline[1:]:  #跳过第一行
            if (temp(line) > 2.005 and temp(line) < 50.01): #选择温度保留范围
                f1.write(line)
    finally:
        f.close()
        f1.close()
        print('OK')
print('%s files have been update'%n)

