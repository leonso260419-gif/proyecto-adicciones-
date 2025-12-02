#este codigo tiene 1 ventana y un boton que te mete a otra ventana mas chica 

#importar las librerias
import tkinter as tk
def mostrar_ventana2():
    ventana1.withdraw() # esta funcion sirve para que oculte la ventana 1
    ventana2.deiconify()# muestre la ventana 2
def regresar ():
    ventana2.withdraw()
    ventana1.deiconify()

#creacion de ventana 1
ventana1= tk.Tk()
label1=tk.Label(ventana1, text="esta es la vcentana numero 1")
ventana1.geometry("600x400")
ventana1.configure(bg="#FFD700")
label1.pack()
btn1=tk.Button(ventana1, text="ir a la ventana 2",command= mostrar_ventana2)
btn1.pack()

#creacion de ventana 2
ventana2= tk.Tk()
label2=tk.Label(ventana2, text="ir a la ventana numero 2")
ventana2.geometry("300x300")
ventana2.configure(bg="#87CEEB")
label2.pack()
btn2=tk.Button(ventana2, text="ir a la venta 1",command=regresar)
btn2.pack()
ventana2.withdraw()

#creacion de la ventanas (lanzamos la interfaz)
ventana1.mainloop()

