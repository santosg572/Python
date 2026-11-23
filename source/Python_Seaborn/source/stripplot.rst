Help on function stripplot in module seaborn.categorical:

stripplot(data=None, *, x=None, y=None, hue=None, order=None, hue_order=None, jitter=True, dodge=False, orient=None, color=None, palette=None, size=5, edgecolor=<default>, linewidth=0, hue_norm=None, log_scale=None, native_scale=False, formatter=None, legend='auto', ax=None, **kwargs)
    Draw a categorical scatterplot using jitter to reduce overplotting.

    A strip plot can be drawn on its own, but it is also a good complement
    to a box or violin plot in cases where you want to show all observations
    along with some representation of the underlying distribution.

    See the :ref:`tutorial <categorical_tutorial>` for more information.

    .. note::
        By default, this function treats one of the variables as categorical
        and draws data at ordinal positions (0, 1, ... n) on the relevant axis.
        As of version 0.13.0, this can be disabled by setting `native_scale=True`.


    Parameters
    ----------
    data : DataFrame, Series, dict, array, or list of arrays
        Dataset for plotting. If `x` and `y` are absent, this is
        interpreted as wide-form. Otherwise it is expected to be long-form.
    x, y, hue : names of variables in `data` or vector data
        Inputs for plotting long-form data. See examples for interpretation.
    order, hue_order : lists of strings
        Order to plot the categorical levels in; otherwise the levels are
        inferred from the data objects.
    jitter : float, `True`/`1` is special-cased
        Amount of jitter (only along the categorical axis) to apply. This
        can be useful when you have many points and they overlap, so that
        it is easier to see the distribution. You can specify the amount
        of jitter (half the width of the uniform random variable support),
        or use `True` for a good default.
    dodge : bool
        When a `hue` variable is assigned, setting this to `True` will
        separate the strips for different hue levels along the categorical
        axis and narrow the amount of space allotedto each strip. Otherwise,
        the points for each level will be plotted in the same strip.
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
    size : float
        Radius of the markers, in points.
    edgecolor : matplotlib color, "gray" is special-cased
        Color of the lines around each point. If you pass `"gray"`, the
        brightness is determined by the color palette used for the body
        of the points. Note that `stripplot` has `linewidth=0` by default,
        so edge colors are only visible with nonzero line width.
    linewidth : float
        Width of the lines that frame the plot elements.
    hue_norm : tuple or :class:`matplotlib.colors.Normalize` object
        Normalization in data units for colormap applied to the `hue`
        variable when it is numeric. Not relevant if `hue` is categorical.

        .. versionadded:: v0.12.0
    log_scale : bool or number, or pair of bools or numbers
        Set axis scale(s) to log. A single value sets the data axis for any numeric
        axes in the plot. A pair of values sets each axis independently.
        Numeric values are interpreted as the desired base (default 10).
        When `None` or `False`, seaborn defers to the existing Axes scale.

        .. versionadded:: v0.13.0
    native_scale : bool
        When True, numeric or datetime values on the categorical axis will maintain
        their original scaling rather than being converted to fixed indices.

        .. versionadded:: v0.13.0
    formatter : callable
        Function for converting categorical data into strings. Affects both grouping
        and tick labels.

        .. versionadded:: v0.13.0
    legend : "auto", "brief", "full", or False
        How to draw the legend. If "brief", numeric `hue` and `size`
        variables will be represented with a sample of evenly spaced values.
        If "full", every group will get an entry in the legend. If "auto",
        choose between brief or full representation based on number of levels.
        If `False`, no legend data is added and no legend is drawn.

        .. versionadded:: v0.13.0
    ax : matplotlib Axes
        Axes object to draw the plot onto, otherwise uses the current Axes.
    kwargs : key, value mappings
        Other keyword arguments are passed through to
        :meth:`matplotlib.axes.Axes.scatter`.

    Returns
    -------
    ax : matplotlib Axes
        Returns the Axes object with the plot drawn onto it.

    See Also
    --------
    swarmplot : A categorical scatterplot where the points do not overlap. Can
                be used with other plots to show each observation.
    boxplot : A traditional box-and-whisker plot with a similar API.
    violinplot : A combination of boxplot and kernel density estimation.
    catplot : Combine a categorical plot with a :class:`FacetGrid`.

    Examples
    --------
    .. include:: ../docstrings/stripplot.rst

