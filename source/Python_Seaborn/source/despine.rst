Help on function despine in module seaborn.utils:

despine(fig=None, ax=None, top=True, right=True, left=False, bottom=False, offset=None, trim=False)
    Remove the top and right spines from plot(s).

    fig : matplotlib figure, optional
        Figure to despine all axes of, defaults to the current figure.
    ax : matplotlib axes, optional
        Specific axes object to despine. Ignored if fig is provided.
    top, right, left, bottom : boolean, optional
        If True, remove that spine.
    offset : int or dict, optional
        Absolute distance, in points, spines should be moved away
        from the axes (negative values move spines inward). A single value
        applies to all spines; a dict can be used to set offset values per
        side.
    trim : bool, optional
        If True, limit spines to the smallest and largest major tick
        on each non-despined axis.

    Returns
    -------
    None

