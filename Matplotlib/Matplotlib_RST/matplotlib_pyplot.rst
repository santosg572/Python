matplotlib.pyplot
=================


https://matplotlib.org/stable/api/pyplot_summary.html

matplotlib.pyplot is a state-based interface to matplotlib. It provides an implicit, MATLAB-like, 
way of plotting. It also opens figures on your screen, and acts as the figure GUI manager.

pyplot is mainly intended for interactive plots and simple cases of programmatic plot generation:

.. code:: Python

   import numpy as np
   import matplotlib.pyplot as plt

   x = np.arange(0, 5, 0.1)
   y = np.sin(x)
   plt.plot(x, y)
   plt.show()

The explicit object-oriented API is recommended for complex plots, though pyplot is still usually 
used to create the figure and often the Axes in the figure. See pyplot.figure, pyplot.subplots, and 
pyplot.subplot_mosaic to create figures, and Axes API for the plotting methods on an Axes:

.. code:: Python

   import numpy as np
   import matplotlib.pyplot as plt

   x = np.arange(0, 5, 0.1)
   y = np.sin(x)
   fig, ax = plt.subplots()
   ax.plot(x, y)
   plt.show()

See Matplotlib Application Interfaces (APIs) for an explanation of the tradeoffs between the 
implicit and explicit interfaces.

Managing Figure and Axes
------------------------

``axes``

Add an Axes to the current figure and make it the current Axes.

``cla

Clear the current Axes.

``clf

Clear the current figure.

``close

Close a figure window, and unregister it from pyplot.

``delaxes

Remove an Axes (defaulting to the current Axes) from its figure.

``fignum_exists

Return whether the figure with the given id exists.

``figure

Create a new figure, or activate an existing figure.

``gca

Get the current Axes.

``gcf

Get the current figure.

``get_figlabels

Return a list of existing figure labels.

``get_fignums

Return a list of existing figure numbers.

``sca

Set the current Axes to ax and the current Figure to the parent of ax.

subplot

Add an Axes to the current figure or retrieve an existing Axes.

subplot2grid

Create a subplot at a specific location inside a regular grid.

subplot_mosaic

Build a layout of Axes based on ASCII art or nested lists.

subplots

Create a figure and a set of subplots.

twinx

Make and return a second Axes that shares the x-axis.

twiny

Make and return a second Axes that shares the y-axis.

Adding data to the plot
Basic
plot

Plot y versus x as lines and/or markers.

errorbar

Plot y versus x as lines and/or markers with attached errorbars.

scatter

A scatter plot of y vs.

plot_date

[Deprecated] Plot coercing the axis to treat floats as dates.

step

Make a step plot.

loglog

Make a plot with log scaling on both the x- and y-axis.

semilogx

Make a plot with log scaling on the x-axis.

semilogy

Make a plot with log scaling on the y-axis.

fill_between

Fill the area between two horizontal curves.

fill_betweenx

Fill the area between two vertical curves.

bar

Make a bar plot.

barh

Make a horizontal bar plot.

bar_label

Label a bar plot.

stem

Create a stem plot.

eventplot

Plot identical parallel lines at the given positions.

pie

Plot a pie chart.

stackplot

Draw a stacked area plot or a streamgraph.

broken_barh

Plot a horizontal sequence of rectangles.

vlines

Plot vertical lines at each x from ymin to ymax.

hlines

Plot horizontal lines at each y from xmin to xmax.

fill

Plot filled polygons.

polar

Make a polar plot.

Spans
axhline

Add a horizontal line spanning the whole or fraction of the Axes.

axhspan

Add a horizontal span (rectangle) across the Axes.

axvline

Add a vertical line spanning the whole or fraction of the Axes.

axvspan

Add a vertical span (rectangle) across the Axes.

axline

Add an infinitely long straight line.

Spectral
acorr

Plot the autocorrelation of x.

angle_spectrum

Plot the angle spectrum.

cohere

Plot the coherence between x and y.

csd

Plot the cross-spectral density.

magnitude_spectrum

Plot the magnitude spectrum.

phase_spectrum

Plot the phase spectrum.

psd

Plot the power spectral density.

specgram

Plot a spectrogram.

xcorr

Plot the cross correlation between x and y.

Statistics
ecdf

Compute and plot the empirical cumulative distribution function of x.

boxplot

Draw a box and whisker plot.

violinplot

Make a violin plot.

Binned
hexbin

Make a 2D hexagonal binning plot of points x, y.

hist

Compute and plot a histogram.

hist2d

Make a 2D histogram plot.

stairs

Draw a stepwise constant function as a line or a filled plot.

Contours
clabel

Label a contour plot.

contour

Plot contour lines.

contourf

Plot filled contours.

2D arrays
imshow

Display data as an image, i.e., on a 2D regular raster.

matshow

Display a 2D array as a matrix in a new figure window.

pcolor

Create a pseudocolor plot with a non-regular rectangular grid.

pcolormesh

Create a pseudocolor plot with a non-regular rectangular grid.

spy

Plot the sparsity pattern of a 2D array.

figimage

Add a non-resampled image to the figure.

Unstructured triangles
triplot

Draw an unstructured triangular grid as lines and/or markers.

tripcolor

Create a pseudocolor plot of an unstructured triangular grid.

tricontour

Draw contour lines on an unstructured triangular grid.

tricontourf

Draw contour regions on an unstructured triangular grid.

Text and annotations
annotate

Annotate the point xy with text text.

text

Add text to the Axes.

figtext

Add text to figure.

table

Add a table to an Axes.

arrow

[Discouraged] Add an arrow to the Axes.

figlegend

Place a legend on the figure.

legend

Place a legend on the Axes.

Vector fields
barbs

Plot a 2D field of wind barbs.

quiver

Plot a 2D field of arrows.

quiverkey

Add a key to a quiver plot.

streamplot

Draw streamlines of a vector flow.

Axis configuration
autoscale

Autoscale the axis view to the data (toggle).

axis

Convenience method to get or set some axis properties.

box

Turn the Axes box on or off on the current Axes.

grid

Configure the grid lines.

locator_params

Control behavior of major tick locators.

minorticks_off

Remove minor ticks from the Axes.

minorticks_on

Display minor ticks on the Axes.

rgrids

Get or set the radial gridlines on the current polar plot.

thetagrids

Get or set the theta gridlines on the current polar plot.

tick_params

Change the appearance of ticks, tick labels, and gridlines.

ticklabel_format

Configure the ScalarFormatter used by default for linear Axes.

xlabel

Set the label for the x-axis.

xlim

Get or set the x limits of the current Axes.

xscale

Set the xaxis' scale.

xticks

Get or set the current tick locations and labels of the x-axis.

ylabel

Set the label for the y-axis.

ylim

Get or set the y-limits of the current Axes.

yscale

Set the yaxis' scale.

yticks

Get or set the current tick locations and labels of the y-axis.

suptitle

Add a centered super title to the figure.

title

Set a title for the Axes.

Layout
margins

Set or retrieve margins around the data for autoscaling axis limits.

subplots_adjust

Adjust the subplot layout parameters.

subplot_tool

Launch a subplot tool window for a figure.

tight_layout

Adjust the padding between and around subplots.

Colormapping
clim

Set the color limits of the current image.

colorbar

Add a colorbar to a plot.

gci

Get the current colorable artist.

sci

Set the current image.

get_cmap

Get a colormap instance, defaulting to rc values if name is None.

set_cmap

Set the default colormap, and applies it to the current image if any.

imread

Read an image from a file into an array.

imsave

Colormap and save an array as an image file.

Colormaps are available via the colormap registry matplotlib.colormaps. For convenience this 
registry is available in pyplot as

matplotlib.pyplot.colormaps[source]
Container for colormaps that are known to Matplotlib by name.

The universal registry instance is matplotlib.colormaps. There should be no need for users to 
instantiate ColormapRegistry themselves.

Read access uses a dict-like interface mapping names to Colormaps:

import matplotlib as mpl
cmap = mpl.colormaps['viridis']
Returned Colormaps are copies, so that their modification does not change the global definition of 
the colormap.

Additional colormaps can be added via ColormapRegistry.register:

mpl.colormaps.register(my_colormap)
To get a list of all registered colormaps, you can do:

from matplotlib import colormaps
list(colormaps)
Additionally, there are shortcut functions to set builtin colormaps; e.g. plt.viridis() is 
equivalent to plt.set_cmap('viridis').

matplotlib.pyplot.color_sequences[source]
Container for sequences of colors that are known to Matplotlib by name.

The universal registry instance is matplotlib.color_sequences. There should be no need for users to 
instantiate ColorSequenceRegistry themselves.

Read access uses a dict-like interface mapping names to lists of colors:

import matplotlib as mpl
colors = mpl.color_sequences['tab10']
For a list of built in color sequences, see Named color sequences. The returned lists are copies, so 
that their modification does not change the global definition of the color sequence.

Additional color sequences can be added via ColorSequenceRegistry.register:

mpl.color_sequences.register('rgb', ['r', 'g', 'b'])
Configuration
rc

Set the current rcParams. group is the grouping for the rc, e.g., for lines.linewidth the group is 
lines, for axes.facecolor, the group is axes, and so on. Group may also be a list or tuple of group 
names, e.g., (xtick, ytick). kwargs is a dictionary attribute name/value pairs, e.g.,::.

rc_context

Return a context manager for temporarily changing rcParams.

rcdefaults

Restore the rcParams from Matplotlib's internal default style.

Output
draw

Redraw the current figure.

draw_if_interactive

Redraw the current figure if in interactive mode.

ioff

Disable interactive mode.

ion

Enable interactive mode.

install_repl_displayhook

Connect to the display hook of the current shell.

isinteractive

Return whether plots are updated after every plotting command.

pause

Run the GUI event loop for interval seconds.

savefig

Save the current figure as an image or vector graphic to a file.

show

Display all open figures.

switch_backend

Set the pyplot backend.

uninstall_repl_displayhook

Disconnect from the display hook of the current shell.

Other
connect

Bind function func to event s.

disconnect

Disconnect the callback with id cid.

findobj

Find artist objects.

get

Return the value of an Artist's property, or print all of them.

getp

Return the value of an Artist's property, or print all of them.

get_current_fig_manager

Return the figure manager of the current figure.

ginput

Blocking call to interact with a figure.

new_figure_manager

Create a new figure manager instance.

set_loglevel

Configure Matplotlib's logging levels.

setp

Set one or more properties on an Artist, or list allowed values.

waitforbuttonpress

Blocking call to interact with the figure.

xkcd

Turn on xkcd sketch-style drawing mode.
