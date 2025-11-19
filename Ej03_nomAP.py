#MEZA LUNA KITZIA SOPHIA
#07/10/2025
#CBTIS89
#Programacion 3°B turno matutino 
#Programa que muestre dos cuadros de texto. Uno para nombre y otro para el apellido. 
# Agrega un botón con el texto Mostrar el Nombre. 
# Al oprimirlo deberá aparecer El nombre y el apellido juntos.
  
import tkinter as tk #tienes que mencionar la libreria
def mostrar_nombre():
    nombre=entrada_nombre.get()
    apellido=entrada_apellido.get()
    etiqueta_resultado.config(text=f"Hola, {nombre }{ apellido}")
#crear la ventana
ventana= tk.Tk()
ventana.title ("Ingresa tu nombre y apellido")
ventana.geometry ("300x200")

#solicita el nombre y pide que ellos lo pongan
etiqueta_nombre= tk.Label(ventana,text="usuario mencione su nombre: ")
etiqueta_nombre.pack()

entrada_nombre=tk.Entry(ventana)
entrada_nombre.pack()
#solicita el nombre y pide que ellos lo pongan
etiqueta_apellido=tk.Label(ventana,text="mencione su apellido : ")
etiqueta_apellido.pack()

entrada_apellido=tk.Entry(ventana)
entrada_apellido.pack()
#boton 
boton_mostrar=tk.Button(ventana,text="revelar nombre",command=mostrar_nombre)
boton_mostrar.pack(pady=10 )
#etiqueta que muestre el resultado despues del boton
etiqueta_resultado=tk.Label (ventana,text="")
etiqueta_resultado.pack()
 #para ejecutar la ventana
ventana.mainloop()