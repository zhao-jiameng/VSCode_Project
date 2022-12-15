import cv2
faceData=cv2.CascadeClassifier("./resources/haarcascade_frontalface_alt.xml")
video=cv2.VideoCapture(0)    #调用本地摄像头（0：允许被调用））
name=1                          #记录人脸变量
while(True):                    #无限抓怕人脸
    flag,videoImg=video.read()  #flag:确定是否获取到人脸    videoImg：截取到的照片
    videoImg=cv2.flip(videoImg,1)#镜像翻转（1：水平翻转 0：垂直翻转 -1：水平+垂直）
    faces=faceData.detectMultiScale(videoImg,scaleFactor=1.3,minNeighbors=5)
    print(faces)
    for x,y,w,h in faces:
        cv2.rectangle(videoImg,pt1=(x,y),pt2=(x+w,y+h),color=[0,0,255],thickness=3)
        if not isinstance(faces,tuple):
            facePhoto=videoImg[y:y+h,x:x+w]     #人脸切片
            cv2.imwrite("./photo/4/%s.jpg"%name,facePhoto)
            print("第%s张人脸数据保存成功"%name)
            name+=1
    cv2.imshow("捕获",videoImg)
    index=cv2.waitKey(1000//60)
    if index==32:           #空格
        print("窗口即将关闭")
        break
    pass
cv2.destroyAllWindows()