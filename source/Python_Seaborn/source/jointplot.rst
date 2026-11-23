Help on function jointplot in module seaborn.axisgrid:

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

