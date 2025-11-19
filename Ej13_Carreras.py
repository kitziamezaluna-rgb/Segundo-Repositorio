#MEZA LUNA KITZIA SOPHIA
#17/10/2025
#CBTIS89
#Programacion 3°B turno matutino 
#♥
#Lista desplegable combo box de carreras
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Lista de carreras")
ventana.geometry("350x200")
ventana.configure(bg="#708090")

etiqueta_escoge = tk.Label(
    ventana,
    text="Escoge la carrera en la que te encuentras",
    font=("Arial", 12, "bold"),
    bg="#708090",
    fg="#ECECEE"
)
etiqueta_escoge.pack(pady=5)

opciones = [
    "ARH", "Arquitectura", "Ecommerce", "CIA",
    "Construcción", "Contabilidad", "Mecatrónica", "Programación"
]

ComboCarreras = ttk.Combobox(ventana, values=opciones, state="readonly")
ComboCarreras.pack(pady=10)

def mostrar_seleccion(event):
    seleccion = ComboCarreras.get()
    etiqueta_carrera.config(
        text=f"Estudiante del CBTIS 89\n Perteneciente a la carrera de: {seleccion}"
    )

ComboCarreras.bind("<<ComboboxSelected>>", mostrar_seleccion)

etiqueta_carrera = tk.Label(ventana, text="", bg="#708090", fg="#ee1414")
etiqueta_carrera.pack(pady=10)

ventana.mainloop()
