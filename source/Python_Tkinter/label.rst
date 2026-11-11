Label
=====

.. code:: Python

   import tkinter as tk

   root = tk.Tk()
   root.title("Ejemplo Label Básico")
   root.geometry("300x150")

   # Crear y mostrar el Label
   lbl = tk.Label(root, text="¡Hola Mundo!") 
   lbl.pack(pady=40)

   root.mainloop()

**2. Personalizar colores, fuente y tamaño++

.. code:: Python

   import tkinter as tk

   root = tk.Tk()
   root.title("Label Personalizado")
   root.geometry("350x180")

   lbl = tk.Label(
       root,
       text="Texto con Estilo",
       bg="navy",
       fg="white",
       font=("Helvetica", 16, "bold"),
       padx=15,
       pady=10
   )
   lbl.pack(pady=40)

   root.mainloop()

**3. Etiqueta con varias líneas y ajuste de texto (wraplength)**

.. code:: Python

   import tkinter as tk

   root = tk.Tk()
   root.title("Label Multilínea")
   root.geometry("350x200")

   texto_largo = "Este es un texto bastante largo que se ajustará automáticamente a varias líneas usando la propiedad wraplength."

   lbl = tk.Label(
       root,
       text=texto_largo,
       wraplength=280,  # Ancho en píxeles antes de hacer salto de línea
       justify="center",
       font=("Arial", 11)
   )
   lbl.pack(pady=30)

   root.mainloop()

**4. Etiqueta dinámica con StringVar**

.. code:: Python

   import tkinter as tk

   def cambiar_texto():
       mensaje.set("¡El texto ha cambiado con éxito!")

   root = tk.Tk()
   root.title("Label Dinámico")
   root.geometry("350x200")

   mensaje = tk.StringVar()
   mensaje.set("Texto inicial...")

   lbl = tk.Label(root, textvariable=mensaje, font=("Verdana", 12))
   lbl.pack(pady=30)

   btn = tk.Button(root, text="Cambiar Texto", command=cambiar_texto)
   btn.pack(pady=10)

   root.mainloop()

.. code:: Python

   import tkinter as tk

   root = tk.Tk()
   root.title("Varias Labels en Tkinter")
   root.geometry("300x200")

   # Crear y empaquetar varias etiquetas
   label1 = tk.Label(root, text="¡Hola Mundo!")
   label1.pack()

   label2 = tk.Label(root, text="Segunda etiqueta", fg="blue", font=("Arial", 12))
   label2.pack(pady=5)

   label3 = tk.Label(root, text="Tercera etiqueta", fg="red")
   label3.pack()

   root.mainloop()

**2. Forma dinámica usando un bucle (for)**

.. code:: Python

   import tkinter as tk

   root = tk.Tk()
   root.title("Labels con bucle")
   root.geometry("300x250")

   textos = ["Primera opción", "Segunda opción", "Tercera opción", "Cuarta opción"]

   for t in textos:
     lbl = tk.Label(root, text=t, font=("Helvetica", 10))
     lbl.pack(pady=4)  # pady añade espacio vertical entre ellas

   root.mainloop()

**3. Usando .grid() para organizarlas en filas y columnas**

.. code:: Python

   import tkinter as tk

   root = tk.Tk()
   root.title("Grid de Labels")

   tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
   tk.Label(root, text="Juan Pérez").grid(row=0, column=1, padx=5, pady=5)

   tk.Label(root, text="Edad:").grid(row=1, column=0, padx=5, pady=5)
   tk.Label(root, text="30").grid(row=1, column=1, padx=5, pady=5)

   root.mainloop()

**Opción 1: Con Tkinter nativo (Formatos PNG o GIF)**

.. code:: Python

   import tkinter as tk

   root = tk.Tk()
   root.title("Imagen con Label")
   root.geometry("400x300")

   # 1. Cargar la imagen (debe estar en la misma carpeta que tu script)
   imagen = tk.PhotoImage(file="imagen.png")

   # 2. Crear el Label con la imagen
   label = tk.Label(root, image=imagen)
   label.pack(expand=True)

   root.mainloop()

**Opción 2: Con la librería Pillow (Recomendado para JPG, PNG y más)**

.. code:: Bash

   pip install pillow

.. code:: Python

   import tkinter as tk
   from PIL import Image, ImageTk

   root = tk.Tk()
   root.title("Imagen JPG con Label")
   root.geometry("400x300")

   # 1. Abrir la imagen con Pillow
   imagen_pil = Image.open("imagen.jpg")

   # 2. Convertirla a un formato compatible con Tkinter
   imagen_tk = ImageTk.PhotoImage(imagen_pil)

   # 3. Mostrarla en el Label
   label = tk.Label(root, image=imagen_tk)
   label.pack(expand=True)

   # Mantener la referencia viva (truco útil)
   label.image = imagen_tk

   root.mainloop()










