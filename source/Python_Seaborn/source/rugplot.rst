Help on function rugplot in module seaborn.distributions:

rugplot(data=None, *, x=None, y=None, hue=None, height=0.025, expand_margins=True, palette=None, hue_order=None, hue_norm=None, legend=True, ax=None, **kwargs)
    Plot marginal distributions by drawing ticks along the x and y axes.

    This function is intended to complement other plots by showing the location
    of individual observations in an unobtrusive way.

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
    height : float
        Proportion of axes extent covered by each rug element. Can be negative.
    expand_margins : bool
        If True, increase the axes margins by the height of the rug to avoid
        overlap with other elements.
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
    legend : bool
        If False, do not add a legend for semantic variables.
    ax : :class:`matplotlib.axes.Axes`
        Pre-existing axes for the plot. Otherwise, call :func:`matplotlib.pyplot.gca`
        internally.
    kwargs
        Other keyword arguments are passed to
        :meth:`matplotlib.collections.LineCollection`

    Returns
    -------
    :class:`matplotlib.axes.Axes`
        The matplotlib axes containing the plot.

    Examples
    --------

    .. include:: ../docstrings/rugplot.rst

