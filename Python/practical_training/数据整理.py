import cv2
import os
import numpy as np


for pro in range(0,5):
    dirs=os.listdir("./photo/%s/"%pro)
    nameList=[]
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
            os.rename("./photo/%s/%s.jpg"%(pro,file),"./photo/%s/%s.jpg"%(pro,loseName[i]))
        except:
            os.remove("./photo/%s/%s.jpg"%(pro,file))
    for i in loseName:
        randomName=np.random.choice(lessThan100,size=1)[0]
        img=cv2.imread("./photo/%s/%s.jpg"%(pro,randomName))
        cv2.imwrite("./photo/%s/%s.jpg"%(pro,i),img)
    for i in compareTo100:
        img=cv2.imread("./photo/%s/%s.jpg"%(pro,i))
        newImg=cv2.resize(img,dsize=(64,64))
        cv2.imwrite("./photo/%s/%s.jpg"%(pro,i),newImg)
pass

