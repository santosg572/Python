Quick start guide
=================

https://matplotlib.org/stable/users/explain/quick_start.html

This tutorial covers some basic usage patterns and best practices to help you get started with Matplotlib.

Este tutorial cubre algunos patrones de uso básicos y mejores prácticas para ayudarlo a comenzar con Matplotlib.


.. code:: Python

   import matplotlib.pyplot as plt
   import numpy as np

A simple example
----------------

Matplotlib graphs your data on ``Figure`` s (e.g., windows, Jupyter widgets, etc.), each of which can 
contain one or more ``Axes``, an area 
where points can be specified in terms of x-y coordinates (or theta-r in a polar plot, x-y-z in a 3D plot, etc.). The simplest way of 
creating a Figure with an Axes is using ``pyplot.subplots``. We can then use ``Axes.plot`` to draw some data on the Axes, 
and ``show`` to display 
the figure:

Matplotlib grafica los datos en figuras (p. ej., ventanas, widgets de Jupyter, etc.), cada una de las cuales puede contener uno o más ejes, un área donde se pueden especificar puntos en términos de coordenadas x-y (o theta-r en un gráfico polar, x-y-z en un gráfico 3D, etc.). La forma más sencilla de crear una figura con ejes es usar pyplot.subplots. Podemos usar Axes.plot para dibujar datos en los ejes y mostrar la figura:


.. code:: Python

   fig, ax = plt.subplots()             # Create a figure containing a single Axes.
   ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
   plt.show()                           # Show the figure.

Depending on the environment you are working in, plt.show() can be left out. This is for example the case with Jupyter notebooks, 
which automatically show all figures created in a code cell.

Según el entorno en el que trabaje, plt.show() puede omitirse. Este es el caso, por ejemplo, de los cuadernos Jupyter, que muestran automáticamente todas las figuras creadas en una celda de código.


Parts of a Figure
-----------------

Here are the components of a Matplotlib Figure.

Figure
------

The whole figure. The Figure keeps track of all the child Axes, a group of 'special' Artists 
(titles, figure legends, colorbars, etc.), and even nested subfigures.

La figura completa. La figura registra todos los ejes secundarios, un grupo de artistas especiales (títulos, leyendas de figuras, barras de colores, etc.) e incluso subfiguras anidadas.


Typically, you'll create a new Figure through one of the following functions:

Normalmente, crearás una nueva figura a través de una de las siguientes funciones:

.. code:: Python

   fig = plt.figure()             # an empty figure with no Axes
   fig, ax = plt.subplots()       # a figure with a single Axes
   fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
   # a figure with one Axes on the left, and two on the right:
   fig, axs = plt.subplot_mosaic([['left', 'right_top'],
                               ['left', 'right_bottom']])

``subplots()`` and ``subplot_mosaic`` are convenience functions that additionally create Axes objects inside 
the Figure, but you can also manually add Axes later on.

subplots() y subplot_mosaic son funciones de conveniencia que además crean objetos Axes dentro de la Figura, pero también puedes agregar Axes manualmente más adelante.


For more on Figures, including panning and zooming, see Introduction to Figures.

Para obtener más información sobre las figuras, incluido el desplazamiento panorámico y el zoom, consulte Introducción a las figuras.

**Axes**

An Axes is an Artist attached to a Figure that contains a region for plotting data, and usually 
includes two (or three in the case of 3D) Axis objects (be aware of the difference between Axes and 
Axis) that provide ticks and tick labels to provide scales for the data in the Axes. Each Axes also 
has a title (set via set_title()), an x-label (set via set_xlabel()), and a y-label set via 
set_ylabel()).

Un Eje es un objeto asociado a una Figura que contiene una región para representar datos y suele incluir dos objetos Eje (o tres en el caso de 3D) (tenga en cuenta la diferencia entre Ejes y Eje) que proporcionan marcas y etiquetas para escalar los datos en los Ejes. Cada Eje también tiene un título (definido mediante set_title()), una etiqueta x (definido mediante set_xlabel()) y una etiqueta y (definido mediante set_ylabel()).

The Axes methods are the primary interface for configuring most parts of your plot (adding data, 
controlling axis scales and limits, adding labels etc.).

Los métodos de Ejes son la interfaz principal para configurar la mayoría de las partes de su gráfico (agregar datos, controlar escalas y límites de ejes, agregar etiquetas, etc.).


**Axis**

These objects set the scale and limits and generate ticks (the marks on the Axis) and ticklabels 
(strings labeling the ticks). The location of the ticks is determined by a Locator object and the 
ticklabel strings are formatted by a Formatter. The combination of the correct Locator and Formatter 
gives very fine control over the tick locations and labels.

Estos objetos establecen la escala y los límites, y generan marcas (las marcas en el eje) y etiquetas de marca (cadenas que las etiquetan). La ubicación de las marcas se determina mediante un objeto localizador, y las cadenas de etiquetas se formatean mediante un formateador. La combinación correcta del localizador y el formateador proporciona un control preciso sobre la ubicación y las etiquetas de las marcas.


**Artist**

Basically, everything visible on the Figure is an Artist (even Figure, Axes, and Axis objects). This 
includes Text objects, Line2D objects, collections objects, Patch objects, etc. When the Figure is 
rendered, all of the Artists are drawn to the canvas. Most Artists are tied to an Axes; such an 
Artist cannot be shared by multiple Axes, or moved from one to another.

Básicamente, todo lo visible en la Figura es un Artista (incluso la Figura, los Ejes y los objetos de Eje). Esto incluye objetos de Texto, objetos de Línea 2D, objetos de Colección, objetos de Parche, etc. Al renderizar la Figura, todos los Artistas se dibujan en el lienzo. La mayoría de los Artistas están vinculados a un Eje; un Artista de este tipo no puede ser compartido por varios Ejes ni transferido de uno a otro.


Types of inputs to plotting functions
-------------------------------------

Plotting functions expect numpy.array or numpy.ma.masked_array as input, or objects that can be 
passed to numpy.asarray. Classes that are similar to arrays ('array-like') such as pandas data 
objects and numpy.matrix may not work as intended. Common convention is to convert these to 
numpy.array objects prior to plotting. For example, to convert a numpy.matrix

Las funciones de representación gráfica esperan numpy.array o numpy.ma.masked_array como entrada, u objetos que se puedan pasar a numpy.asarray. Las clases similares a arrays (similares a arrays), como los objetos de datos de Pandas y numpy.matrix, podrían no funcionar correctamente. La convención habitual es convertirlos en objetos numpy.array antes de representar gráficamente. Por ejemplo, para convertir un objeto numpy.matrix


.. code:: Python

   b = np.matrix([[1, 2], [3, 4]])
   b_asarray = np.asarray(b)

Most methods will also parse a string-indexable object like a dict, a structured numpy array, or a 
pandas.DataFrame. Matplotlib allows you to provide the data keyword argument and generate plots 
passing the strings corresponding to the x and y variables.

La mayoría de los métodos también analizan objetos indexables por cadenas, como un diccionario, una matriz numpy estructurada o un pandas.DataFrame. Matplotlib permite proporcionar el argumento de la palabra clave "data" y generar gráficos pasando las cadenas correspondientes a las variables "x" e "y".


.. code:: Python

   np.random.seed(19680801)  # seed the random number generator.
   data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
   data['b'] = data['a'] + 10 * np.random.randn(50)
   data['d'] = np.abs(data['d']) * 100

   fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
   ax.scatter('a', 'b', c='c', s='d', data=data)
   ax.set_xlabel('entry a')
   ax.set_ylabel('entry b')

Coding styles
-------------

**The explicit and the implicit interfaces**

As noted above, there are essentially two ways to use Matplotlib:

* Explicitly create Figures and Axes, and call methods on them (the "object-oriented (OO) style").

* Rely on pyplot to implicitly create and manage the Figures and Axes, and use pyplot functions for plotting.

See Matplotlib Application Interfaces (APIs) for an explanation of the tradeoffs between the 
implicit and explicit interfaces.

Consulte Interfaces de aplicación (API) de Matplotlib para obtener una explicación de las compensaciones entre las interfaces implícitas y explícitas.


So one can use the OO-style

.. code:: Python

   x = np.linspace(0, 2, 100)  # Sample data.

   # Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
   fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
   ax.plot(x, x, label='linear')  # Plot some data on the Axes.
   ax.plot(x, x**2, label='quadratic')  # Plot more data on the Axes...
   ax.plot(x, x**3, label='cubic')  # ... and some more.
   ax.set_xlabel('x label')  # Add an x-label to the Axes.
   ax.set_ylabel('y label')  # Add a y-label to the Axes.
   ax.set_title("Simple Plot")  # Add a title to the Axes.
   ax.legend()  # Add a legend.

or the pyplot-style:

.. code:: Python

   x = np.linspace(0, 2, 100)  # Sample data.

   plt.figure(figsize=(5, 2.7), layout='constrained')
   plt.plot(x, x, label='linear')  # Plot some data on the (implicit) Axes.
   plt.plot(x, x**2, label='quadratic')  # etc.
   plt.plot(x, x**3, label='cubic')
   plt.xlabel('x label')
   plt.ylabel('y label')
   plt.title("Simple Plot")
   plt.legend()

(In addition, there is a third approach, for the case when embedding Matplotlib in a GUI 
application, which completely drops pyplot, even for figure creation. See the corresponding section 
in the gallery for more info: Embedding Matplotlib in graphical user interfaces.)

(Además, hay un tercer enfoque, para el caso de incorporar Matplotlib en una aplicación GUI, que elimina por completo pyplot, incluso para la creación de figuras. Consulte la sección correspondiente en la galería para obtener más información: Incorporación de Matplotlib en interfaces gráficas de usuario).


Matplotlib's documentation and examples use both the OO and the pyplot styles. In general, we 
suggest using the OO style, particularly for complicated plots, and functions and scripts that are 
intended to be reused as part of a larger project. However, the pyplot style can be very convenient 
for quick interactive work.

La documentación y los ejemplos de Matplotlib utilizan los estilos OO y pyplot. En general, recomendamos usar el estilo OO, especialmente para gráficos complejos, funciones y scripts que se reutilizarán en un proyecto más grande. Sin embargo, el estilo pyplot puede ser muy práctico para trabajos interactivos rápidos.


Note

You may find older examples that use the pylab interface, via from pylab import *. This approach is 
strongly deprecated.

Si necesita hacer los mismos gráficos una y otra vez con diferentes conjuntos de datos, o desea encapsular fácilmente los métodos de Matplotlib, utilice la función de firma recomendada a continuación.


Making a helper functions
-------------------------

If you need to make the same plots over and over again with different data sets, or want to easily 
wrap Matplotlib methods, use the recommended signature function below.

Si necesita hacer los mismos gráficos una y otra vez con diferentes conjuntos de datos, o desea encapsular fácilmente los métodos de Matplotlib, utilice la función de firma recomendada a continuación.


.. code:: Python

   def my_plotter(ax, data1, data2, param_dict):
      """
      A helper function to make a graph.
      """
      out = ax.plot(data1, data2, **param_dict)
      return out

which you would then use twice to populate two subplots:

que luego usarías dos veces para completar dos subparcelas:

.. code:: Python

   data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets
   fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
   my_plotter(ax1, data1, data2, {'marker': 'x'})
   my_plotter(ax2, data3, data4, {'marker': 'o'})

Note that if you want to install these as a python package, or any other customizations you could 
use one of the many templates on the web; Matplotlib has one at mpl-cookiecutter

Tenga en cuenta que si desea instalarlos como un paquete de Python, o cualquier otra personalización, puede usar una de las muchas plantillas en la web; Matplotlib tiene una en mpl-cookiecutter


Styling Artists
---------------

Most plotting methods have styling options for the Artists, accessible either when a plotting method 
is called, or from a "setter" on the Artist. In the plot below we manually set the color, linewidth, 
and linestyle of the Artists created by plot, and we set the linestyle of the second line after the 
fact with set_linestyle.

La mayoría de los métodos de trazado incluyen opciones de estilo para los artistas, accesibles al llamarlos o desde un definidor en el artista. En el gráfico a continuación, configuramos manualmente el color, el ancho y el estilo de línea de los artistas creados por plot, y posteriormente, el estilo de línea de la segunda línea se define con set_linestyle.


.. code:: Python

   fig, ax = plt.subplots(figsize=(5, 2.7))
   x = np.arange(len(data1))
   ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
   l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2)
   l.set_linestyle(':')

Colors
------

Matplotlib has a very flexible array of colors that are accepted for most Artists; see allowable 
color definitions for a list of specifications. Some Artists will take multiple colors. i.e. for a 
scatter plot, the edge of the markers can be different colors from the interior:

Matplotlib ofrece una gama de colores muy flexible, aceptada por la mayoría de los artistas; consulte las definiciones de colores permitidos para obtener una lista de especificaciones. Algunos artistas aceptan varios colores. Por ejemplo, en un diagrama de dispersión, el borde de los marcadores puede tener un color diferente al del interior.

.. code:: Python

   fig, ax = plt.subplots(figsize=(5, 2.7))
   ax.scatter(data1, data2, s=50, facecolor='C0', edgecolor='k')

Linewidths, linestyles, and markersizes
---------------------------------------

Line widths are typically in typographic points (1 pt = 1/72 inch) and available for Artists that 
have stroked lines. Similarly, stroked lines can have a linestyle. See the linestyles example.

Los anchos de línea se expresan generalmente en puntos tipográficos (1 pt = 1/72 de pulgada) y están disponibles para artistas con líneas de trazo. De igual forma, las líneas de trazo pueden tener un estilo de línea. Vea el ejemplo de estilos de línea.


Marker size depends on the method being used. plot specifies markersize in points, and is generally 
the "diameter" or width of the marker. scatter specifies markersize as approximately proportional to 
the visual area of the marker. There is an array of markerstyles available as string codes (see 
markers), or users can define their own MarkerStyle (see Marker reference):

El tamaño del marcador depende del método utilizado. El gráfico especifica el tamaño del marcador en puntos y generalmente representa el diámetro o ancho del marcador. La dispersión especifica el tamaño del marcador como aproximadamente proporcional a su área visual. Existe una variedad de estilos de marcador disponibles como códigos de cadena (véase marcadores), o los usuarios pueden definir su propio estilo de marcador (véase la referencia de marcadores).


.. code:: Python

   fig, ax = plt.subplots(figsize=(5, 2.7))
   ax.plot(data1, 'o', label='data1')
   ax.plot(data2, 'd', label='data2')
   ax.plot(data3, 'v', label='data3')
   ax.plot(data4, 's', label='data4')
   ax.legend()

Labelling plots
---------------

**Axes labels and text**

set_xlabel, set_ylabel, and set_title are used to add text in the indicated locations (see Text in 
Matplotlib for more discussion). Text can also be directly added to plots using text:

.. code:: Python

   mu, sigma = 115, 15
   x = mu + sigma * np.random.randn(10000)
   fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
   # the histogram of the data
   n, bins, patches = ax.hist(x, 50, density=True, facecolor='C0', alpha=0.75)

   ax.set_xlabel('Length [cm]')
   ax.set_ylabel('Probability')
   ax.set_title('Aardvark lengths\n (not really)')
   ax.text(75, .025, r'$\mu=115,\ \sigma=15$')
   ax.axis([55, 175, 0, 0.03])
   ax.grid(True)

All of the text functions return a matplotlib.text.Text instance. Just as with lines above, you can 
customize the properties by passing keyword arguments into the text functions:

Todas las funciones de texto devuelven una instancia de matplotlib.text.Text. Al igual que en las líneas anteriores, puede personalizar las propiedades pasando argumentos de palabra clave a las funciones de texto:


.. code:: Python

   t = ax.set_xlabel('my data', fontsize=14, color='red')

These properties are covered in more detail in Text properties and layout.

Estas propiedades se tratan con más detalle en Propiedades y diseño del texto.


Using mathematical expressions in text
--------------------------------------

Matplotlib accepts TeX equation expressions in any text expression. For example to write the 
expression in the title, you can write a TeX expression surrounded by dollar signs:

.. code:: Python

   ax.set_title(r'$\sigma_i=15$')

where the r preceding the title string signifies that the string is a raw string and not to treat 
backslashes as python escapes. Matplotlib has a built-in TeX expression parser and layout engine, 
and ships its own math fonts – for details see Writing mathematical expressions. You can also use 
LaTeX directly to format your text and incorporate the output directly into your display figures or 
saved postscript – see Text rendering with LaTeX.

Donde la r que precede a la cadena de título indica que la cadena es una cadena sin formato y que no se deben tratar las barras invertidas como escapes de Python. Matplotlib incorpora un analizador de expresiones TeX y un motor de diseño, e incluye sus propias fuentes matemáticas. Para más detalles, consulte "Escribir expresiones matemáticas". También puede usar LaTeX directamente para formatear el texto e incorporar la salida directamente en las figuras o en el archivo PostScript guardado. Consulte "Representación de texto con LaTeX".


Annotations
-----------

We can also annotate points on a plot, often by connecting an arrow pointing to xy, to a piece of 
text at xytext:

.. code:: Python

   fig, ax = plt.subplots(figsize=(5, 2.7))

   t = np.arange(0.0, 5.0, 0.01)
   s = np.cos(2 * np.pi * t)
   line, = ax.plot(t, s, lw=2)

   ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05))

   ax.set_ylim(-2, 2)

In this basic example, both xy and xytext are in data coordinates. There are a variety of other 
coordinate systems one can choose -- see Basic annotation and Advanced annotation for details. More 
examples also can be found in Annotate plots.

En este ejemplo básico, tanto xy como xytext se encuentran en coordenadas de datos. Se pueden elegir otros sistemas de coordenadas; consulte Anotación básica y Anotación avanzada para obtener más información. También encontrará más ejemplos en Anotar gráficos.


Legends
-------

Often we want to identify lines or markers with a Axes.legend:

.. code:: Python 

   fig, ax = plt.subplots(figsize=(5, 2.7))
   ax.plot(np.arange(len(data1)), data1, label='data1')
   ax.plot(np.arange(len(data2)), data2, label='data2')
   ax.plot(np.arange(len(data3)), data3, 'd', label='data3')
   ax.legend()

Legends in Matplotlib are quite flexible in layout, placement, and what Artists they can represent. 
They are discussed in detail in Legend guide.

Las leyendas en Matplotlib son bastante flexibles en cuanto a diseño, ubicación y artistas que pueden representar. Se describen en detalle en la guía de leyendas.


Axis scales and ticks
---------------------

Each Axes has two (or three) Axis objects representing the x- and y-axis. These control the scale of 
the Axis, the tick locators and the tick formatters. Additional Axes can be attached to display 
further Axis objects.

Cada eje tiene dos (o tres) objetos que representan los ejes x e y. Estos controlan la escala del eje, los localizadores y formateadores de marcas. Se pueden añadir ejes adicionales para mostrar más objetos.


Scales
------

In addition to the linear scale, Matplotlib supplies non-linear scales, such as a log-scale. Since 
log-scales are used so much there are also direct methods like loglog, semilogx, and semilogy. There 
are a number of scales (see Scales overview for other examples). Here we set the scale manually:

Además de la escala lineal, Matplotlib proporciona escalas no lineales, como la escala logarítmica. Dado el amplio uso de las escalas logarítmicas, también existen métodos directos como loglog, semilogx y semilogy. Existen diversas escalas (véase la descripción general de escalas para ver otros ejemplos). Aquí configuramos la escala manualmente:



.. code:: Python

   fig, axs = plt.subplots(1, 2, figsize=(5, 2.7), layout='constrained')
   xdata = np.arange(len(data1))  # make an ordinal for this
   data = 10**data1
   axs[0].plot(xdata, data)

   axs[1].set_yscale('log')
   axs[1].plot(xdata, data)

The scale sets the mapping from data values to spacing along the Axis. This happens in both 
directions, and gets combined into a transform, which is the way that Matplotlib maps from data 
coordinates to Axes, Figure, or screen coordinates. See Transformations Tutorial.

La escala establece la asignación de los valores de los datos al espaciado a lo largo del eje. Esto ocurre en ambas direcciones y se combina en una transformación, que es la forma en que Matplotlib asigna las coordenadas de los datos a los ejes, la figura o las coordenadas de la pantalla. Consulte el Tutorial de Transformaciones.


Tick locators and formatters
----------------------------

Each Axis has a tick locator and formatter that choose where along the Axis objects to put tick 
marks. A simple interface to this is set_xticks:

Cada eje cuenta con un localizador de marcas y un formateador que determina en qué punto de los objetos del eje se colocarán las marcas. Una interfaz sencilla para esto es set_xticks:


.. code:: Python

   fig, axs = plt.subplots(2, 1, layout='constrained')
   axs[0].plot(xdata, data1)
   axs[0].set_title('Automatic ticks')

   axs[1].plot(xdata, data1)
   axs[1].set_xticks(np.arange(0, 100, 30), ['zero', '30', 'sixty', '90'])
   axs[1].set_yticks([-1.5, 0, 1.5])  # note that we don't need to specify labels
   axs[1].set_title('Manual ticks')

Different scales can have different locators and formatters; for instance the log-scale above uses 
LogLocator and LogFormatter. See Tick locators and Tick formatters for other formatters and locators 
and information for writing your own.

Las diferentes escalas pueden tener diferentes localizadores y formateadores; por ejemplo, la escala logarítmica anterior utiliza LogLocator y LogFormatter. Consulte Localizadores de marcas y Formateadores de marcas para obtener información sobre otros formateadores y localizadores, así como para crear los suyos propios.


Plotting dates and strings
--------------------------

Matplotlib can handle plotting arrays of dates and arrays of strings, as well as floating point 
numbers. These get special locators and formatters as appropriate. For dates:

Matplotlib puede representar gráficamente matrices de fechas y matrices de cadenas, así como números de punto flotante. Estos reciben localizadores y formateadores especiales según corresponda. Para fechas:


.. code:: Python

   from matplotlib.dates import ConciseDateFormatter

   fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
   dates = np.arange(np.datetime64('2021-11-15'), np.datetime64('2021-12-25'),
                  np.timedelta64(1, 'h'))
   data = np.cumsum(np.random.randn(len(dates)))
   ax.plot(dates, data)
   ax.xaxis.set_major_formatter(ConciseDateFormatter(ax.xaxis.get_major_locator()))

For more information see the date examples (e.g. Date tick labels)

For strings, we get categorical plotting (see: Plotting categorical variables).

.. code:: Python

   fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
   categories = ['turnips', 'rutabaga', 'cucumber', 'pumpkins']

   ax.bar(categories, np.random.rand(len(categories)))

One caveat about categorical plotting is that some methods of parsing text files return a list of 
strings, even if the strings all represent numbers or dates. If you pass 1000 strings, Matplotlib 
will think you meant 1000 categories and will add 1000 ticks to your plot!

Una advertencia sobre la representación gráfica categórica es que algunos métodos de análisis de archivos de texto devuelven una lista de cadenas, incluso si todas representan números o fechas. Si se pasan 1000 cadenas, Matplotlib interpretará que se refiere a 1000 categorías y añadirá 1000 marcas a la gráfica.


Additional Axis objects
-----------------------

Plotting data of different magnitude in one chart may require an additional y-axis. Such an Axis can 
be created by using twinx to add a new Axes with an invisible x-axis and a y-axis positioned at the 
right (analogously for twiny). See Plots with different scales for another example.

Trazar datos de diferente magnitud en un mismo gráfico puede requerir un eje Y adicional. Este eje se puede crear usando twinx para añadir un nuevo eje con un eje X invisible y un eje Y a la derecha (de forma similar a twiny). Consulte Gráficos con diferentes escalas para ver otro ejemplo.


Similarly, you can add a secondary_xaxis or secondary_yaxis having a different scale than the main 
Axis to represent the data in different scales or units. See Secondary Axis for further examples.

De igual forma, puede agregar un eje secundario_x o un eje secundario_y con una escala diferente a la del eje principal para representar los datos en diferentes escalas o unidades. Consulte Eje secundario para ver más ejemplos.


.. code:: Python

   fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(7, 2.7), layout='constrained')
   l1, = ax1.plot(t, s)
   ax2 = ax1.twinx()
   l2, = ax2.plot(t, range(len(t)), 'C1')
   ax2.legend([l1, l2], ['Sine (left)', 'Straight (right)'])

   ax3.plot(t, s)
   ax3.set_xlabel('Angle [rad]')
   ax4 = ax3.secondary_xaxis('top', (np.rad2deg, np.deg2rad))
   ax4.set_xlabel('Angle [°]')

Color mapped data
-----------------

Often we want to have a third dimension in a plot represented by colors in a colormap. Matplotlib 
has a number of plot types that do this:

A menudo queremos tener una tercera dimensión en un gráfico representada por colores en un mapa de colores. Matplotlib ofrece varios tipos de gráficos que permiten esto:


.. code:: Python

   from matplotlib.colors import LogNorm

   X, Y = np.meshgrid(np.linspace(-3, 3, 128), np.linspace(-3, 3, 128))
   Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)

   fig, axs = plt.subplots(2, 2, layout='constrained')
   pc = axs[0, 0].pcolormesh(X, Y, Z, vmin=-1, vmax=1, cmap='RdBu_r')
   fig.colorbar(pc, ax=axs[0, 0])
   axs[0, 0].set_title('pcolormesh()')

   co = axs[0, 1].contourf(X, Y, Z, levels=np.linspace(-1.25, 1.25, 11))
   fig.colorbar(co, ax=axs[0, 1])
   axs[0, 1].set_title('contourf()')

   pc = axs[1, 0].imshow(Z**2 * 100, cmap='plasma', norm=LogNorm(vmin=0.01, vmax=100))
   fig.colorbar(pc, ax=axs[1, 0], extend='both')
   axs[1, 0].set_title('imshow() with LogNorm()')

   pc = axs[1, 1].scatter(data1, data2, c=data3, cmap='RdBu_r')
   fig.colorbar(pc, ax=axs[1, 1], extend='both')
   axs[1, 1].set_title('scatter()')
   pcolormesh(), contourf(), imshow() with LogNorm(), scatter()

Colormaps
---------

These are all examples of Artists that derive from ScalarMappable objects. They all can set a linear 
mapping between vmin and vmax into the colormap specified by cmap. Matplotlib has many colormaps to 
choose from (Choosing Colormaps in Matplotlib) you can make your own (Creating Colormaps in 
Matplotlib) or download as third-party packages.

Estos son ejemplos de artistas derivados de objetos ScalarMappable. Todos pueden establecer una asignación lineal entre vmin y vmax en el mapa de colores especificado por cmap. Matplotlib ofrece una gran variedad de mapas de colores (Elegir mapas de colores en Matplotlib). Puedes crear los tuyos propios (Crear mapas de colores en Matplotlib) o descargarlos como paquetes de terceros.


Normalizations
--------------

Sometimes we want a non-linear mapping of the data to the colormap, as in the LogNorm example above. 
We do this by supplying the ScalarMappable with the norm argument instead of vmin and vmax. More 
normalizations are shown at Colormap normalization.

A veces necesitamos una asignación no lineal de los datos al mapa de colores, como en el ejemplo LogNorm anterior. Para ello, proporcionamos a ScalarMappable el argumento norm en lugar de vmin y vmax. Se muestran más normalizaciones en Normalización del mapa de colores.


Colorbars
---------

Adding a colorbar gives a key to relate the color back to the underlying data. Colorbars are 
figure-level Artists, and are attached to a ScalarMappable (where they get their information about 
the norm and colormap) and usually steal space from a parent Axes. Placement of colorbars can be 
complex: see Placing colorbars for details. You can also change the appearance of colorbars with the 
extend keyword to add arrows to the ends, and shrink and aspect to control the size. Finally, the 
colorbar will have default locators and formatters appropriate to the norm. These can be changed as 
for other Axis objects.

Añadir una barra de colores proporciona una clave para relacionar el color con los datos subyacentes. Las barras de colores son artistas a nivel de figura y se adjuntan a un ScalarMappable (de donde obtienen información sobre la norma y el mapa de colores) y suelen ocupar espacio de un Eje principal. La ubicación de las barras de colores puede ser compleja: consulte "Ubicación de barras de colores" para obtener más información. También puede cambiar la apariencia de las barras de colores con la palabra clave "extend" para añadir flechas en los extremos y "shrink" y "aspect" para controlar el tamaño. Finalmente, la barra de colores tendrá localizadores y formateadores predeterminados adecuados a la norma. Estos se pueden cambiar como para otros objetos de Eje.


Working with multiple Figures and Axes
--------------------------------------

You can open multiple Figures with multiple calls to fig = plt.figure() or fig2, ax = 
plt.subplots(). By keeping the object references you can add Artists to either Figure.

Multiple Axes can be added a number of ways, but the most basic is plt.subplots() as used above. One 
can achieve more complex layouts, with Axes objects spanning columns or rows, using subplot_mosaic.

.. code:: Python

   fig, axd = plt.subplot_mosaic([['upleft', 'right'],
                               ['lowleft', 'right']], layout='constrained')
   axd['upleft'].set_title('upleft')
   axd['lowleft'].set_title('lowleft')
   axd['right'].set_title('right')

Matplotlib has quite sophisticated tools for arranging Axes: See Arranging multiple Axes in a Figure 
and Complex and semantic figure composition (subplot_mosaic).

More reading
------------

For more plot types see Plot types and the API reference, in particular the Axes API.

Total running time of the script: (0 minutes 8.275 seconds)




