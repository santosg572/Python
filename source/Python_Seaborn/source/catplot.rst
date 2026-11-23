Help on function catplot in module seaborn.categorical:

catplot(data=None, *, x=None, y=None, hue=None, row=None, col=None, kind='strip', estimator='mean', errorbar=('ci', 95), n_boot=1000, seed=None, units=None, weights=None, order=None, hue_order=None, row_order=None, col_order=None, col_wrap=None, height=5, aspect=1, log_scale=None, native_scale=False, formatter=None, orient=None, color=None, palette=None, hue_norm=None, legend='auto', legend_out=True, sharex=True, sharey=True, margin_titles=False, facet_kws=None, ci=<deprecated>, **kwargs)
    Figure-level interface for drawing categorical plots onto a FacetGrid.

    This function provides access to several axes-level functions that
    show the relationship between a numerical and one or more categorical
    variables using one of several visual representations. The `kind`
    parameter selects the underlying axes-level function to use.

    Categorical scatterplots:

    - :func:`stripplot` (with `kind="strip"`; the default)
    - :func:`swarmplot` (with `kind="swarm"`)

    Categorical distribution plots:

    - :func:`boxplot` (with `kind="box"`)
    - :func:`violinplot` (with `kind="violin"`)
    - :func:`boxenplot` (with `kind="boxen"`)

    Categorical estimate plots:

    - :func:`pointplot` (with `kind="point"`)
    - :func:`barplot` (with `kind="bar"`)
    - :func:`countplot` (with `kind="count"`)

    Extra keyword arguments are passed to the underlying function, so you
    should refer to the documentation for each to see kind-specific options.

    See the :ref:`tutorial <categorical_tutorial>` for more information.

    .. note::
        By default, this function treats one of the variables as categorical
        and draws data at ordinal positions (0, 1, ... n) on the relevant axis.
        As of version 0.13.0, this can be disabled by setting `native_scale=True`.


    After plotting, the :class:`FacetGrid` with the plot is returned and can
    be used directly to tweak supporting plot details or add other layers.

    Parameters
    ----------
    data : DataFrame, Series, dict, array, or list of arrays
        Dataset for plotting. If `x` and `y` are absent, this is
        interpreted as wide-form. Otherwise it is expected to be long-form.
    x, y, hue : names of variables in `data` or vector data
        Inputs for plotting long-form data. See examples for interpretation.
    row, col : names of variables in `data` or vector data
        Categorical variables that will determine the faceting of the grid.
    kind : str
        The kind of plot to draw, corresponds to the name of a categorical
        axes-level plotting function. Options are: "strip", "swarm", "box", "violin",
        "boxen", "point", "bar", or "count".
    estimator : string or callable that maps vector -> scalar
        Statistical function to estimate within each categorical bin.
    errorbar : string, (string, number) tuple, callable or None
        Name of errorbar method (either "ci", "pi", "se", or "sd"), or a tuple
        with a method name and a level parameter, or a function that maps from a
        vector to a (min, max) interval, or None to hide errorbar. See the
        :doc:`errorbar tutorial </tutorial/error_bars>` for more information.

        .. versionadded:: v0.12.0
    n_boot : int
        Number of bootstrap samples used to compute confidence intervals.
    seed : int, `numpy.random.Generator`, or `numpy.random.RandomState`
        Seed or random number generator for reproducible bootstrapping.
    units : name of variable in `data` or vector data
        Identifier of sampling units; used by the errorbar function to
        perform a multilevel bootstrap and account for repeated measures
    weights : name of variable in `data` or vector data
        Data values or column used to compute weighted statistics.
        Note that the use of weights may limit other statistical options.

        .. versionadded:: v0.13.1
    order, hue_order : lists of strings
        Order to plot the categorical levels in; otherwise the levels are
        inferred from the data objects.
    row_order, col_order : lists of strings
        Order to organize the rows and/or columns of the grid in; otherwise the
        orders are inferred from the data objects.
    col_wrap : int
        "Wrap" the column variable at this width, so that the column facets
        span multiple rows. Incompatible with a ``row`` facet.
    height : scalar
        Height (in inches) of each facet. See also: ``aspect``.
    aspect : scalar
        Aspect ratio of each facet, so that ``aspect * height`` gives the width
        of each facet in inches.
    native_scale : bool
        When True, numeric or datetime values on the categorical axis will maintain
        their original scaling rather than being converted to fixed indices.

        .. versionadded:: v0.13.0
    formatter : callable
        Function for converting categorical data into strings. Affects both grouping
        and tick labels.

        .. versionadded:: v0.13.0
    orient : "v" | "h" | "x" | "y"
        Orientation of the plot (vertical or horizontal). This is usually
        inferred based on the type of the input variables, but it can be used
        to resolve ambiguity when both `x` and `y` are numeric or when
        plotting wide-form data.

        .. versionchanged:: v0.13.0
            Added 'x'/'y' as options, equivalent to 'v'/'h'.
    color : matplotlib color
        Single color for the elements in the plot.
    palette : palette name, list, or dict
        Colors to use for the different levels of the ``hue`` variable. Should
        be something that can be interpreted by :func:`color_palette`, or a
        dictionary mapping hue levels to matplotlib colors.
    hue_norm : tuple or :class:`matplotlib.colors.Normalize` object
        Normalization in data units for colormap applied to the `hue`
        variable when it is numeric. Not relevant if `hue` is categorical.

        .. versionadded:: v0.12.0
    legend : "auto", "brief", "full", or False
        How to draw the legend. If "brief", numeric `hue` and `size`
        variables will be represented with a sample of evenly spaced values.
        If "full", every group will get an entry in the legend. If "auto",
        choose between brief or full representation based on number of levels.
        If `False`, no legend data is added and no legend is drawn.

        .. versionadded:: v0.13.0
    legend_out : bool
        If ``True``, the figure size will be extended, and the legend will be
        drawn outside the plot on the center right.
    share{x,y} : bool, 'col', or 'row' optional
        If true, the facets will share y axes across columns and/or x axes
        across rows.
    margin_titles : bool
        If ``True``, the titles for the row variable are drawn to the right of
        the last column. This option is experimental and may not work in all
        cases.
    facet_kws : dict
        Dictionary of other keyword arguments to pass to :class:`FacetGrid`.
    kwargs : key, value pairings
        Other keyword arguments are passed through to the underlying plotting
        function.

    Returns
    -------
    :class:`FacetGrid`
        Returns the :class:`FacetGrid` object with the plot on it for further
        tweaking.

    Examples
    --------
    .. include:: ../docstrings/catplot.rst

