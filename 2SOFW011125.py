#este codigo da la bienvenida y tiene un boton para iniciar tets


# Importamos las librerías necesarias
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

# Función que se ejecuta con el botón
def iniciar_test():
    messagebox.showinfo("Inicio del test", "Bienvenido al test de adicciones")
    ventanabienv.focus_force()  # Corrección del método

# Configurar la ventana
ventanabienv = tk.Tk()
ventanabienv.title("Software para detectar adicciones a los videojuegos")
ventanabienv.geometry("700x450")
ventanabienv.config(bg="#166FE3")

# Configurar la posición de la pantalla
ancho_pantalla = ventanabienv.winfo_screenwidth()
alto_pantalla = ventanabienv.winfo_screenheight()
x = (ancho_pantalla // 2) - (700 // 2)
y = (alto_pantalla // 2) - (450 // 2)
ventanabienv.geometry(f"600x450+{x}+{y}")

# Título principal
titulo = tk.Label(
    ventanabienv,
    text="BIENVENIDOS A DETECTA VIDEOJUEGOS",
    font=("Arial", 18, "bold"),
    bg="#6AB680",
    fg="#2E2F3A",
    wraplength=550,
    justify="center"
)
titulo.pack(pady=30)

# Insertar una imagen
try:
    imagen = PhotoImage(file="descarga.png")  # Asegúrate de que la imagen esté en la misma carpeta
    img_label = tk.Label(ventanabienv, image=imagen, bg="#1DCCC4")
    img_label.pack(pady=10)
except Exception:
    aviso = tk.Label(ventanabienv, text="No se encontró la imagen", bg="#1DCCC4", fg="green")
    aviso.pack()

# Texto descriptivo
texto = tk.Label(
    ventanabienv,
    text="Este es un software desarrollado para detectar una adicción a los videojuegos en jóvenes.",
    font=("Arial", 12),
    bg="#70E0E0",
    fg="#113636",
    wraplength=500,
    justify="center"
)
texto.pack(pady=20)

# Botón para iniciar el test
boton_iniciar = tk.Button(
    ventanabienv,
    text="INICIAR TEST",
    font=("Arial", 14, "bold"),
    bg= "#858F8F",
    fg="white",
    relief="raised",
    bd=3,
    padx=20,
    pady=10,
    command=iniciar_test
)
boton_iniciar.pack(pady=10)

# Ejecutar la ventana
ventanabienv.mainloop()
