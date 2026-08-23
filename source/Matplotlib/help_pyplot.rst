help pyplot
===========

........................ AbstractContextManager .......................
Help on class AbstractContextManager in module contextlib:

class AbstractContextManager(abc.ABC)
 |  An abstract base class for context managers.
 |
 |  Method resolution order:
 |      AbstractContextManager
 |      abc.ABC
 |      builtins.object
 |
 |  Methods defined here:
........................ Annotation .......................
Help on class Annotation in module matplotlib.text:

class Annotation(Text, _AnnotationBase)
 |  Annotation(
 |      text,
 |      xy,
 |      xytext=None,
 |      xycoords='data',
 |      textcoords=None,
 |      arrowprops=None,
 |      annotation_clip=None,
........................ Arrow .......................
Help on class Arrow in module matplotlib.patches:

class Arrow(Patch)
 |  Arrow(x, y, dx, dy, *, width=1.0, **kwargs)
 |
 |  An arrow patch.
 |
 |  Method resolution order:
 |      Arrow
 |      Patch
 |      matplotlib.artist.Artist
........................ Artist .......................
Help on class Artist in module matplotlib.artist:

class Artist(builtins.object)
 |  Abstract base class for objects that render into a FigureCanvas.
 |
 |  Typically, all visible elements in a figure are subclasses of Artist.
 |
 |  Methods defined here:
 |
 |  __getstate__(self)
 |      Helper for pickle.
........................ AutoLocator .......................
Help on class AutoLocator in module matplotlib.ticker:

class AutoLocator(MaxNLocator)
 |  Place evenly spaced ticks, with the step size and maximum number of ticks chosen
 |  automatically.
 |
 |  This is a subclass of `~matplotlib.ticker.MaxNLocator`, with parameters
 |  *nbins = 'auto'* and *steps = [1, 2, 2.5, 5, 10]*.
 |
 |  Method resolution order:
 |      AutoLocator
........................ AxLine .......................
Help on class AxLine in module matplotlib.lines:

class AxLine(Line2D)
 |  AxLine(xy1, xy2, slope, **kwargs)
 |
 |  A helper class that implements `~.Axes.axline`, by recomputing the artist
 |  transform at draw time.
 |
 |  Method resolution order:
 |      AxLine
 |      Line2D
........................ Axes .......................
Help on class Axes in module matplotlib.axes._axes:

class Axes(matplotlib.axes._base._AxesBase)
 |  Axes(
 |      fig,
 |      *args,
 |      facecolor=None,
 |      frameon=True,
 |      sharex=None,
 |      sharey=None,
 |      label='',
........................ BackendFilter .......................
Help on class BackendFilter in module matplotlib.backends.registry:

class BackendFilter(enum.Enum)
 |  BackendFilter(*values)
 |
 |  Filter used with :meth:`~matplotlib.backends.registry.BackendRegistry.list_builtin`
 |
 |  .. versionadded:: 3.9
 |
 |  Method resolution order:
 |      BackendFilter
........................ Button .......................
Help on class Button in module matplotlib.widgets:

class Button(AxesWidget)
 |  Button(ax, label, image=None, color='0.85', hovercolor='0.95', *, useblit=True)
 |
 |  A GUI neutral button.
 |
 |  For the button to remain responsive you must keep a reference to it.
 |  Call `.on_clicked` to connect to the button.
 |
 |  Attributes
........................ Circle .......................
Help on class Circle in module matplotlib.patches:

class Circle(Ellipse)
 |  Circle(xy, radius=5, **kwargs)
 |
 |  A circle patch.
 |
 |  Method resolution order:
 |      Circle
 |      Ellipse
 |      Patch
........................ Colorizer .......................
Help on class Colorizer in module matplotlib.colorizer:

class Colorizer(builtins.object)
 |  Colorizer(cmap=None, norm=None)
 |
 |  Data to color pipeline.
 |
 |  This pipeline is accessible via `.Colorizer.to_rgba` and executed via
 |  the `.Colorizer.norm` and `.Colorizer.cmap` attributes.
 |
 |  Parameters
........................ ColorizingArtist .......................
Help on class ColorizingArtist in module matplotlib.colorizer:

class ColorizingArtist(_ScalarMappable, matplotlib.artist.Artist)
 |  ColorizingArtist(colorizer, **kwargs)
 |
 |  Base class for artists that make map data to color using a `.colorizer.Colorizer`.
 |
 |  The `.colorizer.Colorizer` applies data normalization before
 |  returning RGBA colors from a `~matplotlib.colors.Colormap`.
 |
 |  Method resolution order:
........................ Colormap .......................
Help on class Colormap in module matplotlib.colors:

class Colormap(builtins.object)
 |  Colormap(name, N=256)
 |
 |  Baseclass for all scalar to RGBA mappings.
 |
 |  Typically, Colormap instances are used to convert data values (floats)
 |  from the interval ``[0, 1]`` to the RGBA color that the respective
 |  Colormap represents. For scaling of data into the ``[0, 1]`` interval see
 |  `matplotlib.colors.Normalize`. Subclasses of `matplotlib.cm.ScalarMappable`
........................ Enum .......................
Help on class Enum in module enum:

class Enum(builtins.object)
 |  Enum(
 |      new_class_name,
 |      /,
 |      names,
 |      *,
 |      module=None,
 |      qualname=None,
 |      type=None,
........................ ExitStack .......................
Help on class ExitStack in module contextlib:

class ExitStack(_BaseExitStack, AbstractContextManager)
 |  Context manager for dynamic management of a stack of exit callbacks.
 |
 |  For example:
 |      with ExitStack() as stack:
 |          files = [stack.enter_context(open(fname)) for fname in filenames]
 |          # All opened files will automatically be closed at the end of
 |          # the with statement, even if attempts to open files later
 |          # in the list raise an exception.
........................ Figure .......................
Help on class Figure in module matplotlib.figure:

class Figure(FigureBase)
 |  Figure(
 |      figsize=None,
 |      dpi=None,
 |      *,
 |      facecolor=None,
 |      edgecolor=None,
 |      linewidth=0.0,
 |      frameon=None,
........................ FigureBase .......................
Help on class FigureBase in module matplotlib.figure:

class FigureBase(matplotlib.artist.Artist)
 |  FigureBase(**kwargs)
 |
 |  Base class for `.Figure` and `.SubFigure` containing the methods that add
 |  artists to the figure or subfigure, create Axes, etc.
 |
 |  Method resolution order:
 |      FigureBase
 |      matplotlib.artist.Artist
........................ FigureCanvasBase .......................
Help on class FigureCanvasBase in module matplotlib.backend_bases:

class FigureCanvasBase(builtins.object)
 |  FigureCanvasBase(figure=None)
 |
 |  The canvas the figure renders into.
 |
 |  Attributes
 |  ----------
 |  figure : `~matplotlib.figure.Figure`
 |      A high-level figure instance.
........................ FigureManagerBase .......................
Help on class FigureManagerBase in module matplotlib.backend_bases:

class FigureManagerBase(builtins.object)
 |  FigureManagerBase(canvas, num)
 |
 |  A backend-independent abstraction of a figure container and controller.
 |
 |  The figure manager is used by pyplot to interact with the window in a
 |  backend-independent way. It's an adapter for the real (GUI) framework that
 |  represents the visual figure on screen.
 |
........................ FixedFormatter .......................
Help on class FixedFormatter in module matplotlib.ticker:

class FixedFormatter(Formatter)
 |  FixedFormatter(seq)
 |
 |  Return fixed strings for tick labels based only on position, not value.
 |
 |  .. note::
 |      `.FixedFormatter` should only be used together with `.FixedLocator`.
 |      Otherwise, the labels may end up in unexpected positions.
 |
........................ FixedLocator .......................
Help on class FixedLocator in module matplotlib.ticker:

class FixedLocator(Locator)
 |  FixedLocator(locs, nbins=None)
 |
 |  Place ticks at a set of fixed values.
 |
 |  If *nbins* is None ticks are placed at all values. Otherwise, the *locs* array of
 |  possible positions will be subsampled to keep the number of ticks
 |  :math:`\leq nbins + 1`. The subsampling will be done to include the smallest
 |  absolute value; for example, if zero is included in the array of possibilities, then
........................ FormatStrFormatter .......................
Help on class FormatStrFormatter in module matplotlib.ticker:

class FormatStrFormatter(Formatter)
 |  FormatStrFormatter(fmt)
 |
 |  Use an old-style ('%' operator) format string to format the tick.
 |
 |  The format string should have a single variable format (%) in it.
 |  It will be applied to the value (not the position) of the tick.
 |
 |  Negative numeric values (e.g., -1) will use a dash, not a Unicode minus;
........................ Formatter .......................
Help on class Formatter in module matplotlib.ticker:

class Formatter(TickHelper)
 |  Create a string based on a tick value and location.
 |
 |  Method resolution order:
 |      Formatter
 |      TickHelper
 |      builtins.object
 |
 |  Methods defined here:
........................ FuncFormatter .......................
Help on class FuncFormatter in module matplotlib.ticker:

class FuncFormatter(Formatter)
 |  FuncFormatter(func)
 |
 |  Use a user-defined function for formatting.
 |
 |  The function should take in two inputs (a tick value ``x`` and a
 |  position ``pos``), and return a string containing the corresponding
 |  tick label.
 |
........................ GridSpec .......................
Help on class GridSpec in module matplotlib.gridspec:

class GridSpec(GridSpecBase)
 |  GridSpec(
 |      nrows,
 |      ncols,
 |      figure=None,
 |      left=None,
 |      bottom=None,
 |      right=None,
 |      top=None,
........................ IndexLocator .......................
Help on class IndexLocator in module matplotlib.ticker:

class IndexLocator(Locator)
 |  IndexLocator(base, offset)
 |
 |  Place ticks at every nth point plotted.
 |
 |  IndexLocator assumes index plotting; i.e., that the ticks are placed at integer
 |  values in the range between 0 and len(data) inclusive.
 |
 |  Method resolution order:
........................ Line2D .......................
Help on class Line2D in module matplotlib.lines:

class Line2D(matplotlib.artist.Artist)
 |  Line2D(
 |      xdata,
 |      ydata,
 |      *,
 |      linewidth=None,
 |      linestyle=None,
 |      color=None,
 |      gapcolor=None,
........................ LinearLocator .......................
Help on class LinearLocator in module matplotlib.ticker:

class LinearLocator(Locator)
 |  LinearLocator(numticks=None, presets=None)
 |
 |  Place ticks at evenly spaced values.
 |
 |  The first time this function is called it will try to set the
 |  number of ticks to make a nice tick partitioning.  Thereafter, the
 |  number of ticks will be fixed so that interactive navigation will
 |  be nice
........................ Locator .......................
Help on class Locator in module matplotlib.ticker:

class Locator(TickHelper)
 |  Determine tick locations.
 |
 |  Note that the same locator should not be used across multiple
 |  `~matplotlib.axis.Axis` because the locator stores references to the Axis
 |  data and view limits.
 |
 |  Method resolution order:
 |      Locator
........................ LogFormatter .......................
Help on class LogFormatter in module matplotlib.ticker:

class LogFormatter(Formatter)
 |  LogFormatter(
 |      base=10.0,
 |      labelOnlyBase=False,
 |      minor_thresholds=None,
 |      linthresh=None
 |  )
 |
 |  Base class for formatting ticks on a log or symlog scale.
........................ LogFormatterExponent .......................
Help on class LogFormatterExponent in module matplotlib.ticker:

class LogFormatterExponent(LogFormatter)
 |  LogFormatterExponent(
 |      base=10.0,
 |      labelOnlyBase=False,
 |      minor_thresholds=None,
 |      linthresh=None
 |  )
 |
 |  Format values for log axis using ``exponent = log_base(value)``.
........................ LogFormatterMathtext .......................
Help on class LogFormatterMathtext in module matplotlib.ticker:

class LogFormatterMathtext(LogFormatter)
 |  LogFormatterMathtext(
 |      base=10.0,
 |      labelOnlyBase=False,
 |      minor_thresholds=None,
 |      linthresh=None
 |  )
 |
 |  Format values for log axis using ``exponent = log_base(value)``.
........................ LogLocator .......................
Help on class LogLocator in module matplotlib.ticker:

class LogLocator(Locator)
 |  LogLocator(base=10.0, subs=(1.0,), *, numticks=None)
 |
 |  Place logarithmically spaced ticks.
 |
 |  Places ticks at the values ``subs[j] * base**i``.
 |
 |  Method resolution order:
 |      LogLocator
........................ MaxNLocator .......................
Help on class MaxNLocator in module matplotlib.ticker:

class MaxNLocator(Locator)
 |  MaxNLocator(nbins=None, **kwargs)
 |
 |  Place evenly spaced ticks, with a cap on the total number of ticks.
 |
 |  Finds nice tick locations with no more than :math:`nbins + 1` ticks being within the
 |  view limits. Locations beyond the limits are added to support autoscaling.
 |
 |  Method resolution order:
........................ MouseButton .......................
Help on class MouseButton in module matplotlib.backend_bases:

class MouseButton(enum.IntEnum)
 |  MouseButton(*values)
 |
 |  Method resolution order:
 |      MouseButton
 |      enum.IntEnum
 |      builtins.int
 |      enum.ReprEnum
 |      enum.Enum
........................ MultipleLocator .......................
Help on class MultipleLocator in module matplotlib.ticker:

class MultipleLocator(Locator)
 |  MultipleLocator(base=1.0, offset=0.0)
 |
 |  Place ticks at every integer multiple of a base plus an offset.
 |
 |  Method resolution order:
 |      MultipleLocator
 |      Locator
 |      TickHelper
........................ Normalize .......................
Help on class Normalize in module matplotlib.colors:

class Normalize(builtins.object)
 |  Normalize(vmin=None, vmax=None, clip=False)
 |
 |  A class which, when called, maps values within the interval
 |  ``[vmin, vmax]`` linearly to the interval ``[0.0, 1.0]``. The mapping of
 |  values outside ``[vmin, vmax]`` depends on *clip*.
 |
 |  Examples
 |  --------
........................ NullFormatter .......................
Help on class NullFormatter in module matplotlib.ticker:

class NullFormatter(Formatter)
 |  Always return the empty string.
 |
 |  Method resolution order:
 |      NullFormatter
 |      Formatter
 |      TickHelper
 |      builtins.object
 |
........................ NullLocator .......................
Help on class NullLocator in module matplotlib.ticker:

class NullLocator(Locator)
 |  No ticks
 |
 |  Method resolution order:
 |      NullLocator
 |      Locator
 |      TickHelper
 |      builtins.object
 |
........................ PolarAxes .......................
Help on class PolarAxes in module matplotlib.projections.polar:

class PolarAxes(matplotlib.axes._axes.Axes)
 |  PolarAxes(
 |      *args,
 |      theta_offset=0,
 |      theta_direction=1,
 |      rlabel_position=22.5,
 |      **kwargs
 |  )
 |
........................ Polygon .......................
Help on class Polygon in module matplotlib.patches:

class Polygon(Patch)
 |  Polygon(xy, *, closed=True, **kwargs)
 |
 |  A general polygon patch.
 |
 |  Method resolution order:
 |      Polygon
 |      Patch
 |      matplotlib.artist.Artist
........................ Rectangle .......................
Help on class Rectangle in module matplotlib.patches:

class Rectangle(Patch)
 |  Rectangle(xy, width, height, *, angle=0.0, rotation_point='xy', **kwargs)
 |
 |  A rectangle defined via an anchor point *xy* and its *width* and *height*.
 |
 |  The rectangle extends from ``xy[0]`` to ``xy[0] + width`` in x-direction
 |  and from ``xy[1]`` to ``xy[1] + height`` in y-direction. ::
 |
 |    :                +------------------+
........................ ScalarFormatter .......................
Help on class ScalarFormatter in module matplotlib.ticker:

class ScalarFormatter(Formatter)
 |  ScalarFormatter(
 |      useOffset=None,
 |      useMathText=None,
 |      useLocale=None,
 |      *,
 |      usetex=None
 |  )
 |
........................ Slider .......................
Help on class Slider in module matplotlib.widgets:

class Slider(SliderBase)
 |  Slider(
 |      ax,
 |      label,
 |      valmin,
 |      valmax,
 |      *,
 |      valinit=0.5,
 |      valfmt=None,
........................ Subplot .......................
Help on class Axes in module matplotlib.axes._axes:

class Axes(matplotlib.axes._base._AxesBase)
 |  Axes(
 |      fig,
 |      *args,
 |      facecolor=None,
 |      frameon=True,
 |      sharex=None,
 |      sharey=None,
 |      label='',
........................ SubplotSpec .......................
Help on class SubplotSpec in module matplotlib.gridspec:

class SubplotSpec(builtins.object)
 |  SubplotSpec(gridspec, num1, num2=None)
 |
 |  The location of a subplot in a `GridSpec`.
 |
 |  .. note::
 |
 |      Likely, you will never instantiate a `SubplotSpec` yourself. Instead,
 |      you will typically obtain one from a `GridSpec` using item-access.
........................ TYPE_CHECKING .......................
Help on bool object:

class bool(int)
 |  bool(object=False, /)
 |
 |  Returns True when the argument is true, False otherwise.
 |  The builtins True and False are the only two instances of the class bool.
 |  The class bool is a subclass of the class int, and cannot be subclassed.
 |
 |  Method resolution order:
 |      bool
........................ Text .......................
Help on class Text in module matplotlib.text:

class Text(matplotlib.artist.Artist)
 |  Text(
 |      x=0,
 |      y=0,
 |      text='',
 |      *,
 |      color=None,
 |      verticalalignment='baseline',
 |      horizontalalignment='left',
........................ TickHelper .......................
Help on class TickHelper in module matplotlib.ticker:

class TickHelper(builtins.object)
 |  Methods defined here:
 |
 |  create_dummy_axis(self, **kwargs)
 |
 |  set_axis(self, axis)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
........................ Widget .......................
Help on class Widget in module matplotlib.widgets:

class Widget(builtins.object)
 |  Abstract base class for GUI neutral widgets.
 |
 |  Methods defined here:
 |
 |  get_active(self)
 |      Get whether the widget is active.
 |
 |  ignore(self, event)
........................ _ColorizerInterface .......................
Help on class _ColorizerInterface in module matplotlib.colorizer:

class _ColorizerInterface(builtins.object)
 |  Base class that contains the interface to `Colorizer` objects from
 |  a `ColorizingArtist` or `.cm.ScalarMappable`.
 |
 |  Note: This class only contain functions that interface the .colorizer
 |  attribute. Other functions that as shared between `.ColorizingArtist`
 |  and `.cm.ScalarMappable` are not included.
 |
 |  Methods defined here:
........................ _NO_PYPLOT_NOTE .......................
Help on list object:

class list(object)
 |  list(iterable=(), /)
 |
 |  Built-in mutable sequence.
 |
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |
 |  Methods defined here:
........................ _REPL_DISPLAYHOOK .......................
Help on _ReplDisplayHook in module matplotlib.pyplot object:

class _ReplDisplayHook(enum.Enum)
 |  _ReplDisplayHook(*values)
 |
 |  Method resolution order:
 |      _ReplDisplayHook
 |      enum.Enum
 |      builtins.object
 |
 |  Data and other attributes defined here:
........................ _ReplDisplayHook .......................
Help on class _ReplDisplayHook in module matplotlib.pyplot:

class _ReplDisplayHook(enum.Enum)
 |  _ReplDisplayHook(*values)
 |
 |  Method resolution order:
 |      _ReplDisplayHook
 |      enum.Enum
 |      builtins.object
 |
 |  Data and other attributes defined here:
........................ __annotations__ .......................
Help on dict object:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
........................ __builtins__ .......................
Help on dict object:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
........................ __cached__ .......................
No Python documentation found for '/home/santosg/miniconda3/lib/python3.13/site-packages/matplotlib/__pycache__/pyplot.cpython-313.pyc'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

........................ __doc__ .......................
No Python documentation found for '`matplotlib.pyplot` is a state-based interface to matplotlib. It provides\nan implicit,  MATLAB-like, way of plotting.  It also opens figures on your\nscreen, and acts as the figure GUI manager.\n\npyplot is mainly intended for interactive plots and simple cases of\nprogrammatic plot generation::\n\n    import numpy as np\n    import matplotlib.pyplot as plt\n\n    x = np.arange(0, 5, 0.1)\n    y = np.sin(x)\n    plt.plot(x, y)\n    plt.show()\n\nThe explicit object-oriented API is recommended for complex plots, though\npyplot is still usually used to create the figure and often the Axes in the\nfigure. See `.pyplot.figure`, `.pyplot.subplots`, and\n`.pyplot.subplot_mosaic` to create figures, and\n:doc:`Axes API </api/axes_api>` for the plotting methods on an Axes::\n\n    import numpy as np\n    import matplotlib.pyplot as plt\n\n    x = np.arange(0, 5, 0.1)\n    y = np.sin(x)\n    fig, ax = plt.subplots()\n    ax.plot(x, y)\n    plt.show()\n\n\nSee :ref:`api_interfaces` for an explanation of the tradeoffs between the\nimplicit and explicit interfaces.'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

........................ __file__ .......................
No Python documentation found for '/home/santosg/miniconda3/lib/python3.13/site-packages/matplotlib/pyplot.py'.
........................ __loader__ .......................
Help on SourceFileLoader in module importlib._bootstrap_external object:

class SourceFileLoader(FileLoader, SourceLoader)
 |  SourceFileLoader(fullname, path)
 |
 |  Concrete implementation of SourceLoader using the file system.
 |
 |  Method resolution order:
 |      SourceFileLoader
 |      FileLoader
 |      SourceLoader
........................ __name__ .......................
Help on module matplotlib.pyplot in matplotlib:

NAME
    matplotlib.pyplot

DESCRIPTION
    `matplotlib.pyplot` is a state-based interface to matplotlib. It provides
    an implicit,  MATLAB-like, way of plotting.  It also opens figures on your
    screen, and acts as the figure GUI manager.

    pyplot is mainly intended for interactive plots and simple cases of
........................ __package__ .......................
Help on package matplotlib:

NAME
    matplotlib - An object-oriented plotting library.

DESCRIPTION
    A procedural interface is provided by the companion pyplot module,
    which may be imported directly, e.g.::

        import matplotlib.pyplot as plt

........................ __spec__ .......................
Help on ModuleSpec in module importlib._bootstrap object:

class ModuleSpec(builtins.object)
 |  ModuleSpec(name, loader, *, origin=None, loader_state=None, is_package=None)
 |
 |  The specification for a module, used for loading.
 |
 |  A module's spec is the source for information about the module.  For
 |  data associated with the module, including source, use the spec's
 |  loader.
 |
........................ _add_pyplot_note .......................
Help on function _add_pyplot_note in module matplotlib.pyplot:

_add_pyplot_note(func, wrapped_func)
    Add a note to the docstring of *func* that it is a pyplot wrapper.

    The note is added to the "Notes" section of the docstring. If that does
    not exist, a "Notes" section is created. In numpydoc, the "Notes"
    section is the third last possible section, only potentially followed by
    "References" and "Examples".

........................ _api .......................
........................ _auto_draw_if_interactive .......................
Help on function _auto_draw_if_interactive in module matplotlib.pyplot:

_auto_draw_if_interactive(fig, val)
    An internal helper function for making sure that auto-redrawing
    works as intended in the plain python repl.

    Parameters
    ----------
    fig : Figure
        A figure object which is assumed to be associated with a canvas

........................ _backend_mod .......................
Help on class backend_mod in module matplotlib.pyplot:

class backend_mod(matplotlib.backend_bases._Backend)
 |  # In that classical approach, backends are implemented as modules, but
 |  # "inherit" default method implementations from backend_bases._Backend.
 |  # This is achieved by creating a "class" that inherits from
 |  # backend_bases._Backend and whose body is filled with the module globals.
 |
 |  Method resolution order:
 |      backend_mod
 |      matplotlib.backend_bases._Backend
........................ _color_sequences .......................
Help on ColorSequenceRegistry in module matplotlib.colors object:

class ColorSequenceRegistry(collections.abc.Mapping)
 |  Container for sequences of colors that are known to Matplotlib by name.
 |
 |  The universal registry instance is `matplotlib.color_sequences`. There
 |  should be no need for users to instantiate `.ColorSequenceRegistry`
 |  themselves.
 |
 |  Read access uses a dict-like interface mapping names to lists of colors::
 |
........................ _colormaps .......................
Help on ColormapRegistry in module matplotlib.cm object:

class ColormapRegistry(collections.abc.Mapping)
 |  ColormapRegistry(cmaps)
 |
 |  Container for colormaps that are known to Matplotlib by name.
 |
 |  The universal registry instance is `matplotlib.colormaps`. There should be
 |  no need for users to instantiate `.ColormapRegistry` themselves.
 |
 |  Read access uses a dict-like interface mapping names to `.Colormap`\s::
........................ _copy_docstring_and_deprecators .......................
Help on function _copy_docstring_and_deprecators in module matplotlib.pyplot:

_copy_docstring_and_deprecators(
    method: 'Any',
    func: 'Callable[_P, _R] | None' = None
) -> 'Callable[[Callable[_P, _R]], Callable[_P, _R]] | Callable[_P, _R]'

........................ _docstring .......................
Help on module matplotlib._docstring in matplotlib:

NAME
........................ _draw_all_if_interactive .......................
Help on function _draw_all_if_interactive in module matplotlib.pyplot:

_draw_all_if_interactive() -> 'None'

........................ _get_backend_mod .......................
Help on function _get_backend_mod in module matplotlib.pyplot:

_get_backend_mod() -> 'type[matplotlib.backend_bases._Backend]'
    Ensure that a backend is selected and return it.

    This is currently private, but may be made public in the future.
........................ _get_pyplot_commands .......................
Help on function _get_pyplot_commands in module matplotlib.pyplot:

_get_pyplot_commands() -> 'list[str]'

........................ _log .......................
Help on Logger in module logging object:

class Logger(Filterer)
 |  Logger(name, level=0)
 |
 |  Instances of the Logger class represent a single logging channel. A
........................ _pylab_helpers .......................
Help on module matplotlib._pylab_helpers in matplotlib:

NAME
    matplotlib._pylab_helpers - Manage figures for the pyplot interface.

CLASSES
    builtins.object
        Gcf

    class Gcf(builtins.object)
     |  Singleton to maintain the relation between figures and their managers, and
........................ _warn_if_gui_out_of_main_thread .......................
Help on function _warn_if_gui_out_of_main_thread in module matplotlib.pyplot:

_warn_if_gui_out_of_main_thread() -> 'None'

........................ acorr .......................
Help on function acorr in module matplotlib.pyplot:

acorr(x: 'ArrayLike', *, data=None, **kwargs) -> 'tuple[np.ndarray, np.ndarray, LineCollection | Line2D, Line2D | None]'
    Plot the autocorrelation of *x*.

    Parameters
........................ angle_spectrum .......................
Help on function angle_spectrum in module matplotlib.pyplot:

angle_spectrum(
    x: 'ArrayLike',
    *,
    Fs: 'float | None' = None,
    Fc: 'int | None' = None,
    window: 'Callable[[ArrayLike], ArrayLike] | ArrayLike | None' = None,
    pad_to: 'int | None' = None,
    sides: "Literal['default', 'onesided', 'twosided'] | None" = None,
    data=None,
........................ annotate .......................
Help on function annotate in module matplotlib.pyplot:

annotate(
    text: 'str',
    xy: 'tuple[float, float]',
    xytext: 'tuple[float, float] | None' = None,
    xycoords: 'CoordsType' = 'data',
    textcoords: 'CoordsType | None' = None,
    arrowprops: 'dict[str, Any] | None' = None,
    annotation_clip: 'bool | None' = None,
    **kwargs
........................ annotations .......................
Help on _Feature in module __future__ object:

class _Feature(builtins.object)
 |  _Feature(optionalRelease, mandatoryRelease, compiler_flag)
 |
 |  Methods defined here:
 |
 |  __init__(self, optionalRelease, mandatoryRelease, compiler_flag)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __repr__(self)
........................ arrow .......................
Help on function arrow in module matplotlib.pyplot:

arrow(x: 'float', y: 'float', dx: 'float', dy: 'float', **kwargs) -> 'FancyArrow'
    [*Discouraged*] Add an arrow to the Axes.

    This draws an arrow from ``(x, y)`` to ``(x+dx, y+dy)``.

    .. admonition:: Discouraged

        The use of this method is discouraged because it is not guaranteed
        that the arrow renders reasonably. For example, the resulting arrow
........................ autoscale .......................
Help on function autoscale in module matplotlib.pyplot:

autoscale(
    enable: 'bool' = True,
    axis: "Literal['both', 'x', 'y']" = 'both',
    tight: 'bool | None' = None
) -> 'None'
    Autoscale the axis view to the data (toggle).

    Convenience method for simple axis view autoscaling.
    It turns autoscaling on or off, and then,
........................ autumn .......................
Help on function autumn in module matplotlib.pyplot:

autumn() -> 'None'
    Set the colormap to 'autumn'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.

........................ available_backends .......................
Help on list object:

........................ axes .......................
Help on function axes in module matplotlib.pyplot:

axes(arg: 'None | tuple[float, float, float, float]' = None, **kwargs) -> 'matplotlib.axes.Axes'
    Add an Axes to the current figure and make it the current Axes.

    Call signatures::

        plt.axes()
        plt.axes(rect, projection=None, polar=False, **kwargs)
        plt.axes(ax)

........................ axhline .......................
Help on function axhline in module matplotlib.pyplot:

axhline(y: 'float' = 0, xmin: 'float' = 0, xmax: 'float' = 1, **kwargs) -> 'Line2D'
    Add a horizontal line spanning the whole or fraction of the Axes.

    Note: If you want to set x-limits in data coordinates, use
    `~.Axes.hlines` instead.

    Parameters
    ----------
    y : float, default: 0
........................ axhspan .......................
Help on function axhspan in module matplotlib.pyplot:

axhspan(
    ymin: 'float',
    ymax: 'float',
    xmin: 'float' = 0,
    xmax: 'float' = 1,
    **kwargs
) -> 'Rectangle'
    Add a horizontal span (rectangle) across the Axes.

........................ axis .......................
Help on function axis in module matplotlib.pyplot:

axis(
    arg: 'tuple[float, float, float, float] | bool | str | None' = None,
    /,
    *,
    emit: 'bool' = True,
    **kwargs
) -> 'tuple[float, float, float, float]'
    Convenience method to get or set some axis properties.

........................ axline .......................
Help on function axline in module matplotlib.pyplot:

axline(
    xy1: 'tuple[float, float]',
    xy2: 'tuple[float, float] | None' = None,
    *,
    slope: 'float | None' = None,
    **kwargs
) -> 'AxLine'
    Add an infinitely long straight line.

........................ axvline .......................
Help on function axvline in module matplotlib.pyplot:

axvline(x: 'float' = 0, ymin: 'float' = 0, ymax: 'float' = 1, **kwargs) -> 'Line2D'
    Add a vertical line spanning the whole or fraction of the Axes.

    Note: If you want to set y-limits in data coordinates, use
    `~.Axes.vlines` instead.

    Parameters
    ----------
    x : float, default: 0
........................ axvspan .......................
Help on function axvspan in module matplotlib.pyplot:

axvspan(
    xmin: 'float',
    xmax: 'float',
    ymin: 'float' = 0,
    ymax: 'float' = 1,
    **kwargs
) -> 'Rectangle'
    Add a vertical span (rectangle) across the Axes.

........................ backend_registry .......................
Help on BackendRegistry in module matplotlib.backends.registry object:

class BackendRegistry(builtins.object)
 |  Registry of backends available within Matplotlib.
 |
 |  This is the single source of truth for available backends.
 |
 |  All use of ``BackendRegistry`` should be via the singleton instance
 |  ``backend_registry`` which can be imported from ``matplotlib.backends``.
 |
 |  Each backend has a name, a module name containing the backend code, and an
........................ bar .......................
Help on function bar in module matplotlib.pyplot:

bar(
    x: 'float | ArrayLike',
    height: 'float | ArrayLike',
    width: 'float | ArrayLike' = 0.8,
    bottom: 'float | ArrayLike | None' = None,
    *,
    align: "Literal['center', 'edge']" = 'center',
    data=None,
    **kwargs
........................ bar_label .......................
Help on function bar_label in module matplotlib.pyplot:

bar_label(
    container: 'BarContainer',
    labels: 'ArrayLike | None' = None,
    *,
    fmt: 'str | Callable[[float], str]' = '%g',
    label_type: "Literal['center', 'edge']" = 'edge',
    padding: 'float' = 0,
    **kwargs
) -> 'list[Annotation]'
........................ barbs .......................
Help on function barbs in module matplotlib.pyplot:

barbs(*args, data=None, **kwargs) -> 'Barbs'
    Plot a 2D field of wind barbs.

    Call signature::

      barbs([X, Y], U, V, [C], /, **kwargs)

    Where *X*, *Y* define the barb locations, *U*, *V* define the barb
    directions, and *C* optionally sets the color.
........................ barh .......................
Help on function barh in module matplotlib.pyplot:

barh(
    y: 'float | ArrayLike',
    width: 'float | ArrayLike',
    height: 'float | ArrayLike' = 0.8,
    left: 'float | ArrayLike | None' = None,
    *,
    align: "Literal['center', 'edge']" = 'center',
    data=None,
    **kwargs
........................ bone .......................
Help on function bone in module matplotlib.pyplot:

bone() -> 'None'
    Set the colormap to 'bone'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.

........................ box .......................
Help on function box in module matplotlib.pyplot:

........................ boxplot .......................
Help on function boxplot in module matplotlib.pyplot:

boxplot(
    x: 'ArrayLike | Sequence[ArrayLike]',
    *,
    notch: 'bool | None' = None,
    sym: 'str | None' = None,
    vert: 'bool | None' = None,
    orientation: "Literal['vertical', 'horizontal']" = 'vertical',
    whis: 'float | tuple[float, float] | None' = None,
    positions: 'ArrayLike | None' = None,
........................ broken_barh .......................
Help on function broken_barh in module matplotlib.pyplot:

broken_barh(
    xranges: 'Sequence[tuple[float, float]]',
    yrange: 'tuple[float, float]',
    *,
    data=None,
    **kwargs
) -> 'PolyCollection'
    Plot a horizontal sequence of rectangles.

........................ cast .......................
Help on function cast in module typing:

cast(typ, val)
    Cast a value to a type.

    This returns the value unchanged.  To the type checker this
    signals that the return value has the designated type, but at
    runtime we intentionally don't check anything (we want this
    to be as fast as possible).

........................ cbook .......................
........................ cla .......................
Help on function cla in module matplotlib.pyplot:

cla() -> 'None'
    Clear the current Axes.

........................ clabel .......................
Help on function clabel in module matplotlib.pyplot:

clabel(CS: 'ContourSet', levels: 'ArrayLike | None' = None, **kwargs) -> 'list[Text]'
    Label a contour plot.

........................ clf .......................
Help on function clf in module matplotlib.pyplot:

clf() -> 'None'
    Clear the current figure.

........................ clim .......................
Help on function clim in module matplotlib.pyplot:

clim(vmin: 'float | None' = None, vmax: 'float | None' = None) -> 'None'
    Set the color limits of the current image.

........................ close .......................
Help on function close in module matplotlib.pyplot:

close(fig: "None | int | str | Figure | Literal['all']" = None) -> 'None'
    Close a figure window, and unregister it from pyplot.

    Parameters
    ----------
    fig : None or int or str or `.Figure`
        The figure to close. There are a number of ways to specify this:

        - *None*: the current figure
........................ cm .......................
Help on module matplotlib.cm in matplotlib:

NAME
    matplotlib.cm - Builtin colormaps, colormap handling utilities, and the `ScalarMappable` mixin.

DESCRIPTION
    .. seealso::

      :doc:`/gallery/color/colormap_reference` for a list of builtin colormaps.

      :ref:`colormap-manipulation` for examples of how to make
........................ cohere .......................
Help on function cohere in module matplotlib.pyplot:

cohere(
    x: 'ArrayLike',
    y: 'ArrayLike',
    *,
    NFFT: 'int' = 256,
    Fs: 'float' = 2,
    Fc: 'int' = 0,
    detrend: "Literal['none', 'mean', 'linear'] | Callable[[ArrayLike], ArrayLike]" = <function detrend_none at 0x7b1e2a4423e0>,
    window: 'Callable[[ArrayLike], ArrayLike] | ArrayLike' = <function window_hanning at 0x7b1e2a442160>,
........................ color_sequences .......................
Help on ColorSequenceRegistry in module matplotlib.colors object:

class ColorSequenceRegistry(collections.abc.Mapping)
 |  Container for sequences of colors that are known to Matplotlib by name.
 |
 |  The universal registry instance is `matplotlib.color_sequences`. There
 |  should be no need for users to instantiate `.ColorSequenceRegistry`
 |  themselves.
 |
 |  Read access uses a dict-like interface mapping names to lists of colors::
 |
........................ colorbar .......................
Help on function colorbar in module matplotlib.pyplot:

colorbar(
    mappable: 'ScalarMappable | ColorizingArtist | None' = None,
    cax: 'matplotlib.axes.Axes | None' = None,
    ax: 'matplotlib.axes.Axes | Iterable[matplotlib.axes.Axes] | None' = None,
    **kwargs
) -> 'Colorbar'
    Add a colorbar to a plot.

    Parameters
........................ colormaps .......................
Help on ColormapRegistry in module matplotlib.cm object:

class ColormapRegistry(collections.abc.Mapping)
 |  ColormapRegistry(cmaps)
 |
 |  Container for colormaps that are known to Matplotlib by name.
 |
 |  The universal registry instance is `matplotlib.colormaps`. There should be
 |  no need for users to instantiate `.ColormapRegistry` themselves.
 |
 |  Read access uses a dict-like interface mapping names to `.Colormap`\s::
........................ connect .......................
Help on function connect in module matplotlib.pyplot:

connect(s: 'str', func: 'Callable[[Event], Any]') -> 'int'
    Bind function *func* to event *s*.

    Parameters
    ----------
    s : str
        One of the following events ids:

        - 'button_press_event'
........................ contour .......................
Help on function contour in module matplotlib.pyplot:

contour(*args, data=None, **kwargs) -> 'QuadContourSet'
    Plot contour lines.

    Call signature::

        contour([X, Y,] Z, /, [levels], **kwargs)

    The arguments *X*, *Y*, *Z* are positional-only.

........................ contourf .......................
Help on function contourf in module matplotlib.pyplot:

contourf(*args, data=None, **kwargs) -> 'QuadContourSet'
    Plot filled contours.

    Call signature::

        contourf([X, Y,] Z, /, [levels], **kwargs)

    The arguments *X*, *Y*, *Z* are positional-only.

........................ cool .......................
Help on function cool in module matplotlib.pyplot:

cool() -> 'None'
    Set the colormap to 'cool'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.

........................ copper .......................
Help on function copper in module matplotlib.pyplot:

........................ csd .......................
Help on function csd in module matplotlib.pyplot:

csd(
    x: 'ArrayLike',
    y: 'ArrayLike',
    *,
    NFFT: 'int | None' = None,
    Fs: 'float | None' = None,
    Fc: 'int | None' = None,
    detrend: "Literal['none', 'mean', 'linear'] | Callable[[ArrayLike], ArrayLike] | None" = None,
    window: 'Callable[[ArrayLike], ArrayLike] | ArrayLike | None' = None,
........................ cycler .......................
Help on function cycler in module cycler:

cycler(*args, **kwargs)
    Create a new `Cycler` object from a single positional argument,
    a pair of positional arguments, or the combination of keyword arguments.

    cycler(arg)
    cycler(label1=itr1[, label2=iter2[, ...]])
    cycler(label, itr)

    Form 1 simply copies a given `Cycler` object.
........................ delaxes .......................
Help on function delaxes in module matplotlib.pyplot:

delaxes(ax: 'matplotlib.axes.Axes | None' = None) -> 'None'
    Remove an `~.axes.Axes` (defaulting to the current Axes) from its figure.

........................ disconnect .......................
Help on function disconnect in module matplotlib.pyplot:

disconnect(cid: 'int') -> 'None'
    Disconnect the callback with id *cid*.

........................ draw .......................
Help on function draw in module matplotlib.pyplot:

draw() -> 'None'
    Redraw the current figure.

    This is used to update a figure that has been altered, but not
    automatically re-drawn.  If interactive mode is on (via `.ion()`), this
    should be only rarely needed, but there may be ways to modify the state of
    a figure without marking it as "stale".  Please report these cases as bugs.

    This is equivalent to calling ``fig.canvas.draw_idle()``, where ``fig`` is
........................ draw_all .......................
Help on method draw_all in module matplotlib._pylab_helpers:

draw_all(force=False) class method of matplotlib._pylab_helpers.Gcf
    Redraw all stale managed figures, or, if *force* is True, all managed
    figures.

........................ draw_if_interactive .......................
Help on function draw_if_interactive in module matplotlib.pyplot:

draw_if_interactive()
    Redraw the current figure if in interactive mode.
........................ ecdf .......................
Help on function ecdf in module matplotlib.pyplot:

ecdf(
    x: 'ArrayLike',
    weights: 'ArrayLike | None' = None,
    *,
    complementary: 'bool' = False,
    orientation: "Literal['vertical', 'horizontal']" = 'vertical',
    compress: 'bool' = False,
    data=None,
    **kwargs
........................ errorbar .......................
Help on function errorbar in module matplotlib.pyplot:

errorbar(
    x: 'float | ArrayLike',
    y: 'float | ArrayLike',
    yerr: 'float | ArrayLike | None' = None,
    xerr: 'float | ArrayLike | None' = None,
    fmt: 'str' = '',
    *,
    ecolor: 'ColorType | None' = None,
    elinewidth: 'float | None' = None,
........................ eventplot .......................
Help on function eventplot in module matplotlib.pyplot:

eventplot(
    positions: 'ArrayLike | Sequence[ArrayLike]',
    *,
    orientation: "Literal['horizontal', 'vertical']" = 'horizontal',
    lineoffsets: 'float | Sequence[float]' = 1,
    linelengths: 'float | Sequence[float]' = 1,
    linewidths: 'float | Sequence[float] | None' = None,
    colors: 'ColorType | Sequence[ColorType] | None' = None,
    alpha: 'float | Sequence[float] | None' = None,
........................ figaspect .......................
Help on function figaspect in module matplotlib.figure:

figaspect(arg)
    Calculate the width and height for a figure with a specified aspect ratio.

    While the height is taken from :rc:`figure.figsize`, the width is
    adjusted to match the desired aspect ratio. Additionally, it is ensured
    that the width is in the range [4., 16.] and the height is in the range
    [2., 16.]. If necessary, the default height is adjusted to ensure this.

    Parameters
........................ figimage .......................
Help on function figimage in module matplotlib.pyplot:

figimage(
    X: 'ArrayLike',
    xo: 'int' = 0,
    yo: 'int' = 0,
    alpha: 'float | None' = None,
    norm: 'str | Normalize | None' = None,
    cmap: 'str | Colormap | None' = None,
    vmin: 'float | None' = None,
    vmax: 'float | None' = None,
........................ figlegend .......................
Help on function figlegend in module matplotlib.pyplot:

figlegend(*args, **kwargs) -> 'Legend'
    Place a legend on the figure.

    Call signatures::

        figlegend()
        figlegend(handles, labels)
        figlegend(handles=handles)
        figlegend(labels)
........................ fignum_exists .......................
Help on function fignum_exists in module matplotlib.pyplot:

fignum_exists(num: 'int | str') -> 'bool'
    Return whether the figure with the given id exists.

    Parameters
    ----------
    num : int or str
        A figure identifier.

    Returns
........................ figtext .......................
Help on function figtext in module matplotlib.pyplot:

figtext(
    x: 'float',
    y: 'float',
    s: 'str',
    fontdict: 'dict[str, Any] | None' = None,
    **kwargs
) -> 'Text'
    Add text to figure.

........................ figure .......................
Help on function figure in module matplotlib.pyplot:

figure(
    num: 'int | str | Figure | SubFigure | None' = None,
    figsize: 'ArrayLike | None' = None,
    dpi: 'float | None' = None,
    *,
    facecolor: 'ColorType | None' = None,
    edgecolor: 'ColorType | None' = None,
    frameon: 'bool' = True,
    FigureClass: 'type[Figure]' = <class 'matplotlib.figure.Figure'>,
........................ fill .......................
Help on function fill in module matplotlib.pyplot:

fill(*args, data=None, **kwargs) -> 'list[Polygon]'
    Plot filled polygons.

    Parameters
    ----------
    *args : sequence of x, y, [color]
        Each polygon is defined by the lists of *x* and *y* positions of
        its nodes, optionally followed by a *color* specifier. See
        :mod:`matplotlib.colors` for supported color specifiers. The
........................ fill_between .......................
Help on function fill_between in module matplotlib.pyplot:

fill_between(
    x: 'ArrayLike',
    y1: 'ArrayLike | float',
    y2: 'ArrayLike | float' = 0,
    where: 'Sequence[bool] | None' = None,
    interpolate: 'bool' = False,
    step: "Literal['pre', 'post', 'mid'] | None" = None,
    *,
    data=None,
........................ fill_betweenx .......................
Help on function fill_betweenx in module matplotlib.pyplot:

fill_betweenx(
    y: 'ArrayLike',
    x1: 'ArrayLike | float',
    x2: 'ArrayLike | float' = 0,
    where: 'Sequence[bool] | None' = None,
    step: "Literal['pre', 'post', 'mid'] | None" = None,
    interpolate: 'bool' = False,
    *,
    data=None,
........................ findobj .......................
Help on function findobj in module matplotlib.pyplot:

findobj(
    o: 'Artist | None' = None,
    match: 'Callable[[Artist], bool] | type[Artist] | None' = None,
    include_self: 'bool' = True
) -> 'list[Artist]'
    Find artist objects.

    Recursively find all `.Artist` instances contained in the artist.

........................ flag .......................
Help on function flag in module matplotlib.pyplot:

flag() -> 'None'
    Set the colormap to 'flag'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.

........................ functools .......................
Help on module functools:

........................ gca .......................
Help on function gca in module matplotlib.pyplot:

gca() -> 'Axes'
    Get the current Axes.

    If there is currently no Axes on this Figure, a new one is created
    using `.Figure.add_subplot`.  (To test whether there is currently an
    Axes on a Figure, check whether ``figure.axes`` is empty.  To test
    whether there is currently a Figure on the pyplot figure stack, check
    whether `.pyplot.get_fignums()` is empty.)

........................ gcf .......................
Help on function gcf in module matplotlib.pyplot:

gcf() -> 'Figure'
    Get the current figure.

    If there is currently no figure on the pyplot figure stack, a new one is
    created using `~.pyplot.figure()`.  (To test whether there is currently a
    figure on the pyplot figure stack, check whether `~.pyplot.get_fignums()`
    is empty.)

........................ gci .......................
........................ get .......................
Help on function get in module matplotlib.pyplot:

get(obj, *args, **kwargs)
    Return the value of an `.Artist`'s *property*, or print all of them.

    Parameters
    ----------
    obj : `~matplotlib.artist.Artist`
        The queried artist; e.g., a `.Line2D`, a `.Text`, or an `~.axes.Axes`.

    property : str or None, default: None
........................ get_backend .......................
Help on function get_backend in module matplotlib:

get_backend(*, auto_select=True)
    Return the name of the current backend.

    Parameters
    ----------
    auto_select : bool, default: True
        Whether to trigger backend resolution if no backend has been
        selected so far. If True, this ensures that a valid backend
        is returned. If False, this returns None if no backend has been
........................ get_cmap .......................
Help on function get_cmap in module matplotlib.pyplot:

get_cmap(name: 'Colormap | str | None' = None, lut: 'int | None' = None) -> 'Colormap'
    Get a colormap instance, defaulting to rc values if *name* is None.

    Parameters
    ----------
    name : `~matplotlib.colors.Colormap` or str or None, default: None
        If a `.Colormap` instance, it will be returned. Otherwise, the name of
        a colormap known to Matplotlib, which will be resampled by *lut*. The
        default, None, means :rc:`image.cmap`.
........................ get_current_fig_manager .......................
Help on function get_current_fig_manager in module matplotlib.pyplot:

get_current_fig_manager() -> 'FigureManagerBase | None'
    Return the figure manager of the current figure.

    The figure manager is a container for the actual backend-depended window
    that displays the figure on screen.

    If no current figure exists, a new one is created, and its figure
    manager is returned.

........................ get_figlabels .......................
Help on function get_figlabels in module matplotlib.pyplot:

get_figlabels() -> 'list[Any]'
    Return a list of existing figure labels.

........................ get_fignums .......................
Help on function get_fignums in module matplotlib.pyplot:

get_fignums() -> 'list[int]'
    Return a list of existing figure numbers.

........................ get_plot_commands .......................
Help on function get_plot_commands in module matplotlib.pyplot:

get_plot_commands() -> 'list[str]'
    [*Deprecated*] Get a sorted list of all of the plotting commands.

    Notes
    -----
    .. deprecated:: 3.7

........................ get_scale_names .......................
Help on function get_scale_names in module matplotlib.scale:
........................ getp .......................
Help on function getp in module matplotlib.pyplot:

getp(obj, *args, **kwargs)
    Return the value of an `.Artist`'s *property*, or print all of them.

    Parameters
    ----------
    obj : `~matplotlib.artist.Artist`
        The queried artist; e.g., a `.Line2D`, a `.Text`, or an `~.axes.Axes`.

    property : str or None, default: None
........................ ginput .......................
Help on function ginput in module matplotlib.pyplot:

ginput(
    n: 'int' = 1,
    timeout: 'float' = 30,
    show_clicks: 'bool' = True,
    mouse_add: 'MouseButton' = <MouseButton.LEFT: 1>,
    mouse_pop: 'MouseButton' = <MouseButton.RIGHT: 3>,
    mouse_stop: 'MouseButton' = <MouseButton.MIDDLE: 2>
) -> 'list[tuple[int, int]]'
    Blocking call to interact with a figure.
........................ gray .......................
Help on function gray in module matplotlib.pyplot:

gray() -> 'None'
    Set the colormap to 'gray'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.

........................ grid .......................
Help on function grid in module matplotlib.pyplot:

........................ hexbin .......................
Help on function hexbin in module matplotlib.pyplot:

hexbin(
    x: 'ArrayLike',
    y: 'ArrayLike',
    C: 'ArrayLike | None' = None,
    *,
    gridsize: 'int | tuple[int, int]' = 100,
    bins: "Literal['log'] | int | Sequence[float] | None" = None,
    xscale: "Literal['linear', 'log']" = 'linear',
    yscale: "Literal['linear', 'log']" = 'linear',
........................ hist .......................
Help on function hist in module matplotlib.pyplot:

hist(
    x: 'ArrayLike | Sequence[ArrayLike]',
    bins: 'int | Sequence[float] | str | None' = None,
    *,
    range: 'tuple[float, float] | None' = None,
    density: 'bool' = False,
    weights: 'ArrayLike | None' = None,
    cumulative: 'bool | float' = False,
    bottom: 'ArrayLike | float | None' = None,
........................ hist2d .......................
Help on function hist2d in module matplotlib.pyplot:

hist2d(
    x: 'ArrayLike',
    y: 'ArrayLike',
    bins: 'None | int | tuple[int, int] | ArrayLike | tuple[ArrayLike, ArrayLike]' = 10,
    *,
    range: 'ArrayLike | None' = None,
    density: 'bool' = False,
    weights: 'ArrayLike | None' = None,
    cmin: 'float | None' = None,
........................ hlines .......................
Help on function hlines in module matplotlib.pyplot:

hlines(
    y: 'float | ArrayLike',
    xmin: 'float | ArrayLike',
    xmax: 'float | ArrayLike',
    colors: 'ColorType | Sequence[ColorType] | None' = None,
    linestyles: 'LineStyleType' = 'solid',
    *,
    label: 'str' = '',
    data=None,
........................ hot .......................
Help on function hot in module matplotlib.pyplot:

hot() -> 'None'
    Set the colormap to 'hot'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.

........................ hsv .......................
Help on function hsv in module matplotlib.pyplot:

........................ importlib .......................
Help on package importlib:

NAME
    importlib - A pure Python implementation of import.

MODULE REFERENCE
    https://docs.python.org/3.13/library/importlib.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
........................ imread .......................
Help on function imread in module matplotlib.pyplot:

imread(fname: 'str | pathlib.Path | BinaryIO', format: 'str | None' = None) -> 'np.ndarray'
    Read an image from a file into an array.

    .. note::

        This function exists for historical reasons.  It is recommended to
        use `PIL.Image.open` instead for loading images.

    Parameters
........................ imsave .......................
Help on function imsave in module matplotlib.pyplot:

imsave(fname: 'str | os.PathLike | BinaryIO', arr: 'ArrayLike', **kwargs) -> 'None'
    Colormap and save an array as an image file.

    RGB(A) images are passed through.  Single channel images will be
    colormapped according to *cmap* and *norm*.

    .. note::

       If you want to save a single channel image as gray scale please use an
........................ imshow .......................
Help on function imshow in module matplotlib.pyplot:

imshow(
    X: 'ArrayLike | PIL.Image.Image',
    cmap: 'str | Colormap | None' = None,
    norm: 'str | Normalize | None' = None,
    *,
    aspect: "Literal['equal', 'auto'] | float | None" = None,
    interpolation: 'str | None' = None,
    alpha: 'float | ArrayLike | None' = None,
    vmin: 'float | None' = None,
........................ inferno .......................
Help on function inferno in module matplotlib.pyplot:

inferno() -> 'None'
    Set the colormap to 'inferno'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.

........................ inspect .......................
Help on module inspect:

........................ install_repl_displayhook .......................
Help on function install_repl_displayhook in module matplotlib.pyplot:

install_repl_displayhook() -> 'None'
    Connect to the display hook of the current shell.

    The display hook gets called when the read-evaluate-print-loop (REPL) of
    the shell has finished the execution of a command. We use this callback
    to be able to automatically update a figure in interactive mode.

    This works both with IPython and with vanilla python shells.

........................ interactive .......................
Help on function interactive in module matplotlib:

interactive(b)
    Set whether to redraw after every plotting command (e.g. `.pyplot.xlabel`).

........................ ioff .......................
Help on function ioff in module matplotlib.pyplot:

ioff() -> 'AbstractContextManager'
    Disable interactive mode.

........................ ion .......................
Help on function ion in module matplotlib.pyplot:

ion() -> 'AbstractContextManager'
    Enable interactive mode.

    See `.pyplot.isinteractive` for more details.

    See Also
    --------
    ioff : Disable interactive mode.
    isinteractive : Whether interactive mode is enabled.
........................ isinteractive .......................
Help on function isinteractive in module matplotlib.pyplot:

isinteractive() -> 'bool'
    Return whether plots are updated after every plotting command.

    The interactive mode is mainly useful if you build plots from the command
    line and want to see the effect of each command while you are building the
    figure.

    In interactive mode:

........................ jet .......................
Help on function jet in module matplotlib.pyplot:

jet() -> 'None'
    Set the colormap to 'jet'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.

........................ legend .......................
Help on function legend in module matplotlib.pyplot:

........................ locator_params .......................
Help on function locator_params in module matplotlib.pyplot:

locator_params(
    axis: "Literal['both', 'x', 'y']" = 'both',
    tight: 'bool | None' = None,
    **kwargs
) -> 'None'
    Control behavior of major tick locators.

    Because the locator is involved in autoscaling, `~.Axes.autoscale_view`
    is called automatically after the parameters are changed.
........................ logging .......................
Help on package logging:

NAME
    logging

MODULE REFERENCE
    https://docs.python.org/3.13/library/logging.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
........................ loglog .......................
Help on function loglog in module matplotlib.pyplot:

loglog(*args, **kwargs) -> 'list[Line2D]'
    Make a plot with log scaling on both the x- and y-axis.

    Call signatures::

        loglog([x], y, [fmt], data=None, **kwargs)
        loglog([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)

    This is just a thin wrapper around `.plot` which additionally changes
........................ magma .......................
Help on function magma in module matplotlib.pyplot:

magma() -> 'None'
    Set the colormap to 'magma'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.

........................ magnitude_spectrum .......................
Help on function magnitude_spectrum in module matplotlib.pyplot:

........................ margins .......................
Help on function margins in module matplotlib.pyplot:

margins(
    *margins: 'float',
    x: 'float | None' = None,
    y: 'float | None' = None,
    tight: 'bool | None' = True
) -> 'tuple[float, float] | None'
    Set or retrieve margins around the data for autoscaling axis limits.

    This allows to configure the padding around the data without having to
........................ matplotlib .......................
Help on package matplotlib:

NAME
    matplotlib - An object-oriented plotting library.

DESCRIPTION
    A procedural interface is provided by the companion pyplot module,
    which may be imported directly, e.g.::

        import matplotlib.pyplot as plt

........................ matshow .......................
Help on function matshow in module matplotlib.pyplot:

matshow(A: 'ArrayLike', fignum: 'None | int' = None, **kwargs) -> 'AxesImage'
    Display a 2D array as a matrix in a new figure window.

    The origin is set at the upper left hand corner.
    The indexing is ``(row, column)`` so that the first index runs vertically
    and the second index runs horizontally in the figure:

    .. code-block:: none

........................ minorticks_off .......................
Help on function minorticks_off in module matplotlib.pyplot:

minorticks_off() -> 'None'
    Remove minor ticks from the Axes.

    Notes
    -----

    .. note::

        This is the :ref:`pyplot wrapper <pyplot_interface>` for `.axes.Axes.minorticks_off`.
........................ minorticks_on .......................
Help on function minorticks_on in module matplotlib.pyplot:

minorticks_on() -> 'None'
    Display minor ticks on the Axes.

    Displaying minor ticks may reduce performance; you may turn them off
    using `minorticks_off()` if drawing speed is a problem.

    Notes
    -----

........................ mlab .......................
Help on module matplotlib.mlab in matplotlib:

NAME
    matplotlib.mlab

DESCRIPTION
    Numerical Python functions written for compatibility with MATLAB
    commands with the same names. Most numerical Python functions can be found in
    the `NumPy`_ and `SciPy`_ libraries. What remains here is code for performing
    spectral computations and kernel density estimations.

........................ new_figure_manager .......................
Help on function new_figure_manager in module matplotlib.pyplot:

new_figure_manager(num, *args, **kwargs)
    Create a new figure manager instance.

........................ nipy_spectral .......................
Help on function nipy_spectral in module matplotlib.pyplot:

nipy_spectral() -> 'None'
    Set the colormap to 'nipy_spectral'.

........................ np .......................
Help on package numpy:

NAME
    numpy

DESCRIPTION
    NumPy
    =====

    Provides
      1. An array object of arbitrary homogeneous items
........................ overload .......................
Help on function overload in module typing:

overload(func)
    Decorator for overloaded functions/methods.

    In a stub file, place two or more stub definitions for the same
    function in a row, each decorated with @overload.

    For example::

        @overload
........................ pause .......................
Help on function pause in module matplotlib.pyplot:

pause(interval: 'float') -> 'None'
    Run the GUI event loop for *interval* seconds.

    If there is an active figure, it will be updated and displayed before the
    pause, and the GUI event loop (if any) will run during the pause.

    This can be used for crude animation.  For more complex animation use
    :mod:`matplotlib.animation`.

........................ pcolor .......................
Help on function pcolor in module matplotlib.pyplot:

pcolor(
    *args: 'ArrayLike',
    shading: "Literal['flat', 'nearest', 'auto'] | None" = None,
    alpha: 'float | None' = None,
    norm: 'str | Normalize | None' = None,
    cmap: 'str | Colormap | None' = None,
    vmin: 'float | None' = None,
    vmax: 'float | None' = None,
    colorizer: 'Colorizer | None' = None,
........................ pcolormesh .......................
Help on function pcolormesh in module matplotlib.pyplot:

pcolormesh(
    *args: 'ArrayLike',
    alpha: 'float | None' = None,
    norm: 'str | Normalize | None' = None,
    cmap: 'str | Colormap | None' = None,
    vmin: 'float | None' = None,
    vmax: 'float | None' = None,
    colorizer: 'Colorizer | None' = None,
    shading: "Literal['flat', 'nearest', 'gouraud', 'auto'] | None" = None,
........................ phase_spectrum .......................
Help on function phase_spectrum in module matplotlib.pyplot:

phase_spectrum(
    x: 'ArrayLike',
    *,
    Fs: 'float | None' = None,
    Fc: 'int | None' = None,
    window: 'Callable[[ArrayLike], ArrayLike] | ArrayLike | None' = None,
    pad_to: 'int | None' = None,
    sides: "Literal['default', 'onesided', 'twosided'] | None" = None,
    data=None,
........................ pie .......................
Help on function pie in module matplotlib.pyplot:

pie(
    x: 'ArrayLike',
    *,
    explode: 'ArrayLike | None' = None,
    labels: 'Sequence[str] | None' = None,
    colors: 'ColorType | Sequence[ColorType] | None' = None,
    autopct: 'str | Callable[[float], str] | None' = None,
    pctdistance: 'float' = 0.6,
    shadow: 'bool' = False,
........................ pink .......................
Help on function pink in module matplotlib.pyplot:

pink() -> 'None'
    Set the colormap to 'pink'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.

........................ plasma .......................
Help on function plasma in module matplotlib.pyplot:

........................ plot .......................
Help on function plot in module matplotlib.pyplot:

plot(
    *args: 'float | ArrayLike | str',
    scalex: 'bool' = True,
    scaley: 'bool' = True,
    data=None,
    **kwargs
) -> 'list[Line2D]'
    Plot y versus x as lines and/or markers.

........................ plot_date .......................
Help on function plot_date in module matplotlib.pyplot:

plot_date(
    x: 'ArrayLike',
    y: 'ArrayLike',
    fmt: 'str' = 'o',
    tz: 'str | datetime.tzinfo | None' = None,
    xdate: 'bool' = True,
    ydate: 'bool' = False,
    *,
    data=None,
........................ polar .......................
Help on function polar in module matplotlib.pyplot:

polar(*args, **kwargs) -> 'list[Line2D]'
    Make a polar plot.

    call signature::

      polar(theta, r, [fmt], **kwargs)

    This is a convenience wrapper around `.pyplot.plot`. It ensures that the
    current Axes is polar (or creates one if needed) and then passes all parameters
........................ prism .......................
Help on function prism in module matplotlib.pyplot:

prism() -> 'None'
    Set the colormap to 'prism'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.

........................ psd .......................
Help on function psd in module matplotlib.pyplot:

........................ quiver .......................
Help on function quiver in module matplotlib.pyplot:

quiver(*args, data=None, **kwargs) -> 'Quiver'
    Plot a 2D field of arrows.

    Call signature::

      quiver([X, Y], U, V, [C], /, **kwargs)

    *X*, *Y* define the arrow locations, *U*, *V* define the arrow directions, and
    *C* optionally sets the color. The arguments *X*, *Y*, *U*, *V*, *C* are
........................ quiverkey .......................
Help on function quiverkey in module matplotlib.pyplot:

quiverkey(
    Q: 'Quiver',
    X: 'float',
    Y: 'float',
    U: 'float',
    label: 'str',
    **kwargs
) -> 'QuiverKey'
    Add a key to a quiver plot.
........................ rc .......................
Help on function rc in module matplotlib.pyplot:

rc(group: 'str', **kwargs) -> 'None'
    Set the current `.rcParams`.  *group* is the grouping for the rc, e.g.,
    for ``lines.linewidth`` the group is ``lines``, for
    ``axes.facecolor``, the group is ``axes``, and so on.  Group may
    also be a list or tuple of group names, e.g., (*xtick*, *ytick*).
    *kwargs* is a dictionary attribute name/value pairs, e.g.,::

      rc('lines', linewidth=2, color='r')

........................ rcParams .......................
Help on RcParams in module matplotlib object:

class RcParams(collections.abc.MutableMapping, builtins.dict)
 |  RcParams(*args, **kwargs)
 |
 |  A dict-like key-value store for config parameters, including validation.
 |
 |  Validating functions are defined and associated with rc parameters in
 |  :mod:`matplotlib.rcsetup`.
 |
 |  The list of rcParams is:
........................ rcParamsDefault .......................
Help on RcParams in module matplotlib object:

class RcParams(collections.abc.MutableMapping, builtins.dict)
 |  RcParams(*args, **kwargs)
 |
 |  A dict-like key-value store for config parameters, including validation.
 |
 |  Validating functions are defined and associated with rc parameters in
 |  :mod:`matplotlib.rcsetup`.
 |
 |  The list of rcParams is:
........................ rcParamsOrig .......................
Help on RcParams in module matplotlib object:

class RcParams(collections.abc.MutableMapping, builtins.dict)
 |  RcParams(*args, **kwargs)
 |
 |  A dict-like key-value store for config parameters, including validation.
 |
 |  Validating functions are defined and associated with rc parameters in
 |  :mod:`matplotlib.rcsetup`.
 |
 |  The list of rcParams is:
........................ rc_context .......................
Help on function rc_context in module matplotlib.pyplot:

rc_context(
    rc: 'dict[str, Any] | None' = None,
    fname: 'str | pathlib.Path | os.PathLike | None' = None
) -> 'AbstractContextManager[None]'
    Return a context manager for temporarily changing rcParams.

    The :rc:`backend` will not be reset by the context manager.

    rcParams changed both through the context manager invocation and
........................ rcdefaults .......................
Help on function rcdefaults in module matplotlib.pyplot:

rcdefaults() -> 'None'
    Restore the `.rcParams` from Matplotlib's internal default style.

    Style-blacklisted `.rcParams` (defined in
    ``matplotlib.style.core.STYLE_BLACKLIST``) are not updated.

    See Also
    --------
    matplotlib.rc_file_defaults
........................ rcsetup .......................
Help on module matplotlib.rcsetup in matplotlib:

NAME
    matplotlib.rcsetup

DESCRIPTION
    The rcsetup module contains the validation code for customization using
    Matplotlib's rc settings.

    Each rc setting is assigned a function used to validate any attempted changes
    to that setting.  The validation functions are defined in the rcsetup module,
........................ requested_backend .......................
Help on NoneType object:

class NoneType(object)
 |  The type of the None singleton.
 |
 |  Methods defined here:
 |
 |  __bool__(self, /)
 |      True if self else False
 |
 |  __eq__(self, value, /)
........................ rgrids .......................
Help on function rgrids in module matplotlib.pyplot:

rgrids(
    radii: 'ArrayLike | None' = None,
    labels: 'Sequence[str | Text] | None' = None,
    angle: 'float | None' = None,
    fmt: 'str | None' = None,
    **kwargs
) -> 'tuple[list[Line2D], list[Text]]'
    Get or set the radial gridlines on the current polar plot.

........................ savefig .......................
Help on function savefig in module matplotlib.pyplot:

savefig(*args, **kwargs) -> 'None'
    Save the current figure as an image or vector graphic to a file.

    Call signature::

      savefig(fname, *, transparent=None, dpi='figure', format=None,
              metadata=None, bbox_inches=None, pad_inches=0.1,
              facecolor='auto', edgecolor='auto', backend=None,
              **kwargs
........................ sca .......................
Help on function sca in module matplotlib.pyplot:

sca(ax: 'Axes') -> 'None'
    Set the current Axes to *ax* and the current Figure to the parent of *ax*.

........................ scatter .......................
Help on function scatter in module matplotlib.pyplot:

scatter(
    x: 'float | ArrayLike',
    y: 'float | ArrayLike',
........................ sci .......................
Help on function sci in module matplotlib.pyplot:

sci(im: 'ColorizingArtist') -> 'None'
    Set the current image.

    This image will be the target of colormap functions like
    ``pyplot.viridis``, and other functions such as `~.pyplot.clim`.  The
    current image is an attribute of the current Axes.

........................ semilogx .......................
Help on function semilogx in module matplotlib.pyplot:
........................ semilogy .......................
Help on function semilogy in module matplotlib.pyplot:

semilogy(*args, **kwargs) -> 'list[Line2D]'
    Make a plot with log scaling on the y-axis.

    Call signatures::

        semilogy([x], y, [fmt], data=None, **kwargs)
        semilogy([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)

    This is just a thin wrapper around `.plot` which additionally changes
........................ set_cmap .......................
Help on function set_cmap in module matplotlib.pyplot:

set_cmap(cmap: 'Colormap | str') -> 'None'
    Set the default colormap, and applies it to the current image if any.

    Parameters
    ----------
    cmap : `~matplotlib.colors.Colormap` or str
        A colormap instance or the name of a registered colormap.

    See Also
........................ set_loglevel .......................
Help on function set_loglevel in module matplotlib.pyplot:

set_loglevel(*args, **kwargs) -> 'None'
    Configure Matplotlib's logging levels.

    Matplotlib uses the standard library `logging` framework under the root
    logger 'matplotlib'.  This is a helper function to:

    - set Matplotlib's root logger level
    - set the root logger handler's level, creating the handler
      if it does not exist yet
........................ setp .......................
Help on function setp in module matplotlib.pyplot:

setp(obj, *args, **kwargs)
    Set one or more properties on an `.Artist`, or list allowed values.

    Parameters
    ----------
    obj : `~matplotlib.artist.Artist` or list of `.Artist`
        The artist(s) whose properties are being set or queried.  When setting
        properties, all artists are affected; when querying the allowed values,
        only the first instance in the sequence is queried.
........................ show .......................
Help on function show in module matplotlib.pyplot:

show(*, block=None)
    Display all open figures.

    Parameters
    ----------
    block : bool, optional
        Whether to wait for all figures to be closed before returning.

        If `True` block and run the GUI main loop until all figure windows
........................ specgram .......................
Help on function specgram in module matplotlib.pyplot:

specgram(
    x: 'ArrayLike',
    *,
    NFFT: 'int | None' = None,
    Fs: 'float | None' = None,
    Fc: 'int | None' = None,
    detrend: "Literal['none', 'mean', 'linear'] | Callable[[ArrayLike], ArrayLike] | None" = None,
    window: 'Callable[[ArrayLike], ArrayLike] | ArrayLike | None' = None,
    noverlap: 'int | None' = None,
........................ spring .......................
Help on function spring in module matplotlib.pyplot:

spring() -> 'None'
    Set the colormap to 'spring'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.

........................ spy .......................
Help on function spy in module matplotlib.pyplot:

........................ stackplot .......................
Help on function stackplot in module matplotlib.pyplot:

stackplot(
    x,
    *args,
    labels=(),
    colors=None,
    hatch=None,
    baseline='zero',
    data=None,
    **kwargs
........................ stairs .......................
Help on function stairs in module matplotlib.pyplot:

stairs(
    values: 'ArrayLike',
    edges: 'ArrayLike | None' = None,
    *,
    orientation: "Literal['vertical', 'horizontal']" = 'vertical',
    baseline: 'float | ArrayLike | None' = 0,
    fill: 'bool' = False,
    data=None,
    **kwargs
........................ stem .......................
Help on function stem in module matplotlib.pyplot:

stem(
    *args: 'ArrayLike | str',
    linefmt: 'str | None' = None,
    markerfmt: 'str | None' = None,
    basefmt: 'str | None' = None,
    bottom: 'float' = 0,
    label: 'str | None' = None,
    orientation: "Literal['vertical', 'horizontal']" = 'vertical',
    data=None
........................ step .......................
Help on function step in module matplotlib.pyplot:

step(
    x: 'ArrayLike',
    y: 'ArrayLike',
    *args,
    where: "Literal['pre', 'post', 'mid']" = 'pre',
    data=None,
    **kwargs
) -> 'list[Line2D]'
    Make a step plot.
........................ streamplot .......................
Help on function streamplot in module matplotlib.pyplot:

streamplot(
    x,
    y,
    u,
    v,
    density=1,
    linewidth=None,
    color=None,
    cmap=None,
........................ style .......................
Help on package matplotlib.style in matplotlib:

NAME
    matplotlib.style

PACKAGE CONTENTS
    core

FUNCTIONS
    context(style, after_reset=False)
        Context manager for using style settings temporarily.
........................ subplot .......................
Help on function subplot in module matplotlib.pyplot:

subplot(*args, **kwargs) -> 'Axes'
    Add an Axes to the current figure or retrieve an existing Axes.

    This is a wrapper of `.Figure.add_subplot` which provides additional
    behavior when working with the implicit API (see the notes section).

    Call signatures::

       subplot(nrows, ncols, index, **kwargs)
........................ subplot2grid .......................
Help on function subplot2grid in module matplotlib.pyplot:

subplot2grid(
    shape: 'tuple[int, int]',
    loc: 'tuple[int, int]',
    rowspan: 'int' = 1,
    colspan: 'int' = 1,
    fig: 'Figure | None' = None,
    **kwargs
) -> 'matplotlib.axes.Axes'
    Create a subplot at a specific location inside a regular grid.
........................ subplot_mosaic .......................
Help on function subplot_mosaic in module matplotlib.pyplot:

subplot_mosaic(
    mosaic: 'str | list[HashableList[_T]] | list[HashableList[Hashable]]',
    *,
    sharex: 'bool' = False,
    sharey: 'bool' = False,
    width_ratios: 'ArrayLike | None' = None,
    height_ratios: 'ArrayLike | None' = None,
    empty_sentinel: 'Any' = '.',
    subplot_kw: 'dict[str, Any] | None' = None,
........................ subplot_tool .......................
Help on function subplot_tool in module matplotlib.pyplot:

subplot_tool(targetfig: 'Figure | None' = None) -> 'SubplotTool | None'
    Launch a subplot tool window for a figure.

    Returns
    -------
    `matplotlib.widgets.SubplotTool`

........................ subplots .......................
Help on function subplots in module matplotlib.pyplot:
........................ subplots_adjust .......................
Help on function subplots_adjust in module matplotlib.pyplot:

subplots_adjust(
    left: 'float | None' = None,
    bottom: 'float | None' = None,
    right: 'float | None' = None,
    top: 'float | None' = None,
    wspace: 'float | None' = None,
    hspace: 'float | None' = None
) -> 'None'
    Adjust the subplot layout parameters.
........................ summer .......................
Help on function summer in module matplotlib.pyplot:

summer() -> 'None'
    Set the colormap to 'summer'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.

........................ suptitle .......................
Help on function suptitle in module matplotlib.pyplot:

........................ switch_backend .......................
Help on function switch_backend in module matplotlib.pyplot:

switch_backend(newbackend: 'str') -> 'None'
    Set the pyplot backend.

    Switching to an interactive backend is possible only if no event loop for
    another interactive backend has started.  Switching to and from
    non-interactive backends is always possible.

    If the new backend is different than the current backend then all open
    Figures will be closed via ``plt.close('all')``.
........................ sys .......................
Help on built-in module sys:

NAME
    sys

MODULE REFERENCE
    https://docs.python.org/3.13/library/sys.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
........................ table .......................
Help on function table in module matplotlib.pyplot:

table(
    cellText=None,
    cellColours=None,
    cellLoc='right',
    colWidths=None,
    rowLabels=None,
    rowColours=None,
    rowLoc='left',
    colLabels=None,
........................ text .......................
Help on function text in module matplotlib.pyplot:

text(
    x: 'float',
    y: 'float',
    s: 'str',
    fontdict: 'dict[str, Any] | None' = None,
    **kwargs
) -> 'Text'
    Add text to the Axes.

........................ thetagrids .......................
Help on function thetagrids in module matplotlib.pyplot:

thetagrids(
    angles: 'ArrayLike | None' = None,
    labels: 'Sequence[str | Text] | None' = None,
    fmt: 'str | None' = None,
    **kwargs
) -> 'tuple[list[Line2D], list[Text]]'
    Get or set the theta gridlines on the current polar plot.

    Call signatures::
........................ threading .......................
Help on module threading:

NAME
    threading - Thread module emulating a subset of Java's threading model.

MODULE REFERENCE
    https://docs.python.org/3.13/library/threading.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
........................ tick_params .......................
Help on function tick_params in module matplotlib.pyplot:

tick_params(axis: "Literal['both', 'x', 'y']" = 'both', **kwargs) -> 'None'
    Change the appearance of ticks, tick labels, and gridlines.

    Tick properties that are not explicitly set using the keyword
    arguments remain unchanged unless *reset* is True. For the current
    style settings, see `.Axis.get_tick_params`.

    Parameters
    ----------
........................ ticklabel_format .......................
Help on function ticklabel_format in module matplotlib.pyplot:

ticklabel_format(
    *,
    axis: "Literal['both', 'x', 'y']" = 'both',
    style: "Literal['', 'sci', 'scientific', 'plain'] | None" = None,
    scilimits: 'tuple[int, int] | None' = None,
    useOffset: 'bool | float | None' = None,
    useLocale: 'bool | None' = None,
    useMathText: 'bool | None' = None
) -> 'None'
........................ tight_layout .......................
Help on function tight_layout in module matplotlib.pyplot:

tight_layout(
    *,
    pad: 'float' = 1.08,
    h_pad: 'float | None' = None,
    w_pad: 'float | None' = None,
    rect: 'tuple[float, float, float, float] | None' = None
) -> 'None'
    Adjust the padding between and around subplots.

........................ time .......................
Help on built-in module time:

NAME
    time - This module provides various functions to manipulate time values.

DESCRIPTION
    There are two standard representations of time.  One is the number
    of seconds since the Epoch, in UTC (a.k.a. GMT).  It may be an integer
    or a floating-point number (to represent fractions of seconds).
    The epoch is the point where the time starts, the return value of time.gmtime(0).
    It is January 1, 1970, 00:00:00 (UTC) on all platforms.
........................ title .......................
Help on function title in module matplotlib.pyplot:

title(
    label: 'str',
    fontdict: 'dict[str, Any] | None' = None,
    loc: "Literal['left', 'center', 'right'] | None" = None,
    pad: 'float | None' = None,
    *,
    y: 'float | None' = None,
    **kwargs
) -> 'Text'
........................ tricontour .......................
Help on function tricontour in module matplotlib.pyplot:

tricontour(*args, **kwargs)
    Draw contour lines on an unstructured triangular grid.

    Call signatures::

        tricontour(triangulation, z, [levels], ...)
        tricontour(x, y, z, [levels], *, [triangles=triangles], [mask=mask], ...)

    The triangular grid can be specified either by passing a `.Triangulation`
........................ tricontourf .......................
Help on function tricontourf in module matplotlib.pyplot:

tricontourf(*args, **kwargs)
    Draw contour regions on an unstructured triangular grid.

    Call signatures::

        tricontourf(triangulation, z, [levels], ...)
        tricontourf(x, y, z, [levels], *, [triangles=triangles], [mask=mask], ...)

    The triangular grid can be specified either by passing a `.Triangulation`
........................ tripcolor .......................
Help on function tripcolor in module matplotlib.pyplot:

tripcolor(
    *args,
    alpha=1.0,
    norm=None,
    cmap=None,
    vmin=None,
    vmax=None,
    shading='flat',
    facecolors=None,
........................ triplot .......................
Help on function triplot in module matplotlib.pyplot:

triplot(*args, **kwargs)
    Draw an unstructured triangular grid as lines and/or markers.

    Call signatures::

      triplot(triangulation, ...)
      triplot(x, y, [triangles], *, [mask=mask], ...)

    The triangular grid can be specified either by passing a `.Triangulation`
........................ twinx .......................
Help on function twinx in module matplotlib.pyplot:

twinx(ax: 'matplotlib.axes.Axes | None' = None) -> '_AxesBase'
    Make and return a second Axes that shares the *x*-axis.  The new Axes will
    overlay *ax* (or the current Axes if *ax* is *None*), and its ticks will be
    on the right.

    Examples
    --------
    :doc:`/gallery/subplots_axes_and_figures/two_scales`

........................ twiny .......................
Help on function twiny in module matplotlib.pyplot:

twiny(ax: 'matplotlib.axes.Axes | None' = None) -> '_AxesBase'
    Make and return a second Axes that shares the *y*-axis.  The new Axes will
    overlay *ax* (or the current Axes if *ax* is *None*), and its ticks will be
    on the top.

    Examples
    --------
    :doc:`/gallery/subplots_axes_and_figures/two_scales`

........................ uninstall_repl_displayhook .......................
Help on function uninstall_repl_displayhook in module matplotlib.pyplot:

uninstall_repl_displayhook() -> 'None'
    Disconnect from the display hook of the current shell.

........................ violinplot .......................
Help on function violinplot in module matplotlib.pyplot:

violinplot(
    dataset: 'ArrayLike | Sequence[ArrayLike]',
    positions: 'ArrayLike | None' = None,
........................ viridis .......................
Help on function viridis in module matplotlib.pyplot:

viridis() -> 'None'
    Set the colormap to 'viridis'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.

........................ vlines .......................
Help on function vlines in module matplotlib.pyplot:

........................ waitforbuttonpress .......................
Help on function waitforbuttonpress in module matplotlib.pyplot:

waitforbuttonpress(timeout: 'float' = -1) -> 'None | bool'
    Blocking call to interact with the figure.

    Wait for user input and return True if a key was pressed, False if a
    mouse button was pressed and None if no input was given within
    *timeout* seconds.  Negative values deactivate *timeout*.

    Notes
    -----
........................ winter .......................
Help on function winter in module matplotlib.pyplot:

winter() -> 'None'
    Set the colormap to 'winter'.

    This changes the default colormap as well as the colormap of the current
    image if there is one. See ``help(colormaps)`` for more information.

........................ xcorr .......................
Help on function xcorr in module matplotlib.pyplot:

........................ xkcd .......................
Help on function xkcd in module matplotlib.pyplot:

xkcd(scale: 'float' = 1, length: 'float' = 100, randomness: 'float' = 2) -> 'ExitStack'
    Turn on `xkcd <https://xkcd.com/>`_ sketch-style drawing mode.

    This will only have an effect on things drawn after this function is called.

    For best results, install the `xkcd script <https://github.com/ipython/xkcd-font/>`_
    font; xkcd fonts are not packaged with Matplotlib.

    Parameters
........................ xlabel .......................
Help on function xlabel in module matplotlib.pyplot:

xlabel(
    xlabel: 'str',
    fontdict: 'dict[str, Any] | None' = None,
    labelpad: 'float | None' = None,
    *,
    loc: "Literal['left', 'center', 'right'] | None" = None,
    **kwargs
) -> 'Text'
    Set the label for the x-axis.
........................ xlim .......................
Help on function xlim in module matplotlib.pyplot:

xlim(*args, **kwargs) -> 'tuple[float, float]'
    Get or set the x limits of the current Axes.

    Call signatures::

        left, right = xlim()  # return the current xlim
        xlim((left, right))   # set the xlim to left, right
        xlim(left, right)     # set the xlim to left, right

........................ xscale .......................
Help on function xscale in module matplotlib.pyplot:

xscale(value: 'str | ScaleBase', **kwargs) -> 'None'
    Set the xaxis' scale.

    Parameters
    ----------
    value : str or `.ScaleBase`
        The axis scale type to apply.  Valid string values are the names of scale
        classes ("linear", "log", "function",...).  These may be the names of any
        of the :ref:`built-in scales<builtin_scales>` or of any custom scales
........................ xticks .......................
Help on function xticks in module matplotlib.pyplot:

xticks(
    ticks: 'ArrayLike | None' = None,
    labels: 'Sequence[str] | None' = None,
    *,
    minor: 'bool' = False,
    **kwargs
) -> 'tuple[list[Tick] | np.ndarray, list[Text]]'
    Get or set the current tick locations and labels of the x-axis.

........................ ylabel .......................
Help on function ylabel in module matplotlib.pyplot:

ylabel(
    ylabel: 'str',
    fontdict: 'dict[str, Any] | None' = None,
    labelpad: 'float | None' = None,
    *,
    loc: "Literal['bottom', 'center', 'top'] | None" = None,
    **kwargs
) -> 'Text'
    Set the label for the y-axis.
........................ ylim .......................
Help on function ylim in module matplotlib.pyplot:

ylim(*args, **kwargs) -> 'tuple[float, float]'
    Get or set the y-limits of the current Axes.

    Call signatures::

        bottom, top = ylim()  # return the current ylim
        ylim((bottom, top))   # set the ylim to bottom, top
        ylim(bottom, top)     # set the ylim to bottom, top

........................ yscale .......................
Help on function yscale in module matplotlib.pyplot:

yscale(value: 'str | ScaleBase', **kwargs) -> 'None'
    Set the yaxis' scale.

    Parameters
    ----------
    value : str or `.ScaleBase`
        The axis scale type to apply.  Valid string values are the names of scale
        classes ("linear", "log", "function",...).  These may be the names of any
        of the :ref:`built-in scales<builtin_scales>` or of any custom scales
........................ yticks .......................
Help on function yticks in module matplotlib.pyplot:

yticks(
    ticks: 'ArrayLike | None' = None,
    labels: 'Sequence[str] | None' = None,
    *,
    minor: 'bool' = False,
    **kwargs
) -> 'tuple[list[Tick] | np.ndarray, list[Text]]'
    Get or set the current tick locations and labels of the y-axis.

