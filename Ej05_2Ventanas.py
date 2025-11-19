#MEZA LUNA KITZIA SOPHIA
#07/10/2025
#CBTIS89
#Programacion 3°B turno matutino 
#Realiza un programa con dos botones. 
# Cada botón abrirá una ventana. 
# La primera ventana contendrá etiquetas con tu nombre y apellidos 
# la segunda ventana tendrá el mensaje, «Programado con Python»

import tkinter as tk
from tkinter import Toplevel #esto es para que se puedan abrir mas ventanas

ventana=tk.Tk()
ventana.title("Bienvenido usuario")
ventana.geometry("300x200")
#ventana uno es basicamente en donde va a estar todo cuando ponermos abrir ventana uno es para que aparezca dentro de esta
def abrir_ventana1(): # se esta llamando para que aparezca en la primera ventana
    hija1=Toplevel(ventana)
    hija1.title("nombre y apellido")
    hija1.geometry ("200x200")
    tk.Label (hija1,text ="Nombre: Sophia").pack(pady=5)
    # para hacer esto el tk es un apodo para tkinter, el oack es para decir donde lo queremos 
    # el (pady=5) es para decir que queremos un espacio de 5 pixeles y la y es para decir que lo quieres de arriba para abajo
    tk.Label(hija1, text="Apellido: Luna").pack(pady=5)

def abrir_ventana2():
    hija2=Toplevel(ventana)
    hija2.title("MENSAJE")
    hija2.geometry("200x200")
    tk.Label(hija2,text="esto ha sido creado con python").pack(pady=5)
    tk.Label(hija2,text="gracias :)").pack(pady=20)

#ahora se colocaran los botones en la ventana estos lo que haran sera abrir cada ventana hija dependiendo de lo seleccionado
Btn1= tk.Button(ventana,text="ventana, hija1",command=abrir_ventana1)
Btn1.pack(pady=10)
#el command le dice a python que tiene que hacer cuando el usuario presione el boton
Btn2=tk.Button(ventana,text="ventana, hija2",command=abrir_ventana2)
Btn2.pack(pady=20)
ventana.mainloop()# esto hace que permanezca abiertas las ventanas
