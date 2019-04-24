# -*- coding: UTF-8 -*-
import os
import wx


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        #一些变量的初始化
        self.dirname = ''
        self.filenames = []
        self.newFilenames = []
        self.addstrings = '请在这里输入要添加的文字'
        
        # 初始化Frame
        wx.Frame.__init__(self, parent, title=title, size=(400, -1))

        #添加文本框
        self.textSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.textLabel = wx.StaticText(self, -1, u"选择您所需\n要的功能：")
        self.textSizerR = wx.BoxSizer(wx.VERTICAL)
        self.subtextSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.texts = []
        self.texts.append(wx.TextCtrl(self, -1, self.addstrings, size=(175,-1)))
        self.textPosition = wx.SpinCtrl(self, -1, min=0, max=100, initial=0)
        self.textDaoxu = wx.CheckBox(self, -1, u"倒序")
        self.subtextSizer1.Add(self.textPosition, 0, wx.EXPAND)
        self.subtextSizer1.Add(self.texts[0], 1, wx.EXPAND)
        self.subtextSizer1.Add(self.textDaoxu, 0, wx.EXPAND)


        self.textSizerR.Add(self.subtextSizer1, 0, wx.ALIGN_CENTER)
        self.textSizer.Add(self.textLabel, 0, wx.ALIGN_CENTER)
        self.textSizer.Add(self.textSizerR, 0, wx.ALIGN_CENTER)
        # 文本事件
        self.Bind(wx.EVT_TEXT, self.OnKey, self.texts[0])
        self.Bind(wx.EVT_TEXT, self.OnKey, self.textPosition)
        self.Bind(wx.EVT_CHECKBOX, self.OnKey, self.textDaoxu)
        
        #添加按钮
        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        self.buttons.append(wx.Button(self, -1, "添加文件"))
        self.buttons.append(wx.Button(self, -1, "清空"))
        self.buttons.append(wx.Button(self, -1, "执行改名！"))
        self.buttons.append(wx.Button(self, -1, "待定"))
        for button in self.buttons:
            self.buttonSizer.Add(button, 1, wx.EXPAND)
        #按钮事件
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.buttons[0])
        self.Bind(wx.EVT_BUTTON, self.OnClear, self.buttons[1])
        self.Bind(wx.EVT_BUTTON, self.OnExecute, self.buttons[2])
        # self.Bind(wx.EVT_BUTTON, self.O, self.buttons[3])

        #添加左右栏预览
        self.listBox1 = wx.BoxSizer(wx.VERTICAL)
        self.listLabel1 = wx.StaticText(self, -1, u"原文件名")
        self.listContent1 = wx.ListBox(self, -1, size=(300, 300), style=wx.LB_SINGLE)
        self.listContent1.SetBackgroundColour('gray')
        self.listBox1.AddMany([(self.listLabel1, 0,  wx.ALIGN_CENTER), (self.listContent1, 1, wx.EXPAND)])

        self.listBox2 = wx.BoxSizer(wx.VERTICAL)
        self.listLabel2 = wx.StaticText(self, -1, u"改名预览")
        self.listContent2 = wx.ListBox(self, -1, size=(300, 300), style=wx.LB_SINGLE)
        # self.listContent2.SetBackgroundColour('darkgray')
        self.listBox2.AddMany([(self.listLabel2, 0,  wx.ALIGN_CENTER), (self.listContent2, 1, wx.EXPAND)])

        self.listBox = wx.BoxSizer(wx.HORIZONTAL)
        self.listBox.AddMany([(self.listBox1, 1, wx.EXPAND),(self.listBox2, 1, wx.EXPAND)])
        
        #添加状态栏
        self.CreateStatusBar() 

        # 添加菜单栏
        filemenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&添加文件", " 添加需要改名的文件")
        menuExit = filemenu.Append(wx.ID_EXIT, "&退出", " 退出程序")
        aboutmenu = wx.Menu()
        menuAbout = aboutmenu.Append(wx.ID_ABOUT, "&关于", " 关于")
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&文件")
        menuBar.Append(aboutmenu, "&关于")
        self.SetMenuBar(menuBar)
        # 菜单栏事件
        self.Bind(wx.EVT_MENU, self.OnClick, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)



        # 创建主Sizer
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.textSizer, 0, wx.EXPAND)
        self.sizer.Add(self.buttonSizer, 0, wx.EXPAND)
        self.sizer.Add(self.listBox, 1, wx.EXPAND)

        self.SetSizer(self.sizer)
        self.SetAutoLayout(True)
        self.sizer.Fit(self)
        self.Show()

    #---------------------------------------
    #  响应事件函数
    #---------------------------------------

    # 关于
    def OnAbout(self, e):
        dlg = wx.MessageDialog(
            self, "文件批量改名\n ----by lixplus", "关于本程序", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    # 退出
    def OnExit(self, e):
        self.Close(True)

    #改名函数
    def OnKey(self, e):
        self.addstrings = self.texts[0].GetValue()
        self.Refresh(e)

    #改名函数
    def ChangeName(self, filename):
        filenameLength=len(filename)
        if not self.textDaoxu.GetValue():
            addpoint=self.textPosition.GetValue()
        else:
            addpoint=filenameLength-min(self.textPosition.GetValue(),filenameLength)
        tempname=list(filename)
        tempname.insert(min(addpoint, filenameLength),self.addstrings)
        return "".join(tempname)


    #清空所有添加的文件
    def OnClear(self, e):
        self.filenames = []
        self.listContent1.Clear()
        self.listContent2.Clear()

    #执行改名
    def OnExecute(self, e):
        for n in range(0,len(self.filenames)):
            oldname=os.path.normpath(os.path.join(self.dirname+os.sep,self.filenames[n]))
            newname=os.path.normpath(os.path.join(self.dirname+os.sep,self.newFilenames[n]))
            os.rename(oldname,newname)
        dlg = wx.MessageDialog(None, u"文件名修改成功", u"提示信息", wx.OK)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()
            self.OnClear(self)  # 成功后清空内容

    # 刷新预览
    def Refresh(self, e):
        self.newFilenames = list(map(self.ChangeName, self.filenames))
        self.listContent2.Set(self.newFilenames)

    # 添加文件
    def OnClick(self, e):
        dlg = wx.FileDialog(self, "添加需要更名的文件", self.dirname, "", "*.*", wx.FD_MULTIPLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.filenames = dlg.GetFilenames()
            self.dirname = dlg.GetDirectory()
            self.listContent1.Set(self.filenames)

            self.newFilenames = list(map(self.ChangeName, self.filenames))
            self.listContent2.Set(self.newFilenames)
        dlg.Destroy()


app = wx.App(False)
frame = MainWindow(None, "文件改名器")
app.MainLoop()
