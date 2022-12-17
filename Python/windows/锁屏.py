import sys
import os
import tkinter as tk
from tkinter import *
from os import system
from tkinter import messagebox
#代码的入参改成 sys.argv[1]
face_id=sys.argv[1]
class App:
    def __init__(self):
        self.root=Tk()
        self.root.title("锁屏")
        self.root.attributes("-fullscreen", True)
        self.root.wm_attributes('-topmost',1)
        self.root.overrideredirect(True)
        self.root.bind("<Key>",self.key_watcher)
        self.version_10()
        self.root.mainloop()

    def start(self,pythonFile,face_id):
        self.button1.destroy()
        os.system(f"python {pythonFile} {face_id}")
        exit()
        App()

    def version_10(self):
        self.n=1
        self.root.config(bg='#0078d7')
        self.big_words_label=Label(self.root)
        self.button1=Label(self.root)
        self.big_words_label.config(font=("微软雅黑",20,),fg='white',bg='#0078d7',justify="left")
        self.big_words_label.config(text=f"您的电脑已锁定,点击下方进行人脸识别")
        self.button1=tk.Button(self.root,bd=0,bg='#0078d7',fg='white',font=10,width=12,height=12,text="点击开始人脸识别",command=lambda:self.start("./用户选择.py",face_id))
        self.big_words_label.place(relx=0.01,rely=0.32,width=self.root.winfo_screenwidth()*1,
                                height=self.root.winfo_screenheight()*0.3,anchor="nw")
        self.button1.place(relx=0.3, rely=0.6, width=self.root.winfo_screenwidth() * 0.4,
                            height=self.root.winfo_screenheight() * 0.05, anchor="nw")

    def key_watcher(self,event):
        if event.keycode==27 :
            ret=messagebox.askyesno("重启","确定要重启您的电脑吗？")
            if ret:
                exit()

if __name__ == '__main__':
    a=App()

