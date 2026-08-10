API Reference
=============

https://matplotlib.org/stable/api/index.html


Matplotlib interfaces
---------------------

Matplotlib has two interfaces. See Matplotlib Application Interfaces (APIs) for a more detailed 
description of both and their recommended use cases.

Axes interface (object-based, explicit)
---------------------------------------

create a Figure and one or more Axes objects, then explicitly use methods on these objects to add 
data, configure limits, set labels etc.

API:

* subplots: create Figure and Axes

* axes: add data, limits, labels etc.

* Figure: for figure-level methods

Example:

.. code:: Python

   fig, ax = plt.subplots()
   ax.plot(x, y)
   ax.set_title("Sample plot")
   plt.show()

pyplot interface (function-based, implicit)
-------------------------------------------

consists of functions in the pyplot module. Figure and Axes are manipulated through these functions 
and are only implicitly present in the background.

API:

* matplotlib.pyplot

Example:

.. code:: Python

   plt.plot(x, y)
   plt.title("Sample plot")
   plt.show()


Modules
-------

**Alphabetical list of modules:**

matplotlib
matplotlib.animation
matplotlib.artist
matplotlib.axes
matplotlib.axis
matplotlib.backend_bases
matplotlib.backend_managers
matplotlib.backend_tools
matplotlib.backends
matplotlib.bezier
matplotlib.category
matplotlib.cbook
matplotlib.cm
matplotlib.collections
matplotlib.colorbar
matplotlib.colorizer
matplotlib.colors
matplotlib.container
matplotlib.contour
matplotlib.dates
matplotlib.dviread
matplotlib.figure
matplotlib.font_manager
matplotlib.ft2font
matplotlib.gridspec
matplotlib.hatch
matplotlib.image
matplotlib.inset
matplotlib.layout_engine
matplotlib.legend
matplotlib.legend_handler
matplotlib.lines
matplotlib.markers
matplotlib.mathtext
matplotlib.mlab
matplotlib.offsetbox
matplotlib.patches
matplotlib.path
matplotlib.patheffects
matplotlib.pyplot
matplotlib.projections
matplotlib.quiver
matplotlib.rcsetup
matplotlib.sankey
matplotlib.scale
matplotlib.sphinxext.mathmpl
matplotlib.sphinxext.plot_directive
matplotlib.sphinxext.figmpl_directive
matplotlib.sphinxext.roles
matplotlib.spines
matplotlib.style
matplotlib.table
matplotlib.testing
matplotlib.text
matplotlib.texmanager
matplotlib.ticker
matplotlib.transforms
matplotlib.tri
matplotlib.typing
matplotlib.units
matplotlib.widgets
matplotlib._afm
matplotlib._api
matplotlib._docstring
matplotlib._enums
matplotlib._type1font
matplotlib._tight_bbox
matplotlib._tight_layout
mpl_toolkits.mplot3d
mpl_toolkits.axes_grid1
mpl_toolkits.axisartist
pylab

