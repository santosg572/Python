import tkinter as tk

def saludar():
  print("¡Hola, familia!")

# 1. Crear la ventana principal

root = tk.Tk()

# 2. Configurar la ventana
root.title("Mi primera aplicación")
root.geometry("600x300")

ancho = root.winfo_width()
alto = root.winfo_height()
print(ancho)
print(alto)

# 3. Agregar un widget (etiqueta)
etiqueta = tk.Label(root, text="¡Hola, Tkinter!")
etiqueta.pack(pady=5)

boton = tk.Button(root, text="¡Hola, mundo!", command=saludar)
boton.pack(pady=5)

# 4. Iniciar el bucle de eventos

ancho = root.winfo_width()
alto = root.winfo_height()

print(ancho)
print(alto)

root.mainloop()


