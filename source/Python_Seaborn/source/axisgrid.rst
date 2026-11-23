Help on module seaborn.axisgrid in seaborn:

NAME
    seaborn.axisgrid

CLASSES
    Grid(_BaseGrid)
        FacetGrid
        PairGrid
    _BaseGrid(builtins.object)
        JointGrid

    class FacetGrid(Grid)
     |  FacetGrid(data, *, row=None, col=None, hue=None, col_wrap=None, sharex=True, sharey=True, height=3, aspect=1, palette=None, row_order=None, col_order=None, hue_order=None, hue_kws=None, dropna=False, legend_out=True, despine=True, margin_titles=False, xlim=None, ylim=None, subplot_kws=None, gridspec_kws=None)
     |
     |  Multi-plot grid for plotting conditional relationships.
     |
     |  Method resolution order:
     |      FacetGrid
     |      Grid
     |      _BaseGrid
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, data, *, row=None, col=None, hue=None, col_wrap=None, sharex=True, sharey=True, height=3, aspect=1, palette=None, row_order=None, col_order=None, hue_order=None, hue_kws=None, dropna=False, legend_out=True, despine=True, margin_titles=False, xlim=None, ylim=None, subplot_kws=None, gridspec_kws=None)
     |      Initialize the matplotlib figure and FacetGrid object.
     |
     |      This class maps a dataset onto multiple axes arrayed in a grid of rows
     |      and columns that correspond to *levels* of variables in the dataset.
     |      The plots it produces are often called "lattice", "trellis", or
     |      "small-multiple" graphics.
     |
     |      It can also represent levels of a third variable with the ``hue``
     |      parameter, which plots different subsets of data in different colors.
     |      This uses color to resolve elements on a third dimension, but only
     |      draws subsets on top of each other and will not tailor the ``hue``
     |      parameter for the specific visualization the way that axes-level
     |      functions that accept ``hue`` will.
     |
     |      The basic workflow is to initialize the :class:`FacetGrid` object with
     |      the dataset and the variables that are used to structure the grid. Then
     |      one or more plotting functions can be applied to each subset by calling
     |      :meth:`FacetGrid.map` or :meth:`FacetGrid.map_dataframe`. Finally, the
     |      plot can be tweaked with other methods to do things like change the
     |      axis labels, use different ticks, or add a legend. See the detailed
     |      code examples below for more information.
     |
     |      .. warning::
     |
     |          When using seaborn functions that infer semantic mappings from a
     |          dataset, care must be taken to synchronize those mappings across
     |          facets (e.g., by defining the ``hue`` mapping with a palette dict or
     |          setting the data type of the variables to ``category``). In most cases,
     |          it will be better to use a figure-level function (e.g. :func:`relplot`
     |          or :func:`catplot`) than to use :class:`FacetGrid` directly.
     |
     |      See the :ref:`tutorial <grid_tutorial>` for more information.
     |
     |      Parameters
     |      ----------
     |      data : DataFrame
     |          Tidy ("long-form") dataframe where each column is a variable and each
     |          row is an observation.
     |      row, col, hue : strings
     |          Variables that define subsets of the data, which will be drawn on
     |          separate facets in the grid. See the ``{var}_order`` parameters to
     |          control the order of levels of this variable.
     |      col_wrap : int
     |          "Wrap" the column variable at this width, so that the column facets
     |          span multiple rows. Incompatible with a ``row`` facet.
     |      share{x,y} : bool, 'col', or 'row' optional
     |          If true, the facets will share y axes across columns and/or x axes
     |          across rows.
     |      height : scalar
     |          Height (in inches) of each facet. See also: ``aspect``.
     |      aspect : scalar
     |          Aspect ratio of each facet, so that ``aspect * height`` gives the width
     |          of each facet in inches.
     |      palette : palette name, list, or dict
     |          Colors to use for the different levels of the ``hue`` variable. Should
     |          be something that can be interpreted by :func:`color_palette`, or a
     |          dictionary mapping hue levels to matplotlib colors.
     |      {row,col,hue}_order : lists
     |          Order for the levels of the faceting variables. By default, this
     |          will be the order that the levels appear in ``data`` or, if the
     |          variables are pandas categoricals, the category order.
     |      hue_kws : dictionary of param -> list of values mapping
     |          Other keyword arguments to insert into the plotting call to let
     |          other plot attributes vary across levels of the hue variable (e.g.
     |          the markers in a scatterplot).
     |      legend_out : bool
     |          If ``True``, the figure size will be extended, and the legend will be
     |          drawn outside the plot on the center right.
     |      despine : boolean
     |          Remove the top and right spines from the plots.
     |      margin_titles : bool
     |          If ``True``, the titles for the row variable are drawn to the right of
     |          the last column. This option is experimental and may not work in all
     |          cases.
     |      {x, y}lim: tuples
     |          Limits for each of the axes on each facet (only relevant when
     |          share{x, y} is True).
     |      subplot_kws : dict
     |          Dictionary of keyword arguments passed to matplotlib subplot(s)
     |          methods.
     |      gridspec_kws : dict
     |          Dictionary of keyword arguments passed to
     |          :class:`matplotlib.gridspec.GridSpec`
     |          (via :meth:`matplotlib.figure.Figure.subplots`).
     |          Ignored if ``col_wrap`` is not ``None``.
     |
     |      See Also
     |      --------
     |      PairGrid : Subplot grid for plotting pairwise relationships
     |      relplot : Combine a relational plot and a :class:`FacetGrid`
     |      displot : Combine a distribution plot and a :class:`FacetGrid`
     |      catplot : Combine a categorical plot and a :class:`FacetGrid`
     |      lmplot : Combine a regression plot and a :class:`FacetGrid`
     |
     |      Examples
     |      --------
     |
     |      .. note::
     |
     |          These examples use seaborn functions to demonstrate some of the
     |          advanced features of the class, but in most cases you will want
     |          to use figue-level functions (e.g. :func:`displot`, :func:`relplot`)
     |          to make the plots shown here.
     |
     |      .. include:: ../docstrings/FacetGrid.rst
     |
     |  despine(self, **kwargs)
     |      Remove axis spines from the facets.
     |
     |  facet_axis(self, row_i, col_j, modify_state=True)
     |      Make the axis identified by these indices active and return it.
     |
     |  facet_data(self)
     |      Generator for name indices and data subsets for each facet.
     |
     |      Yields
     |      ------
     |      (i, j, k), data_ijk : tuple of ints, DataFrame
     |          The ints provide an index into the {row, col, hue}_names attribute,
     |          and the dataframe contains a subset of the full data corresponding
     |          to each facet. The generator yields subsets that correspond with
     |          the self.axes.flat iterator, or self.axes[i, j] when `col_wrap`
     |          is None.
     |
     |  map(self, func, *args, **kwargs)
     |      Apply a plotting function to each facet's subset of the data.
     |
     |      Parameters
     |      ----------
     |      func : callable
     |          A plotting function that takes data and keyword arguments. It
     |          must plot to the currently active matplotlib Axes and take a
     |          `color` keyword argument. If faceting on the `hue` dimension,
     |          it must also take a `label` keyword argument.
     |      args : strings
     |          Column names in self.data that identify variables with data to
     |          plot. The data for each variable is passed to `func` in the
     |          order the variables are specified in the call.
     |      kwargs : keyword arguments
     |          All keyword arguments are passed to the plotting function.
     |
     |      Returns
     |      -------
     |      self : object
     |          Returns self.
     |
     |  map_dataframe(self, func, *args, **kwargs)
     |      Like ``.map`` but passes args as strings and inserts data in kwargs.
     |
     |      This method is suitable for plotting with functions that accept a
     |      long-form DataFrame as a `data` keyword argument and access the
     |      data in that DataFrame using string variable names.
     |
     |      Parameters
     |      ----------
     |      func : callable
     |          A plotting function that takes data and keyword arguments. Unlike
     |          the `map` method, a function used here must "understand" Pandas
     |          objects. It also must plot to the currently active matplotlib Axes
     |          and take a `color` keyword argument. If faceting on the `hue`
     |          dimension, it must also take a `label` keyword argument.
     |      args : strings
     |          Column names in self.data that identify variables with data to
     |          plot. The data for each variable is passed to `func` in the
     |          order the variables are specified in the call.
     |      kwargs : keyword arguments
     |          All keyword arguments are passed to the plotting function.
     |
     |      Returns
     |      -------
     |      self : object
     |          Returns self.
     |
     |  refline(self, *, x=None, y=None, color='.5', linestyle='--', **line_kws)
     |      Add a reference line(s) to each facet.
     |
     |      Parameters
     |      ----------
     |      x, y : numeric
     |          Value(s) to draw the line(s) at.
     |      color : :mod:`matplotlib color <matplotlib.colors>`
     |          Specifies the color of the reference line(s). Pass ``color=None`` to
     |          use ``hue`` mapping.
     |      linestyle : str
     |          Specifies the style of the reference line(s).
     |      line_kws : key, value mappings
     |          Other keyword arguments are passed to :meth:`matplotlib.axes.Axes.axvline`
     |          when ``x`` is not None and :meth:`matplotlib.axes.Axes.axhline` when ``y``
     |          is not None.
     |
     |      Returns
     |      -------
     |      :class:`FacetGrid` instance
     |          Returns ``self`` for easy method chaining.
     |
     |  set_axis_labels(self, x_var=None, y_var=None, clear_inner=True, **kwargs)
     |      Set axis labels on the left column and bottom row of the grid.
     |
     |  set_titles(self, template=None, row_template=None, col_template=None, **kwargs)
     |      Draw titles either above each facet or on the grid margins.
     |
     |      Parameters
     |      ----------
     |      template : string
     |          Template for all titles with the formatting keys {col_var} and
     |          {col_name} (if using a `col` faceting variable) and/or {row_var}
     |          and {row_name} (if using a `row` faceting variable).
     |      row_template:
     |          Template for the row variable when titles are drawn on the grid
     |          margins. Must have {row_var} and {row_name} formatting keys.
     |      col_template:
     |          Template for the column variable when titles are drawn on the grid
     |          margins. Must have {col_var} and {col_name} formatting keys.
     |
     |      Returns
     |      -------
     |      self: object
     |          Returns self.
     |
     |  set_xlabels(self, label=None, clear_inner=True, **kwargs)
     |      Label the x axis on the bottom row of the grid.
     |
     |  set_xticklabels(self, labels=None, step=None, **kwargs)
     |      Set x axis tick labels of the grid.
     |
     |  set_ylabels(self, label=None, clear_inner=True, **kwargs)
     |      Label the y axis on the left column of the grid.
     |
     |  set_yticklabels(self, labels=None, **kwargs)
     |      Set y axis tick labels on the left column of the grid.
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  ax
     |      The :class:`matplotlib.axes.Axes` when no faceting variables are assigned.
     |
     |  axes
     |      An array of the :class:`matplotlib.axes.Axes` objects in the grid.
     |
     |  axes_dict
     |      A mapping of facet names to corresponding :class:`matplotlib.axes.Axes`.
     |
     |      If only one of ``row`` or ``col`` is assigned, each key is a string
     |      representing a level of that variable. If both facet dimensions are
     |      assigned, each key is a ``({row_level}, {col_level})`` tuple.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from Grid:
     |
     |  add_legend(self, legend_data=None, title=None, label_order=None, adjust_subtitles=False, **kwargs)
     |      Draw a legend, maybe placing it outside axes and resizing the figure.
     |
     |      Parameters
     |      ----------
     |      legend_data : dict
     |          Dictionary mapping label names (or two-element tuples where the
     |          second element is a label name) to matplotlib artist handles. The
     |          default reads from ``self._legend_data``.
     |      title : string
     |          Title for the legend. The default reads from ``self._hue_var``.
     |      label_order : list of labels
     |          The order that the legend entries should appear in. The default
     |          reads from ``self.hue_names``.
     |      adjust_subtitles : bool
     |          If True, modify entries with invisible artists to left-align
     |          the labels and set the font size to that of a title.
     |      kwargs : key, value pairings
     |          Other keyword arguments are passed to the underlying legend methods
     |          on the Figure or Axes object.
     |
     |      Returns
     |      -------
     |      self : Grid instance
     |          Returns self for easy chaining.
     |
     |  tick_params(self, axis='both', **kwargs)
     |      Modify the ticks, tick labels, and gridlines.
     |
     |      Parameters
     |      ----------
     |      axis : {'x', 'y', 'both'}
     |          The axis on which to apply the formatting.
     |      kwargs : keyword arguments
     |          Additional keyword arguments to pass to
     |          :meth:`matplotlib.axes.Axes.tick_params`.
     |
     |      Returns
     |      -------
     |      self : Grid instance
     |          Returns self for easy chaining.
     |
     |  tight_layout(self, *args, **kwargs)
     |      Call fig.tight_layout within rect that exclude the legend.
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties inherited from Grid:
     |
     |  legend
     |      The :class:`matplotlib.legend.Legend` object, if present.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from _BaseGrid:
     |
     |  apply(self, func, *args, **kwargs)
     |      Pass the grid to a user-supplied function and return self.
     |
     |      The `func` must accept an object of this type for its first
     |      positional argument. Additional arguments are passed through.
     |      The return value of `func` is ignored; this method returns self.
     |      See the `pipe` method if you want the return value.
     |
     |      Added in v0.12.0.
     |
     |  pipe(self, func, *args, **kwargs)
     |      Pass the grid to a user-supplied function and return its value.
     |
     |      The `func` must accept an object of this type for its first
     |      positional argument. Additional arguments are passed through.
     |      The return value of `func` becomes the return value of this method.
     |      See the `apply` method if you want to return self instead.
     |
     |      Added in v0.12.0.
     |
     |  savefig(self, *args, **kwargs)
     |      Save an image of the plot.
     |
     |      This wraps :meth:`matplotlib.figure.Figure.savefig`, using bbox_inches="tight"
     |      by default. Parameters are passed through to the matplotlib function.
     |
     |  set(self, **kwargs)
     |      Set attributes on each subplot Axes.
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties inherited from _BaseGrid:
     |
     |  fig
     |      DEPRECATED: prefer the `figure` property.
     |
     |  figure
     |      Access the :class:`matplotlib.figure.Figure` object underlying the grid.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _BaseGrid:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class JointGrid(_BaseGrid)
     |  JointGrid(data=None, *, x=None, y=None, hue=None, height=6, ratio=5, space=0.2, palette=None, hue_order=None, hue_norm=None, dropna=False, xlim=None, ylim=None, marginal_ticks=False)
     |
     |  Grid for drawing a bivariate plot with marginal univariate plots.
     |
     |  Many plots can be drawn by using the figure-level interface :func:`jointplot`.
     |  Use this class directly when you need more flexibility.
     |
     |  Method resolution order:
     |      JointGrid
     |      _BaseGrid
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, data=None, *, x=None, y=None, hue=None, height=6, ratio=5, space=0.2, palette=None, hue_order=None, hue_norm=None, dropna=False, xlim=None, ylim=None, marginal_ticks=False)
     |      Set up the grid of subplots and store data internally for easy plotting.
     |
     |      Parameters
     |      ----------
     |      data : :class:`pandas.DataFrame`, :class:`numpy.ndarray`, mapping, or sequence
     |          Input data structure. Either a long-form collection of vectors that can be
     |          assigned to named variables or a wide-form dataset that will be internally
     |          reshaped.
     |      x, y : vectors or keys in ``data``
     |          Variables that specify positions on the x and y axes.
     |      height : number
     |          Size of each side of the figure in inches (it will be square).
     |      ratio : number
     |          Ratio of joint axes height to marginal axes height.
     |      space : number
     |          Space between the joint and marginal axes
     |      dropna : bool
     |          If True, remove missing observations before plotting.
     |      {x, y}lim : pairs of numbers
     |          Set axis limits to these values before plotting.
     |      marginal_ticks : bool
     |          If False, suppress ticks on the count/density axis of the marginal plots.
     |      hue : vector or key in ``data``
     |          Semantic variable that is mapped to determine the color of plot elements.
     |          Note: unlike in :class:`FacetGrid` or :class:`PairGrid`, the axes-level
     |          functions must support ``hue`` to use it in :class:`JointGrid`.
     |      palette : string, list, dict, or :class:`matplotlib.colors.Colormap`
     |          Method for choosing the colors to use when mapping the ``hue`` semantic.
     |          String values are passed to :func:`color_palette`. List or dict values
     |          imply categorical mapping, while a colormap object implies numeric mapping.
     |      hue_order : vector of strings
     |          Specify the order of processing and plotting for categorical levels of the
     |          ``hue`` semantic.
     |      hue_norm : tuple or :class:`matplotlib.colors.Normalize`
     |          Either a pair of values that set the normalization range in data units
     |          or an object that will map from data units into a [0, 1] interval. Usage
     |          implies numeric mapping.
     |
     |      See Also
     |      --------
     |      jointplot : Draw a bivariate plot with univariate marginal distributions.
     |      PairGrid : Set up a figure with joint and marginal views on multiple variables.
     |      jointplot : Draw multiple bivariate plots with univariate marginal distributions.
     |
     |      Examples
     |      --------
     |
     |      .. include:: ../docstrings/JointGrid.rst
     |
     |  plot(self, joint_func, marginal_func, **kwargs)
     |      Draw the plot by passing functions for joint and marginal axes.
     |
     |      This method passes the ``kwargs`` dictionary to both functions. If you
     |      need more control, call :meth:`JointGrid.plot_joint` and
     |      :meth:`JointGrid.plot_marginals` directly with specific parameters.
     |
     |      Parameters
     |      ----------
     |      joint_func, marginal_func : callables
     |          Functions to draw the bivariate and univariate plots. See methods
     |          referenced above for information about the required characteristics
     |          of these functions.
     |      kwargs
     |          Additional keyword arguments are passed to both functions.
     |
     |      Returns
     |      -------
     |      :class:`JointGrid` instance
     |          Returns ``self`` for easy method chaining.
     |
     |  plot_joint(self, func, **kwargs)
     |      Draw a bivariate plot on the joint axes of the grid.
     |
     |      Parameters
     |      ----------
     |      func : plotting callable
     |          If a seaborn function, it should accept ``x`` and ``y``. Otherwise,
     |          it must accept ``x`` and ``y`` vectors of data as the first two
     |          positional arguments, and it must plot on the "current" axes.
     |          If ``hue`` was defined in the class constructor, the function must
     |          accept ``hue`` as a parameter.
     |      kwargs
     |          Keyword argument are passed to the plotting function.
     |
     |      Returns
     |      -------
     |      :class:`JointGrid` instance
     |          Returns ``self`` for easy method chaining.
     |
     |  plot_marginals(self, func, **kwargs)
     |      Draw univariate plots on each marginal axes.
     |
     |      Parameters
     |      ----------
     |      func : plotting callable
     |          If a seaborn function, it should  accept ``x`` and ``y`` and plot
     |          when only one of them is defined. Otherwise, it must accept a vector
     |          of data as the first positional argument and determine its orientation
     |          using the ``vertical`` parameter, and it must plot on the "current" axes.
     |          If ``hue`` was defined in the class constructor, it must accept ``hue``
     |          as a parameter.
     |      kwargs
     |          Keyword argument are passed to the plotting function.
     |
     |      Returns
     |      -------
     |      :class:`JointGrid` instance
     |          Returns ``self`` for easy method chaining.
     |
     |  refline(self, *, x=None, y=None, joint=True, marginal=True, color='.5', linestyle='--', **line_kws)
     |      Add a reference line(s) to joint and/or marginal axes.
     |
     |      Parameters
     |      ----------
     |      x, y : numeric
     |          Value(s) to draw the line(s) at.
     |      joint, marginal : bools
     |          Whether to add the reference line(s) to the joint/marginal axes.
     |      color : :mod:`matplotlib color <matplotlib.colors>`
     |          Specifies the color of the reference line(s).
     |      linestyle : str
     |          Specifies the style of the reference line(s).
     |      line_kws : key, value mappings
     |          Other keyword arguments are passed to :meth:`matplotlib.axes.Axes.axvline`
     |          when ``x`` is not None and :meth:`matplotlib.axes.Axes.axhline` when ``y``
     |          is not None.
     |
     |      Returns
     |      -------
     |      :class:`JointGrid` instance
     |          Returns ``self`` for easy method chaining.
     |
     |  set_axis_labels(self, xlabel='', ylabel='', **kwargs)
     |      Set axis labels on the bivariate axes.
     |
     |      Parameters
     |      ----------
     |      xlabel, ylabel : strings
     |          Label names for the x and y variables.
     |      kwargs : key, value mappings
     |          Other keyword arguments are passed to the following functions:
     |
     |          - :meth:`matplotlib.axes.Axes.set_xlabel`
     |          - :meth:`matplotlib.axes.Axes.set_ylabel`
     |
     |      Returns
     |      -------
     |      :class:`JointGrid` instance
     |          Returns ``self`` for easy method chaining.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from _BaseGrid:
     |
     |  apply(self, func, *args, **kwargs)
     |      Pass the grid to a user-supplied function and return self.
     |
     |      The `func` must accept an object of this type for its first
     |      positional argument. Additional arguments are passed through.
     |      The return value of `func` is ignored; this method returns self.
     |      See the `pipe` method if you want the return value.
     |
     |      Added in v0.12.0.
     |
     |  pipe(self, func, *args, **kwargs)
     |      Pass the grid to a user-supplied function and return its value.
     |
     |      The `func` must accept an object of this type for its first
     |      positional argument. Additional arguments are passed through.
     |      The return value of `func` becomes the return value of this method.
     |      See the `apply` method if you want to return self instead.
     |
     |      Added in v0.12.0.
     |
     |  savefig(self, *args, **kwargs)
     |      Save an image of the plot.
     |
     |      This wraps :meth:`matplotlib.figure.Figure.savefig`, using bbox_inches="tight"
     |      by default. Parameters are passed through to the matplotlib function.
     |
     |  set(self, **kwargs)
     |      Set attributes on each subplot Axes.
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties inherited from _BaseGrid:
     |
     |  fig
     |      DEPRECATED: prefer the `figure` property.
     |
     |  figure
     |      Access the :class:`matplotlib.figure.Figure` object underlying the grid.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _BaseGrid:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class PairGrid(Grid)
     |  PairGrid(data, *, hue=None, vars=None, x_vars=None, y_vars=None, hue_order=None, palette=None, hue_kws=None, corner=False, diag_sharey=True, height=2.5, aspect=1, layout_pad=0.5, despine=True, dropna=False)
     |
     |  Subplot grid for plotting pairwise relationships in a dataset.
     |
     |  This object maps each variable in a dataset onto a column and row in a
     |  grid of multiple axes. Different axes-level plotting functions can be
     |  used to draw bivariate plots in the upper and lower triangles, and the
     |  marginal distribution of each variable can be shown on the diagonal.
     |
     |  Several different common plots can be generated in a single line using
     |  :func:`pairplot`. Use :class:`PairGrid` when you need more flexibility.
     |
     |  See the :ref:`tutorial <grid_tutorial>` for more information.
     |
     |  Method resolution order:
     |      PairGrid
     |      Grid
     |      _BaseGrid
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, data, *, hue=None, vars=None, x_vars=None, y_vars=None, hue_order=None, palette=None, hue_kws=None, corner=False, diag_sharey=True, height=2.5, aspect=1, layout_pad=0.5, despine=True, dropna=False)
     |      Initialize the plot figure and PairGrid object.
     |
     |      Parameters
     |      ----------
     |      data : DataFrame
     |          Tidy (long-form) dataframe where each column is a variable and
     |          each row is an observation.
     |      hue : string (variable name)
     |          Variable in ``data`` to map plot aspects to different colors. This
     |          variable will be excluded from the default x and y variables.
     |      vars : list of variable names
     |          Variables within ``data`` to use, otherwise use every column with
     |          a numeric datatype.
     |      {x, y}_vars : lists of variable names
     |          Variables within ``data`` to use separately for the rows and
     |          columns of the figure; i.e. to make a non-square plot.
     |      hue_order : list of strings
     |          Order for the levels of the hue variable in the palette
     |      palette : dict or seaborn color palette
     |          Set of colors for mapping the ``hue`` variable. If a dict, keys
     |          should be values  in the ``hue`` variable.
     |      hue_kws : dictionary of param -> list of values mapping
     |          Other keyword arguments to insert into the plotting call to let
     |          other plot attributes vary across levels of the hue variable (e.g.
     |          the markers in a scatterplot).
     |      corner : bool
     |          If True, don't add axes to the upper (off-diagonal) triangle of the
     |          grid, making this a "corner" plot.
     |      height : scalar
     |          Height (in inches) of each facet.
     |      aspect : scalar
     |          Aspect * height gives the width (in inches) of each facet.
     |      layout_pad : scalar
     |          Padding between axes; passed to ``fig.tight_layout``.
     |      despine : boolean
     |          Remove the top and right spines from the plots.
     |      dropna : boolean
     |          Drop missing values from the data before plotting.
     |
     |      See Also
     |      --------
     |      pairplot : Easily drawing common uses of :class:`PairGrid`.
     |      FacetGrid : Subplot grid for plotting conditional relationships.
     |
     |      Examples
     |      --------
     |
     |      .. include:: ../docstrings/PairGrid.rst
     |
     |  map(self, func, **kwargs)
     |      Plot with the same function in every subplot.
     |
     |      Parameters
     |      ----------
     |      func : callable plotting function
     |          Must take x, y arrays as positional arguments and draw onto the
     |          "currently active" matplotlib Axes. Also needs to accept kwargs
     |          called ``color`` and  ``label``.
     |
     |  map_diag(self, func, **kwargs)
     |      Plot with a univariate function on each diagonal subplot.
     |
     |      Parameters
     |      ----------
     |      func : callable plotting function
     |          Must take an x array as a positional argument and draw onto the
     |          "currently active" matplotlib Axes. Also needs to accept kwargs
     |          called ``color`` and  ``label``.
     |
     |  map_lower(self, func, **kwargs)
     |      Plot with a bivariate function on the lower diagonal subplots.
     |
     |      Parameters
     |      ----------
     |      func : callable plotting function
     |          Must take x, y arrays as positional arguments and draw onto the
     |          "currently active" matplotlib Axes. Also needs to accept kwargs
     |          called ``color`` and  ``label``.
     |
     |  map_offdiag(self, func, **kwargs)
     |      Plot with a bivariate function on the off-diagonal subplots.
     |
     |      Parameters
     |      ----------
     |      func : callable plotting function
     |          Must take x, y arrays as positional arguments and draw onto the
     |          "currently active" matplotlib Axes. Also needs to accept kwargs
     |          called ``color`` and  ``label``.
     |
     |  map_upper(self, func, **kwargs)
     |      Plot with a bivariate function on the upper diagonal subplots.
     |
     |      Parameters
     |      ----------
     |      func : callable plotting function
     |          Must take x, y arrays as positional arguments and draw onto the
     |          "currently active" matplotlib Axes. Also needs to accept kwargs
     |          called ``color`` and  ``label``.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from Grid:
     |
     |  add_legend(self, legend_data=None, title=None, label_order=None, adjust_subtitles=False, **kwargs)
     |      Draw a legend, maybe placing it outside axes and resizing the figure.
     |
     |      Parameters
     |      ----------
     |      legend_data : dict
     |          Dictionary mapping label names (or two-element tuples where the
     |          second element is a label name) to matplotlib artist handles. The
     |          default reads from ``self._legend_data``.
     |      title : string
     |          Title for the legend. The default reads from ``self._hue_var``.
     |      label_order : list of labels
     |          The order that the legend entries should appear in. The default
     |          reads from ``self.hue_names``.
     |      adjust_subtitles : bool
     |          If True, modify entries with invisible artists to left-align
     |          the labels and set the font size to that of a title.
     |      kwargs : key, value pairings
     |          Other keyword arguments are passed to the underlying legend methods
     |          on the Figure or Axes object.
     |
     |      Returns
     |      -------
     |      self : Grid instance
     |          Returns self for easy chaining.
     |
     |  tick_params(self, axis='both', **kwargs)
     |      Modify the ticks, tick labels, and gridlines.
     |
     |      Parameters
     |      ----------
     |      axis : {'x', 'y', 'both'}
     |          The axis on which to apply the formatting.
     |      kwargs : keyword arguments
     |          Additional keyword arguments to pass to
     |          :meth:`matplotlib.axes.Axes.tick_params`.
     |
     |      Returns
     |      -------
     |      self : Grid instance
     |          Returns self for easy chaining.
     |
     |  tight_layout(self, *args, **kwargs)
     |      Call fig.tight_layout within rect that exclude the legend.
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties inherited from Grid:
     |
     |  legend
     |      The :class:`matplotlib.legend.Legend` object, if present.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from _BaseGrid:
     |
     |  apply(self, func, *args, **kwargs)
     |      Pass the grid to a user-supplied function and return self.
     |
     |      The `func` must accept an object of this type for its first
     |      positional argument. Additional arguments are passed through.
     |      The return value of `func` is ignored; this method returns self.
     |      See the `pipe` method if you want the return value.
     |
     |      Added in v0.12.0.
     |
     |  pipe(self, func, *args, **kwargs)
     |      Pass the grid to a user-supplied function and return its value.
     |
     |      The `func` must accept an object of this type for its first
     |      positional argument. Additional arguments are passed through.
     |      The return value of `func` becomes the return value of this method.
     |      See the `apply` method if you want to return self instead.
     |
     |      Added in v0.12.0.
     |
     |  savefig(self, *args, **kwargs)
     |      Save an image of the plot.
     |
     |      This wraps :meth:`matplotlib.figure.Figure.savefig`, using bbox_inches="tight"
     |      by default. Parameters are passed through to the matplotlib function.
     |
     |  set(self, **kwargs)
     |      Set attributes on each subplot Axes.
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties inherited from _BaseGrid:
     |
     |  fig
     |      DEPRECATED: prefer the `figure` property.
     |
     |  figure
     |      Access the :class:`matplotlib.figure.Figure` object underlying the grid.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _BaseGrid:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

FUNCTIONS
    jointplot(data=None, *, x=None, y=None, hue=None, kind='scatter', height=6, ratio=5, space=0.2, dropna=False, xlim=None, ylim=None, color=None, palette=None, hue_order=None, hue_norm=None, marginal_ticks=False, joint_kws=None, marginal_kws=None, **kwargs)
        Draw a plot of two variables with bivariate and univariate graphs.

        This function provides a convenient interface to the :class:`JointGrid`
        class, with several canned plot kinds. This is intended to be a fairly
        lightweight wrapper; if you need more flexibility, you should use
        :class:`JointGrid` directly.

        Parameters
        ----------
        data : :class:`pandas.DataFrame`, :class:`numpy.ndarray`, mapping, or sequence
            Input data structure. Either a long-form collection of vectors that can be
            assigned to named variables or a wide-form dataset that will be internally
            reshaped.
        x, y : vectors or keys in ``data``
            Variables that specify positions on the x and y axes.
        hue : vector or key in ``data``
            Semantic variable that is mapped to determine the color of plot elements.
        kind : { "scatter" | "kde" | "hist" | "hex" | "reg" | "resid" }
            Kind of plot to draw. See the examples for references to the underlying functions.
        height : numeric
            Size of the figure (it will be square).
        ratio : numeric
            Ratio of joint axes height to marginal axes height.
        space : numeric
            Space between the joint and marginal axes
        dropna : bool
            If True, remove observations that are missing from ``x`` and ``y``.
        {x, y}lim : pairs of numbers
            Axis limits to set before plotting.
        color : :mod:`matplotlib color <matplotlib.colors>`
            Single color specification for when hue mapping is not used. Otherwise, the
            plot will try to hook into the matplotlib property cycle.
        palette : string, list, dict, or :class:`matplotlib.colors.Colormap`
            Method for choosing the colors to use when mapping the ``hue`` semantic.
            String values are passed to :func:`color_palette`. List or dict values
            imply categorical mapping, while a colormap object implies numeric mapping.
        hue_order : vector of strings
            Specify the order of processing and plotting for categorical levels of the
            ``hue`` semantic.
        hue_norm : tuple or :class:`matplotlib.colors.Normalize`
            Either a pair of values that set the normalization range in data units
            or an object that will map from data units into a [0, 1] interval. Usage
            implies numeric mapping.
        marginal_ticks : bool
            If False, suppress ticks on the count/density axis of the marginal plots.
        {joint, marginal}_kws : dicts
            Additional keyword arguments for the plot components.
        kwargs
            Additional keyword arguments are passed to the function used to
            draw the plot on the joint Axes, superseding items in the
            ``joint_kws`` dictionary.

        Returns
        -------
        :class:`JointGrid`
            An object managing multiple subplots that correspond to joint and marginal axes
            for plotting a bivariate relationship or distribution.

        See Also
        --------
        JointGrid : Set up a figure with joint and marginal views on bivariate data.
        PairGrid : Set up a figure with joint and marginal views on multiple variables.
        jointplot : Draw multiple bivariate plots with univariate marginal distributions.

        Examples
        --------

        .. include:: ../docstrings/jointplot.rst

    pairplot(data, *, hue=None, hue_order=None, palette=None, vars=None, x_vars=None, y_vars=None, kind='scatter', diag_kind='auto', markers=None, height=2.5, aspect=1, corner=False, dropna=False, plot_kws=None, diag_kws=None, grid_kws=None, size=None)
        Plot pairwise relationships in a dataset.

        By default, this function will create a grid of Axes such that each numeric
        variable in ``data`` will by shared across the y-axes across a single row and
        the x-axes across a single column. The diagonal plots are treated
        differently: a univariate distribution plot is drawn to show the marginal
        distribution of the data in each column.

        It is also possible to show a subset of variables or plot different
        variables on the rows and columns.

        This is a high-level interface for :class:`PairGrid` that is intended to
        make it easy to draw a few common styles. You should use :class:`PairGrid`
        directly if you need more flexibility.

        Parameters
        ----------
        data : `pandas.DataFrame`
            Tidy (long-form) dataframe where each column is a variable and
            each row is an observation.
        hue : name of variable in ``data``
            Variable in ``data`` to map plot aspects to different colors.
        hue_order : list of strings
            Order for the levels of the hue variable in the palette
        palette : dict or seaborn color palette
            Set of colors for mapping the ``hue`` variable. If a dict, keys
            should be values  in the ``hue`` variable.
        vars : list of variable names
            Variables within ``data`` to use, otherwise use every column with
            a numeric datatype.
        {x, y}_vars : lists of variable names
            Variables within ``data`` to use separately for the rows and
            columns of the figure; i.e. to make a non-square plot.
        kind : {'scatter', 'kde', 'hist', 'reg'}
            Kind of plot to make.
        diag_kind : {'auto', 'hist', 'kde', None}
            Kind of plot for the diagonal subplots. If 'auto', choose based on
            whether or not ``hue`` is used.
        markers : single matplotlib marker code or list
            Either the marker to use for all scatterplot points or a list of markers
            with a length the same as the number of levels in the hue variable so that
            differently colored points will also have different scatterplot
            markers.
        height : scalar
            Height (in inches) of each facet.
        aspect : scalar
            Aspect * height gives the width (in inches) of each facet.
        corner : bool
            If True, don't add axes to the upper (off-diagonal) triangle of the
            grid, making this a "corner" plot.
        dropna : boolean
            Drop missing values from the data before plotting.
        {plot, diag, grid}_kws : dicts
            Dictionaries of keyword arguments. ``plot_kws`` are passed to the
            bivariate plotting function, ``diag_kws`` are passed to the univariate
            plotting function, and ``grid_kws`` are passed to the :class:`PairGrid`
            constructor.

        Returns
        -------
        grid : :class:`PairGrid`
            Returns the underlying :class:`PairGrid` instance for further tweaking.

        See Also
        --------
        PairGrid : Subplot grid for more flexible plotting of pairwise relationships.
        JointGrid : Grid for plotting joint and marginal distributions of two variables.

        Examples
        --------

        .. include:: ../docstrings/pairplot.rst

DATA
    __all__ = ['FacetGrid', 'PairGrid', 'JointGrid', 'pairplot', 'jointplo...

FILE
    /Users/leopoldogonzalez/miniconda3/lib/python3.12/site-packages/seaborn/axisgrid.py


