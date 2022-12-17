import cv2 
import os 
import numpy as np
import tkinter as tk
from tkinter import messagebox
        


#为即将录入的脸标记一个id
face_id= ""

class MyCollectApp(tk.Toplevel):
    def __init__(self):
        super().__init__() 
        self.title('用户信息')
        self.setupUI()

    def setupUI(self):
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        l1 = tk.Label(row1, text="请输入姓名：",height=2,width=10)
        l1.pack(side=tk.LEFT)  
        self.xls_text = tk.StringVar()
        tk.Entry(row1, textvariable=self.xls_text).pack(side=tk.RIGHT)

        row2 = tk.Frame(self)
        row2.pack(fill="x")
        tk.Button(row2, text="点击确认", command=self.on_click).pack(side=tk.RIGHT)

    def on_click(self):
        global face_id
        face_id = self.xls_text.get().lstrip()
        if len(face_id) == 0:
            messagebox.showwarning(title='系统提示',message='请输入用户名!')
            return False
        self.quit()
        self.destroy()

var_box = tk.messagebox.askyesno(title='系统提示', message='是否采集人脸数据需要')  
if var_box:
    app = MyCollectApp()
    app.mainloop()
else:
    pass


cap = cv2.VideoCapture(0)
faceData = cv2.CascadeClassifier("./resources/haarcascade_frontalface_default.xml") 


if not os.path.exists("D:\\face_data\%s"%face_id):
    os.makedirs("D:\\face_data\%s"%face_id)
#sampleNum用来计数样本数目
count = 0

while True:    
    success,img = cap.read()   
    img=cv2.flip(img,1) 
    if success is True: 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    else:   
        break
    faces = faceData.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+w), (255, 0, 0))
        count += 1  
        cv2.imwrite("D://face_data/%s/%s.jpg"%(face_id,count),gray[y:y+h,x:x+w]) 
        cv2.imshow('正在录取你的人脸信息，请面朝摄像头稍等片刻',img)       
    k = cv2.waitKey(1)        
    if k == '32':
        break        
    elif count >= 200:
        break
cv2.destroyAllWindows()

#数据清洗
dirs=os.listdir("D:\\face_data\%s"%face_id)
for i in range(1,len(dirs)+1):      #循环人脸
    img=cv2.imread("D:\\face_data\%s\%s.jpg"%(face_id,i))
    faces=faceData.detectMultiScale(img,scaleFactor=1.3,minNeighbors=5)
    if isinstance(faces,tuple):
        os.remove("D:\\face_data\%s\%s.jpg"%(face_id,i))

#数据整理
nameList=[]
dirs=os.listdir("D:\\face_data\%s"%face_id)
for i in dirs:
    s=int(i.split(".")[0])
    nameList.append(s)
npNameList=np.array(nameList)
moreThan100=npNameList[npNameList>100]
lessThan100=npNameList[npNameList<=100]
compareTo100=np.arange(1,101)
loseName=list(set(compareTo100).difference(lessThan100))

for i,file in enumerate(moreThan100):
    try:
        os.rename("D:\\face_data\%s\%s.jpg"%(face_id,file)),"D:\\face_data\%s\%s.jpg"%(face_id,loseName[i])
    except:
        os.remove("D:\\face_data\%s\%s.jpg"%(face_id,file))
for i in loseName:
    randomName=np.random.choice(lessThan100,size=1)[0]
    img=cv2.imread("D:\\face_data\%s\%s.jpg"%(face_id,randomName))
    cv2.imwrite("D:\\face_data\%s\%s.jpg"%(face_id,i),img)
for i in compareTo100:
    img=cv2.imread("D:\\face_data\%s\%s.jpg"%(face_id,i))
    newImg=cv2.resize(img,dsize=(64,64))
    cv2.imwrite("D:\\face_data\%s\%s.jpg"%(face_id,i),newImg)
