Entry
=====

.. code:: Python

   import tkinter as tk


   def mostrar_texto():
     texto_ingresado = entrada.get()  # Lee el texto del Entry
     etiqueta_resultado.config(text=f"Hola, {texto_ingresado}")


   root = tk.Tk()
   root.title("Ejemplo Básico de Entry")
   root.geometry("300x150")

   # Etiqueta de instrucción
   label = tk.Label(root, text="Escribe tu nombre:")
   label.pack(pady=5)

   # Widget Entry
   entrada = tk.Entry(root, width=25)
   entrada.pack(pady=5)

   # Botón para obtener el texto
   boton = tk.Button(root, text="Saludar", command=mostrar_texto)
   boton.pack(pady=5)

   # Etiqueta para mostrar el resultado
   etiqueta_resultado = tk.Label(root, text="")
   etiqueta_resultado.pack(pady=5)

   root.mainloop()

**2. Campo para contraseña (ocultar caracteres con show="*")**

.. code:: Python

   import tkinter as tk

   root = tk.Tk()
   root.title("Campo de Contraseña")
   root.geometry("250x120")

   tk.Label(root, text="Contraseña:").pack(pady=5)

   # show="*" oculta el texto con asteriscos
   entrada_pass = tk.Entry(root, show="*", width=20)
   entrada_pass.pack(pady=5)


   def ver_password():
     print("Contraseña escrita:", entrada_pass.get())


   tk.Button(root, text="Enviar", command=ver_password).pack(pady=5)

   root.mainloop()

**3. Insertar texto por defecto y limpiar el campo**

.. code:: Python

   import tkinter as tk

   root = tk.Tk()
   root.title("Insertar y Borrar")
   root.geometry("300x150")

   entrada = tk.Entry(root, width=30)
   entrada.pack(pady=10)

   # Inserta texto en la posición 0 (al inicio)
   entrada.insert(0, "Texto predeterminado")


   def limpiar_campo():
     # Borra desde el índice 0 hasta el final (tk.END)
     entrada.delete(0, tk.END)


   boton_limpiar = tk.Button(root, text="Limpiar", command=limpiar_campo)
   boton_limpiar.pack(pady=5)

   root.mainloop()

**4. Usar ttk.Entry (Estilo moderno)**

.. code:: Python

   import tkinter as tk
   from tkinter import ttk

   root = tk.Tk()
   root.title("ttk.Entry Moderno")
   root.geometry("250x120")

   # Colocar el foco automáticamente en el Entry
   entry_moderno = ttk.Entry(root)
   entry_moderno.pack(pady=20)
   entry_moderno.focus()

   root.mainloop()





