ecdfplot
======================

Help on function ecdfplot in module seaborn.distributions:

ecdfplot(data=None, *, x=None, y=None, hue=None, weights=None, stat='proportion', complementary=False, palette=None, hue_order=None, hue_norm=None, log_scale=None, legend=True, ax=None, **kwargs)
    Plot empirical cumulative distribution functions.

    An ECDF represents the proportion or count of observations falling below each
    unique value in a dataset. Compared to a histogram or density plot, it has the
    advantage that each observation is visualized directly, meaning that there are
    no binning or smoothing parameters that need to be adjusted. It also aids direct
    comparisons between multiple distributions. A downside is that the relationship
    between the appearance of the plot and the basic properties of the distribution
    (such as its central tendency, variance, and the presence of any bimodality)
    may not be as intuitive.

    More information is provided in the :ref:`user guide <tutorial_ecdf>`.

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
    weights : vector or key in ``data``
        If provided, weight the contribution of the corresponding data points
        towards the cumulative distribution using these values.
    stat : {{"proportion", "percent", "count"}}
        Distribution statistic to compute.
    complementary : bool
        If True, use the complementary CDF (1 - CDF)
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
    log_scale : bool or number, or pair of bools or numbers
        Set axis scale(s) to log. A single value sets the data axis for any numeric
        axes in the plot. A pair of values sets each axis independently.
        Numeric values are interpreted as the desired base (default 10).
        When `None` or `False`, seaborn defers to the existing Axes scale.
    legend : bool
        If False, suppress the legend for semantic variables.
    ax : :class:`matplotlib.axes.Axes`
        Pre-existing axes for the plot. Otherwise, call :func:`matplotlib.pyplot.gca`
        internally.
    kwargs
        Other keyword arguments are passed to :meth:`matplotlib.axes.Axes.plot`.

    Returns
    -------
    :class:`matplotlib.axes.Axes`
        The matplotlib axes containing the plot.

    See Also
    --------
    displot : Figure-level interface to distribution plot functions.
    histplot : Plot a histogram of binned counts with optional normalization or smoothing.
    kdeplot : Plot univariate or bivariate distributions using kernel density estimation.
    rugplot : Plot a tick at each observation value along the x and/or y axes.

    Examples
    --------

    .. include:: ../docstrings/ecdfplot.rst

