Label
=====

La etiqueta de Tkinter es un widget que se utiliza para implementar cuadros de visualización donde se puede colocar texto o imágenes. El texto que muestra este widget se 
puede modificar en cualquier momento. También se utiliza para realizar tareas como subrayar parte del texto y extenderlo a varias líneas. Es importante tener en cuenta que 
una etiqueta solo puede usar una fuente a la vez para mostrar texto. Para usar una etiqueta, simplemente hay que especificar qué se va a mostrar en ella (puede ser texto, 
un mapa de bits o una imagen).

**Nota:**  Para más información, puede leer nuestro artículo.

1. ¿Qué son los widgets?

2. Descripción general de Python Tkinter

3. Tutorial de Python Tkinter


**Sintaxis del widget de etiquetas de Tkinter**

.. code:: Python

   Sintaxis: Etiqueta (maestro, opción)



**Parámetros:**

* maestro: Esto representa la ventana principal
* Opciones: A continuación se muestra la lista de las opciones más utilizadas para este widget. Estas opciones se pueden usar como pares clave-valor separados por comas.

**Opciones de etiquetas de Tkinter**

* Anchor: Esta opción se utiliza para controlar la posición del texto si el widget dispone de más espacio del necesario. El valor predeterminado es anchor=CENTER, que 
centra 
el texto en el espacio disponible.
* bg: Esta opción se utiliza para establecer el color de fondo normal que se muestra detrás de la etiqueta y el indicador.
* altura: Esta opción se utiliza para establecer la dimensión vertical del nuevo marco.
* Ancho: Ancho de la etiqueta en caracteres (¡no en píxeles!). Si no se especifica esta opción, la etiqueta se ajustará al tamaño de su contenido.
* bd: Esta opción se utiliza para establecer el tamaño del borde alrededor del indicador. El valor predeterminado de bd es de 2 píxeles.
* Fuente: Si está mostrando texto en la etiqueta (con la opción text o textvariable), la opción font se utiliza para especificar en qué fuente se mostrará ese texto en la 
etiqueta.
* cursor: Se utiliza para especificar qué cursor se mostrará al pasar el ratón sobre la etiqueta. Por defecto, se utiliza el cursor estándar.
* `textvariable`: Como su nombre indica, está asociada a una variable de Tkinter (normalmente de tipo `StringVar`) con la etiqueta. Si se modifica la variable, el texto de 
la etiqueta se actualiza.
* Mapa de bits: Se utiliza para asignar el mapa de bits al objeto gráfico especificado, de modo que la etiqueta pueda representar los gráficos en lugar de texto.
* fg: El color de la etiqueta, utilizado para etiquetas de texto y de mapa de bits. El valor predeterminado depende del sistema. Si se muestra un mapa de bits, este es el 
color que aparecerá en la posición de los bits con valor 1 del mapa de bits.
* Imagen: Esta opción se utiliza para mostrar una imagen estática en el widget de etiqueta.
padx: Esta opción se utiliza para agregar espacios adicionales entre la izquierda y la derecha del texto dentro de la etiqueta. El valor predeterminado para esta opción es 
1.
* pady: Esta opción se utiliza para agregar espacios adicionales entre la parte superior e inferior del texto dentro de la etiqueta. El valor predeterminado para esta 
opción 
es 1.
* Justificar: Esta opción define cómo alinear varias líneas de texto. Use IZQUIERDA, DERECHA o CENTRO como valores. Para posicionar el texto dentro del widget, use la 
opción 
de anclaje. El valor predeterminado de justificar es CENTRO.
* relieve: Esta opción se utiliza para especificar la apariencia de un borde decorativo alrededor de la etiqueta. El valor predeterminado para esta opción es plano.
* subrayar: Esto
* longitud de ajuste: En lugar de tener una sola línea como texto de etiqueta, se puede dividir en la cantidad de líneas donde cada línea tiene la cantidad de caracteres 
especificada en esta opción.

**Ejemplo de widget de etiqueta en Tkinter**

En este ejemplo, el código Python que se muestra a continuación crea una ventana de interfaz gráfica de usuario (GUI) de Tkinter con el texto "¡Hola, mundo!". La etiqueta 
tiene estilos definidos con atributos específicos como fuente, color y dimensiones, y está centrada con un borde elevado. Finalmente, se inicia el bucle de eventos 
principal para mostrar la ventana de la GUI hasta que el usuario interactúe con ella.

.. code:: Python

   import tkinter as tk

   #  Create the main window
   root = tk.Tk()
   root.geometry("400x250")  # Set window size
   root.title("Welcome to My App")  # Set window title

   # Create a StringVar to associate with the label
   text_var = tk.StringVar()
   text_var.set("Hello, World!")

   # Create the label widget with all options
   label = tk.Label(root, 
                 textvariable=text_var, 
                 anchor=tk.CENTER,       
                 bg="lightblue",      
                 height=3,              
                 width=30,              
                 bd=3,                  
                 font=("Arial", 16, "bold"), 
                 cursor="hand2",   
                 fg="red",             
                 padx=15,               
                 pady=15,                
                 justify=tk.CENTER,    
                 relief=tk.RAISED,     
                 underline=0,           
                 wraplength=250         
                )

   # Pack the label into the window
   label.pack(pady=20)  # Add some padding to the top


   # Run the main event loop
   root.mainloop()
------------------------------------------------------------------------------------------------



