#MEZA LUNA KITZIA SOPHIA
#13/10/2025
#CBTIS89
#Programacion 3°B turno matutino
#Programa que salude al usuario (proyectado por maestra)


#importamos la libreria tkinter y le damos un alias tk
import tkinter as tk

#crea la ventana principal
ventana=tk.Tk() #instancia principal de la aplicacion

#configurar el titulo de la ventana
ventana.title("ventana de saludo")

#definir el tamaño de la ventana (ancho x alto)
ventana.geometry("400x300")

#agregar un texto (etiqueta)
etiqueta=tk.Label(ventana,text="¡hola, buenos dias !",font=("Arial",16))
etiqueta.pack(pady=20)#pack coloca el elemento en ka ventana y el pady es como se coloca

#agregar boton
def saludar():
    etiqueta.config(text="¡que tal!. ¿como te va tu dia?")

boton=tk.Button(text="saludar",command=saludar)
boton.pack(pady=10)
#ejecutar el bucle principa, de la aplicacion
ventana.mainloop()