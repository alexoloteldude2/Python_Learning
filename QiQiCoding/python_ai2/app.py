import cv2, numpy, os
labels, faces=[],[]
file='lbpcascade_frontalface_improved.xml'
face_cascade=cv2.CascadeClassifier(file)
recogniser=cv2.face.LBPHFaceRecognizer.create()
def detect_face(image):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.2,5,minSize=(20,20))
    if(len(faces)==0):
        return None
    (x,y,w,h)=faces[0]
    return gray[y:y+w,x:x+h]

def read_face(label,images_path):
    files=os.listdir(images_path)
    for file in files:
        image=cv2.imread(images_path+'/'+file)
        face=detect_face(image)
        if face is not None:
            face=cv2.resize(face,(256,256))
            faces.append(face)
            labels.append(label)
if __name__=='__main__':
    read_face(2,'training/iron_man')
    read_face(1,'training/spider_man')
    recogniser.train(faces,numpy.array(labels))
    recogniser.save('trainer.yml')
