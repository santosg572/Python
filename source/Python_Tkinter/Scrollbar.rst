Scrollbar
=========

.. code:: Python

   import tkinter as tk

   # Crear la ventana principal
   ventana = tk.Tk()
   ventana.title("Ejemplo de Scrollbar con Text")
   ventana.geometry("400x300")

   # 1. Crear el widget de Scrollbar
   scrollbar = tk.Scrollbar(ventana, orient="vertical")
   scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

   # 2. Crear el widget de Text y vincularlo con el Scrollbar
   texto = tk.Text(ventana, yscrollcommand=scrollbar.set)
   texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

   # 3. Configurar la acción del Scrollbar para mover el texto
   scrollbar.config(command=texto.yview)

   # Insertar texto de prueba para ver el scroll en funcionamiento
   for i in range(1, 51):
     texto.insert(tk.END, f"Esta es la línea de texto número {i}\n")

   # Iniciar el bucle de la aplicación
   ventana.mainloop()



