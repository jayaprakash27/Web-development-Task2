import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("hero_alum.jpg")

r=cv2.resize(img,(int(img.shape[1]),int(img.shape[0])))
grayimg=cv2.cvtColor(r,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(grayimg,scaleFactor=1.05,minNeighbors=5)
for x,y,w,h in faces:
    r=cv2.rectangle(r,(x,y),(x+w,y+h),(255,255,0),2)
cv2.imshow("deadpool",r)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(faces)