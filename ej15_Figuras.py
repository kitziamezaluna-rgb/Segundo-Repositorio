#MEZA LUNA KITZIA SOPHIA
#17/10/2025
#CBTIS89
#Programacion 3°B turno matutino 
#♥
#Programa para aprender a utilizar el pillow y muestre figruas geometricas

# ...existing code...
import tkinter as tk
import os
 
from tkinter import ttk

# Intentar importar Pillow; si no está, el programa funciona sin mostrar imágenes
try:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
except Exception:
    PIL_AVAILABLE = False

# Ruta base del archivo actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Diccionario con rutas completas a las imágenes (si existen)
figuras = {
    "Cuadrado": os.path.join(BASE_DIR, "cuadrado.png"),
    "Rectángulo": os.path.join(BASE_DIR, "rectangulo.png"),
    "Círculo": os.path.join(BASE_DIR, "circulo.png"),
    "Triángulo": os.path.join(BASE_DIR, "triangulo.png")
}

def mostrar_imagen(event):
    sel = lista_figuras.curselection()
    if not sel:
        return
    seleccion = lista_figuras.get(sel)
    ruta = figuras.get(seleccion)

    if not PIL_AVAILABLE:
        etiqueta_imagen.config(text=f"Pillow no instalado. Seleccionado: {seleccion}", image="")
        etiqueta_imagen.image = None
        return

    if not ruta or not os.path.exists(ruta):
        etiqueta_imagen.config(text="Imagen no encontrada", image="")
        etiqueta_imagen.image = None
        return

    try:
        imagen = Image.open(ruta)
        imagen = imagen.resize((200, 200), Image.LANCZOS)
        imagen_tk = ImageTk.PhotoImage(imagen)
        etiqueta_imagen.config(image=imagen_tk, text="")
        etiqueta_imagen.image = imagen_tk  # mantener referencia
    except Exception:
        etiqueta_imagen.config(text="Error al cargar imagen", image="")
        etiqueta_imagen.image = None

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Visualizador de Figuras y Operaciones")
ventana.geometry("480x520")

# Título
titulo = tk.Label(ventana, text="Selecciona una figura:", font=("Arial", 14))
titulo.pack(pady=10)

# Listbox de figuras (pack fuera del bucle)
lista_figuras = tk.Listbox(ventana, font=("Arial", 12), height=4)
for figura in figuras.keys():
    lista_figuras.insert(tk.END, figura)
lista_figuras.pack(padx=10)

# Etiqueta para imagen o mensajes
etiqueta_imagen = tk.Label(ventana, text="")
etiqueta_imagen.pack(pady=10)

# Evento al seleccionar
lista_figuras.bind("<<ListboxSelect>>", mostrar_imagen)


# Ejecutar
ventana.mainloop()
# ...existing code...