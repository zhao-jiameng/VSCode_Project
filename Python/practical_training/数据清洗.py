import cv2
import os       #文件夹操作库
pro=4           #从哪位人开始下标
#for pro in range(0,5):
dirs=os.listdir("./photo/%s"%pro) #获取当前文件夹所有图片
faceData=cv2.CascadeClassifier("./resources/haarcascade_frontalface_alt.xml")
for i in range(1,len(dirs)+1):      #循环人脸
    img=cv2.imread("./photo/%s/%s.jpg"%(pro,i))
    faces=faceData.detectMultiScale(img,scaleFactor=1.3,minNeighbors=5)
    if isinstance(faces,tuple):
        os.remove("./photo/%s/%s.jpg"%(pro,i))
    pass
pass