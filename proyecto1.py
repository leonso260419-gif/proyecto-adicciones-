
import tkinter as tk                  
from tkinter import messagebox      


#CLASE PRINCIPAL
class App:
    def __init__(self, root):#constructor de la clase
        # Ventana principal de la aplicación
        self.root = root#guarda la ventana principal
        self.root.title("Detecta Juegos")   #Título de la ventana
        self.root.geometry("420x520") #Tamaño fijo
        self.root.config(bg="#F5F7FA") #Color de fondo general de la ventana
        self.show_welcome_screen() #Llama al metodo para nostrar la pantalla de bienvenida al iniciar

    #MÉTODO PARA LIMPIAR LA VENTANA
    def clear_window(self):#para no ver todos los witgen en las ventanas
        #Elimina todos los widgets (botones, etiquetas, entradas) de la ventana actual
        for widget in self.root.winfo_children():#debuelve los witges hijos a la ventana principal
            widget.destroy()#elimina los witgents de la ventana

    #PANTALLA DE BIENVENIDA
    def show_welcome_screen(self):#metodo de clase
        self.clear_window() # Limpia cualquier ventana anterior
        self.root.config(bg="#F5F7FA")#fondo de ventana
        #Permite que todos los métodos de la clase App puedan modificar la ventana principal sin necesidad de pasarla como parámetro cada vez.
        # cargar imagen
        try:
            logo_img = Image.open("imagen_adiccion.png")     #Abre la imagen
            logo_img = logo_img.resize((120, 120))           #Ajusta su tamaño
            self.logo = ImageTk.PhotoImage(logo_img)          #Convierte a formato compatible con Tkinter
            tk.Label(self.root, image=self.logo, bg="#F5F7FA").pack(pady=10)  #Muestra la imagen
        except:
            #Si no encuentra la imagen
            tk.Label(self.root, text="[Logotipo no encontrado]", bg="#F5F7FA",
                     font=("Arial", 10, "italic")).pack(pady=20)

        #Título de bienvenida
        tk.Label(self.root, text="Bienvenido a Detecta Juegos",
                 font=("Arial", 18, "bold"), bg="#F5F7FA", fg="#0D47A1").pack(pady=10)

        #Botones principales
        tk.Button(self.root, text="Crear cuenta", bg="#1E88E5", fg="white",
                  width=20, command=self.show_create_account, relief="flat").pack(pady=5)
        tk.Button(self.root, text="Iniciar sesión", bg="#00ACC1", fg="white",
                  width=20, command=self.show_login, relief="flat").pack(pady=5)

    #Misión
        tk.Label(self.root,
                 text="Nuestra misión: Ayudarte a detectar y prevenir conductas problemáticas relacionadas con videojuegos.",
                 bg="#F5F7FA", fg="#0D1B2A", font=("Arial", 10, "italic"),
                 wraplength=350, justify="center").pack(pady=15)

    #CREAR CUENTA
    def show_create_account(self):#metodo de clase
        self.clear_window()#limpia la ventana
        self.root.config(bg="#F5F7FA")

        #Título
        tk.Label(self.root, text="Crear Cuenta", font=("Arial", 16, "bold"),
                 bg="#F5F7FA", fg="#0D47A1").pack(pady=10)

        #correo y contraseña
        tk.Label(self.root, text="Correo Electrónico:", bg="#F5F7FA", fg="#0D1B2A").pack()
        tk.Entry(self.root, width=30, relief="groove").pack()
        tk.Label(self.root, text="Contraseña:", bg="#F5F7FA", fg="#0D1B2A").pack()
        tk.Entry(self.root, show="*", width=30, relief="groove").pack()

        #Casilla de términos
        accept_terms = tk.IntVar()
        tk.Checkbutton(self.root, text="Aceptar términos y condiciones",
                       variable=accept_terms, bg="#F5F7FA", fg="#0D1B2A").pack(pady=5)

        #Botones de acción
        tk.Button(self.root, text="Registrar", bg="#1E88E5", fg="white",
                  width=15, command=lambda: messagebox.showinfo("Info", "Cuenta creada con éxito"),
                  relief="flat").pack(pady=5)#organiza los widgets 

        tk.Button(self.root, text="Ir a Iniciar Sesión", bg="#BBDEFB", fg="#0D1B2A",
                  width=15, command=self.show_login, relief="flat").pack(pady=5)#crear botones con acciones asociadas a las ventanas

        tk.Button(self.root, text="Regresar a Bienvenida", bg="#E3F2FD", fg="#0D1B2A",
                  width=15, command=self.show_welcome_screen, relief="flat").pack(pady=5)

#INICIAR SESIÓN
    def show_login(self):
        self.clear_window()
        self.root.config(bg="#F5F7FA")

        tk.Label(self.root, text="Iniciar Sesión", font=("Arial", 16, "bold"),
                 bg="#F5F7FA", fg="#0D47A1").pack(pady=10)

        tk.Label(self.root, text="Correo Electrónico:", bg="#F5F7FA", fg="#0D1B2A").pack()
        tk.Entry(self.root, width=30, relief="groove").pack()
        tk.Label(self.root, text="Contraseña:", bg="#F5F7FA", fg="#0D1B2A").pack()
        tk.Entry(self.root, show="*", width=30, relief="groove").pack()
                            #oculta la contraseña
        tk.Button(self.root, text="Iniciar sesión", bg="#1E88E5", fg="white",
                  width=15, command=self.show_main_menu, relief="flat").pack(pady=5)
                            #al hacer clik se muestra la siguente ventana
        tk.Button(self.root, text="Ir a Crear Cuenta", bg="#BBDEFB", fg="#0D1B2A",
                  width=15, command=self.show_create_account, relief="flat").pack(pady=5)
        tk.Button(self.root, text="Regresar a Bienvenida", bg="#E3F2FD", fg="#0D1B2A",
                  width=15, command=self.show_welcome_screen, relief="flat").pack(pady=5)

#MENÚ PRINCIPAL
    def show_main_menu(self):
        self.clear_window()
        self.root.config(bg="#F5F7FA")

        tk.Label(self.root, text="Menú Principal", font=("Arial", 16, "bold"),
                 bg="#F5F7FA", fg="#0D47A1").pack(pady=10)

        #Botones para navegar a distintas secciones
        tk.Button(self.root, text="Perfil", bg="#1E88E5", fg="white",
                  width=20, command=self.show_profile, relief="flat").pack(pady=5)
        tk.Button(self.root, text="Cuestionario de preguntas", bg="#00ACC1", fg="white",
                  width=20, command=self.show_questionnaire, relief="flat").pack(pady=5)
        tk.Button(self.root, text="Resultado de diagnóstico", bg="#0D47A1", fg="white",
                  width=20, command=self.show_diagnostic_results, relief="flat").pack(pady=5)
        tk.Button(self.root, text="Recursos de ayuda y educación", bg="#BBDEFB", fg="#0D1B2A",
                  width=20, command=lambda: messagebox.showinfo("Info", "Recursos electrónicos"), relief="flat").pack(pady=5)
        tk.Button(self.root, text="Regresar a Iniciar Sesión", bg="#E3F2FD", fg="#0D1B2A",
                  width=20, command=self.show_login, relief="flat").pack(pady=5)

    #PERFIL
    def show_profile(self):
        self.clear_window()
        self.root.config(bg="#F5F7FA")

        tk.Label(self.root, text="Perfil", font=("Arial", 16, "bold"),
                 bg="#F5F7FA", fg="#0D47A1").pack(pady=10)

        tk.Label(self.root, text="Nombre:", bg="#F5F7FA", fg="#0D1B2A").pack()
        tk.Entry(self.root, width=30, relief="groove").pack()
        tk.Label(self.root, text="Edad:", bg="#F5F7FA", fg="#0D1B2A").pack()
        tk.Entry(self.root, width=30, relief="groove").pack()

        tk.Button(self.root, text="Editar", bg="#BBDEFB", fg="#0D1B2A",
                  width=15, command=lambda: messagebox.showinfo("Info", "Editar perfil"), relief="flat").pack(pady=5)
        tk.Button(self.root, text="Guardar", bg="#1E88E5", fg="white",
                  width=15, command=lambda: messagebox.showinfo("Info", "Perfil guardado"), relief="flat").pack(pady=5)
        tk.Button(self.root, text="Regresar a Menú Principal", bg="#E3F2FD", fg="#0D1B2A",
                  width=15, command=self.show_main_menu, relief="flat").pack(pady=5)

    #CUESTIONARIO
    def show_questionnaire(self):
        self.clear_window()
        self.root.config(bg="#F5F7FA")

        tk.Label(self.root, text="Cuestionario de Preguntas", font=("Arial", 16, "bold"),
                 bg="#F5F7FA", fg="#0D47A1").pack(pady=10)
        tk.Label(self.root, text="Pregunta 1: ¿Cuánto tiempo juegas?",
                 bg="#F5F7FA", fg="#0D1B2A").pack(pady=5)
        tk.Entry(self.root, width=30, relief="groove").pack(pady=5)

        tk.Label(self.root, text="Pregunta 2: ¿cuantos dias a la semabna juegas ?",
                 bg="#F5F7FA", fg="#0D1B2A").pack(pady=5)
        tk.Entry(self.root, width=30, relief="groove").pack(pady=5)

        tk.Button(self.root, text="Responder", bg="#1E88E5", fg="white",
                  width=15, command=lambda: messagebox.showinfo("Info", "Respuesta registrada"), relief="flat").pack(pady=5)
        tk.Button(self.root, text="Ver resultados", bg="#00ACC1", fg="white",
                  width=15, command=self.show_diagnostic_results, relief="flat").pack(pady=5)
        tk.Button(self.root, text="Regresar a Menú Principal", bg="#088CF2", fg="#0D1B2A",
                  width=15, command=self.show_main_menu, relief="flat").pack(pady=5)

    #RESULTADOS DEL DIAGNÓSTICO
    def show_diagnostic_results(self):
        self.clear_window()
        self.root.config(bg="#F5F7FA")

        tk.Label(self.root, text="Resultados de Diagnóstico", font=("Arial", 16, "bold"),
                 bg="#F5F7FA", fg="#0D47A1").pack(pady=10)

        #Secciones donde luego se mostrarán datos o gráficas
        tk.Label(self.root, text="Gráfica:", bg="#F5F7FA", fg="#0D1B2A").pack()
        tk.Label(self.root, text="Clasificación de diseño:", bg="#F5F7FA", fg="#0D1B2A").pack()
        tk.Label(self.root, text="Resultados:", bg="#F5F7FA", fg="#0D1B2A").pack()

        #Botones
        tk.Button(self.root, text="Descargar", bg="#1E88E5", fg="white",
                  width=15, command=lambda: messagebox.showinfo("Info", "Información descargada"), relief="flat").pack(pady=5)
        tk.Button(self.root, text="Regresar a Menú Principal", bg="#E3F2FD", fg="#0D1B2A",
                  width=15, command=self.show_main_menu, relief="flat").pack(pady=5)


#ejecutar ventana
if __name__ == "__main__":#sirve para importar
    root = tk.Tk() 
    app = App(root) #comportamiento del sotware
    root.mainloop()
