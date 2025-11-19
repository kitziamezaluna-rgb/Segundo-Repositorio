#MEZA LUNA KITZIA SOPHIA
#17/10/2025
#CBTIS89
#Programacion 3°B turno matutino 
#♥
#Programa de radiobotones para calcular descuentos 
import tkinter as tk 

ventana=tk.Tk()
ventana.title("Calcular Descuentos")
ventana.geometry("400x300")


etiqueta_cantidad=tk.Label(ventana, text="Ingresa el precio total de los articulos")
etiqueta_cantidad.pack()

entrada_cantidad=tk.Entry(ventana,justify="center")
entrada_cantidad.pack()

def ejecutar_radio():
    opcion=seleccion.get()

    if opcion ==1:
        cantidad=float(entrada_cantidad.get())
        descuentos=cantidad*0.05
        resultado=cantidad-descuentos
        etiqueta_resultado.config(text=f"Hola estimado cliente \n usted obtuvo un descuento de {descuentos} el cual corresponde al 5% de su compra \n debera de pagar {resultado }")
    elif opcion==2:
        cantidad=float(entrada_cantidad.get())
        descuentos=cantidad*0.10
        resultado=cantidad-descuentos
        etiqueta_resultado.config(text=f"Hola estimado cliente \n usted obtuvo un descuento de {descuentos} el cual corresponde al 10% de su compra \n debera de pagar {resultado}")
    elif opcion==3:
        cantidad=float(entrada_cantidad.get())
        descuentos=cantidad*0.15
        resultado=cantidad-descuentos
        etiqueta_resultado.config(text=f"Hola estimado cliente \n usted obtuvo un descuento de {descuentos} el cual corresponde al 15% de su compra \n debera de pagar {resultado}")
 
 #almacena la opcion seleccionada
seleccion=tk.IntVar()

radioB1=tk.Radiobutton(ventana, text="Descuento del 5%",variable=seleccion,value=1,command=ejecutar_radio)
radioB2=tk.Radiobutton(ventana,text="Descuento del 10%",variable=seleccion,value=2,command=ejecutar_radio)
radioB3=tk.Radiobutton(ventana,text="Descuento del 15%",variable=seleccion,value=3,command=ejecutar_radio)

radioB1.pack(pady=10)
radioB2.pack(pady=10)
radioB3.pack(pady=10)

etiqueta_resultado=tk.Label(ventana,text="",wraplength=350,justify="left")#wraplength para que el texto se ajuste al tamaño de la ventana
etiqueta_resultado.pack(pady=20)

ventana.mainloop()
