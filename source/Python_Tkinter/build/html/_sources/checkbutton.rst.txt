Checkbutton
===========

El widget Checkbutton es un widget estándar de Tkinter que se utiliza para implementar selecciones de encendido/apagado. Los Checkbuttons pueden contener texto o imágenes. 
Al pulsar el botón, Tkinter llama a la función o método indicado.

**Nota:**  Para más información, puede leer nuestro artículo.

1. ¿Qué son los widgets?

2. Descripción general de Python Tkinter

3. Tutorial de Python Tkinter

**Sintaxis del widget Checkbutton de Tkinter**

La sintaxis para usar el botón de verificación se muestra a continuación.

**Sintaxis : Checkbutton (master, options)**

**Parámetros:**


* maestro : Este parámetro se utiliza para representar la ventana principal.
* Opciones : Hay muchas opciones disponibles que pueden utilizarse como pares clave-valor separados por comas.

**Opciones de botón de verificación de Tkinter**

Las siguientes son opciones de uso común que se pueden utilizar con este widget:

* activebackground: Esta opción se utilizaba para representar el color de fondo cuando el botón de verificación estaba debajo del cursor.
* activeforeground: Esta opción se utilizaba para representar el color de primer plano cuando el botón de verificación estaba debajo del cursor.
* bg: Esta opción se utilizaba para representar el color de fondo normal que se mostraba detrás de la etiqueta y el indicador.
* Mapa de bits: Esta opción se utilizaba para mostrar una imagen monocromática en un botón.
* bd: Esta opción se utiliza para representar el tamaño del borde alrededor del indicador y el valor predeterminado es de 2 píxeles.
* comando: Esta opción está asociada a una función que se llamará cuando cambie el estado del botón de verificación.
* cursor: Al usar esta opción, el cursor del ratón cambiará a ese patrón cuando esté sobre el botón de verificación.
* disabledforeground: El color de primer plano utilizado para mostrar el texto de un botón de verificación deshabilitado. El valor predeterminado es una versión punteada 
del 
color de primer plano predeterminado.
* Fuente: Esta opción se utilizaba para representar la fuente utilizada para el texto.
* fg: Esta opción se utilizaba para representar el color utilizado para renderizar el texto.
* altura: Esta opción se utilizaba para representar el número de líneas de texto en el botón de verificación y su valor predeterminado es 1.
* highlightcolor: Esta opción se utilizaba para representar el color del resaltado de enfoque cuando el botón de verificación tenía el foco.
* Imagen: Esta opción se utilizaba para mostrar una imagen gráfica en el botón.
* justificar: Esta opción se utiliza para controlar cómo se justifica el texto: CENTRO, IZQUIERDA o DERECHA.
* Valor de desajuste: La variable de control asociada se establece en 0 por defecto si el botón no está seleccionado. Podemos cambiar el estado de una variable no 
seleccionada a otro valor.
* onvalue: La variable de control asociada se establece en 1 de forma predeterminada si el botón está seleccionado. Podemos cambiar el estado de la variable seleccionada a 
otro valor.
* padx: Esta opción se utilizaba para indicar cuánto espacio dejar a la izquierda y a la derecha del botón de verificación y del texto. Su valor predeterminado es 1 píxel.
* pady: Esta opción se utilizaba para indicar cuánto espacio dejar por encima y por debajo del botón de verificación y el texto. Su valor predeterminado es 1 píxel.
* relieve: El tipo de borde del botón de verificación. Su valor predeterminado es plano.
* selectcolor: Esta opción se utiliza para representar el color del botón de verificación cuando está activado. El valor predeterminado es selectcolor="rojo".
* selectimage: La imagen se muestra en el botón de verificación cuando está configurado.
* Estado: Representa el estado del botón de verificación. Por defecto, está configurado como normal. Podemos cambiarlo a DESACTIVADO para que el botón no responda. El 
botón 
de verificación está ACTIVO cuando tiene el foco.
* texto: Esta opción solía usar saltos de línea ("\n") para mostrar varias líneas de texto.
* Subrayado: Esta opción se utiliza para representar el índice del carácter que se va a subrayar en el texto. La indexación comienza en cero.
* variable: Esta opción se utiliza para representar la variable asociada que realiza un seguimiento del estado del botón de verificación.
* Ancho: Esta opción solía representar el ancho del botón de verificación y también el número de caracteres que se muestran en forma de texto.
longitud de ajuste: Esta opción dividirá el texto en la cantidad de partes especificada.

**Métodos**

Los métodos utilizados en este widget son los siguientes:

* deseleccionar(): Este método se llama para desactivar el botón de verificación.
* flash(): El botón de verificación parpadea entre los colores activo y normal.
* invoke(): Este método invocará el método asociado con el botón de verificación.
* select(): Este método se llama para activar el botón de verificación.
* toggle(): Este método se utiliza para alternar entre los diferentes botones de verificación.

**Botón de verificación con funcionalidad de alternancia**

En este ejemplo, el código siguiente configura una ventana de Tkinter con un botón de verificación llamado «Habilitar función». Al hacer clic, muestra si el botón está 
seleccionado o no. Personaliza la apariencia del botón y le añade una imagen de mapa de bits. Finalmente, el botón se muestra en la ventana y parpadea brevemente.

.. code:: Python

   import tkinter as tk

   def on_button_toggle():
       if var.get() == 1:
           print("Checkbutton is selected")
       else:
           print("Checkbutton is deselected")

   root = tk.Tk()

   # Creating a Checkbutton
   var = tk.IntVar()
   checkbutton = tk.Checkbutton(root, text="Enable Feature", variable=var, 
                             onvalue=1, offvalue=0, command=on_button_toggle)

   # Setting options for the Checkbutton
   checkbutton.config(bg="lightgrey", fg="blue", font=("Arial", 12), 
                   selectcolor="green", relief="raised", padx=10, pady=5)

   # Adding a bitmap to the Checkbutton
   checkbutton.config(bitmap="info", width=20, height=2)

   # Placing the Checkbutton in the window
   checkbutton.pack(padx=40, pady=40)

   # Calling methods on the Checkbutton
   checkbutton.flash()

   root.mainloop()


**Múltiples botones de verificación para la selección**

En este ejemplo, el código siguiente crea una ventana de Tkinter con tres botones de verificación etiquetados como «Tutorial», «Estudiante» y «Cursos». Cada botón alterna 
entre los estados seleccionado y deseleccionado. El tamaño de la ventana está configurado en 300x200 píxeles y cada botón tiene un tamaño de 2x10 unidades.

.. code::

   from tkinter import *

   root = Tk() 
   root.geometry("300x200") 

   w = Label(root, text ='GeeksForGeeks', font = "50") 
   w.pack() 

   Checkbutton1 = IntVar() 
   Checkbutton2 = IntVar() 
   Checkbutton3 = IntVar() 

   Button1 = Checkbutton(root, text = "Tutorial", 
                    variable = Checkbutton1, 
                    onvalue = 1, 
                    offvalue = 0, 
                    height = 2, 
                    width = 10) 

   Button2 = Checkbutton(root, text = "Student", 
                    variable = Checkbutton2, 
                    onvalue = 1, 
                    offvalue = 0, 
                    height = 2, 
                    width = 10) 

   Button3 = Checkbutton(root, text = "Courses", 
                    variable = Checkbutton3, 
                    onvalue = 1, 
                    offvalue = 0, 
                    height = 2, 
                    width = 10) 
    
   Button1.pack() 
   Button2.pack() 
   Button3.pack() 

   mainloop() 


