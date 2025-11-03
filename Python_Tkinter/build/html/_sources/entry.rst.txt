Entry
=====

Python ofrece múltiples opciones para desarrollar una interfaz gráfica de usuario (GUI). De entre todos los métodos, Tkinter es el más utilizado. Python con Tkinter es la 
forma más rápida y sencilla de crear aplicaciones GUI. Crear una GUI con Tkinter es una tarea fácil.

En Python 3, Tkinter viene preinstalado, pero también se puede instalar mediante el siguiente comando: 

.. code:: Python

   pip install tkinter

Ejemplo: Ahora vamos a crear una ventana sencilla usando Tkinter.
 

.. code:: Python

   # creating a simple tkinter window
   # if you are using python2 
   # use import Tkinter as tk  

   import tkinter as tk


   root = tk.Tk()
   root.title("First Tkinter Window")
   root.mainloop()

**El widget de entrada**

El widget de entrada es un widget de Tkinter que se utiliza para introducir o mostrar una sola línea de texto. 
 

Sintaxis: 

**entrada = tk.Entrada(padre, opciones)**

**Parámetros: **
 

1) Ventana principal: La ventana o marco principal en el que se mostrará el widget.

2) Opciones: Las distintas opciones que ofrece el widget de entrada son: 
 
* bg: El color de fondo normal que se muestra detrás de la etiqueta y el indicador. 
* bd: El tamaño del borde alrededor del indicador. El valor predeterminado es de 2 píxeles. 
* Fuente: La fuente utilizada para el texto. 
* fg: El color utilizado para renderizar el texto. 
* justificar: Si el texto contiene varias líneas, esta opción controla cómo se justifica el texto: CENTRO, IZQUIERDA o DERECHA. 
* Relieve: Con el valor predeterminado, relieve=PLANO. Puede configurar esta opción con cualquiera de los otros estilos, como: HUNDIDO, RÍGIDO, ELEVADO, RANURA. 
* mostrar: Normalmente, los caracteres que escribe el usuario aparecen en la entrada. Para crear una entrada .password. que muestre cada carácter como un asterisco, 
configure mostrar="*". 
* textvariable: Para poder recuperar el texto actual de su widget de entrada, debe establecer esta opción en una instancia de la clase StringVar.

**Métodos: Los distintos métodos que proporciona el widget de entrada son: **

* get() : Devuelve el texto actual de la entrada como una cadena. 
* eliminar(): Elimina caracteres del widget 
* insertar ( índice, 'nombre') : Inserta la cadena 'nombre' antes del carácter en el índice dado. 

**Ejemplo:**
 
.. code:: Python

   # Program to make a simple 
   # login screen  

   import tkinter as tk
 
   root=tk.Tk()

   # setting the windows size
   root.geometry("600x400")
 
   # declaring string variable
   # for storing name and password
   name_var=tk.StringVar()
   passw_var=tk.StringVar()

 
   # defining a function that will
   # get the name and password and 
   # print them on the screen
   def submit():
      name=name_var.get()
      password=passw_var.get()
    
      print("The name is : " + name)
      print("The password is : " + password)
    
      name_var.set("")
      passw_var.set("")
        
   # creating a label for 
   # name using widget Label
   name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
 
   # creating a entry for input
   # name using widget Entry
   name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
 
   # creating a label for password
   passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
 
   # creating a entry for password
   passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
 
   # creating a button using the widget 
   # Button that will call the submit function 
   sub_btn=tk.Button(root,text = 'Submit', command = submit)
 
   # placing the label and entry in
   # the required position using grid
   # method
   name_label.grid(row=0,column=0)
   name_entry.grid(row=0,column=1)
   passw_label.grid(row=1,column=0)
   passw_entry.grid(row=1,column=1)
   sub_btn.grid(row=2,column=1)
 
   # performing an infinite loop 
   # for the window to display
   root.mainloop()


