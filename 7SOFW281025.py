#es el codigo principal de como tiene que quedar el programa

import tkinter as tk
from tkinter import ttk

# Configuración de colores y fuentes
COLOR_FONDO = "#424242"
COLOR_MENU = "#0d6980"
COLOR_TEXTO = "#4FFFFF"
FUENTE_TITULO = ("Arial", 16, "bold")
FUENTE_TEXTO = ("Arial", 12)

# Ventana principal
root = tk.Tk()
root.title("Aplicación para detectar adicciones")
root.geometry("900x500")
root.config(bg=COLOR_FONDO)

# Frame del menú lateral
menu_frame = tk.Frame(root, bg=COLOR_MENU, width=200)
menu_frame.pack(side="left", fill="y")

# Frame del contenido
contenido_frame = tk.Frame(root, bg=COLOR_FONDO)
contenido_frame.pack(side="right", fill="both", expand=True)

# Función para cambiar de página
def mostrar_pagina(nombre):
    for widget in contenido_frame.winfo_children():
        widget.destroy()
    paginas[nombre]()

# --- Páginas ---
def pagina_bienvenida():
    tk.Label(contenido_frame, text="Bienvenido al software de detección de adicciones a los videojuegos",
             bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_TITULO, wraplength=600).pack(pady=40)
    tk.Label(contenido_frame, text="Aquí podrás realizar un test para evaluar tus hábitos y recibir orientación.",
             bg=COLOR_FONDO, fg="white", font=FUENTE_TEXTO, wraplength=600).pack(pady=20)

def pagina_registro():
    tk.Label(contenido_frame, text="Registro de usuario", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_TITULO).pack(pady=20)
    for campo in ["Nombre:", "Edad:", "Email:"]:
        tk.Label(contenido_frame, text=campo, bg=COLOR_FONDO, fg="white", font=FUENTE_TEXTO).pack()
        tk.Entry(contenido_frame).pack(pady=5)
    ttk.Button(contenido_frame, text="Continuar", command=lambda: mostrar_pagina("test")).pack(pady=20)

def pagina_test():
    tk.Label(contenido_frame, text="Test de adicción a los videojuegos", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_TITULO).pack(pady=20)
    tk.Label(contenido_frame, text="Responde a las siguientes preguntas:", bg=COLOR_FONDO, fg="white", font=FUENTE_TEXTO).pack(pady=10)
    ttk.Button(contenido_frame, text="Ver resultados", command=lambda: mostrar_pagina("resultados")).pack(pady=20)

def pagina_resultados():
    tk.Label(contenido_frame, text="Resultados del test", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_TITULO).pack(pady=20)
    tk.Label(contenido_frame, text="Aquí se mostrarán tus resultados e interpretación.", bg=COLOR_FONDO, fg="white", font=FUENTE_TEXTO).pack(pady=10)

def pagina_sintomas():
    tk.Label(contenido_frame, text="Síntomas y señales de adicción", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_TITULO).pack(pady=20)

def pagina_historias():
    tk.Label(contenido_frame, text="Historias inspiradoras", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_TITULO).pack(pady=20)

def pagina_ayuda():
    tk.Label(contenido_frame, text="Ayuda y recursos", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_TITULO).pack(pady=20)

# Diccionario de páginas
paginas = {
    "Bienvenida": pagina_bienvenida,
    "Registro": pagina_registro,
    "Test": pagina_test,
    "Resultados": pagina_resultados,
    "Síntomas": pagina_sintomas,
    "Historias": pagina_historias,
    "Ayuda": pagina_ayuda,
}

# Botones del menú
for nombre in paginas:
    ttk.Button(menu_frame, text=nombre, command=lambda n=nombre: mostrar_pagina(n)).pack(fill="x", pady=5, padx=10)

ttk.Button(menu_frame, text="Salir", command=root.quit).pack(side="bottom", pady=10)

# Mostrar la página de bienvenida al iniciar
pagina_bienvenida()

root.mainloop()
