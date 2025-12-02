#ventana que se oculta al mostrar otra ventana
import tkinter as tk

def mostrar_ventana2():
    ventana1.withdraw()  # Oculta la ventana 1
    ventana2.deiconify()  # Muestra la ventana 2

def regresar():
    ventana2.withdraw()  # Oculta la ventana 2
    ventana1.deiconify()  # Muestra la ventana 1

# Creación de ventana 1
ventana1 = tk.Tk()
ventana1.geometry("600x400")
ventana1.configure(bg="#FFD700")  # Color de fondo para la ventana 1 (ej. dorado)

label1 = tk.Label(ventana1, text="Esta es la ventana número 1", bg="#FFD700")
label1.pack()

btn1 = tk.Button(ventana1, text="Ir a la ventana 2", command=mostrar_ventana2,)
btn1.pack()

# Creación de ventana 2
ventana2 = tk.Tk()
ventana2.withdraw()
ventana2.geometry("300x300")
ventana2.configure(bg="#87CEEB")  # Color de fondo para la ventana 2 (ej. azul claro)

label2 = tk.Label(ventana2, text="Ir a la ventana número 2", bg="#87CEEB")
label2.pack()

btn2 = tk.Button(ventana2, text="Ir a la ventana 1", command=regresar,)
btn2.pack()

ventana2.withdraw()

# Creación de la interfaz (lanzamos la ventana)
ventana1.mainloop()