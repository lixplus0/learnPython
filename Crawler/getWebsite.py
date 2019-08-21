# coding=utf-8
import os
import time
import re
import requests
import json

json_file = "./driver.json"

def load_file():
    if os.path.exists(json_file):
        with open(json_file, mode='r', encoding='utf-8') as f:
            return json.load(f)
    else:
        with open(json_file, mode='w', encoding='utf-8') as f:
            json.dump({}, f)
            return {}

def write_file(jsons):
    with open(json_file, mode='w', encoding='utf-8') as f:
        json.dump(jsons, f)


if __name__ == "__main__":
    WEBSITE = 'https://newsupport.lenovo.com.cn/api/drive/drive_listnew?searchKey=3110338&sysid=138'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
    
    try:
        res_sub = requests.get(WEBSITE, headers=headers)
        info_json = json.loads(res_sub.content)['data']
        old_info = load_file()
        print(old_info)
        # notebook_series = info_json['driverSerious'][0]['NodeCode']
        # notebook_pic = info_json['driverSerious'][0]['PicturePath']
        # part_list = info_json['partList']
        # for part in part_list:
        #     part_name = part['PartName']
        #     drive_list = part['drivelist']
        #     for drive in drive_list:
        #         drive_name = drive['DriverName']
        #         pub_date = drive['DriverIssuedDateTime']
        #         drive_version = drive['Version']
        #         file_path = drive['FilePath']
        #         print(drive_name + drive_version + pub_date)

            
    except:
        print('error')
