import cv2

img=cv2.imread("./img/zjm3.jpeg")
#导入人脸数据特征包
faceData=cv2.CascadeClassifier("./resources/haarcascade_frontalface_alt.xml")

#对比人脸
faces=faceData.detectMultiScale(img,scaleFactor=1.1,minNeighbors=1)
# scaleFactor:缩放因子（默认1.3），值越小扫描越细致，越大越容易忽略人脸数据
# minNeighbors:最小邻居值（默认3），值越小越放松，值越大条件越苛刻
print(faces)

for x,y,w,h in faces:
    cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color=[0,0,255],thickness=2)         #绘制矩形

img=cv2.resize(img,None,fx=0.5,fy=0.5)#等比例缩放窗口
cv2.imshow("赵嘉盟",img) #显示照片
cv2.waitKey()           #窗口等待停留（ms）
cv2.destroyAllWindows()     #释放资源