import cv2
import numpy as np
import os


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

xml = "C:\\Program Files (x86)\\Python37-32\\lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml"


faceCascata = cv2.CascadeClassifier(xml);


font = cv2.FONT_HERSHEY_SIMPLEX
id = 0

nomes = open('BD\\nomes.txt', 'r').read()
nomes = nomes.rsplit()


nomes[0] = nomes[0]
nomes[1] = nomes[1]
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
cam.set(cv2.CAP_PROP_FPS, 45)
#cam.set(3, 1000)
#cam.set(4, 400)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1000);
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 200);

minA = 0.25*cam.get(3)
minL = 0.25*cam.get(4)

cont = 0

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
    faces = faceCascata.detectMultiScale( 
        img,
        scaleFactor = 1.3,
        minNeighbors = 5,
        minSize = (int(minA), int(minL))
    )
    
    for(x,y,w,h) in faces:
        rosto = gray[y:y+h, x:x+w]
        lang, alt = rosto.shape
        if(lang * alt <= 20*20):
        
            continue
        rosto = cv2.resize(rosto, (255,255)) 
        ids, pronabilidade = recognizer.predict(rosto)
        cont += 1
        if(pronabilidade < 100 and 100 - pronabilidade <= 53.5):
            id = 'Desconhecido'
            pronabilidade = ' {0}%'.format(round(100 - pronabilidade))
            lista = []
        elif(100 - pronabilidade >= 53.5):
            lista = []
            if len(nomes) >= 1:
                id = nomes[ids]
                for i in range(len(campos)):
                    lista.append(campos[i][ids])
                    
                pronabilidade = "  {0}%".format(round(100 - pronabilidade))
                cor = (0,0,0)
                cv2.rectangle(img, (x-1, y + h + 70), (x+w, y+h+10), cor, cv2.FILLED)
                distancia = 0
                for string, campo in zip(lista, ordem):
                    cv2.putText(img, str(campo+": "+string), (x,y+h+20+distancia), font, 0.5, (255,255,255), 1)
                    distancia += 15
        else:
            id = 'Desconhecido'
            pronabilidade = ' {0}%'.format(round(100 - pronabilidade))
            lista = []
        #CIMA
        cv2.line(img, (x, y), (x+30, y), (0,0,0), 2)
        cv2.line(img, (x+w, y), (x+w-30, y), (0,0,0), 2)
        
        cv2.line(img, (x, y), (x, y+30), (0,0,0), 2)
        cv2.line(img, (x+w, y), (x+w, y+30), (0,0,0), 2)

        #BAIXO
        cv2.line(img, (x, y+h), (x+30, y+h), (0,0,0), 2)
        cv2.line(img, (x, y+h), (x, y+h-30), (0,0,0), 2)

        cv2.line(img, (x+w, y+h), (x+w-30, y+h), (0,0,0), 2)
        cv2.line(img, (x+w, y+h), (x+w, y+h-30), (0,0,0), 2)
        
        
        cv2.rectangle(img, (x+10, y - 30), (x+w-10, y- 10), cor, cv2.FILLED)
        
        cv2.putText(img, "Nome: "+str(id), (x+10,y-15), font, 0.5, (255,255,255), 1)
        cv2.putText(img, str(pronabilidade), (x+w-int(50),y-15), font, 0.5, (255,255,255), 1)
        id = ''
    
    cv2.imshow('Sorria',img) 
    
    k = cv2.waitKey(10) & 0xff    
    if k == 27:
        break
cam.release()
cv2.destroyAllWindows()
