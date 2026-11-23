move_legend
======================

Help on function move_legend in module seaborn.utils:

move_legend(obj, loc, **kwargs)
    Recreate a plot's legend at a new location.

    The name is a slight misnomer. Matplotlib legends do not expose public
    control over their position parameters. So this function creates a new legend,
    copying over the data from the original object, which is then removed.

    Parameters
    ----------
    obj : the object with the plot
        This argument can be either a seaborn or matplotlib object:

        - :class:`seaborn.FacetGrid` or :class:`seaborn.PairGrid`
        - :class:`matplotlib.axes.Axes` or :class:`matplotlib.figure.Figure`

    loc : str or int
        Location argument, as in :meth:`matplotlib.axes.Axes.legend`.

    kwargs
        Other keyword arguments are passed to :meth:`matplotlib.axes.Axes.legend`.

    Examples
    --------

    .. include:: ../docstrings/move_legend.rst

