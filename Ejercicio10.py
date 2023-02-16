#! /usr/bin/env python3
from tkinter import *
window = Tk()
window.title("Suma de números complejos")
window.geometry('500x200')
lbl = Label(window, text="El resultado dará (a+c)+(b+d)i")
lbl.grid(column=0, row=0)
#Defino las ventanas en donde voy a poder escribir
txt_a = Entry(window,width=10)
txt_b = Entry(window,width=10)
txt_c = Entry(window,width=10)
txt_d = Entry(window,width=10)

#Dichas ventanas las situo
txt_a.grid(column=2, row=1)
txt_b.grid(column=5, row=1)
txt_c.grid(column=2, row=2)
txt_d.grid(column=5, row=2)

#Defino texto para que se entienda qué es lo que hay que escribir siguiente
texta = Label(window, text="a=")
textb = Label(window, text="b=")
textc = Label(window, text="c=")
textd = Label(window, text="d=")
#Ubico estas etiquetas
texta.grid(column=1, row=1)
textb.grid(column=3, row=1)
textc.grid(column=1, row=2)
textd.grid(column=3, row=2)

#Ahora defino la función lo que va a hacer, osea sumar los numeros complejos
def clicked ():
  ac = float(txt_a.get())+float(txt_c.get())
  bd = float(txt_b.get())+float(txt_d.get())
  lbl.configure(text= "%.3f i + %.3f" % (ac, bd))
btn = Button(window, text="Sumar", command=clicked)
btn.grid(column=0, row=4)
window.mainloop()
