import os
import socket
import time
from pywifi import const, PyWiFi, Profile

def interfaces_status(iface):
    '''查看无线网卡连接状态'''
    if iface.status() in [const.IFACE_CONNECTED, const.IFACE_CONNECTING]:
        return True
    return False

def clear():
    os.system('cls')

def network_status(testserver=('www.baidu.com', 443)):
    '''判断网络是否连通'''
    s = socket.socket()
    s.settimeout(3)
    try:
        status = s.connect_ex(testserver)
    except:
        return False
    else:
        if status == 0:
            s.close()
            return True
        return False


def wifi_scan(iface):
    '''扫描周围WIFI'''
    iface.scan()
    return iface.scan_results()


def wifi_connect(iface):
    '''连接WIFI，网络连通返回真'''
    known_wifi = ['NBLXZ_5G', 'HBNU']
    profile = Profile()  # 配置文件
    for wifi in known_wifi:
        iface.disconnect()
        time.sleep(1)
        profile.ssid = wifi  # wifi名称
        iface.connect(iface.add_network_profile(profile))
        print('正在尝试连接到%s...' % wifi)
        time.sleep(5)
        network_ok = network_status()
        time.sleep(1)
        if network_ok:
            return True
    return False


def logs(log_strings):
    '''将记录写入log文件'''
    f = open('wifiControl.log', 'a+')
    f.write(log_strings)
    f.close()


if __name__ == "__main__":
    TIME_INTERVAL = input('请输入检测时间间隔(分钟)：')
    TIME_INTERVAL = int(TIME_INTERVAL)
    clear()
    print('WIFI自动重连程序正在运行\r\n当前每隔 %s 分钟检测一次\r\n日志 记录在同级目录下的wifiControl.log' % TIME_INTERVAL)
    while True:
        log_strings = ''
        if not network_status():
            IFACE = PyWiFi().interfaces()[0]  # 获取第一个无线网卡
            time.sleep(1)
            if not interfaces_status(IFACE):
                CONNECTED = wifi_connect(IFACE)
                if CONNECTED:
                    log_strings += '连接成功,连接时间为'+time.asctime(
                        time.localtime(time.time()))+'\n'
                    print(log_strings)
        else:
            log_strings += '网络正常' + \
                time.asctime(time.localtime(time.time())) + \
                '。每隔 %s 分钟检测一次\n' % TIME_INTERVAL
        logs(log_strings)
        time.sleep(TIME_INTERVAL * 60)
