#MEZA LUNA KITZIA SOPHIA
#13/10/2025
#CBTIS89
#Programacion 3°B turno matutino
#codigo que pida al usuario una contraseña la cual es MELK140509
import tkinter as tk
from tkinter import messagebox

# Función para verificar la contraseña
def verificar_password():
   password = entrada_password.get()
   if password == "MELK140509":
      messagebox.showinfo("Resultado", "Acceso correcto")
   else:
      messagebox.showwarning("Resultado", "Acceso denegado")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Verificador de acceso")
ventana.geometry("300x150")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingresa la contraseña:")
etiqueta.pack(pady=10)

# Cuadro de texto (password)
entrada_password = tk.Entry(ventana, show="*")
entrada_password.pack()

# Botón
boton_verificar = tk.Button(ventana, text="Verificar", command=verificar_password)
boton_verificar.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()