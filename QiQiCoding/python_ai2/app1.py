import cv2
names=('none','spider_man','iron_man')
file='lbpcascade_frontalface_improved.xml'
face_cascade=cv2.CascadeClassifier(file)
recogniser=cv2.face.LBPHFaceRecognizer.create()
recogniser.read('trainer.yml')
image=cv2.imread('testing/test1.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.2,5)
for (x, y, w, h) in faces:
    face = gray[y:y+w, x:x+h]
    face = cv2.resize(face, (256, 256))
    label, confidence = recogniser.predict(face)
    confidence = 100 - confidence
    if label > 0 and confidence > 50 :
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        text = '%s:%d' % (names[label], confidence)
        print(text)
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(image, text, (x, y), font, 2.5, (0, 255, 0), 2)
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()