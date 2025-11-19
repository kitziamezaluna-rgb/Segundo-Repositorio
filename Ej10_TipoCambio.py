#MEZA LUNA KITZIA SOPHIA
#15/10/2025
#CBTIS89
#Programacion 3°B turno matutino 
#prorama que  haga tipos de cambios

import tkinter as tk
from tkinter import messagebox

def calcular_dolares():
    try:
        dinero=float(entrada_dinero.get())
        dolares=dinero*18.45
        etiqueta_cambio.config(text=f"el resultado del cambio es de ${dolares:.2f}")
    except ValueError:
        messagebox.showerror("ERROR","\n Coloque una cantidad de dinero ")

def calcular_euros():
    try:
        dinero=float(entrada_dinero.get())
        euros=dinero*21.46
        etiqueta_cambio.config(text=f"el resultado del cabio es de ${euros:.2f}")
    except ValueError:
        messagebox.showerror("ERROR","\n Coloque una cantidad de dinero")

def calcular_libras():
    try:
        dinero=float(entrada_dinero.get())
        libras=dinero*24.66
        etiqueta_cambio.config(text=f"el resultado del cabio es de ${libras:.2f}")
    except ValueError:
        messagebox.showerror("ERROR","\n Coloque una cantidad de dinero")

def calcular_yenes():
    try:
        dinero=float(entrada_dinero.get())
        yenes=dinero*0.12
        etiqueta_cambio.config(text=f"el resultado del cabio es de ${yenes:.2f}")
    except ValueError:
        messagebox.showerror("ERROR","\n Coloque una cantidad de dinero")

ventana=tk.Tk ()
ventana.title("DIVISAS")
ventana.geometry("400x300")
ventana.resizable(False,False)

etiqueta_dinero=tk.Label(ventana,text="CANTIDAD")
etiqueta_dinero.pack(pady=5)

entrada_dinero=tk.Entry(ventana,text="Calculando cambio")
entrada_dinero.pack()

btn_dolares=tk.Button(ventana,text="Dolares",command=calcular_dolares)
btn_dolares.pack(pady=5)
btn_euros=tk.Button(ventana,text="Euros",command=calcular_euros)
btn_euros.pack(pady=5)
btn_libras=tk.Button(ventana,text="Libras",command=calcular_libras)
btn_libras.pack(pady=5)

etiqueta_cambio=tk.Label(ventana,text="",font=("Arial",12,"bold"))
etiqueta_cambio.pack(pady=10)

ventana.mainloop()
