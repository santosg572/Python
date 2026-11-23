mpl_palette
======================

Help on function mpl_palette in module seaborn.palettes:

mpl_palette(name, n_colors=6, as_cmap=False)
    Return a palette or colormap from the matplotlib registry.

    For continuous palettes, evenly-spaced discrete samples are chosen while
    excluding the minimum and maximum value in the colormap to provide better
    contrast at the extremes.

    For qualitative palettes (e.g. those from colorbrewer), exact values are
    indexed (rather than interpolated), but fewer than `n_colors` can be returned
    if the palette does not define that many.

    Parameters
    ----------
    name : string
        Name of the palette. This should be a named matplotlib colormap.
    n_colors : int
        Number of discrete colors in the palette.

    Returns
    -------
    list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    Examples
    --------
    .. include:: ../docstrings/mpl_palette.rst

