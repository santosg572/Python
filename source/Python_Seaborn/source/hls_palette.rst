Help on function hls_palette in module seaborn.palettes:

hls_palette(n_colors=6, h=0.01, l=0.6, s=0.65, as_cmap=False)
    Return hues with constant lightness and saturation in the HLS system.

    The hues are evenly sampled along a circular path. The resulting palette will be
    appropriate for categorical or cyclical data.

    The `h`, `l`, and `s` values should be between 0 and 1.

    .. note::
        While the separation of the resulting colors will be mathematically
        constant, the HLS system does not construct a perceptually-uniform space,
        so their apparent intensity will vary.

    Parameters
    ----------
    n_colors : int
        Number of colors in the palette.
    h : float
        The value of the first hue.
    l : float
        The lightness value.
    s : float
        The saturation intensity.
    as_cmap : bool
        If True, return a matplotlib colormap object.

    Returns
    -------
    palette
        list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    See Also
    --------
    husl_palette : Make a palette using evenly spaced hues in the HUSL system.

    Examples
    --------
    .. include:: ../docstrings/hls_palette.rst

