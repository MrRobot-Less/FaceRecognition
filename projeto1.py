import cv2
import numpy as np
import dlib
import os


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

xml = "C:\\Program Files (x86)\\Python37-32\\lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml"
olhos = "C:\\Program Files (x86)\\Python37-32\\lib\\site-packages\\cv2\\data\\haarcascade_eye.xml"

faceCascata = cv2.CascadeClassifier(xml);

olhoCascata = cv2.CascadeClassifier(xml);

font = cv2.FONT_HERSHEY_SIMPLEX
id = 0

nomes = open('BD\\nomes.txt', 'r').read()
nomes = nomes.rsplit()


nomes.append(nomes[1])

email = open('BD\\email.txt', 'r').read()
email = email.rsplit()

idade = open('BD\\idades.txt', 'r').read()
idade = idade.rsplit()

status = open("BD\\status.txt", "r").read()
status = status.rsplit()

hobby = open("BD\\hobby.txt", "r").read()
hobby = hobby.rsplit()

cam = cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FPS, 60)
#cam.set(3, 1000)
#cam.set(4, 400)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1000);
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 200);

minA = 0.2*cam.get(3)
minL = 0.2*cam.get(4)

cont = 0

detector = dlib.get_frontal_face_detector()
#predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

vv = 0
cor=(0,0,0)
ordem = ["Data Nasc", "E-mail", "Status", "Hobby"]
campos = [idade, email, status, hobby]
def quadrado(img, x, y, w, h):
    cv2.rectangle(img, (x,y), (x+w,y+h), cor, 2)

while True:
    ret, img = cam.read()
    img = cv2.flip(img,180)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = detector(gray)
    for face in faces:
        x = face.left()
        y = face.top()
        x1 = face.right()
        y1 = face.bottom()
        rosto = gray[y:y1, x:x1]
        ids, pronabilidade = recognizer.predict(rosto)
        if(pronabilidade < 100 and 100 - pronabilidade <= 45):
            id = 'Desconhecido'
            pronabilidade = ' {0}%'.format(round(100 - pronabilidade))
            lista = []
        elif(100 - pronabilidade >= 45):
            lista = []
            if len(nomes) >= 1:
                id = nomes[ids]
                for i in range(len(campos)):
                    lista.append(campos[i][ids])
                    
                pronabilidade = "  {0}%".format(round(100 - pronabilidade))
                cor = (0,0,0)
                cv2.rectangle(img, (x-1, y1 + 70), (x1, y1+10), cor, cv2.FILLED)
                distancia = 0
                for string, campo in zip(lista, ordem):
                    cv2.putText(img, str(campo+": "+string), (x,y1+20+distancia), font, 0.5, (255,255,255), 1)
                    distancia += 15
        else:
            id = 'Desconhecido'
            pronabilidade = ' {0}%'.format(round(100 - pronabilidade))
            lista = []
        
        cv2.line(img, (x, y), (x+30, y), (0,0,0), 2)
        cv2.line(img, (x1, y), (x1-30, y), (0,0,0), 2)
        
        cv2.line(img, (x, y), (x, y+30), (0,0,0), 2)
        cv2.line(img, (x1, y), (x1, y+30), (0,0,0), 2)

        #BAIXO
        cv2.line(img, (x, y1), (x+30, y1), (0,0,0), 2)
        cv2.line(img, (x, y1), (x, y1-30), (0,0,0), 2)

        cv2.line(img, (x1, y1), (x1-30, y1), (0,0,0), 2)
        cv2.line(img, (x1, y1), (x1, y1-30), (0,0,0), 2)
        
        
        cv2.rectangle(img, (x+10, y - 30), (x1-10, y- 10), cor, cv2.FILLED)
        
        cv2.putText(img, "Nome: "+str(id), (x+10,y-15), font, 0.5, (255,255,255), 1)
        cv2.putText(img, str(pronabilidade), (x1-int(50),y-15), font, 0.5, (255,255,255), 1)
        id = ''

    cv2.imshow('Sorria',img) 
    
    k = cv2.waitKey(10) & 0xff    
    if k == 27:
        break
cam.release()
cv2.destroyAllWindows()
