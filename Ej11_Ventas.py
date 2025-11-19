#MEZA LUNA KITZIA SOPHIA
#15/10/2025
#CBTIS89
#Programacion 3°B turno matutino 
#Programa que calcule subtotal iva descuento y total a pagar
import tkinter as tk
from tkinter import messagebox

def Calcular_subtotal():
    try:
        precioA = float(entrada_precioA.get())
        CantidadA = float(entrada_CantidadA.get())
        subtotal = precioA * CantidadA
        etiqueta_resultado.config(text=f"Resultado = ${subtotal:.2f}")
    except ValueError:
        messagebox.showerror("ERROR", "Coloque valores en las dos casillas")
    
def Calcular_iva():
    try:
        precioA = float(entrada_precioA.get())
        CantidadA = float(entrada_CantidadA.get())
        subtotal = precioA * CantidadA
        Iva = subtotal * 0.16
        etiqueta_resultado.config(text=f"IVA (16%) = ${Iva:.2f}")
    except ValueError:
        messagebox.showerror("ERROR", "Coloque valores en las dos casillas")

def Total_pagar():
    try:
        precioA = float(entrada_precioA.get())
        CantidadA = float(entrada_CantidadA.get())
        subtotal = precioA * CantidadA
        Iva = subtotal * 0.16
        total = subtotal + Iva
        etiqueta_resultado.config(text=f"Total a pagar = ${total:.2f}")
    except ValueError:
        messagebox.showerror("ERROR", "Coloque valores en las dos casillas")


ventana = tk.Tk()
ventana.title("CÁLCULO DE VENTAS")
ventana.geometry("300x400")
ventana.resizable(False, False)

etiqueta_cantidad = tk.Label(ventana, text="Cantidad de artículos")
etiqueta_cantidad.pack(pady=5)

entrada_CantidadA = tk.Entry(ventana, justify="center")
entrada_CantidadA.pack()

etiqueta_precioA = tk.Label(ventana, text="Precio por artículo")
etiqueta_precioA.pack()

entrada_precioA = tk.Entry(ventana, justify="center")
entrada_precioA.pack()

btn_subtotal = tk.Button(ventana, text="Subtotal", command=Calcular_subtotal,)
btn_subtotal.pack(pady=5)

btn_iva = tk.Button(ventana, text="IVA", command=Calcular_iva)
btn_iva.pack(pady=5)

btn_total = tk.Button(ventana, text="Total a pagar", command=Total_pagar)
btn_total.pack(pady=5)

etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12, "bold"),fg="#c41616")
etiqueta_resultado.pack(pady=10)

ventana.mainloop()
