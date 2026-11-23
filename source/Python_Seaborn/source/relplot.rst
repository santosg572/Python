Help on function relplot in module seaborn.relational:

relplot(data=None, *, x=None, y=None, hue=None, size=None, style=None, units=None, weights=None, row=None, col=None, col_wrap=None, row_order=None, col_order=None, palette=None, hue_order=None, hue_norm=None, sizes=None, size_order=None, size_norm=None, markers=None, dashes=None, style_order=None, legend='auto', kind='scatter', height=5, aspect=1, facet_kws=None, **kwargs)
    Figure-level interface for drawing relational plots onto a FacetGrid.

    This function provides access to several different axes-level functions
    that show the relationship between two variables with semantic mappings
    of subsets. The `kind` parameter selects the underlying axes-level
    function to use:

    - :func:`scatterplot` (with `kind="scatter"`; the default)
    - :func:`lineplot` (with `kind="line"`)

    Extra keyword arguments are passed to the underlying function, so you
    should refer to the documentation for each to see kind-specific options.

    The relationship between `x` and `y` can be shown for different subsets
    of the data using the `hue`, `size`, and `style` parameters. These
    parameters control what visual semantics are used to identify the different
    subsets. It is possible to show up to three dimensions independently by
    using all three semantic types, but this style of plot can be hard to
    interpret and is often ineffective. Using redundant semantics (i.e. both
    `hue` and `style` for the same variable) can be helpful for making
    graphics more accessible.

    See the :ref:`tutorial <relational_tutorial>` for more information.

    The default treatment of the `hue` (and to a lesser extent, `size`)
    semantic, if present, depends on whether the variable is inferred to
    represent "numeric" or "categorical" data. In particular, numeric variables
    are represented with a sequential colormap by default, and the legend
    entries show regular "ticks" with values that may or may not exist in the
    data. This behavior can be controlled through various parameters, as
    described and illustrated below.

    After plotting, the :class:`FacetGrid` with the plot is returned and can
    be used directly to tweak supporting plot details or add other layers.

    Parameters
    ----------
    data : :class:`pandas.DataFrame`, :class:`numpy.ndarray`, mapping, or sequence
        Input data structure. Either a long-form collection of vectors that can be
        assigned to named variables or a wide-form dataset that will be internally
        reshaped.
    x, y : vectors or keys in ``data``
        Variables that specify positions on the x and y axes.
    hue : vector or key in `data`
        Grouping variable that will produce elements with different colors.
        Can be either categorical or numeric, although color mapping will
        behave differently in latter case.
    size : vector or key in `data`
        Grouping variable that will produce elements with different sizes.
        Can be either categorical or numeric, although size mapping will
        behave differently in latter case.
    style : vector or key in `data`
        Grouping variable that will produce elements with different styles.
        Can have a numeric dtype but will always be treated as categorical.
    units : vector or key in `data`
        Grouping variable identifying sampling units. When used, a separate
        line will be drawn for each unit with appropriate semantics, but no
        legend entry will be added. Useful for showing distribution of
        experimental replicates when exact identities are not needed.
    weights : vector or key in `data`
        Data values or column used to compute weighted estimation.
        Note that use of weights currently limits the choice of statistics
        to a 'mean' estimator and 'ci' errorbar.
    row, col : vectors or keys in ``data``
        Variables that define subsets to plot on different facets.
    col_wrap : int
        "Wrap" the column variable at this width, so that the column facets
        span multiple rows. Incompatible with a ``row`` facet.
    row_order, col_order : lists of strings
        Order to organize the rows and/or columns of the grid in, otherwise the
        orders are inferred from the data objects.
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
    sizes : list, dict, or tuple
        An object that determines how sizes are chosen when `size` is used.
        List or dict arguments should provide a size for each unique data value,
        which forces a categorical interpretation. The argument may also be a
        min, max tuple.
    size_order : list
        Specified order for appearance of the `size` variable levels,
        otherwise they are determined from the data. Not relevant when the
        `size` variable is numeric.
    size_norm : tuple or Normalize object
        Normalization in data units for scaling plot objects when the
        `size` variable is numeric.
    style_order : list
        Specified order for appearance of the `style` variable levels
        otherwise they are determined from the data. Not relevant when the
        `style` variable is numeric.
    dashes : boolean, list, or dictionary
        Object determining how to draw the lines for different levels of the
        `style` variable. Setting to `True` will use default dash codes, or
        you can pass a list of dash codes or a dictionary mapping levels of the
        `style` variable to dash codes. Setting to `False` will use solid
        lines for all subsets. Dashes are specified as in matplotlib: a tuple
        of `(segment, gap)` lengths, or an empty string to draw a solid line.
    markers : boolean, list, or dictionary
        Object determining how to draw the markers for different levels of the
        `style` variable. Setting to `True` will use default markers, or
        you can pass a list of markers or a dictionary mapping levels of the
        `style` variable to markers. Setting to `False` will draw
        marker-less lines.  Markers are specified as in matplotlib.
    legend : "auto", "brief", "full", or False
        How to draw the legend. If "brief", numeric `hue` and `size`
        variables will be represented with a sample of evenly spaced values.
        If "full", every group will get an entry in the legend. If "auto",
        choose between brief or full representation based on number of levels.
        If `False`, no legend data is added and no legend is drawn.
    kind : string
        Kind of plot to draw, corresponding to a seaborn relational plot.
        Options are `"scatter"` or `"line"`.
    height : scalar
        Height (in inches) of each facet. See also: ``aspect``.
    aspect : scalar
        Aspect ratio of each facet, so that ``aspect * height`` gives the width
        of each facet in inches.
    facet_kws : dict
        Dictionary of other keyword arguments to pass to :class:`FacetGrid`.
    kwargs : key, value pairings
        Other keyword arguments are passed through to the underlying plotting
        function.

    Returns
    -------
    :class:`FacetGrid`
        An object managing one or more subplots that correspond to conditional data
        subsets with convenient methods for batch-setting of axes attributes.

    Examples
    --------

    .. include:: ../docstrings/relplot.rst

