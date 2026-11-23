blend_palette
======================

Help on function blend_palette in module seaborn.palettes:

blend_palette(colors, n_colors=6, as_cmap=False, input='rgb')
    Make a palette that blends between a list of colors.

    Parameters
    ----------
    colors : sequence of colors in various formats interpreted by `input`
        hex code, html color name, or tuple in `input` space.
    n_colors : int, optional
        Number of colors in the palette.
    as_cmap : bool, optional
        If True, return a :class:`matplotlib.colors.ListedColormap`.

    Returns
    -------
    palette
        list of RGB tuples or :class:`matplotlib.colors.ListedColormap`

    Examples
    --------
    .. include: ../docstrings/blend_palette.rst

