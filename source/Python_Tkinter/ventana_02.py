import tkinter as tk

# 1. Crear la ventana principal
root = tk.Tk()

# 2. Configurar la ventana
root.title("Mi primera aplicación")
root.geometry("400x300")

# 3. Agregar un widget (etiqueta)
etiqueta = tk.Label(root, text="¡Hola, Tkinter!")
etiqueta.pack(pady=50)

# 4. Iniciar el bucle de eventos
root.mainloop()


