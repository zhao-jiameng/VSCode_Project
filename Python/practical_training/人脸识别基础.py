#安装库识别读取图片
import cv2
#读取照片
img=cv2.imread("H:\VSCode_Project\Python\practical_training\img\zjm.jpg")
#img=cv2.cvtColor(img,code=cv2.COLOR_BGR2GRAY) #降维
print(img)
print(type(img.shape))
print(img.shape) #高 宽 维
#img=cv2.resize(img,dsize=(600,800)) #调整图片大小（宽高）
img=cv2.resize(img,None,fx=0.1,fy=0.1)#等比例缩放窗口
cv2.imshow("赵嘉盟",img) #显示照片
cv2.waitKey()           #窗口等待停留（ms）
cv2.destroyAllWindows()     #释放资源