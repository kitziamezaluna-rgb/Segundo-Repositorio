#MEZA LUNA KITZIA SOPHIA
#13/10/2025
#CBTIS89
#Programacion 3°B turno matutino 
#prorama que calcule el iva el descuento y el total a pagar de una compra
import tkinter as tk
from tkinter import messagebox  # Esto nos ayudará a mostrar advertencias de errores que cometa el usuario

# --- FUNCIONES ---
def calcular_iva():
    try:
        cantidad = float(entrada_cantidad.get())
        iva = cantidad * 0.16
        etiqueta_resultado.config(text=f"IVA (16%): ${iva:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor introduzca números válidos")

def calcular_descuento():
    try:
        cantidad = float(entrada_cantidad.get())
        descuento = cantidad * 0.10
        etiqueta_resultado.config(text=f"Descuento (10%): ${descuento:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor introduzca números válidos")

def pago_final():
    try:
        cantidad = float(entrada_cantidad.get())
        iva = cantidad * 0.16
        descuento = cantidad * 0.10
        total = cantidad + iva - descuento
        etiqueta_resultado.config(text=f"Total a pagar: ${total:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor introduzca números válidos")

# --- INTERFAZ GRÁFICA ---
ventana = tk.Tk()
ventana.title("BIENVENIDO: CÁLCULO DE IVA Y DESCUENTO")
ventana.geometry("300x350")
ventana.resizable(False, False)

# Etiquetas y cajas
etiqueta_cantidad = tk.Label(ventana, text="Ingresa el precio del producto")
etiqueta_cantidad.pack(pady=10)

entrada_cantidad = tk.Entry(ventana, justify="center")
entrada_cantidad.pack()

# Botones
btn_iva = tk.Button(ventana, text="Calcular IVA", command=calcular_iva)
btn_iva.pack(pady=5)

btn_descuento = tk.Button(ventana, text="Calcular Descuento", command=calcular_descuento)
btn_descuento.pack(pady=5)

btn_total = tk.Button(ventana, text="Calcular Total a Pagar", command=pago_final)
btn_total.pack(pady=5)

# Resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12, "bold"))
etiqueta_resultado.pack(pady=10)

ventana.mainloop()
