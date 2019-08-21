# coding=utf-8
import os
import time
import re
import requests
import json

class CkeckDriver():
    def __init__(self):
        self.WEBSITE = 'https://newsupport.lenovo.com.cn/api/drive/drive_listnew?searchKey=3110338&sysid=138'
        self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
        self.json_file = "driver.json"
        self.old_json_info = self.load_file()
        self.new_json_info = self.get_webinfo()
        self.flag = 0

    def get_webinfo(self):
        '''读取官网驱动信息'''
        res = requests.get(self.WEBSITE, headers=self.headers)
        return json.loads(res.content)['data']

    def load_file(self):
        '''读取json文件，否则创建一个空文件'''
        if os.path.exists(self.json_file):
            with open(self.json_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            self.write_file({})
            return {}

    def write_file(self, json_info):
        '''以覆盖的方式写入json文件'''
        with open(self.json_file, 'w', encoding='utf-8') as f:
            json.dump(json_info, f)


    def main_method(self):
        try:
            notebook_series = self.new_json_info['driverSerious'][0]['NodeCode']
            notebook_pic = self.new_json_info['driverSerious'][0]['PicturePath']
            part_list = self.new_json_info['partList']
            for i in range(0, len(part_list)):
                part_name = part_list[i]['PartName']
                drive_list = part_list[i]['drivelist']
                for j in range(0, len(drive_list)):
                    new_drive_version = drive_list[j]['Version']
                    old_drive_version = self.old_json_info['partList'][i]['drivelist'][j]['Version']
                    if old_drive_version == new_drive_version:
                        continue
                    else:
                        self.flag += 1
                        drive_name = drive_list[j]['DriverName']
                        pub_date = drive_list[j]['DriverIssuedDateTime']
                        file_path = drive_list[j]['FilePath']
                        print(drive_name + '需要更新')
            if self.flag == 0:
                print('所有驱动都不需要更新')
               
        except:
            print('error')

if __name__ == "__main__":
    check_driver = CkeckDriver()  # 创建类的实例
    check_driver.main_method()