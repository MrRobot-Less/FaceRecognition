import cv2, os
import numpy as np
from PIL import Image
import PIL
from tkinter import *

recognizer = cv2.face.LBPHFaceRecognizer_create()
xml_path = 'C:\\Program Files (x86)\\Python37-32\\lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml'
detector = cv2.CascadeClassifier(xml_path)
ids = []
faceSamples=[]

def getImagesAndLabels(path):
    global ids, faceSamples
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
    for imagePath in imagePaths:
        PIL_img = PIL.Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img,'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        print(id)
        faces = detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[x:x+w,y:y+h])
            ids.append(id)
    #return faceSamples,ids

for i in  range(1):
    getImagesAndLabels('dataset')
    recognizer.train(faceSamples, np.array(ids))
recognizer.save('trainer/trainer.yml')
print("TREINAMENTO TERMINADO COM SUCESSO")
#root = Tk(className = 'POPUP')
#root.title('POPUP')
#Label(root, text="TREINAMENTO TERMINADO COM SUCESSO!!!").pack()
#Button(root, text="OK", command=root.destroy).pack()
