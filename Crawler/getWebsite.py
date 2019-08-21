# coding=utf-8
import os
import time
import re
import requests
import json

json_file = "driver.json"

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
        old_info_json = load_file()
        notebook_series = info_json['driverSerious'][0]['NodeCode']
        notebook_pic = info_json['driverSerious'][0]['PicturePath']
        part_list = info_json['partList']
        old_part_list = old_info_json['partList']
        for i in range(0, len(part_list)):
            part_name = part_list[i]['PartName']
            drive_list = part_list[i]['drivelist']
            old_drive_list = old_part_list[i]['drivelist']
            for j in range(0, len(drive_list)):
                drive_version = drive_list[j]['Version']
                old_drive_version = old_drive_list[j]['Version']
                if drive_version == old_drive_version:
                    print('break')
                else:
                    drive_name = drive_list[j]['DriverName']
                    pub_date = drive_list[j]['DriverIssuedDateTime']
                    file_path = drive_list[j]['FilePath']
                    print(drive_name + drive_version)

            
    except:
        print('error')
