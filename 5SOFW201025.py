import tkinter as tk

# Función para ir de una ventana a otra
def ir_a(actual, siguiente):
    actual.withdraw()  # Oculta la ventana actual
    siguiente.deiconify()  # Muestra la siguiente ventana

# Función para regresar de una ventana a otra
def regresar(actual, anterior):
    actual.withdraw()
    anterior.deiconify()

# Ventana de bienvenida
ventana_bien = tk.Tk()
ventana_bien.title("1 - Ventana de Bienvenida")
ventana_bien.geometry("600x400")

tk.Label(ventana_bien, text="Bienvenido al software de detección de adicciones a los videojuegos").pack(pady=20)
tk.Label(ventana_bien, text="Descripción del programa...").pack()
btn1 = tk.Button(ventana_bien, text="Iniciar", command=lambda: ir_a(ventana_bien, ventana2))
btn1.pack(pady=30)

# Ventana de registro (oculta al inicio)
ventana2 = tk.Toplevel()
ventana2.title("2 - Ventana de Registro")
ventana2.geometry("600x400")
ventana2.withdraw()

tk.Label(ventana2, text="Registro de usuario").pack(pady=20)
tk.Label(ventana2, text="Nombre:").pack()
tk.Entry(ventana2).pack()
tk.Label(ventana2, text="Edad:").pack()
tk.Entry(ventana2).pack()
tk.Label(ventana2, text="Email:").pack()
tk.Entry(ventana2).pack()

tk.Button(ventana2, text="Regresar", command=lambda: regresar(ventana2, ventana_bien)).pack(side="left", padx=50, pady=40)
tk.Button(ventana2, text="Continuar", command=lambda: ir_a(ventana2, ventana3)).pack(side="right", padx=50, pady=40)

# Ventana del test (oculta al inicio)
ventana3 = tk.Toplevel()
ventana3.title("3 - Ventana Test Adicciones")
ventana3.geometry("600x400")
ventana3.withdraw()

tk.Label(ventana3, text="Esta es la ventana donde se incluirá el test para adicciones").pack(pady=20)
tk.Label(ventana3, text="Responde a las siguientes preguntas", wraplength=500).pack(pady=50)

tk.Button(ventana3, text="Regresar", command=lambda: regresar(ventana3, ventana2)).pack(side="left", padx=50, pady=40)
tk.Button(ventana3, text="Continuar", command=lambda: print("Ir a ventana4")).pack(side="right", padx=50, pady=40)

# Ejecutar la ventana principal
ventana_bien.mainloop()
