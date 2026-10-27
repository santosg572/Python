Frame
=====

Un Frame en Tkinter es un widget de tipo contenedor que se utiliza para agrupar y organizar otros widgets dentro de una ventana. Funciona como una "caja" rectangular que 
ayuda a dividir una interfaz gráfica en secciones, facilitando la gestión del diseño y la disposición de los elementos de la aplicación. 
This video demonstrates how to create a Frame in Tkinter with a red background and other properties:

**Características principales**

* Contenedor de widgets: Su función principal es agrupar otros widgets (como botones, etiquetas, campos de texto) y colocarlos dentro de él.
* Organización de la interfaz: Permite estructurar una interfaz compleja en secciones más pequeñas y manejables, lo que mejora la organización visual y la gestión del 
código.
* Apariencia personalizable: Puedes configurar su ancho, alto, color de fondo, borde y estilo de relieve para que se adapte a tus necesidades de diseño.
* Jerarquía de widgets: Los widgets dentro de un Frame pueden ser gestionados por gestores de geometría como pack, que a su vez pueden anidar otros Frames, creando una 
jerarquía de elementos en la aplicación. 

This video explains the hierarchical structure of Tkinter Frames with a simple analogy:


**Ejemplo de uso**

1. Importar la biblioteca Tkinter.

2. Crear una ventana principal.

3. Instanciar un Frame especificando la ventana como su "padre" (master).

4. Añadir otros widgets al Frame, en lugar de directamente a la ventana, indicando el Frame como su master al crearlos.

5. Usar un gestor de geometría como pack() para mostrar el Frame en la ventana. 

This video shows how to create a Frame and place buttons inside it, demonstrating the concept of placing widgets within a Frame:

---------------------------------------------------------

Python ofrece múltiples opciones para desarrollar interfaces gráficas de usuario (GUI). De entre todos los métodos, Tkinter es el más utilizado. Se trata de una interfaz 
estándar de Python para el kit de herramientas Tk, incluido con Python . Crear una GUI con Python y Tkinter es la forma más rápida y sencilla de desarrollar aplicaciones 
GUI.

**Nota:**  Para más información, puede leer nuestro artículo. 

1. ¿Qué son los widgets?

2. Descripción general de Python Tkinter

3. Tutorial de Python Tkinter

**¿Qué es un Frame en Tkinter?**

Un marco es una región rectangular en la pantalla. También puede usarse como clase base para implementar widgets complejos. Se utiliza para organizar un grupo de widgets.

**Sintaxis del widget Frame de Tkinter**

A continuación se muestra la sintaxis para usar el widget de marco.

**Sintaxis:   w = frame( maestro, opciones)**


**Parámetros:**

* maestro : Este parámetro se utiliza para representar la ventana principal.
* Opciones : Hay muchas opciones disponibles que pueden utilizarse como pares clave-valor separados por comas.

**Opciones de marcos Tkinter**

Las siguientes son opciones de uso común que se pueden utilizar con este widget:

* bg: Esta opción se utilizaba para representar el color de fondo normal que se mostraba detrás de la etiqueta y el indicador.
* bd: Esta opción se utiliza para representar el tamaño del borde alrededor del indicador y el valor predeterminado es de 2 píxeles.
* cursor: Al usar esta opción, el cursor del ratón cambiará a ese patrón cuando esté sobre el marco.
* altura: La dimensión vertical del nuevo marco.
* highlightcolor: Esta opción se utilizaba para representar el color del resaltado de enfoque cuando el marco tenía el enfoque.
* highlightthickness: Esta opción se utilizaba para representar el color del resaltado de enfoque cuando el fotograma no estaba enfocado.
* highlightbackground: Esta opción se utilizaba para representar el grosor del resaltado de enfoque.
* relieve: El tipo de borde del marco. Su valor predeterminado es plano.
* Ancho: Esta opción solía representar el ancho del marco.

**Ejemplo de widget de marco en Tkinter**

En este ejemplo, el código que se muestra a continuación define funciones para crear widgets de Tkinter con opciones personalizadas, lo que facilita su creación con menos 
líneas de código. Genera una interfaz gráfica de usuario (GUI) con una ventana principal que contiene un marco, etiquetas y botones, todos con opciones específicas como el 
color de fondo, el tamaño del borde, el estilo del cursor y más, lo que mejora la coherencia visual y la usabilidad.


.. code:: Python

   import  tkinter  as  tk
​   # Función para crear widgets con todas las opciones
   def  crear_widget ( padre , tipo_widget , ** opciones ):
       Devuelve  widget_type ( padre , ** opciones )
​   # Crea la ventana principal
   ventana  =  crear_widget ( Ninguno , tk . Tk )
   ventana.título ( "Ejemplo de interfaz gráfica de usuario " )
​   # Crea un widget de marco con todas las opciones
   marco  =  crear_widget ( ventana , tk . Marco , bg = 'azul claro' , bd = 3 , cursor = 'mano2' , altura = 100 ,
                      color de resaltado = 'rojo' , grosor de resaltado = 2 , fondo de resaltado = 'negro' ,
                      relieve = tk . ELEVADO , ancho = 200 )
   marco.pack ( padx = 20 , pady = 20 )​​
​   # Crear widget de etiqueta con todas las opciones
   etiqueta  =  crear_widget ( marco , tk . Etiqueta , texto = 'GeeksForGeeks' , fuente = '50' , fondo = 'azul claro' , ancho = 3 , cursor = 'mano2' ,
                      color de resaltado = 'rojo' , grosor de resaltado = 2 , fondo de resaltado = 'negro' ,
                      alivio = tk . ELEVADO )
   etiqueta . paquete ()
​   # Crea un marco para los botones
   button_frame  =  create_widget ( window , tk . Frame , bg = 'lightblue' , bd = 3 , cursor = 'hand2' , height = 50 ,
                              color de resaltado = 'rojo' , grosor de resaltado = 2 , fondo de resaltado = 'negro' ,
                              relieve = tk . ELEVADO , ancho = 200 )
   button_frame.pack ( pady = 10 )​​
​   # Función para crear botones con todas las opciones
   def  crear_botón ( padre , texto , fg ):
       return  create_widget ( parent , tk.Button , text = text , fg = fg , bg = ' lightblue' , bd = 3 , cursor = ' hand2' ,
                         color de resaltado = 'rojo' , grosor de resaltado = 2 , fondo de resaltado = 'negro' ,
                         alivio = tk . ELEVADO )
​   # Crear botones
   botones_info  = [( "Geeks1" , "rojo" ), ( "Geeks2" , "marrón" ), ( "Geeks3" , "azul" ),
                ( "Geeks4" , "verde" ), ( "Geeks5" , "verde" ), ( "Geeks6" , "verde" )]
​   para  texto , fg  en  buttons_info :
       botón  =  crear_botón ( marco_botón , texto = texto , fg = fg )
       botón . pack ( lado = tk . LEFT )
​   # Ejecutar el bucle de eventos de Tkinter
   ventana.bucle principal ( )



