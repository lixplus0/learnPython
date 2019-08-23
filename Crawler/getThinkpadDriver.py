# coding=utf-8
import os
import time
import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class CheckDriver():
    def __init__(self):
        self.WEBSITE = 'https://newsupport.lenovo.com.cn/api/drive/drive_listnew?searchKey=3110338&sysid=138'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
        # self.json_file = r"D:\Learn_Codes\LearnPython\Crawler\driver.json"
        self.json_file = r".\driver.json"
        self.old_json_info = {}
        self.new_json_info = {}
        self.flag = 0
        self.message_list = []
        self.mail_title = ''

    def email(self):
        """发送提醒邮件"""
        sender = 'lixplus@sina.cn'  # 填写发件人
        pwd = 'Lidathena0ssg'  # 登录密码
        receivers = ['lixplus@qq.com']  # 填写收件人

        send_message = self.fomat_mail_message()
        message = MIMEText(send_message, "plain", 'utf-8')
        # 三个参数：第一个为文本内容，第二个为plain设置文本格式，第三个为utf-8设置编码
        message['From'] = Header(sender)
        message['To'] = Header("X. Li<lixplus@qq.com>")
        message["Subject"] = "驱动程序更新"

        try:
            # 使用非本地服务器，需要建立ssl连接
            smtpObj = smtplib.SMTP_SSL("smtp.sina.cn", 465)
            # 发件箱邮件服务器
            smtpObj.login(sender, pwd)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print("Error：无法发送邮件.Case:%s" % e)

    def fomat_mail_message(self):
        send_message = self.mail_title + "以下驱动需要更新:\r\n\r\n"
        i = 1
        for msg in self.message_list:
            send_message += str(i) + '. ' + msg + '\r\n\r\n'
            i += 1
        return send_message

    def reset(self):
        '''重置flag'''
        self.flag = 0
        self.message_list = []

    def get_webinfo(self):
        '''读取官网驱动信息'''
        res = requests.get(self.WEBSITE, headers=self.headers)
        return json.loads(res.content)['data']

    def load_file(self):
        '''读取json文件，否则创建'''
        if os.path.exists(self.json_file):
            with open(self.json_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            self.write_file(self.new_json_info)
            print('初始化json文件成功')
            return self.new_json_info

    def write_file(self, json_info):
        '''以覆盖的方式写入json文件'''
        with open(self.json_file, 'w', encoding='utf-8') as f:
            json.dump(json_info, f)

    def main_method(self):
        try:
            self.new_json_info = self.get_webinfo()
            self.old_json_info = self.load_file()
            notebook_series = self.new_json_info['driverSerious'][0]['NodeCode']
            # notebook_pic = self.new_json_info['driverSerious'][0]['PicturePath']
            self.mail_title = notebook_series + '\r\n'
            new_part_list = self.new_json_info['partList']
            old_part_list = self.old_json_info['partList']
            for i in range(0, len(new_part_list)):
                part_name = new_part_list[i]['PartName'] # 判断
                new_drive_list = new_part_list[i]['drivelist']
                old_i = 0
                while new_part_list[i]['PartID'] != old_part_list[old_i]['PartID']:
                    old_i += 1
                old_drive_list = old_part_list[old_i]['drivelist']
                for j in range(0, len(new_drive_list)):
                    new_drive_version = new_drive_list[j]['Version']
                    
                    old_drive_version = old_drive_list[j]['Version']
                    if old_drive_version == new_drive_version:
                        continue
                    else:
                        self.flag += 1
                        drive_name = drive_list[j]['DriverName']
                        pub_date = drive_list[j]['DriverIssuedDateTime']
                        file_path = drive_list[j]['FilePath']
                        update_msg = part_name + ': ' + drive_name + ' ' + old_drive_version + \
                            '==>' + new_drive_version + ' 更新日期: ' + pub_date + ' \r\n    下载链接: ' + file_path
                        self.message_list.append(update_msg)
                        
            if self.flag == 0:
                print('所有驱动都不需要更新 ' + time.strftime("%Y-%m-%d", time.localtime()) )
            else:
                self.email()
                self.write_file(self.new_json_info)
                print('json文件更新成功 ' + time.strftime("%Y-%m-%d", time.localtime()) )
                self.reset()
        except:
            print('error')

if __name__ == "__main__":
    check_driver = CheckDriver()  # 创建类的实例
    while True:
        check_driver.main_method()
        time.sleep(24*60*60)
