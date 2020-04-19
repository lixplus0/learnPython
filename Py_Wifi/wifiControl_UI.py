# -*- coding: utf-8 -*-
import wx
import threading
import os
import socket
import time
from pywifi import const, PyWiFi, Profile

class WorkerThread(threading.Thread):
    '''
This just simulates some long-running task that periodically sends a message to the GUI thread.
    '''
    def __init__(self, window):
        threading.Thread.__init__(self)
        self.window = window
        self.timeToQuit = threading.Event()
        self.timeToQuit.clear()
        self.messageDelay = self.window.TIME_INTERVAL * 60

    def stop(self):
        self.timeToQuit.set()

    def run(self):    # 运行一个线程
        wx.CallAfter(self.window.LogMessage)
        while True:
            self.timeToQuit.wait(self.messageDelay)
            if self.timeToQuit.isSet():
                break
            wx.CallAfter(self.window.LogMessage)

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='WIFI自动重连')
        self.TIME_INTERVAL = 30
        self.wifi_name = 'NBLXZ_5G;HBNU'
        self.threads = WorkerThread(self)
        panel = wx.Panel(self)
        
        settingSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        textLabel1 = wx.StaticText(panel, -1, u"输入已连接过的可用WIFI，用 ; 间隔   ")
        self.wifiText = wx.TextCtrl(panel, -1, self.wifi_name)
        settingSizer1.Add(textLabel1, 0, wx.ALIGN_CENTER)
        settingSizer1.Add(self.wifiText, 0, wx.ALIGN_CENTER)
        settingSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        textLabel2 = wx.StaticText(panel, -1, u"输入检测间隔：(分钟)   ")
        self.detectInterval = wx.SpinCtrl(panel, -1, min=1, max=7*24*60, initial= self.TIME_INTERVAL,size=(100,-1))
        startBtn = wx.Button(panel, -1, "设置",size=(50,-1))
        clearBtn = wx.Button(panel,-1,"清空",size=(50,-1))
        settingSizer2.Add(textLabel2, 0, wx.ALIGN_CENTER)
        settingSizer2.Add(self.detectInterval, 0, wx.ALIGN_CENTER)
        settingSizer2.Add(startBtn, 1, wx.ALIGN_CENTER)
        settingSizer2.Add(clearBtn, 1, wx.ALIGN_CENTER)

        inner = wx.BoxSizer(wx.VERTICAL)
        inner.Add(settingSizer1, 0, wx.RIGHT, 15)
        inner.Add(settingSizer2, 0, wx.RIGHT, 15)

        self.log = wx.TextCtrl(panel, -1, '', style=wx.TE_RICH | wx.TE_MULTILINE | wx.TE_READONLY)

        main = wx.BoxSizer(wx.VERTICAL)
        main.Add(inner, 0, wx.ALL, 5)
        main.Add(self.log, 1, wx.EXPAND | wx.ALL, 5)
        panel.SetSizer(main)
        self.Bind(wx.EVT_BUTTON, self.OnStartButton, startBtn)
        self.Bind(wx.EVT_BUTTON, self.OnClearButton, clearBtn)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnClearButton(self, evt):
        '''清空显示日志，并将记录写入log文件'''
        f = open('wifiControl.log', 'a+')
        f.write(self.log.GetValue())
        f.close()
        dlg = wx.MessageDialog(None, u"按 OK 以清空，历史日志将记录在wifiControl.log文件中", u"操作成功", wx.OK | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Close(True)
        dlg.Destroy()
        self.log.SetValue('')


    def OnStartButton(self, evt):
        self.wifi_name = self.wifiText.GetValue()
        self.TIME_INTERVAL = self.detectInterval.GetValue()
        self.threads.stop()
        self.threads = WorkerThread(self)
        self.threads.start()#启动线程

    def OnCloseWindow(self, evt):
        self.threads.stop()
        self.Destroy()

#---------------wifi重连相关函数---------------------------------
    def interfaces_status(self, iface):
        '''查看无线网卡连接状态'''
        if iface.status() in [const.IFACE_CONNECTED, const.IFACE_CONNECTING]:
            return True
        return False

    def network_status(self, testserver=('www.baidu.com', 443)):
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

    def wifi_connect(self, iface):
        '''连接WIFI，网络连通返回真'''
        known_wifi = self.wifi_name.split(';')
        profile = Profile()  # 配置文件
        for wifi in known_wifi:
            iface.disconnect()
            time.sleep(1)
            profile.ssid = wifi  # wifi名称
            iface.connect(iface.add_network_profile(profile))
            time.sleep(5)
            network_ok = self.network_status()
            time.sleep(1)
            if network_ok:
                return True
        return False


    def LogMessage(self):#注册一个消息 
        log_strings = ''
        if not self.network_status():
            IFACE = PyWiFi().interfaces()[0]  # 获取第一个无线网卡
            time.sleep(1)
            if not self.interfaces_status(IFACE):
                CONNECTED = self.wifi_connect(IFACE)
                if CONNECTED:
                    log_strings = '连接成功,连接时间为'+time.asctime(
                        time.localtime(time.time()))+'\n'
        else:
            log_strings = '网络正常' + \
                time.asctime(time.localtime(time.time())) + \
                '。每隔 %s 分钟检测一次\n' % self.TIME_INTERVAL
        # self.logs(log_strings)
        self.log.AppendText(log_strings)


if __name__ == "__main__":
    app = wx.App()
    frm = MyFrame()
    frm.Show()
    app.MainLoop()
