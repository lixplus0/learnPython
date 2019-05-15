import os
import smtplib
import time
from email.mime.text import MIMEText

import requests
from lxml import etree


def email():
    """发送提醒邮件"""
    sender = 'lixplus@sina.cn'  # 填写发件人
    pwd = 'Lidathena0ssg'  # 登录密码
    receivers = ['lixplus@qq.com']  # 填写收件人

    message = MIMEText("你好，网站有内容更新，请及时查看", "plain", 'utf-8')
    # 三个参数：第一个为文本内容，第二个为plain设置文本格式，第三个为utf-8设置编码
    message['From'] = "信息更新提醒 <lixplus@sina.cn>"
    message['To'] = "X. Li <lixplus@qq.com>"

    subject = "网站有内容更新"
    # 邮件主题
    message["Subject"] = subject

    try:
        # 使用非本地服务器，需要建立ssl连接
        smtpObj = smtplib.SMTP_SSL("smtp.sina.cn", 465)
        # 发件箱邮件服务器
        smtpObj.login(sender, pwd)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error：无法发送邮件.Case:%s" % e)


while True:
    url = "https://www.ttkmj.net/a/6526"  # 目标跟踪网页
    content = requests.get(url).content
    html = etree.HTML(content)
    title = html.xpath('//*[@id="article"]/table[2]/tbody/tr[4]/td[3]')[0].text
    # 获取第一篇文章标题
    print("当前的标题为:%s" % title)
    # 屏幕打印获取的第一篇文章标题

    if not os.path.isfile("D:\\title_temp.txt"):
        # 判断title_temp.txt文件是否存在，不存在则创建，并写入获取的第一篇文章标题
        f = open("D:\\title_temp.txt", "w")
        f.write(title)
        print(r"将当前标题记录在D:\title_temp.txt中，等待检测")
        f.close()
    else:
        # title_temp.txt文件存在的话，提取里面标题，和获取的标题对比
        with open("D:\\title_temp.txt", "r+") as f:
            old_title = f.read()
            if old_title != title:
                email()  # 发送qq邮件
                # 如果读取内容和获取的网站第一篇文章标题不一致，则表明网站更新
                f.seek(0)
                f.truncate()
                print("网站有更新，需通知")
                f.write(title)
                # 写入最新的标题内容，方便下一次比对
                break
            else:
                # 否则的话，表明网站没有更新
                print("网站暂时没有更新\n")
    time.sleep(5)
    # 检测网页内容时间间隔，单位为秒（s）
