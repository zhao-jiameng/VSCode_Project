from sklearn.model_selection import train_test_split        #机器学习库
from sklearn.neighbors import KNeighborsClassifier          #最近值
import numpy as np
import cv2

list=[]     #全部人脸
for i in range(5):
    for j in range(1,101):
        img=cv2.imread("./photo/%s/%s.jpg"%(i,j))
        grayImg=cv2.cvtColor(img,code=cv2.COLOR_BGR2GRAY) #降维
        list.append(grayImg)

y=[]        #标记的人脸
for i in range(5):
    y.append(i)
y=y*100
y=sorted(y)

list=np.array(list)
y=np.array(y)
list=list.reshape(500,4096)     #转换500列4096的矩阵
#用来训练的人脸，用来测试的人脸，标记用来训练的人脸，标记用来测试的人脸
x_train,x_test,y_train,y_test=train_test_split(list,y,test_size=0.1)
label=["赵嘉盟","刘泳妍","程钰","刘东鑫","江海瑞"]
knn=KNeighborsClassifier(5)     #最小临近值，识别5次
knn.fit(x_train,y_train)        #训练

for i in range(50):
    cv2.namedWindow("who",flags=cv2.WINDOW_NORMAL)  #自定义窗口
    cv2.resizeWindow("who",width=300,height=300)
    cv2.imshow("who",x_test[i].reshape(64,64))
    print("这个人是：",label[y_test[i]])
    index=cv2.waitKey()
    if index==32:
        break
