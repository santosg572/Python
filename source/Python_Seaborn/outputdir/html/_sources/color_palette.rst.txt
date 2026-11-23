color_palette
======================

Help on function color_palette in module seaborn.palettes:

color_palette(palette=None, n_colors=None, desat=None, as_cmap=False)
    Return a list of colors or continuous colormap defining a palette.

    Possible ``palette`` values include:
        - Name of a seaborn palette (deep, muted, bright, pastel, dark, colorblind)
        - Name of matplotlib colormap
        - 'husl' or 'hls'
        - 'ch:<cubehelix arguments>'
        - 'light:<color>', 'dark:<color>', 'blend:<color>,<color>',
        - A sequence of colors in any format matplotlib accepts

    Calling this function with ``palette=None`` will return the current
    matplotlib color cycle.

    This function can also be used in a ``with`` statement to temporarily
    set the color cycle for a plot or set of plots.

    See the :ref:`tutorial <palette_tutorial>` for more information.

    Parameters
    ----------
    palette : None, string, or sequence, optional
        Name of palette or None to return current palette. If a sequence, input
        colors are used but possibly cycled and desaturated.
    n_colors : int, optional
        Number of colors in the palette. If ``None``, the default will depend
        on how ``palette`` is specified. Named palettes default to 6 colors,
        but grabbing the current palette or passing in a list of colors will
        not change the number of colors unless this is specified. Asking for
        more colors than exist in the palette will cause it to cycle. Ignored
        when ``as_cmap`` is True.
    desat : float, optional
        Proportion to desaturate each color by.
    as_cmap : bool
        If True, return a :class:`matplotlib.colors.ListedColormap`.

    Returns
    -------
    list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    See Also
    --------
    set_palette : Set the default color cycle for all plots.
    set_color_codes : Reassign color codes like ``"b"``, ``"g"``, etc. to
                      colors from one of the seaborn palettes.

    Examples
    --------

    .. include:: ../docstrings/color_palette.rst

