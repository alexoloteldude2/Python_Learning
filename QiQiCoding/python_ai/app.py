import cv2
# img = cv2.imread('images/face1.jpg')
# pos=(10,50)
# font = cv2.FONT_HERSHEY_SIMPLEX
# color = (255,255,0)
# cv2.putText(img,"hi world :)",pos,font,2,color,2)
# cv2.imshow("name",img)





# img = cv2.imread('images/face2.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# file = 'ai/haarcascade_frontalface_default.xml'
# facecascade = cv2.CascadeClassifier(file)
# faces = facecascade.detectMultiScale(gray, 1.3,2)
# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


file = 'ai/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(file)
vc=cv2.VideoCapture(1)
vc.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
vc.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
while True:
    retval,frame=vc.read()
    if not retval or cv2.waitKey(16) & 0xFF == ord('q'):
        print(retval)
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,2)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),3)
    cv2.imshow('frame',frame)
vc.release()
cv2.destroyAllWindows()







