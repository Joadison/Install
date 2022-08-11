import os
import time
import datetime, random
from tkinter import ttk
from tkinter import *

def acss():
    mrt1 = mtr.get()
    senha = Senh.get()
    os.system('C:/Windows/System32/net.exe use \\\\10.1.2.60\\tjce\\Aplicativos /u:tjce-dom-01\\%s %s' % (mrt1, senha))
    os.system('start cmdkey /generic:"\\\\10.1.2.60\\tjce\\Aplicativos" /user:"tjce-dom-01\\%s" /pass:"%s" ' % (mrt1, senha))
    os.system('start \\\\10.1.2.60\\tjce\\Aplicativos')

def acssdes():
    os.system('C:/Windows/System32/net.exe use /delete \\\\10.1.2.60\\tjce\\Aplicativos')
    os.system('start cmdkey /delete:\\\\10.1.2.60\\tjce\\Aplicativos')

root = Tk()
root.title('Suporte Remoto')
root.geometry('260x120')
root.configure(background='#71a6ff')
##########################################
#MATRICULA
Lmrt = Label(root,text = "Matrciula",
             foreground="white",
             background="#71a6ff").place(x = 10, y = 10, width=100, height=15)
mtr = Entry(root)
mtr.pack()
mtr.place(x = 35, y = 30, width=100, height=15)
##########################################
#SENHA
Lsenh = Label(root, text = "Senha",
      foreground="white",
      background="#71a6ff",).place(x = 5, y = 55, width=90, height=15)
Senh = Entry(root, show='*')
Senh.pack()
Senh.place(x = 35, y = 80, width=100, height=15)
##########################################
#BUTTON
Butt = Button(root, text="Entrar",
       foreground="white",
       background="#71a6ff",
       command= acss).place(x = 170, y =70, width=50, height=30)

#BUTTON
Butt = Button(root, text="Sair",
       foreground="white",
       background="#71a6ff",
       command= acssdes).place(x = 170, y =20, width=50, height=30)

root.mainloop()
