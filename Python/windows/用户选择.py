import cv2 
import os 
import sys
import numpy as np
import tkinter as tk
from sklearn.model_selection import train_test_split        
from sklearn.neighbors import KNeighborsClassifier  

print("开始人脸识别")
if not os.path.exists("D:\\face"):
    os.makedirs("D:\\face")
#记录用户id
face_id= sys.argv[1]
list=[]     #全部人脸
#获取电脑保存的所有人脸
dirs=os.listdir("D:\\face_data")
n=len(dirs)
for i in dirs:
    for j in range(1,101):
        img=cv2.imread("D:\\face_data\%s\%s.jpg"%(i,j))
        list.append(img)

y=[]        #标记的人脸
for i in range(n):
    y.append(i)
y=y*100
y=sorted(y)

list=np.array(list).reshape(n*100,4096*3)
y=np.array(y)   
x_train,x_test,y_train,y_test=train_test_split(list,y,test_size=0.1)
label=dirs
knn=KNeighborsClassifier(5)     #最小临近值，识别5次
knn.fit(x_train,y_train)        #训练


#对比
faceData=cv2.CascadeClassifier("./resources/haarcascade_frontalface_alt.xml")
video=cv2.VideoCapture(0)    #调用本地摄像头（0：允许被调用））
name=0                          #记录人脸变量
while(True):                    #无限抓怕人脸
    flag,videoImg=video.read()  #flag:确定是否获取到人脸    videoImg：截取到的照片
    videoImg=cv2.flip(videoImg,1)#镜像翻转（1：水平翻转 0：垂直翻转 -1：水平+垂直）
    faces=faceData.detectMultiScale(videoImg,scaleFactor=1.3,minNeighbors=5)
    print(faces)
    for x,y,w,h in faces:
        cv2.rectangle(videoImg,pt1=(x,y),pt2=(x+w,y+h),color=[0,0,255],thickness=3)
        if not isinstance(faces,tuple):
            facePhoto=videoImg[y:y+h,x:x+w]     #人脸切片
            img=cv2.resize(facePhoto,dsize=(64,64))
            cv2.imwrite("D:\\face\%s.jpg"%name,img)
            name+=1
    cv2.imshow("捕获",videoImg)
    cv2.waitKey(1000//60)
    if name>=10:           #空格
        print("捕获完毕")
        break
cv2.destroyAllWindows()



list2=[]
for i in range(11):
    for j in range(11):
        img=cv2.imread("D:\\face\%s.jpg"%i)
        list2.append(img)
    cv2.namedWindow("摄像头",flags=cv2.WINDOW_NORMAL)  #自定义窗口
    cv2.resizeWindow("摄像头",width=300,height=300)
    cv2.imshow("摄像头",list2[i].reshape(64,64*3))
    print("face_id:%s"%face_id)
    index=label[y_test[i]]
    print(y_test[i])
    print(index)
    if index==face_id:
        exit()
    if index==10:
        tk.messagebox.showinfo(title='系统提示', message='识别失败')
        