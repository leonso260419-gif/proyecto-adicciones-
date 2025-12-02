#este codigo te da la bienvenida y tiene un boton de iniciar tets

#importamos las librerias necesarias
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
#funcion que se ejecuta con el boton
def iniciar_test():
    messagebox.showinfo("inicio del test", "bienvenido al test de adicciones")
    ventanabienv.destroy()


#configurar la ventana
ventanabienv=tk.Tk()
ventanabienv.title("Sotware para detectar adicciones a los videojuegos ")
ventanabienv.geometry("600x400")
ventanabienv.config(bg= "#A6E053")#color de fondo

#configurar posicion de la pantalla
ancho_pantalla = ventanabienv.winfo_screenmmwidth()
alto_pantalla=ventanabienv.winfo_screenheight()
x=(ancho_pantalla// 2) - (600 // 2)
y=(alto_pantalla//2)- (400 // 2)
ventanabienv.geometry(f"700x450+{x}+{y}")

#configurar los widgets o elementos graficos 
#bienvenida principal

titulo = tk.Label(
    ventanabienv,
    text="BIENVENIDOS A DETECTA VIDEOJUGEGOS",
    font=("Arial", 18, "bold"),
    bg="#276FF5",
    fg= "#A6E053",
    wraplength= 550,
    justify="center"
)

titulo.pack(pady=30)
#insertar una imagen
try:
    imagen = PhotoImage(File="descarga.png")
    img_tabel = tk.Label (ventanabienv, imagen=imagen, bg= "#1DCCC4")
    img_tabel.pack(pady=10)
except Exception:
    aviso = tk.Label(ventanabienv, text ="no se encuentro la imagen", bg= "#1DCCC4",fg= "green")
    aviso.pack()

 #texto descriptivo
texto=tk.Label(
    ventanabienv,
    text=("Esto es un sotware desarrollado para detectar una adiccion a los videojuegos en jovenes "
),
font= ("Arial",12,),
bg= "#70E0E0",
fg="#113636",
wraplength=500,
justify="center",
)
texto.pack(pady=20)
#elemento para iniciar el test
boton_iniciar = tk.Button(
    ventanabienv,
    text="inicio TEST",
    font=("Arial", 14, "bold"),
    bg= "#858F8F",
    fg="white",
    relief="raised",
    bd=3,
    padx=20,
    pady=10,
    command= iniciar_test 
)
boton_iniciar.pack(pady=10)
#ejecutar ventana
ventanabienv.mainloop()