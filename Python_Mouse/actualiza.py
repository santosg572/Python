desde la importación de tkinter *
desde tkinter importar ttk
def actualizar_imagen():
    #¿qué debería ir aquí?
    devolver
raíz = Tk()
img1 = FotoImagen(archivo="img01.jpg")
img2 = FotoImagen(archivo="img02.jpg")
label_pic = ttk.Label(raíz, imagen=img1)
botón_actualización = ttk.Button(raíz, texto="Actualizar imagen", comando=actualizar_imagen)
raíz.mainloop()
