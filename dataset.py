import cv2, os, subprocess
from tkinter import *
from datetime import datetime

root = Tk(className = 'reconhecimento_facial_principal')
root.title('Reconhecimento Facial')

nomevalue = StringVar()
emailvalue = StringVar()
idadevalue = StringVar()
statusvalue = StringVar()
hobbyvalue = StringVar()

l = Label(root, text="Adicionar Nova Pessoa")
l.config(font=("Courier", 15))
l.pack()

Label(root, text="Nome: ").pack()
w1 = Entry(root, textvariable=nomevalue).pack()

Label(root, text="Data de Nascimento: ").pack()
w3 = Entry(root, textvariable=idadevalue).pack()

Label(root, text="E-mail: ").pack()
w2 = Entry(root, textvariable=emailvalue).pack()

Label(root, text="Status: ").pack()
w4 = Entry(root, textvariable=statusvalue).pack()

Label(root, text="Hobby: ").pack()
w5 = Entry(root, textvariable=hobbyvalue).pack()

texto = 1
def reset():
    global texto
    try:
        if(texto <= 1):
            cmd = 'del /Q dataset'.split()
            subprocess.Popen(cmd,shell=True)
            cmd = 'del /Q trainer'.split()
            subprocess.Popen(cmd,shell=True)
            path = "BD"
            arq = [os.path.join(path,f) for f in os.listdir(path)] 
            for i in arq:
                a = open(i, "w")
                a.write("")
                a.close()
            Label(root, text="Banco Restaurado com sucesso").pack()
            texto+=1
    except:
        if(texto <= 1):
            Label(root, text="Banco não restaurado").pack()
            texto+=1
        
def adiciona_pessoa_btn():
    
    Nome = nomevalue.get()
    Email = emailvalue.get()
    Idade = idadevalue.get()
    Status = statusvalue.get()
    Hobby = hobbyvalue.get()
    if len(Nome.split()) > 1:
        Nome = Nome.split()[0]
    if(len(Hobby) >= 4):
        arq = open("BD\\hobby.txt", "r").read()
        arq2 = open("BD\\hobby.txt", "w")
        arq2.write(arq+str(Hobby)+"\n")
        arq2.close()
    if(Status != ""):
        arq = open("BD\\status.txt", "r").read()
        arq2 = open("BD\\status.txt", "w")
        arq2.write(arq+str(Status)+"\n")
        arq2.close()
    else:
        Status = "Dado Desconhecido"
        arq = open("BD\\status.txt", "r").read()
        arq2 = open("BD\\status.txt", "w")
        arq2.write(arq+str(Status)+"\n")
        arq2.close()
    if(len(Idade) == 8 or len(Idade) == 10):
        arq = open("BD\\idades.txt", "r").read()
        arq2 = open("BD\\idades.txt", "w")
        arq2.write(arq+str(Idade)+"\n")
        arq2.close()
    else:
        Idade = "Dado Desconhecido"
        arq = open("BD\\idades.txt", "r").read()
        arq2 = open("BD\\idades.txt", "w")
        arq2.write(arq+str(Idade)+"\n")
        arq2.close()
    if "@" in Email:
        arq = open("BD\\email.txt", "r").read()
        arq1 = open("BD\\email.txt", "w")
        arq1.write(arq+Email+"\n")
        arq1.close()
    else:
        Email = "Dado Desconhecido"
        arq = open("BD\\email.txt", "r").read()
        arq1 = open("BD\\email.txt", "w")
        arq1.write(arq+Email+"\n")
        arq1.close()
    root.destroy()
    if(Nome != ""):
        vid_cam = cv2.VideoCapture(1)
        xml_path = 'C:\\Program Files (x86)\\Python37-32\\lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml'
        face_detector = cv2.CascadeClassifier(xml_path)
        nomes = open('BD\\nomes.txt', 'r').read()
        nomes = nomes.split()

        face_id = len(nomes)
        nomes.append(Nome)
        nomes = "\n".join(nomes)
        nome = open('BD\\nomes.txt', 'w')
        nome.write(nomes)
        nome.close()
        count = 0

        while True:
            print(count)
            _, image_frame = vid_cam.read()
            image_frame = cv2.flip(image_frame,180)
            gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                rosto = gray[y:y+h,x:x+w]
                cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
                lang, alt = rosto.shape
                if(lang * alt <= 20*20):
                    continue
                count += 1
                rosto = cv2.resize(rosto, (255,255))
                cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", rosto)
            cv2.imshow('frame', image_frame)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break


            elif count >= 150:
                break
            
        vid_cam.release()
        cv2.destroyAllWindows()
add_btn = Button(root, text = "Adicionar", command = adiciona_pessoa_btn)
add_btn.pack()

add_btn2 = Button(root, text = "Resetar Banco de Dados", command = reset)
add_btn2.pack()

root.mainloop()

