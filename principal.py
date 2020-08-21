import subprocess, os
import tkinter as tk
from PIL import ImageTk, Image


Image_path="testes.jpg"

def treinar():
    cmd = "python treinar.py"
    subprocess.Popen(cmd)
    #os.system(cmd)

def add_dados():
    cmd = "python dataset.py"
    subprocess.Popen(cmd)
    #os.system(cmd)

def reconhecer():
    cmd = "python projeto.py".split()
    subprocess.Popen(cmd)

root = tk.Tk()
root.title('Reconhecimento Facial')

l = tk.Label(root, text="Bem-Vindo")
l.config(font=("Courier", 15))
l.pack()

img = Image.open(Image_path)
img.resize((250, 250), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

w = img.width()
h = img.height()
root.geometry("%dx%d+0+0" % (w, h - 50))

#tk.Button(root, text = "Adicionar", command = root.destroy).pack()
panel1 = tk.Label(root, image=img)
panel1.pack(side='top', fill='both', expand='no')
panel1.image = img

tk.Button(root, text = "Adicionar Dados", command = add_dados).place(x = 20, y = int(h/2) + 125)
tk.Button(root, text = "Treinar Dados", command = treinar).place(x = (w/2) - 45, y = int(h/2) + 125)
tk.Button(root, text = "Reconhecer", command = reconhecer).place(x = w - 90, y = int(h/2) + 125)
root.mainloop()
