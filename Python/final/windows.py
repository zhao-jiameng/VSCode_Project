import tkinter as tk
import os
from tkinter import messagebox

class Page_1:  # 这是第一个页面
    def __init__(self, window):
        self.window = window
        self.window.title("人脸识别解锁")
        self.window.geometry("800x320")
        self.window.config(bg="#F9C03D")
        self.button = tk.Button(self.window, text="开始使用", height=5,width=100, command=self.page_1_1)
        self.button.pack()
        self.button1 = tk.Button(self.window, text="录入人脸", height=5,width=100, command=self.page_1_2)
        self.button1.pack()
        self.button2 = tk.Button(self.window, text="退出使用", height=5,width=100, command=self.page_1_3)
        self.button2.pack()


    def page_1_1(self):
        self.button.destroy()
        self.button1.destroy()
        self.button2.destroy()
        Page_1_1(root)

    def start(self,pythonFile):
        self.button.destroy()
        self.button1.destroy()
        self.button2.destroy()
        os.system(f"python {pythonFile}")
        Page_1(root)


    def page_1_2(self):
        self.button.destroy()
        self.button1.destroy()
        self.button2.destroy()
        Page_1_2(root)

    def page_1_3(self):
        self.button.destroy()
        self.button1.destroy()
        self.button2.destroy()
        Page_1_3(root)

class Page_1_1:  # 这是第二个页面
    def __init__(self, window):
        self.window = window
        self.window.title("录入人脸")
        self.window.geometry("800x320")
        self.window.config(bg="#0F375A")
        self.button = tk.Button(self.window, text="返回", height=5,width=100, command=self.back)
        self.button1 = tk.Button(self.window, text="请从上述用户选择您要锁屏的用户",height=3,width=100, command=self.setupUI(root))
        self.tk= tk
        self.button.pack()
        self.button1.pack()

    def start(self,pythonFile,face_id):
    
        self.button.destroy()
        self.button1.destroy()
        os.system(f"python {pythonFile} {face_id}")
        tk.messagebox.askyesno(title='系统提示', message='识别成功')
        exit()
        Page_1(root)

    def back(self):
        dirs=os.listdir("D:\\face_data")
        n=len(dirs)
        for i in range(n):
            self.button.destroy()
        Page_1(root)

    face_id = ""
    def setupUI(self,window):
        self.window = window
        self.window.title("选择用户")
        self.window.geometry("800x320")
        self.window.config(bg="#0F375A")
        #获取电脑保存的所有人脸
        dirs=os.listdir("D:\\face_data")
        n=len(dirs)
        for i in range(n):
            self.button=tk.Button(self.window,text="%s"%dirs[i],height=3,width=100,command=lambda:self.start("./锁屏.py",dirs[i]))
            self.button.pack()      

    def on_click(self):
        global face_id
        face_id = self.xls_text.get().lstrip()
        if len(face_id) == 0:
            messagebox.showwarning(title='系统提示',message='请输入用户名!')
            return False
        self.button.destroy()
        self.button1.destroy()
        self.row1.destroy()
        self.row2.destroy()
        Page_1_1(root)

class Page_1_2:  # Page_1-3 退出
    def __init__(self, window):
        self.window = window
        self.window.title("录入人脸")
        self.window.geometry("800x320")
        self.window.config(bg="#0F375A")
        self.button = tk.Button(root, text="返回", height=5,width=100, command=self.back)
        self.button.pack()
        self.button1 = tk.Button(root, text="录入人脸",height=5,width=100, command=lambda:self.start("./初始化.py"))
        self.button1.pack()

    def start(self,pythonFile):
        self.button.destroy()
        self.button1.destroy()
        os.system(f"python {pythonFile}")
        Page_1(root)

    def back(self):
        self.button.destroy()
        self.button1.destroy()
        Page_1(root)

class Page_1_3:  # Page_1-3 退出
    def __init__(self, window):
        self.window = window
        self.window.title("退出软件")
        self.window.geometry("800x320")
        self.window.config(bg="#0F375A")
        self.button = tk.Button(root, text="返回", height=5,width=100, command=self.back)
        self.button.pack()
        self.button1 = tk.Button(root, text="退出", height=5,width=100, command=root.destroy)
        self.button1.pack()

    def back(self):
        self.button.destroy()
        self.button1.destroy()
        Page_1(root)

root = tk.Tk()
p1 = Page_1(root)
root.mainloop()
