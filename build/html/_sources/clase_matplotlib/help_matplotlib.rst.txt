matplotlib.pyplot
=================

&&&&&&&&&&&&&&&&&&&&&&& bar &&&&&&&&&&&&&&&&&&&&&&&&&
Help on function bar in module matplotlib.pyplot:

bar(x: 'float | ArrayLike', height: 'float | ArrayLike', width: 'float | ArrayLike' = 0.8, bottom: 'float | ArrayLike | None' = None, *, align: "Literal['center', 'edge']" = 'center', data: 'DataParamType' = None, **kwargs) -> 'BarContainer'
    Make a bar plot.

    The bars are positioned at *x* with the given *align*\ment. Their
    dimensions are given by *height* and *width*. The vertical baseline
    is *bottom* (default 0).

    Many parameters can take either a single value applying to all bars
    or a sequence of values, one for each bar.

    Parameters
    ----------
    x : float or array-like
        The x coordinates of the bars. See also *align* for the
        alignment of the bars to the coordinates.

        Bars are often used for categorical data, i.e. string labels below
        the bars. You can provide a list of strings directly to *x*.
        ``bar(['A', 'B', 'C'], [1, 2, 3])`` is often a shorter and more
        convenient notation compared to
        ``bar(range(3), [1, 2, 3], tick_label=['A', 'B', 'C'])``. They are
        equivalent as long as the names are unique. The explicit *tick_label*
        notation draws the names in the sequence given. However, when having
        duplicate values in categorical *x* data, these values map to the same
        numerical x coordinate, and hence the corresponding bars are drawn on
        top of each other.

    height : float or array-like
        The height(s) of the bars.

        Note that if *bottom* has units (e.g. datetime), *height* should be in
        units that are a difference from the value of *bottom* (e.g. timedelta).

    width : float or array-like, default: 0.8
        The width(s) of the bars.

        Note that if *x* has units (e.g. datetime), then *width* should be in
        units that are a difference (e.g. timedelta) around the *x* values.

    bottom : float or array-like, default: 0
        The y coordinate(s) of the bottom side(s) of the bars.

        Note that if *bottom* has units, then the y-axis will get a Locator and
        Formatter appropriate for the units (e.g. dates, or categorical).

    align : {'center', 'edge'}, default: 'center'
        Alignment of the bars to the *x* coordinates:

        - 'center': Center the base on the *x* positions.
        - 'edge': Align the left edges of the bars with the *x* positions.

        To align the bars on the right edge pass a negative *width* and
        ``align='edge'``.

    Returns
    -------
    `.BarContainer`
        Container with all the bars and optionally errorbars.

    Other Parameters
    ----------------
    color : :mpltype:`color` or list of :mpltype:`color`, optional
        The colors of the bar faces. This is an alias for *facecolor*.
        If both are given, *facecolor* takes precedence.

    facecolor : :mpltype:`color` or list of :mpltype:`color`, optional
        The colors of the bar faces.
        If both *color* and *facecolor are given, *facecolor* takes precedence.

    edgecolor : :mpltype:`color` or list of :mpltype:`color`, optional
        The colors of the bar edges.

    linewidth : float or array-like, optional
        Width of the bar edge(s). If 0, don't draw edges.

    tick_label : str or list of str, optional
        The tick labels of the bars.
        Default: None (Use default numeric labels.)

    label : str or list of str, optional
        A single label is attached to the resulting `.BarContainer` as a
        legend label for the whole dataset.
        If a list is provided, it must be the same length as *x* and
        labels the individual bars. Repeated labels are not de-duplicated
        and will cause repeated label entries, so this is best used when
        bars also differ in style (e.g., by passing a list to *color*).

        Tip: Use `.bar_label` to place labels on the bars.

    xerr, yerr : float or array-like of shape(N,) or shape(2, N), optional
        If not *None*, add horizontal / vertical errorbars to the bar tips.
        The values are +/- sizes relative to the data:

        - scalar: symmetric +/- values for all bars
        - shape(N,): symmetric +/- values for each bar
        - shape(2, N): Separate - and + values for each bar. First row
          contains the lower errors, the second row contains the upper
          errors.
        - *None*: No errorbar. (Default)

        This is a convenience shortcut for an extra `~.axes.Axes.errorbar`
        call. See its documentation and
        :doc:`/gallery/statistics/errorbar_features` for an example on
        the usage of *xerr* and *yerr*.

    ecolor : :mpltype:`color` or list of :mpltype:`color`, default: 'black'
        The line color of the errorbars.
        Multiple colors are only supported if the errorbars do not have
        caps. If you need individually colored errorbars with caps, instead
        use explicit `~.axes.Axes.errorbar` calls for each data point.

    capsize : float, default: :rc:`errorbar.capsize`
       The length of the error bar caps in points.

    error_kw : dict, optional
        Dictionary of keyword arguments to be passed to the
        `~.Axes.errorbar` method. Values of *ecolor* or *capsize* defined
        here take precedence over the independent keyword arguments.

    log : bool, default: False
        If *True*, set the y-axis to be log scale.

    data : indexable object, optional
        If given, all parameters also accept a string ``s``, which is
        interpreted as ``data[s]`` if ``s`` is a key in ``data``.

    **kwargs : `.Rectangle` properties

    Properties:
        agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image
        alpha: float or None
        angle: unknown
        animated: bool
        antialiased or aa: bool or None
        bounds: (left, bottom, width, height)
        capstyle: `.CapStyle` or {'butt', 'projecting', 'round'}
        clip_box: `~matplotlib.transforms.BboxBase` or None
        clip_on: bool
        clip_path: Patch or (Path, Transform) or None
        color: :mpltype:`color`
        edgecolor or ec: :mpltype:`color` or None
        edgegapcolor: :mpltype:`color` or None
        facecolor or fc: :mpltype:`color` or None
        figure: `~matplotlib.figure.Figure` or `~matplotlib.figure.SubFigure`
        fill: bool
        gid: str
        hatch: {'/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}
        hatch_linewidth: unknown
        hatchcolor: :mpltype:`color` or 'edge' or None
        height: unknown
        in_layout: bool
        joinstyle: `.JoinStyle` or {'miter', 'round', 'bevel'}
        label: object
        linestyle or ls: {'-', '--', '-.', ':', '', ...} or (offset, on-off-seq)
        linewidth or lw: float or None
        mouseover: bool
        path_effects: list of `.AbstractPathEffect`
        picker: None or bool or float or callable
        rasterized: bool
        sketch_params: (scale: float, length: float, randomness: float)
        snap: bool or None
        transform: `~matplotlib.transforms.Transform`
        url: str
        visible: bool
        width: unknown
        x: unknown
        xy: (float, float)
        y: unknown
        zorder: float

    See Also
    --------
    barh : Plot a horizontal bar plot.
    grouped_bar : Plot multiple datasets as grouped bar plot.
    bar_label : Add labels to bars.

    Notes
    -----

    .. note::

        This is the :ref:`pyplot wrapper <pyplot_interface>` for `.axes.Axes.bar`.

    Stacked bars can be achieved by passing individual *bottom* values per
    bar. See :doc:`/gallery/lines_bars_and_markers/bar_stacked`.

None
&&&&&&&&&&&&&&&&&&&&&&& colormaps &&&&&&&&&&&&&&&&&&&&&&&&&
Help on ColormapRegistry in module matplotlib.cm object:

class ColormapRegistry(collections.abc.Mapping)
 |  ColormapRegistry(cmaps)
 |
 |  Container for colormaps that are known to Matplotlib by name.
 |
 |  The universal registry instance is `matplotlib.colormaps`. There should be
 |  no need for users to instantiate `.ColormapRegistry` themselves.
 |
 |  Read access uses a dict-like interface mapping names to `.Colormap`\s::
 |
 |      import matplotlib as mpl
 |      cmap = mpl.colormaps['viridis']
 |
 |  Returned `.Colormap`\s are copies, so that their modification does not
 |  change the global definition of the colormap.
 |
 |  Additional colormaps can be added via `.ColormapRegistry.register`::
 |
 |      mpl.colormaps.register(my_colormap)
 |
 |  To get a list of all registered colormaps, you can do::
 |
 |      from matplotlib import colormaps
 |      list(colormaps)
 |
 |  Method resolution order:
 |      ColormapRegistry
 |      collections.abc.Mapping
 |      collections.abc.Collection
 |      collections.abc.Sized
 |      collections.abc.Iterable
 |      collections.abc.Container
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __call__(self)
 |      Return a list of the registered colormap names.
 |
 |      This exists only for backward-compatibility in `.pyplot` which had a
 |      ``plt.colormaps()`` method. The recommended way to get this list is
 |      now ``list(colormaps)``.
 |
 |  __getitem__(self, item)
 |
 |  __init__(self, cmaps)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __iter__(self)
 |
 |  __len__(self)
 |
 |  __str__(self)
 |      Return str(self).
 |
 |  get_cmap(self, cmap)
 |      Return a color map specified through *cmap*.
 |
 |      Parameters
 |      ----------
 |      cmap : str or `~matplotlib.colors.Colormap` or None
 |
 |          - if a `.Colormap`, return it
 |          - if a string, look it up in ``mpl.colormaps``
 |          - if None, return the Colormap defined in :rc:`image.cmap`
 |
 |      Returns
 |      -------
 |      Colormap
 |
 |  register(self, cmap, *, name=None, force=False)
 |      Register a new colormap.
 |
 |      The colormap name can then be used as a string argument to any ``cmap``
 |      parameter in Matplotlib. It is also available in ``pyplot.get_cmap``.
 |
 |      The colormap registry stores a copy of the given colormap, so that
 |      future changes to the original colormap instance do not affect the
 |      registered colormap. Think of this as the registry taking a snapshot
 |      of the colormap at registration.
 |
 |      Parameters
 |      ----------
 |      cmap : matplotlib.colors.Colormap
 |          The colormap to register.
 |
 |      name : str, optional
 |          The name for the colormap. If not given, ``cmap.name`` is used.
 |
 |      force : bool, default: False
 |          If False, a ValueError is raised if trying to overwrite an already
 |          registered name. True supports overwriting registered colormaps
 |          other than the builtin colormaps.
 |
 |  unregister(self, name)
 |      Remove a colormap from the registry.
 |
 |      You cannot remove built-in colormaps.
 |
 |      If the named colormap is not registered, returns with no error, raises
 |      if you try to de-register a default colormap.
 |
 |      .. warning::
 |
 |          Colormap names are currently a shared namespace that may be used
 |          by multiple packages. Use `unregister` only if you know you
 |          have registered that name before. In particular, do not
 |          unregister just in case to clean the name before registering a
 |          new colormap.
 |
 |      Parameters
 |      ----------
 |      name : str
 |          The name of the colormap to be removed.
 |
 |      Raises
 |      ------
 |      ValueError
 |          If you try to remove a default built-in colormap.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __abstractmethods__ = frozenset()
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from collections.abc.Mapping:
 |
 |  __contains__(self, key)
 |
 |  __eq__(self, other)
 |      Return self==value.
 |
 |  get(self, key, default=None)
 |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
 |
 |  items(self)
 |      D.items() -> a set-like object providing a view on D's items
 |
 |  keys(self)
 |      D.keys() -> a set-like object providing a view on D's keys
 |
 |  values(self)
 |      D.values() -> an object providing a view on D's values
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from collections.abc.Mapping:
 |
 |  __hash__ = None
 |
 |  __reversed__ = None
 |
 |  ----------------------------------------------------------------------
 |  Class methods inherited from collections.abc.Collection:
 |
 |  __subclasshook__(C) from abc.ABCMeta
 |      Abstract classes can override this to customize issubclass().
 |
 |      This is invoked early on by abc.ABCMeta.__subclasscheck__().
 |      It should return True, False or NotImplemented.  If it returns
 |      NotImplemented, the normal algorithm is used.  Otherwise, it
 |      overrides the normal algorithm (and the outcome is cached).
 |
 |  ----------------------------------------------------------------------
 |  Class methods inherited from collections.abc.Iterable:
 |
 |  __class_getitem__ = GenericAlias(...) from abc.ABCMeta
 |      Represent a PEP 585 generic type
 |
 |      E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).

None
&&&&&&&&&&&&&&&&&&&&&&& draw &&&&&&&&&&&&&&&&&&&&&&&&&
Help on function draw in module matplotlib.pyplot:

draw() -> 'None'
    Redraw the current figure.

    This is used to update a figure that has been altered, but not
    automatically re-drawn.  If interactive mode is on (via `.ion()`), this
    should be only rarely needed, but there may be ways to modify the state of
    a figure without marking it as "stale".  Please report these cases as bugs.

    This is equivalent to calling ``fig.canvas.draw_idle()``, where ``fig`` is
    the current figure.

    See Also
    --------
    .FigureCanvasBase.draw_idle
    .FigureCanvasBase.draw

None
&&&&&&&&&&&&&&&&&&&&&&& hist &&&&&&&&&&&&&&&&&&&&&&&&&
Help on function hist in module matplotlib.pyplot:

hist(x: 'ArrayLike | Sequence[ArrayLike]', bins: 'int | Sequence[float] | str | None' = None, *, range: 'tuple[float, float] | None' = None, density: 'bool' = False, weights: 'ArrayLike | None' = None, cumulative: 'bool | float' = False, bottom: 'ArrayLike | float | None' = None, histtype: "Literal['bar', 'barstacked', 'step', 'stepfilled']" = 'bar', align: "Literal['left', 'mid', 'right']" = 'mid', orientation: "Literal['vertical', 'horizontal']" = 'vertical', rwidth: 'float | None' = None, log: 'bool' = False, color: 'ColorType | Sequence[ColorType] | None' = None, label: 'str | Sequence[str] | None' = None, stacked: 'bool' = False, data: 'DataParamType' = None, **kwargs) -> 'tuple[np.ndarray | list[np.ndarray], np.ndarray, BarContainer | Polygon | list[BarContainer | Polygon]]'
    Compute and plot a histogram.

    This method uses `numpy.histogram` to bin the data in *x* and count the
    number of values in each bin, then draws the distribution either as a
    `.BarContainer` or `.Polygon`. The *bins*, *range*, *density*, and
    *weights* parameters are forwarded to `numpy.histogram`.

    If the data has already been binned and counted, use `~.bar` or
    `~.stairs` to plot the distribution::

        counts, bins = np.histogram(x)
        plt.stairs(counts, bins)

    Alternatively, plot pre-computed bins and counts using ``hist()`` by
    treating each bin as a single point with a weight equal to its count::

        plt.hist(bins[:-1], bins, weights=counts)

    The data input *x* can be a singular array, a list of datasets of
    potentially different lengths ([*x0*, *x1*, ...]), or a 2D ndarray in
    which each column is a dataset. Note that the ndarray form is
    transposed relative to the list form. If the input is an array, then
    the return value is a tuple (*n*, *bins*, *patches*); if the input is a
    sequence of arrays, then the return value is a tuple
    ([*n0*, *n1*, ...], *bins*, [*patches0*, *patches1*, ...]).

    Masked arrays are not supported.

    Parameters
    ----------
    x : (n,) array or sequence of (n,) arrays
        Input values, this takes either a single array or a sequence of
        arrays which are not required to be of the same length.

    bins : int or sequence or str, default: :rc:`hist.bins`
        If *bins* is an integer, it defines the number of equal-width bins
        in the range.

        If *bins* is a sequence, it defines the bin edges, including the
        left edge of the first bin and the right edge of the last bin;
        in this case, bins may be unequally spaced.  All but the last
        (righthand-most) bin is half-open.  In other words, if *bins* is::

            [1, 2, 3, 4]

        then the first bin is ``[1, 2)`` (including 1, but excluding 2) and
        the second ``[2, 3)``.  The last bin, however, is ``[3, 4]``, which
        *includes* 4.

        If *bins* is a string, it is one of the binning strategies
        supported by `numpy.histogram_bin_edges`: 'auto', 'fd', 'doane',
        'scott', 'stone', 'rice', 'sturges', or 'sqrt'.

    range : tuple or None, default: None
        The lower and upper range of the bins. Lower and upper outliers
        are ignored. If not provided, *range* is ``(x.min(), x.max())``.
        Range has no effect if *bins* is a sequence.

        If *bins* is a sequence or *range* is specified, autoscaling
        is based on the specified bin range instead of the
        range of x.

    density : bool, default: False
        If ``True``, draw and return a probability density: each bin
        will display the bin's raw count divided by the total number of
        counts *and the bin width*
        (``density = counts / (sum(counts) * np.diff(bins))``),
        so that the area under the histogram integrates to 1
        (``np.sum(density * np.diff(bins)) == 1``).

        If *stacked* is also ``True``, the sum of the histograms is
        normalized to 1.

    weights : (n,) array-like or None, default: None
        An array of weights, of the same shape as *x*.  Each value in
        *x* only contributes its associated weight towards the bin count
        (instead of 1).  If *density* is ``True``, the weights are
        normalized, so that the integral of the density over the range
        remains 1.

    cumulative : bool or -1, default: False
        If ``True``, then a histogram is computed where each bin gives the
        counts in that bin plus all bins for smaller values. The last bin
        gives the total number of datapoints.

        If *density* is also ``True`` then the histogram is normalized such
        that the last bin equals 1.

        If *cumulative* is a number less than 0 (e.g., -1), the direction
        of accumulation is reversed.  In this case, if *density* is also
        ``True``, then the histogram is normalized such that the first bin
        equals 1.

    bottom : array-like or float, default: 0
        Location of the bottom of each bin, i.e. bins are drawn from
        ``bottom`` to ``bottom + hist(x, bins)`` If a scalar, the bottom
        of each bin is shifted by the same amount. If an array, each bin
        is shifted independently and the length of bottom must match the
        number of bins. If None, defaults to 0.

    histtype : {'bar', 'barstacked', 'step', 'stepfilled'}, default: 'bar'
        The type of histogram to draw.

        - 'bar' is a traditional bar-type histogram.  If multiple data
          are given the bars are arranged side by side.
        - 'barstacked' is a bar-type histogram where multiple
          data are stacked on top of each other.
        - 'step' generates a lineplot that is by default unfilled.
        - 'stepfilled' generates a lineplot that is by default filled.

    align : {'left', 'mid', 'right'}, default: 'mid'
        The horizontal alignment of the histogram bars.

        - 'left': bars are centered on the left bin edges.
        - 'mid': bars are centered between the bin edges.
        - 'right': bars are centered on the right bin edges.

    orientation : {'vertical', 'horizontal'}, default: 'vertical'
        If 'horizontal', `~.Axes.barh` will be used for bar-type histograms
        and the *bottom* kwarg will be the left edges.

    rwidth : float or None, default: None
        The relative width of the bars as a fraction of the bin width.  If
        ``None``, automatically compute the width.

        Ignored if *histtype* is 'step' or 'stepfilled'.

    log : bool, default: False
        If ``True``, the histogram axis will be set to a log scale.

    color : :mpltype:`color` or list of :mpltype:`color` or None, default: None
        Color or sequence of colors, one per dataset.  Default (``None``)
        uses the standard line color sequence.

        .. versionadded:: 3.10
           It is now possible to use a single color with multiple datasets.

    label : str or list of str, optional
        String, or sequence of strings to match multiple datasets.  Bar
        charts yield multiple patches per dataset, but only the first gets
        the label, so that `~.Axes.legend` will work as expected.

    stacked : bool, default: False
        If ``True``, multiple data are stacked on top of each other If
        ``False`` multiple data are arranged side by side if histtype is
        'bar' or on top of each other if histtype is 'step'

    Returns
    -------
    n : array or list of arrays
        The values of the histogram bins. See *density* and *weights* for a
        description of the possible semantics.  If input *x* is an array,
        then this is an array of length *nbins*. If input is a sequence of
        arrays ``[data1, data2, ...]``, then this is a list of arrays with
        the values of the histograms for each of the arrays in the same
        order.  The dtype of the array *n* (or of its element arrays) will
        always be float even if no weighting or normalization is used.

    bins : array
        The edges of the bins. Length nbins + 1 (nbins left edges and right
        edge of last bin).  Always a single array even when multiple data
        sets are passed in.

    patches : `.BarContainer` or list of a single `.Polygon` or list of such objects
        Container of individual artists used to create the histogram
        or list of such containers if there are multiple input datasets.

    Other Parameters
    ----------------
    data : indexable object, optional
        If given, the following parameters also accept a string ``s``, which is
        interpreted as ``data[s]`` if ``s`` is a key in ``data``:

        *x*, *weights*

    **kwargs
        `~matplotlib.patches.Patch` properties. The following properties
        additionally accept a sequence of values corresponding to the
        datasets in *x*:
        *edgecolor*, *facecolor*, *linewidth*, *linestyle*, *hatch*.

        .. versionadded:: 3.10
           Allowing sequences of values in above listed Patch properties.

    See Also
    --------
    hist2d : 2D histogram with rectangular bins
    hexbin : 2D histogram with hexagonal bins
    stairs : Plot a pre-computed histogram
    bar : Plot a pre-computed histogram

    Notes
    -----

    .. note::

        This is the :ref:`pyplot wrapper <pyplot_interface>` for `.axes.Axes.hist`.

    For large numbers of bins (>1000), plotting can be significantly
    accelerated by using `~.Axes.stairs` to plot a pre-computed histogram
    (``plt.stairs(*np.histogram(data))``), or by setting *histtype* to
    'step' or 'stepfilled' rather than 'bar' or 'barstacked'.

None
&&&&&&&&&&&&&&&&&&&&&&& errorbar &&&&&&&&&&&&&&&&&&&&&&&&&
Help on function errorbar in module matplotlib.pyplot:

errorbar(x: 'float | ArrayLike', y: 'float | ArrayLike', yerr: 'float | ArrayLike | None' = None, xerr: 'float | ArrayLike | None' = None, fmt: 'str' = '', *, ecolor: 'ColorType | None' = None, elinewidth: 'float | None' = None, capsize: 'float | None' = None, barsabove: 'bool' = False, lolims: 'bool | ArrayLike' = False, uplims: 'bool | ArrayLike' = False, xlolims: 'bool | ArrayLike' = False, xuplims: 'bool | ArrayLike' = False, errorevery: 'int | tuple[int, int]' = 1, capthick: 'float | None' = None, elinestyle: 'LineStyleType | None' = None, data: 'DataParamType' = None, **kwargs) -> 'ErrorbarContainer'
    Plot y versus x as lines and/or markers with attached errorbars.

    *x*, *y* define the data locations, *xerr*, *yerr* define the errorbar
    sizes. By default, this draws the data markers/lines as well as the
    errorbars. Use fmt='none' to draw errorbars without any data markers.

    .. versionadded:: 3.7
       Caps and error lines are drawn in polar coordinates on polar plots.


    Parameters
    ----------
    x, y : float or array-like
        The data positions.

    xerr, yerr : float or array-like, shape(N,) or shape(2, N), optional
        The errorbar sizes:

        - scalar: Symmetric +/- values for all data points.
        - shape(N,): Symmetric +/-values for each data point.
        - shape(2, N): Separate - and + values for each bar. First row
          contains the lower errors, the second row contains the upper
          errors.
        - *None*: No errorbar.

        All values must be >= 0.

        See :doc:`/gallery/statistics/errorbar_features`
        for an example on the usage of ``xerr`` and ``yerr``.

    fmt : str, default: ''
        The format for the data points / data lines. See `.plot` for
        details.

        Use 'none' (case-insensitive) to plot errorbars without any data
        markers.

    ecolor : :mpltype:`color`, default: None
        The color of the errorbar lines.  If None, use the color of the
        line connecting the markers.

    elinewidth : float, default: None
        The linewidth of the errorbar lines. If None, the linewidth of
        the current style is used.

    elinestyle : str or tuple, default: 'solid'
       The linestyle of the errorbar lines.
       Valid values for linestyles include {'-', '--', '-.',
        ':', '', (offset, on-off-seq)}. See `.Line2D.set_linestyle` for a
        complete description.

    capsize : float, default: :rc:`errorbar.capsize`
        The length of the error bar caps in points.

    capthick : float, default: None
        An alias to the keyword argument *markeredgewidth* (a.k.a. *mew*).
        This setting is a more sensible name for the property that
        controls the thickness of the error bar cap in points. For
        backwards compatibility, if *mew* or *markeredgewidth* are given,
        then they will over-ride *capthick*. This may change in future
        releases.

    barsabove : bool, default: False
        If True, will plot the errorbars above the plot
        symbols. Default is below.

    lolims, uplims, xlolims, xuplims : bool or array-like, default: False
        These arguments can be used to indicate that a value gives only
        upper/lower limits.  In that case a caret symbol is used to
        indicate this. *lims*-arguments may be scalars, or array-likes of
        the same length as *xerr* and *yerr*.  To use limits with inverted
        axes, `~.Axes.set_xlim` or `~.Axes.set_ylim` must be called before
        :meth:`errorbar`.  Note the tricky parameter names: setting e.g.
        *lolims* to True means that the y-value is a *lower* limit of the
        True value, so, only an *upward*-pointing arrow will be drawn!

    errorevery : int or (int, int), default: 1
        draws error bars on a subset of the data. *errorevery* =N draws
        error bars on the points (x[::N], y[::N]).
        *errorevery* =(start, N) draws error bars on the points
        (x[start::N], y[start::N]). e.g. errorevery=(6, 3)
        adds error bars to the data at (x[6], x[9], x[12], x[15], ...).
        Used to avoid overlapping error bars when two series share x-axis
        values.

    Returns
    -------
    `.ErrorbarContainer`
        The container contains:

        - data_line : A `~matplotlib.lines.Line2D` instance of x, y plot markers
          and/or line.
        - caplines : A tuple of `~matplotlib.lines.Line2D` instances of the error
          bar caps.
        - barlinecols : A tuple of `.LineCollection` with the horizontal and
          vertical error ranges.

    Other Parameters
    ----------------
    data : indexable object, optional
        If given, the following parameters also accept a string ``s``, which is
        interpreted as ``data[s]`` if ``s`` is a key in ``data``:

        *x*, *y*, *xerr*, *yerr*

    **kwargs
        All other keyword arguments are passed on to the `~.Axes.plot` call
        drawing the markers. For example, this code makes big red squares
        with thick green edges::

            x, y, yerr = rand(3, 10)
            errorbar(x, y, yerr, marker='s', mfc='red',
                     mec='green', ms=20, mew=4)

        where *mfc*, *mec*, *ms* and *mew* are aliases for the longer
        property names, *markerfacecolor*, *markeredgecolor*, *markersize*
        and *markeredgewidth*.

        Valid kwargs for the marker properties are:

        - *dashes*
        - *dash_capstyle*
        - *dash_joinstyle*
        - *drawstyle*
        - *fillstyle*
        - *linestyle*
        - *marker*
        - *markeredgecolor*
        - *markeredgewidth*
        - *markerfacecolor*
        - *markerfacecoloralt*
        - *markersize*
        - *markevery*
        - *solid_capstyle*
        - *solid_joinstyle*

        Refer to the corresponding `.Line2D` property for more details:

        Properties:
        agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image
        alpha: float or None
        animated: bool
        antialiased or aa: bool
        clip_box: `~matplotlib.transforms.BboxBase` or None
        clip_on: bool
        clip_path: Patch or (Path, Transform) or None
        color or c: :mpltype:`color`
        dash_capstyle: `.CapStyle` or {'butt', 'projecting', 'round'}
        dash_joinstyle: `.JoinStyle` or {'miter', 'round', 'bevel'}
        dashes: sequence of floats (on/off ink in points) or (None, None)
        data: (2, N) array or two 1D arrays
        drawstyle or ds: {'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'}, default: 'default'
        figure: `~matplotlib.figure.Figure` or `~matplotlib.figure.SubFigure`
        fillstyle: {'full', 'left', 'right', 'bottom', 'top', 'none'}
        gapcolor: :mpltype:`color` or None
        gid: str
        in_layout: bool
        label: object
        linestyle or ls: {'-', '--', '-.', ':', '', ...} or (offset, on-off-seq)
        linewidth or lw: float
        marker: marker style string, `~.path.Path` or `~.markers.MarkerStyle`
        markeredgecolor or mec: :mpltype:`color`
        markeredgewidth or mew: float
        markerfacecolor or mfc: :mpltype:`color`
        markerfacecoloralt or mfcalt: :mpltype:`color`
        markersize or ms: float
        markevery: None or int or (int, int) or slice or list[int] or float or (float, float) or list[bool]
        mouseover: bool
        path_effects: list of `.AbstractPathEffect`
        picker: float or callable[[Artist, Event], tuple[bool, dict]]
        pickradius: float
        rasterized: bool
        sketch_params: (scale: float, length: float, randomness: float)
        snap: bool or None
        solid_capstyle: `.CapStyle` or {'butt', 'projecting', 'round'}
        solid_joinstyle: `.JoinStyle` or {'miter', 'round', 'bevel'}
        transform: unknown
        url: str
        visible: bool
        xdata: 1D array
        ydata: 1D array
        zorder: float

    Notes
    -----

    .. note::

        This is the :ref:`pyplot wrapper <pyplot_interface>` for `.axes.Axes.errorbar`.

None
&&&&&&&&&&&&&&&&&&&&&&& imsave &&&&&&&&&&&&&&&&&&&&&&&&&
Help on function imsave in module matplotlib.pyplot:

imsave(fname: 'str | os.PathLike | BinaryIO', arr: 'ArrayLike', **kwargs) -> 'None'
    Colormap and save an array as an image file.

    RGB(A) images are passed through.  Single channel images will be
    colormapped according to *cmap* and *norm*.

    .. note::

       If you want to save a single channel image as gray scale please use an
       image I/O library (such as pillow, tifffile, or imageio) directly.

    Parameters
    ----------
    fname : str or path-like or file-like
        A path or a file-like object to store the image in.
        If *format* is not set, then the output format is inferred from the
        extension of *fname*, if any, and from :rc:`savefig.format` otherwise.
        If *format* is set, it determines the output format.
    arr : array-like
        The image data. Accepts NumPy arrays or sequences
        (e.g., lists or tuples). The shape can be one of
        MxN (luminance), MxNx3 (RGB) or MxNx4 (RGBA).
    vmin, vmax : float, optional
        *vmin* and *vmax* set the color scaling for the image by fixing the
        values that map to the colormap color limits. If either *vmin*
        or *vmax* is None, that limit is determined from the *arr*
        min/max value.
    cmap : str or `~matplotlib.colors.Colormap`, default: :rc:`image.cmap`
        A Colormap instance or registered colormap name. The colormap
        maps scalar data to colors. It is ignored for RGB(A) data.
    format : str, optional
        The file format, e.g. 'png', 'pdf', 'svg', ...  The behavior when this
        is unset is documented under *fname*.
    origin : {'upper', 'lower'}, default: :rc:`image.origin`
        Indicates whether the ``(0, 0)`` index of the array is in the upper
        left or lower left corner of the Axes.
    dpi : float
        The DPI to store in the metadata of the file.  This does not affect the
        resolution of the output image.  Depending on file format, this may be
        rounded to the nearest integer.
    metadata : dict, optional
        Metadata in the image file.  The supported keys depend on the output
        format, see the documentation of the respective backends for more
        information.
        Currently only supported for "png", "pdf", "ps", "eps", and "svg".
    pil_kwargs : dict, optional
        Keyword arguments passed to `PIL.Image.Image.save`.  If the 'pnginfo'
        key is present, it completely overrides *metadata*, including the
        default 'Software' key.

    Notes
    -----

    .. note::

        This is equivalent to `matplotlib.image.imsave`.

None
&&&&&&&&&&&&&&&&&&&&&&& stem &&&&&&&&&&&&&&&&&&&&&&&&&
Help on function stem in module matplotlib.pyplot:

stem(*args: 'ArrayLike | str', linefmt: 'str | None' = None, markerfmt: 'str | None' = None, basefmt: 'str | None' = None, bottom: 'float' = 0, label: 'str | None' = None, orientation: "Literal['vertical', 'horizontal']" = 'vertical', data: 'DataParamType' = None) -> 'StemContainer'
    Create a stem plot.

    A stem plot draws lines perpendicular to a baseline at each location
    *locs* from the baseline to *heads*, and places a marker there. For
    vertical stem plots (the default), the *locs* are *x* positions, and
    the *heads* are *y* values. For horizontal stem plots, the *locs* are
    *y* positions, and the *heads* are *x* values.

    Call signature::

      stem([locs,] heads, linefmt=None, markerfmt=None, basefmt=None)

    The *locs*-positions are optional. *linefmt* may be provided as
    positional, but all other formats must be provided as keyword
    arguments.

    Parameters
    ----------
    locs : array-like, default: (0, 1, ..., len(heads) - 1)
        For vertical stem plots, the x-positions of the stems.
        For horizontal stem plots, the y-positions of the stems.

    heads : array-like
        For vertical stem plots, the y-values of the stem heads.
        For horizontal stem plots, the x-values of the stem heads.

    linefmt : str, optional
        A string defining the color and/or linestyle of the vertical lines:

        =========  =============
        Character  Line Style
        =========  =============
        ``'-'``    solid line
        ``'--'``   dashed line
        ``'-.'``   dash-dot line
        ``':'``    dotted line
        =========  =============

        Default: 'C0-', i.e. solid line with the first color of the color
        cycle.

        Note: Markers specified through this parameter (e.g. 'x') will be
        silently ignored. Instead, markers should be specified using
        *markerfmt*.

    markerfmt : str, optional
        A string defining the color and/or shape of the markers at the stem
        heads. If the marker is not given, use the marker 'o', i.e. filled
        circles. If the color is not given, use the color from *linefmt*.

    basefmt : str, default: 'C3-' ('C2-' in classic mode)
        A format string defining the properties of the baseline.

    orientation : {'vertical', 'horizontal'}, default: 'vertical'
        The orientation of the stems.

    bottom : float, default: 0
        The y/x-position of the baseline (depending on *orientation*).

    label : str, optional
        The label to use for the stems in legends.

    data : indexable object, optional
        If given, all parameters also accept a string ``s``, which is
        interpreted as ``data[s]`` if ``s`` is a key in ``data``.

    Returns
    -------
    `.StemContainer`
        The container may be treated like a tuple
        (*markerline*, *stemlines*, *baseline*)

    Notes
    -----

    .. note::

        This is the :ref:`pyplot wrapper <pyplot_interface>` for `.axes.Axes.stem`.

    .. seealso::
        The MATLAB function
        `stem <https://www.mathworks.com/help/matlab/ref/stem.html>`_
        which inspired this method.

None
&&&&&&&&&&&&&&&&&&&&&&& plot &&&&&&&&&&&&&&&&&&&&&&&&&
Help on function plot in module matplotlib.pyplot:

plot(*args: 'float | ArrayLike | str', scalex: 'bool' = True, scaley: 'bool' = True, data: 'DataParamType' = None, **kwargs) -> 'list[Line2D]'
    Plot y versus x as lines and/or markers.

    Call signatures::

        plot([x], y, [fmt], *, data=None, **kwargs)
        plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)

    The coordinates of the points or line nodes are given by *x*, *y*.

    The optional parameter *fmt* is a convenient way for defining basic
    formatting like color, marker and linestyle. It's a shortcut string
    notation described in the *Notes* section below.

    >>> plot(x, y)        # plot x and y using default line style and color
    >>> plot(x, y, 'bo')  # plot x and y using blue circle markers
    >>> plot(y)           # plot y using x as index array 0..N-1
    >>> plot(y, 'r+')     # ditto, but with red plusses

    You can use `.Line2D` properties as keyword arguments for more
    control on the appearance. Line properties and *fmt* can be mixed.
    The following two calls yield identical results:

    >>> plot(x, y, 'go--', linewidth=2, markersize=12)
    >>> plot(x, y, color='green', marker='o', linestyle='dashed',
    ...      linewidth=2, markersize=12)

    When conflicting with *fmt*, keyword arguments take precedence.


    **Plotting labelled data**

    There's a convenient way for plotting objects with labelled data (i.e.
    data that can be accessed by index ``obj['y']``). Instead of giving
    the data in *x* and *y*, you can provide the object in the *data*
    parameter and just give the labels for *x* and *y*::

    >>> plot('xlabel', 'ylabel', data=obj)

    All indexable objects are supported. This could e.g. be a `dict`, a
    `pandas.DataFrame` or a structured numpy array.


    **Plotting multiple sets of data**

    There are various ways to plot multiple sets of data.

    - The most straight forward way is just to call `plot` multiple times.
      Example:

      >>> plot(x1, y1, 'bo')
      >>> plot(x2, y2, 'go')

    - If *x* and/or *y* are 2D arrays, a separate data set will be drawn
      for every column. If both *x* and *y* are 2D, they must have the
      same shape. If only one of them is 2D with shape (N, m) the other
      must have length N and will be used for every data set m.

      Example:

      >>> x = [1, 2, 3]
      >>> y = np.array([[1, 2], [3, 4], [5, 6]])
      >>> plot(x, y)

      is equivalent to:

      >>> for col in range(y.shape[1]):
      ...     plot(x, y[:, col])

    - The third way is to specify multiple sets of *[x]*, *y*, *[fmt]*
      groups::

      >>> plot(x1, y1, 'g^', x2, y2, 'g-')

      In this case, any additional keyword argument applies to all
      datasets. Also, this syntax cannot be combined with the *data*
      parameter.

    By default, each line is assigned a different style specified by a
    'style cycle'. The *fmt* and line property parameters are only
    necessary if you want explicit deviations from these defaults.
    Alternatively, you can also change the style cycle using
    :rc:`axes.prop_cycle`.


    Parameters
    ----------
    x, y : array-like or float
        The horizontal / vertical coordinates of the data points.
        *x* values are optional and default to ``range(len(y))``.

        Commonly, these parameters are 1D arrays.

        They can also be scalars, or two-dimensional (in that case, the
        columns represent separate data sets).

        These arguments cannot be passed as keywords.

    fmt : str, optional
        A format string, e.g. 'ro' for red circles. See the *Notes*
        section for a full description of the format strings.

        Format strings are just an abbreviation for quickly setting
        basic line properties. All of these and more can also be
        controlled by keyword arguments.

        This argument cannot be passed as keyword.

    data : indexable object, optional
        An object with labelled data. If given, provide the label names to
        plot in *x* and *y*.

        .. note::
            Technically there's a slight ambiguity in calls where the
            second label is a valid *fmt*. ``plot('n', 'o', data=obj)``
            could be ``plt(x, y)`` or ``plt(y, fmt)``. In such cases,
            the former interpretation is chosen, but a warning is issued.
            You may suppress the warning by adding an empty format string
            ``plot('n', 'o', '', data=obj)``.

    Returns
    -------
    list of `.Line2D`
        A list of lines representing the plotted data.

    Other Parameters
    ----------------
    scalex, scaley : bool, default: True
        These parameters determine if the view limits are adapted to the
        data limits. The values are passed on to
        `~.axes.Axes.autoscale_view`.

    **kwargs : `~matplotlib.lines.Line2D` properties, optional
        *kwargs* are used to specify properties like a line label (for
        auto legends), linewidth, antialiasing, marker face color.
        Example::

        >>> plot([1, 2, 3], [1, 2, 3], 'go-', label='line 1', linewidth=2)
        >>> plot([1, 2, 3], [1, 4, 9], 'rs', label='line 2')

        If you specify multiple lines with one plot call, the kwargs apply
        to all those lines. In case the label object is iterable, each
        element is used as labels for each set of data.

        Here is a list of available `.Line2D` properties:

        Properties:
        agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image
        alpha: float or None
        animated: bool
        antialiased or aa: bool
        clip_box: `~matplotlib.transforms.BboxBase` or None
        clip_on: bool
        clip_path: Patch or (Path, Transform) or None
        color or c: :mpltype:`color`
        dash_capstyle: `.CapStyle` or {'butt', 'projecting', 'round'}
        dash_joinstyle: `.JoinStyle` or {'miter', 'round', 'bevel'}
        dashes: sequence of floats (on/off ink in points) or (None, None)
        data: (2, N) array or two 1D arrays
        drawstyle or ds: {'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'}, default: 'default'
        figure: `~matplotlib.figure.Figure` or `~matplotlib.figure.SubFigure`
        fillstyle: {'full', 'left', 'right', 'bottom', 'top', 'none'}
        gapcolor: :mpltype:`color` or None
        gid: str
        in_layout: bool
        label: object
        linestyle or ls: {'-', '--', '-.', ':', '', ...} or (offset, on-off-seq)
        linewidth or lw: float
        marker: marker style string, `~.path.Path` or `~.markers.MarkerStyle`
        markeredgecolor or mec: :mpltype:`color`
        markeredgewidth or mew: float
        markerfacecolor or mfc: :mpltype:`color`
        markerfacecoloralt or mfcalt: :mpltype:`color`
        markersize or ms: float
        markevery: None or int or (int, int) or slice or list[int] or float or (float, float) or list[bool]
        mouseover: bool
        path_effects: list of `.AbstractPathEffect`
        picker: float or callable[[Artist, Event], tuple[bool, dict]]
        pickradius: float
        rasterized: bool
        sketch_params: (scale: float, length: float, randomness: float)
        snap: bool or None
        solid_capstyle: `.CapStyle` or {'butt', 'projecting', 'round'}
        solid_joinstyle: `.JoinStyle` or {'miter', 'round', 'bevel'}
        transform: unknown
        url: str
        visible: bool
        xdata: 1D array
        ydata: 1D array
        zorder: float

    See Also
    --------
    scatter : XY scatter plot with markers of varying size and/or color (
        sometimes also called bubble chart).

    Notes
    -----

    .. note::

        This is the :ref:`pyplot wrapper <pyplot_interface>` for `.axes.Axes.plot`.

    **Format Strings**

    A format string consists of a part for color, marker and line::

        fmt = '[marker][line][color]'

    Each of them is optional. If not provided, the value from the style
    cycle is used. Exception: If ``line`` is given, but no ``marker``,
    the data will be a line without markers.

    Other combinations such as ``[color][marker][line]`` are also
    supported, but note that their parsing may be ambiguous.

    **Markers**

    =============   ===============================
    character       description
    =============   ===============================
    ``'.'``         point marker
    ``','``         pixel marker
    ``'o'``         circle marker
    ``'v'``         triangle_down marker
    ``'^'``         triangle_up marker
    ``'<'``         triangle_left marker
    ``'>'``         triangle_right marker
    ``'1'``         tri_down marker
    ``'2'``         tri_up marker
    ``'3'``         tri_left marker
    ``'4'``         tri_right marker
    ``'8'``         octagon marker
    ``'s'``         square marker
    ``'p'``         pentagon marker
    ``'P'``         plus (filled) marker
    ``'*'``         star marker
    ``'h'``         hexagon1 marker
    ``'H'``         hexagon2 marker
    ``'+'``         plus marker
    ``'x'``         x marker
    ``'X'``         x (filled) marker
    ``'D'``         diamond marker
    ``'d'``         thin_diamond marker
    ``'|'``         vline marker
    ``'_'``         hline marker
    =============   ===============================

    **Line Styles**

    =============    ===============================
    character        description
    =============    ===============================
    ``'-'``          solid line style
    ``'--'``         dashed line style
    ``'-.'``         dash-dot line style
    ``':'``          dotted line style
    =============    ===============================

    Example format strings::

        'b'    # blue markers with default shape
        'or'   # red circles
        '-g'   # green solid line
        '--'   # dashed line with default color
        '^k:'  # black triangle_up markers connected by a dotted line

    **Colors**

    The supported color abbreviations are the single letter codes

    =============    ===============================
    character        color
    =============    ===============================
    ``'b'``          blue
    ``'g'``          green
    ``'r'``          red
    ``'c'``          cyan
    ``'m'``          magenta
    ``'y'``          yellow
    ``'k'``          black
    ``'w'``          white
    =============    ===============================

    and the ``'CN'`` colors that index into the default property cycle.

    If the color is the only part of the format string, you can
    additionally use any  `matplotlib.colors` spec, e.g. full names
    (``'green'``) or hex strings (``'#008000'``).

None
&&&&&&&&&&&&&&&&&&&&&&& boxplot &&&&&&&&&&&&&&&&&&&&&&&&&
Help on function boxplot in module matplotlib.pyplot:

boxplot(x: 'ArrayLike | Sequence[ArrayLike]', *, notch: 'bool | None' = None, sym: 'str | None' = None, vert: 'bool | None' = None, orientation: "Literal['vertical', 'horizontal']" = 'vertical', whis: 'float | tuple[float, float] | None' = None, positions: 'ArrayLike | None' = None, widths: 'float | ArrayLike | None' = None, patch_artist: 'bool | None' = None, bootstrap: 'int | None' = None, usermedians: 'ArrayLike | None' = None, conf_intervals: 'ArrayLike | None' = None, meanline: 'bool | None' = None, showmeans: 'bool | None' = None, showcaps: 'bool | None' = None, showbox: 'bool | None' = None, showfliers: 'bool | None' = None, boxprops: 'dict[str, Any] | None' = None, tick_labels: 'Sequence[str] | None' = None, flierprops: 'dict[str, Any] | None' = None, medianprops: 'dict[str, Any] | None' = None, meanprops: 'dict[str, Any] | None' = None, capprops: 'dict[str, Any] | None' = None, whiskerprops: 'dict[str, Any] | None' = None, manage_ticks: 'bool' = True, autorange: 'bool' = False, zorder: 'float | None' = None, capwidths: 'float | ArrayLike | None' = None, label: 'Sequence[str] | None' = None, data: 'DataParamType' = None) -> 'dict[str, Any]'
    Draw a box and whisker plot.

    The box extends from the first quartile (Q1) to the third
    quartile (Q3) of the data, with a line at the median.
    The whiskers extend from the box to the farthest data point
    lying within 1.5x the inter-quartile range (IQR) from the box.
    Flier points are those past the end of the whiskers.
    See https://en.wikipedia.org/wiki/Box_plot for reference.

    .. code-block:: none

              Q1-1.5IQR   Q1   median  Q3   Q3+1.5IQR
                           |-----:-----|
           o      |--------|     :     |--------|    o  o
                           |-----:-----|
         flier             <----------->            fliers
                                IQR


    Parameters
    ----------
    x : 1D array or sequence of 1D arrays or 2D array
        The input data. Possible values:

        - 1D array: A single box is drawn.
        - sequence of 1D arrays: A box is drawn for each array in the sequence.
        - 2D array: A box is drawn for each column in the array.

    notch : bool, default: :rc:`boxplot.notch`
        Whether to draw a notched boxplot (`True`), or a rectangular
        boxplot (`False`).  The notches represent the confidence interval
        (CI) around the median.  The documentation for *bootstrap*
        describes how the locations of the notches are computed by
        default, but their locations may also be overridden by setting the
        *conf_intervals* parameter.

        .. note::

            In cases where the values of the CI are less than the
            lower quartile or greater than the upper quartile, the
            notches will extend beyond the box, giving it a
            distinctive "flipped" appearance. This is expected
            behavior and consistent with other statistical
            visualization packages.

    sym : str, optional
        The default symbol for flier points.  An empty string ('') hides
        the fliers.  If `None`, then the fliers default to 'b+'.  More
        control is provided by the *flierprops* parameter.

    vert : bool, optional
        .. deprecated:: 3.11
            Use *orientation* instead.

            If this is given during the deprecation period, it overrides
            the *orientation* parameter.

        If True, plots the boxes vertically.
        If False, plots the boxes horizontally.

    orientation : {'vertical', 'horizontal'}, default: 'vertical'
        If 'horizontal', plots the boxes horizontally.
        Otherwise, plots the boxes vertically.

        .. versionadded:: 3.10

    whis : float or (float, float), default: 1.5
        The position of the whiskers.

        If a float, the lower whisker is at the lowest datum above
        ``Q1 - whis*(Q3-Q1)``, and the upper whisker at the highest datum
        below ``Q3 + whis*(Q3-Q1)``, where Q1 and Q3 are the first and
        third quartiles.  The default value of ``whis = 1.5`` corresponds
        to Tukey's original definition of boxplots.

        If a pair of floats, they indicate the percentiles at which to
        draw the whiskers (e.g., (5, 95)).  In particular, setting this to
        (0, 100) results in whiskers covering the whole range of the data.

        In the edge case where ``Q1 == Q3``, *whis* is automatically set
        to (0, 100) (cover the whole range of the data) if *autorange* is
        True.

        Beyond the whiskers, data are considered outliers and are plotted
        as individual points.

    bootstrap : int, optional
        Specifies whether to bootstrap the confidence intervals
        around the median for notched boxplots. If *bootstrap* is
        None, no bootstrapping is performed, and notches are
        calculated using a Gaussian-based asymptotic approximation
        (see McGill, R., Tukey, J.W., and Larsen, W.A., 1978, and
        Kendall and Stuart, 1967). Otherwise, bootstrap specifies
        the number of times to bootstrap the median to determine its
        95% confidence intervals. Values between 1000 and 10000 are
        recommended.

    usermedians : 1D array-like, optional
        A 1D array-like of length ``len(x)``.  Each entry that is not
        `None` forces the value of the median for the corresponding
        dataset.  For entries that are `None`, the medians are computed
        by Matplotlib as normal.

    conf_intervals : array-like, optional
        A 2D array-like of shape ``(len(x), 2)``.  Each entry that is not
        None forces the location of the corresponding notch (which is
        only drawn if *notch* is `True`).  For entries that are `None`,
        the notches are computed by the method specified by the other
        parameters (e.g., *bootstrap*).

    positions : array-like, optional
        The positions of the boxes. The ticks and limits are
        automatically set to match the positions. Defaults to
        ``range(1, N+1)`` where N is the number of boxes to be drawn.

    widths : float or array-like
        The widths of the boxes.  The default is 0.5, or ``0.15*(distance
        between extreme positions)``, if that is smaller.

    patch_artist : bool, default: :rc:`boxplot.patchartist`
        If `False` produces boxes with the Line2D artist. Otherwise,
        boxes are drawn with Patch artists.

    tick_labels : list of str, optional
        The tick labels of each boxplot.
        Ticks are always placed at the box *positions*. If *tick_labels* is given,
        the ticks are labelled accordingly. Otherwise, they keep their numeric
        values.

        .. versionchanged:: 3.9
            Renamed from *labels*, which is also removed in 3.11.

    manage_ticks : bool, default: True
        If True, the tick locations and labels will be adjusted to match
        the boxplot positions.

    autorange : bool, default: False
        When `True` and the data are distributed such that the 25th and
        75th percentiles are equal, *whis* is set to (0, 100) such
        that the whisker ends are at the minimum and maximum of the data.

    meanline : bool, default: :rc:`boxplot.meanline`
        If `True` (and *showmeans* is `True`), will try to render the
        mean as a line spanning the full width of the box according to
        *meanprops* (see below).  Not recommended if *shownotches* is also
        True.  Otherwise, means will be shown as points.

    zorder : float, default: ``Line2D.zorder = 2``
        The zorder of the boxplot.

    Returns
    -------
    dict
      A dictionary mapping each component of the boxplot to a list
      of the `.Line2D` instances created. That dictionary has the
      following keys (assuming vertical boxplots):

      - ``boxes``: the main body of the boxplot showing the
        quartiles and the median's confidence intervals if
        enabled.

      - ``medians``: horizontal lines at the median of each box.

      - ``whiskers``: the vertical lines extending to the most
        extreme, non-outlier data points.

      - ``caps``: the horizontal lines at the ends of the
        whiskers.

      - ``fliers``: points representing data that extend beyond
        the whiskers (fliers).

      - ``means``: points or lines representing the means.

    Other Parameters
    ----------------
    showcaps : bool, default: :rc:`boxplot.showcaps`
        Show the caps on the ends of whiskers.
    showbox : bool, default: :rc:`boxplot.showbox`
        Show the central box.
    showfliers : bool, default: :rc:`boxplot.showfliers`
        Show the outliers beyond the caps.
    showmeans : bool, default: :rc:`boxplot.showmeans`
        Show the arithmetic means.
    capprops : dict, default: None
        The style of the caps.
    capwidths : float or array, default: None
        The widths of the caps.
    boxprops : dict, default: None
        The style of the box.
    whiskerprops : dict, default: None
        The style of the whiskers.
    flierprops : dict, default: None
        The style of the fliers.
    medianprops : dict, default: None
        The style of the median.
    meanprops : dict, default: None
        The style of the mean.
    label : str or list of str, optional
        Legend labels. Use a single string when all boxes have the same style and
        you only want a single legend entry for them. Use a list of strings to
        label all boxes individually. To be distinguishable, the boxes should be
        styled individually, which is currently only possible by modifying the
        returned artists, see e.g. :doc:`/gallery/statistics/boxplot_demo`.

        In the case of a single string, the legend entry will technically be
        associated with the first box only. By default, the legend will show the
        median line (``result["medians"]``); if *patch_artist* is True, the legend
        will show the box `.Patch` artists (``result["boxes"]``) instead.

        .. versionadded:: 3.9

    data : indexable object, optional
        If given, all parameters also accept a string ``s``, which is
        interpreted as ``data[s]`` if ``s`` is a key in ``data``.

    See Also
    --------
    .Axes.bxp : Draw a boxplot from pre-computed statistics.
    violinplot : Draw an estimate of the probability density function.

    Notes
    -----

    .. note::

        This is the :ref:`pyplot wrapper <pyplot_interface>` for `.axes.Axes.boxplot`.

None
&&&&&&&&&&&&&&&&&&&&&&& imread &&&&&&&&&&&&&&&&&&&&&&&&&
Help on function imread in module matplotlib.pyplot:

imread(fname: 'str | pathlib.Path | BinaryIO', format: 'str | None' = None) -> 'np.ndarray'
    Read an image from a file into an array.

    .. note::

        This function exists for historical reasons.  It is recommended to
        use `PIL.Image.open` instead for loading images.

    Parameters
    ----------
    fname : str or file-like
        The image file to read: a filename, a URL or a file-like object opened
        in read-binary mode.

        Passing a URL is deprecated.  Please open the URL
        for reading and pass the result to Pillow, e.g. with
        ``np.array(PIL.Image.open(urllib.request.urlopen(url)))``.
    format : str, optional
        The image file format assumed for reading the data.  The image is
        loaded as a PNG file if *format* is set to "png", if *fname* is a path
        or opened file with a ".png" extension, or if it is a URL.  In all
        other cases, *format* is ignored and the format is auto-detected by
        `PIL.Image.open`.

    Returns
    -------
    `numpy.array`
        The image data. The returned array has shape

        - (M, N) for grayscale images.
        - (M, N, 3) for RGB images.
        - (M, N, 4) for RGBA images.

        PNG images are returned as float arrays (0-1).  All other formats are
        returned as int arrays, with a bit depth determined by the file's
        contents.

    Notes
    -----

    .. note::

        This is equivalent to `matplotlib.image.imread`.

None
&&&&&&&&&&&&&&&&&&&&&&& imshow &&&&&&&&&&&&&&&&&&&&&&&&&
Help on function imshow in module matplotlib.pyplot:

imshow(X: 'ArrayLike | PIL.Image.Image', cmap: 'str | Colormap | None' = None, norm: 'str | Normalize | None' = None, *, aspect: "Literal['equal', 'auto'] | float | None" = None, interpolation: 'str | None' = None, alpha: 'float | ArrayLike | None' = None, vmin: 'float | None' = None, vmax: 'float | None' = None, colorizer: 'Colorizer | None' = None, origin: "Literal['upper', 'lower'] | None" = None, extent: 'tuple[float, float, float, float] | None' = None, interpolation_stage: "Literal['data', 'rgba', 'auto'] | None" = None, filternorm: 'bool' = True, filterrad: 'float' = 4.0, resample: 'bool | None' = None, url: 'str | None' = None, data: 'DataParamType' = None, **kwargs) -> 'AxesImage'
    Display data as an image, i.e., on a 2D regular raster.

    The input may either be actual RGB(A) data, or 2D scalar data, which
    will be rendered as a pseudocolor image. For displaying a grayscale
    image, set up the colormapping using the parameters
    ``cmap='gray', vmin=0, vmax=255``.

    The number of pixels used to render an image is set by the Axes size
    and the figure *dpi*. This can lead to aliasing artifacts when
    the image is resampled, because the displayed image size will usually
    not match the size of *X* (see
    :doc:`/gallery/images_contours_and_fields/image_antialiasing`).
    The resampling can be controlled via the *interpolation* parameter
    and/or :rc:`image.interpolation`.

    Parameters
    ----------
    X : array-like or PIL image
        The image data. Supported array shapes are:

        - (M, N): an image with scalar data. The values are mapped to
          colors using normalization and a colormap. See parameters *norm*,
          *cmap*, *vmin*, *vmax*.
        - (M, N, 3): an image with RGB values (0-1 float or 0-255 int).
        - (M, N, 4): an image with RGBA values (0-1 float or 0-255 int),
          i.e. including transparency.

        The first two dimensions (M, N) define the rows and columns of
        the image.

        Out-of-range RGB(A) values are clipped.

    cmap : str or `~matplotlib.colors.Colormap`, default: :rc:`image.cmap`
        The Colormap instance or registered colormap name used to map scalar data
        to colors.

        This parameter is ignored if *X* is RGB(A).

    norm : str or `~matplotlib.colors.Normalize`, optional
        The normalization method used to scale scalar data to the [0, 1] range
        before mapping to colors using *cmap*. By default, a linear scaling is
        used, mapping the lowest value to 0 and the highest to 1.

        If given, this can be one of the following:

        - An instance of `.Normalize` or one of its subclasses
          (see :ref:`colormapnorms`).
        - A scale name, i.e. one of "linear", "log", "symlog", "logit", etc.  For a
          list of available scales, call `matplotlib.scale.get_scale_names()`.
          In that case, a suitable `.Normalize` subclass is dynamically generated
          and instantiated.

        This parameter is ignored if *X* is RGB(A).

    vmin, vmax : float, optional
        When using scalar data and no explicit *norm*, *vmin* and *vmax* define
        the data range that the colormap covers. By default, the colormap covers
        the complete value range of the supplied data. It is an error to use
        *vmin*/*vmax* when a *norm* instance is given (but using a `str` *norm*
        name together with *vmin*/*vmax* is acceptable).

        This parameter is ignored if *X* is RGB(A).

    colorizer : `~matplotlib.colorizer.Colorizer` or None, default: None
        The Colorizer object used to map color to data. If None, a Colorizer
        object is created from a *norm* and *cmap*.

        This parameter is ignored if *X* is RGB(A).

    aspect : {'equal', 'auto'} or float or None, default: None
        The aspect ratio of the Axes.  This parameter is particularly
        relevant for images since it determines whether data pixels are
        square.

        This parameter is a shortcut for explicitly calling
        `.Axes.set_aspect`. See there for further details.

        - 'equal': Ensures an aspect ratio of 1. Pixels will be square
          (unless pixel sizes are explicitly made non-square in data
          coordinates using *extent*).
        - 'auto': The Axes is kept fixed and the aspect is adjusted so
          that the data fit in the Axes. In general, this will result in
          non-square pixels.

        Normally, None (the default) means to use :rc:`image.aspect`.  However, if
        the image uses a transform that does not contain the axes data transform,
        then None means to not modify the axes aspect at all (in that case, directly
        call `.Axes.set_aspect` if desired).

    interpolation : str, default: :rc:`image.interpolation`
        The interpolation method used.

        Supported values are 'none', 'auto', 'nearest', 'bilinear',
        'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', 'hermite',
        'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell',
        'sinc', 'lanczos', 'blackman'.

        The data *X* is resampled to the pixel size of the image on the
        figure canvas, using the interpolation method to either up- or
        downsample the data.

        If *interpolation* is 'none', then for the ps, pdf, and svg
        backends no down- or upsampling occurs, and the image data is
        passed to the backend as a native image.  Note that different ps,
        pdf, and svg viewers may display these raw pixels differently. On
        other backends, 'none' is the same as 'nearest'.

        If *interpolation* is the default 'auto', then 'nearest'
        interpolation is used if the image is upsampled by more than a
        factor of three (i.e. the number of display pixels is at least
        three times the size of the data array).  If the upsampling rate is
        smaller than 3, or the image is downsampled, then 'hanning'
        interpolation is used to act as an anti-aliasing filter, unless the
        image happens to be upsampled by exactly a factor of two or one.

        See
        :doc:`/gallery/images_contours_and_fields/interpolation_methods`
        for an overview of the supported interpolation methods, and
        :doc:`/gallery/images_contours_and_fields/image_antialiasing` for
        a discussion of image antialiasing.

        Some interpolation methods require an additional radius parameter,
        which can be set by *filterrad*. Additionally, the antigrain image
        resize filter is controlled by the parameter *filternorm*.

    interpolation_stage : {'auto', 'data', 'rgba'}, default: 'auto'
        Supported values:

        - 'data': Interpolation is carried out on the data provided by the user
          This is useful if interpolating between pixels during upsampling.
        - 'rgba': The interpolation is carried out in RGBA-space after the
          color-mapping has been applied. This is useful if downsampling and
          combining pixels visually.
        - 'auto': Select a suitable interpolation stage automatically. This uses
          'rgba' when downsampling, or upsampling at a rate less than 3, and
          'data' when upsampling at a higher rate.

        See :doc:`/gallery/images_contours_and_fields/image_antialiasing` for
        a discussion of image antialiasing.

    alpha : float or array-like, optional
        The alpha blending value, between 0 (transparent) and 1 (opaque).
        If *alpha* is an array, the alpha blending values are applied pixel
        by pixel, and *alpha* must have the same shape as *X*.

    origin : {'upper', 'lower'}, default: :rc:`image.origin`
        Place the [0, 0] index of the array in the upper left or lower
        left corner of the Axes. The convention (the default) 'upper' is
        typically used for matrices and images.

        Note that the vertical axis points upward for 'lower'
        but downward for 'upper'.

        See the :ref:`imshow_extent` tutorial for
        examples and a more detailed description.

    extent : floats (left, right, bottom, top), optional
        The bounding box in data coordinates that the image will fill.
        These values may be unitful and match the units of the Axes.
        The image is stretched individually along x and y to fill the box.

        The default extent is determined by the following conditions.
        Pixels have unit size in data coordinates. Their centers are on
        integer coordinates, and their center coordinates range from 0 to
        columns-1 horizontally and from 0 to rows-1 vertically.

        Note that the direction of the vertical axis and thus the default
        values for top and bottom depend on *origin*:

        - For ``origin == 'upper'`` the default is
          ``(-0.5, numcols-0.5, numrows-0.5, -0.5)``.
        - For ``origin == 'lower'`` the default is
          ``(-0.5, numcols-0.5, -0.5, numrows-0.5)``.

        See the :ref:`imshow_extent` tutorial for
        examples and a more detailed description.

    filternorm : bool, default: True
        A parameter for the antigrain image resize filter (see the
        antigrain documentation).  If *filternorm* is set, the filter
        normalizes integer values and corrects the rounding errors. It
        doesn't do anything with the source floating point values, it
        corrects only integers according to the rule of 1.0 which means
        that any sum of pixel weights must be equal to 1.0.  So, the
        filter function must produce a graph of the proper shape.

    filterrad : float > 0, default: 4.0
        The filter radius for filters that have a radius parameter, i.e.
        when interpolation is one of: 'sinc', 'lanczos' or 'blackman'.

    resample : bool, default: :rc:`image.resample`
        When *True*, use a full resampling method.  When *False*, only
        resample when the output image is larger than the input image.

    url : str, optional
        Set the url of the created `.AxesImage`. See `.Artist.set_url`.

    Returns
    -------
    `~matplotlib.image.AxesImage`

    Other Parameters
    ----------------
    data : indexable object, optional
        If given, all parameters also accept a string ``s``, which is
        interpreted as ``data[s]`` if ``s`` is a key in ``data``.

    **kwargs : `~matplotlib.artist.Artist` properties
        These parameters are passed on to the constructor of the
        `.AxesImage` artist.

    See Also
    --------
    matshow : Plot a matrix or an array as an image.

    Notes
    -----

    .. note::

        This is the :ref:`pyplot wrapper <pyplot_interface>` for `.axes.Axes.imshow`.

    Unless *extent* is used, pixel centers will be located at integer
    coordinates. In other words: the origin will coincide with the center
    of pixel (0, 0).

    There are two common representations for RGB images with an alpha
    channel:

    -   Straight (unassociated) alpha: R, G, and B channels represent the
        color of the pixel, disregarding its opacity.
    -   Premultiplied (associated) alpha: R, G, and B channels represent
        the color of the pixel, adjusted for its opacity by multiplication.

    `~matplotlib.pyplot.imshow` expects RGB images adopting the straight
    (unassociated) alpha representation.

None
&&&&&&&&&&&&&&&&&&&&&&& show &&&&&&&&&&&&&&&&&&&&&&&&&
Help on function show in module matplotlib.pyplot:

show(*args, **kwargs) -> 'None'
    Display all open figures.

    Parameters
    ----------
    block : bool, optional
        Whether to wait for all figures to be closed before returning.

        If `True` block and run the GUI main loop until all figure windows
        are closed.

        If `False` ensure that all figure windows are displayed and return
        immediately.  In this case, you are responsible for ensuring
        that the event loop is running to have responsive figures.

        Defaults to True in non-interactive mode and to False in interactive
        mode (see `.pyplot.isinteractive`).

    See Also
    --------
    ion : Enable interactive mode, which shows / updates the figure after
          every plotting command, so that calling ``show()`` is not necessary.
    ioff : Disable interactive mode.
    savefig : Save the figure to an image file instead of showing it on screen.

    Notes
    -----
    **Saving figures to file and showing a window at the same time**

    If you want an image file as well as a user interface window, use
    `.pyplot.savefig` before `.pyplot.show`. At the end of (a blocking)
    ``show()`` the figure is closed and thus unregistered from pyplot. Calling
    `.pyplot.savefig` afterwards would save a new and thus empty figure. This
    limitation of command order does not apply if the show is non-blocking or
    if you keep a reference to the figure and use `.Figure.savefig`.

    **Auto-show in jupyter notebooks**

    The jupyter backends (activated via ``%matplotlib inline``,
    ``%matplotlib notebook``, or ``%matplotlib widget``), call ``show()`` at
    the end of every cell by default. Thus, you usually don't have to call it
    explicitly there.

None
&&&&&&&&&&&&&&&&&&&&&&& violinplot &&&&&&&&&&&&&&&&&&&&&&&&&
Help on function violinplot in module matplotlib.pyplot:

violinplot(dataset: 'ArrayLike | Sequence[ArrayLike]', positions: 'ArrayLike | None' = None, *, vert: 'bool | None' = None, orientation: "Literal['vertical', 'horizontal']" = 'vertical', widths: 'float | ArrayLike' = 0.5, showmeans: 'bool' = False, showextrema: 'bool' = True, showmedians: 'bool' = False, quantiles: 'Sequence[float | Sequence[float]] | None' = None, points: 'int' = 100, bw_method: "Literal['scott', 'silverman'] | float | Callable[[GaussianKDE], float] | None" = None, side: "Literal['both', 'low', 'high']" = 'both', facecolor: 'Sequence[ColorType] | ColorType | None' = None, linecolor: 'Sequence[ColorType] | ColorType | None' = None, data: 'DataParamType' = None) -> 'dict[str, Collection]'
    Make a violin plot.

    Make a violin plot for each column of *dataset* or each vector in
    sequence *dataset*.  Each filled area extends to represent the
    entire data range, with optional lines at the mean, the median,
    the minimum, the maximum, and user-specified quantiles.

    Parameters
    ----------
    dataset : 1D array or sequence of 1D arrays or 2D array
        The input data. Possible values:

        - 1D array: A single violin is drawn.
        - sequence of 1D arrays: A violin is drawn for each array in the sequence.
        - 2D array: A violin is drawn for each column in the array.

        Non-finite and masked values are ignored.

    positions : array-like, default: [1, 2, ..., n]
        The positions of the violins; i.e. coordinates on the x-axis for
        vertical violins (or y-axis for horizontal violins).

    vert : bool, optional
        .. deprecated:: 3.10
            Use *orientation* instead.

            If this is given during the deprecation period, it overrides
            the *orientation* parameter.

        If True, plots the violins vertically.
        If False, plots the violins horizontally.

    orientation : {'vertical', 'horizontal'}, default: 'vertical'
        If 'horizontal', plots the violins horizontally.
        Otherwise, plots the violins vertically.

        .. versionadded:: 3.10

    widths : float or array-like, default: 0.5
        The maximum width of each violin in units of the *positions* axis.
        The default is 0.5, which is half the available space when using default
        *positions*.

    showmeans : bool, default: False
        Whether to show the mean with a line.

    showextrema : bool, default: True
        Whether to show extrema with a line.

    showmedians : bool, default: False
        Whether to show the median with a line.

    quantiles : array-like, default: None
        If not None, set a list of floats in interval [0, 1] for each violin,
        which stands for the quantiles that will be rendered for that
        violin.

    points : int, default: 100
        The number of points to evaluate each of the gaussian kernel density
        estimations at.

    bw_method : {'scott', 'silverman'} or float or callable, default: 'scott'
        The method used to calculate the estimator bandwidth.  If a
        float, this will be used directly as `!kde.factor`.  If a
        callable, it should take a `matplotlib.mlab.GaussianKDE` instance as
        its only parameter and return a float.

    side : {'both', 'low', 'high'}, default: 'both'
        'both' plots standard violins. 'low'/'high' only
        plots the side below/above the positions value.

    facecolor : :mpltype:`color` or list of :mpltype:`color`, optional
        If provided, will set the face color(s) of the violins.

        .. versionadded:: 3.11

    linecolor : :mpltype:`color` or list of :mpltype:`color`, optional
        If provided, will set the line color(s) of the violins (the
        horizontal and vertical spines and body edges).

        .. versionadded:: 3.11

    data : indexable object, optional
        If given, the following parameters also accept a string ``s``, which is
        interpreted as ``data[s]`` if ``s`` is a key in ``data``:

        *dataset*

    Returns
    -------
    dict
        A dictionary mapping each component of the violinplot to a
        list of the corresponding collection instances created. The
        dictionary has the following keys:

        - ``bodies``: A list of the `~.collections.PolyCollection`
          instances containing the filled area of each violin.

        - ``cmeans``: A `~.collections.LineCollection` instance that marks
          the mean values of each of the violin's distribution.

        - ``cmins``: A `~.collections.LineCollection` instance that marks
          the bottom of each violin's distribution.

        - ``cmaxes``: A `~.collections.LineCollection` instance that marks
          the top of each violin's distribution.

        - ``cbars``: A `~.collections.LineCollection` instance that marks
          the centers of each violin's distribution.

        - ``cmedians``: A `~.collections.LineCollection` instance that
          marks the median values of each of the violin's distribution.

        - ``cquantiles``: A `~.collections.LineCollection` instance created
          to identify the quantile values of each of the violin's
          distribution.

    See Also
    --------
    .Axes.violin : Draw a violin from pre-computed statistics.
    boxplot : Draw a box and whisker plot.

    Notes
    -----

    .. note::

        This is the :ref:`pyplot wrapper <pyplot_interface>` for `.axes.Axes.violinplot`.

None
&&&&&&&&&&&&&&&&&&&&&&& time &&&&&&&&&&&&&&&&&&&&&&&&&
Help on built-in module time:

NAME
    time - This module provides various functions to manipulate time values.

DESCRIPTION
    There are two standard representations of time.  One is the number
    of seconds since the Epoch, in UTC (a.k.a. GMT).  It may be an integer
    or a floating point number (to represent fractions of seconds).
    The Epoch is system-defined; on Unix, it is generally January 1st, 1970.
    The actual value can be retrieved by calling gmtime(0).

    The other representation is a tuple of 9 integers giving local time.
    The tuple items are:
      year (including century, e.g. 1998)
      month (1-12)
      day (1-31)
      hours (0-23)
      minutes (0-59)
      seconds (0-59)
      weekday (0-6, Monday is 0)
      Julian day (day in the year, 1-366)
      DST (Daylight Savings Time) flag (-1, 0 or 1)
    If the DST flag is 0, the time is given in the regular time zone;
    if it is 1, the time is given in the DST time zone;
    if it is -1, mktime() should guess based on the date and time.

CLASSES
    builtins.tuple(builtins.object)
        struct_time

    class struct_time(builtins.tuple)
     |  struct_time(iterable=(), /)
     |
     |  The time value as returned by gmtime(), localtime(), and strptime(), and
     |  accepted by asctime(), mktime() and strftime().  May be considered as a
     |  sequence of 9 integers.
     |
     |  Note that several fields' values are not the same as those defined by
     |  the C language standard for struct tm.  For example, the value of the
     |  field tm_year is the actual year, not year - 1900.  See individual
     |  fields' descriptions for details.
     |
     |  Method resolution order:
     |      struct_time
     |      builtins.tuple
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  tm_gmtoff
     |      offset from UTC in seconds
     |
     |  tm_hour
     |      hours, range [0, 23]
     |
     |  tm_isdst
     |      1 if summer time is in effect, 0 if not, and -1 if unknown
     |
     |  tm_mday
     |      day of month, range [1, 31]
     |
     |  tm_min
     |      minutes, range [0, 59]
     |
     |  tm_mon
     |      month of year, range [1, 12]
     |
     |  tm_sec
     |      seconds, range [0, 61])
     |
     |  tm_wday
     |      day of week, range [0, 6], Monday is 0
     |
     |  tm_yday
     |      day of year, range [1, 366]
     |
     |  tm_year
     |      year, for example, 1993
     |
     |  tm_zone
     |      abbreviation of timezone name
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __match_args__ = ('tm_year', 'tm_mon', 'tm_mday', 'tm_hour', 'tm_min',...
     |
     |  n_fields = 11
     |
     |  n_sequence_fields = 9
     |
     |  n_unnamed_fields = 0
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __contains__(self, key, /)
     |      Return bool(key in self).
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __getitem__(self, key, /)
     |      Return self[key].
     |
     |  __getnewargs__(self, /)
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __len__(self, /)
     |      Return len(self).
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __mul__(self, value, /)
     |      Return self*value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __rmul__(self, value, /)
     |      Return value*self.
     |
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |
     |      Raises ValueError if the value is not present.
     |
     |  ----------------------------------------------------------------------
     |  Class methods inherited from builtins.tuple:
     |
     |  __class_getitem__(...) from builtins.type
     |      See PEP 585

FUNCTIONS
    asctime(...)
        asctime([tuple]) -> string

        Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.
        When the time tuple is not present, current time as returned by localtime()
        is used.

    clock_getres(...)
        clock_getres(clk_id) -> floating point number

        Return the resolution (precision) of the specified clock clk_id.

    clock_gettime(...)
        clock_gettime(clk_id) -> float

        Return the time of the specified clock clk_id.

    clock_gettime_ns(...)
        clock_gettime_ns(clk_id) -> int

        Return the time of the specified clock clk_id as nanoseconds.

    clock_settime(...)
        clock_settime(clk_id, time)

        Set the time of the specified clock clk_id.

    clock_settime_ns(...)
        clock_settime_ns(clk_id, time)

        Set the time of the specified clock clk_id with nanoseconds.

    ctime(...)
        ctime(seconds) -> string

        Convert a time in seconds since the Epoch to a string in local time.
        This is equivalent to asctime(localtime(seconds)). When the time tuple is
        not present, current time as returned by localtime() is used.

    get_clock_info(...)
        get_clock_info(name: str) -> dict

        Get information of the specified clock.

    gmtime(...)
        gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min,
                               tm_sec, tm_wday, tm_yday, tm_isdst)

        Convert seconds since the Epoch to a time tuple expressing UTC (a.k.a.
        GMT).  When 'seconds' is not passed in, convert the current time instead.

        If the platform supports the tm_gmtoff and tm_zone, they are available as
        attributes only.

    localtime(...)
        localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,
                                  tm_sec,tm_wday,tm_yday,tm_isdst)

        Convert seconds since the Epoch to a time tuple expressing local time.
        When 'seconds' is not passed in, convert the current time instead.

    mktime(...)
        mktime(tuple) -> floating point number

        Convert a time tuple in local time to seconds since the Epoch.
        Note that mktime(gmtime(0)) will not generally return zero for most
        time zones; instead the returned value will either be equal to that
        of the timezone or altzone attributes on the time module.

    monotonic(...)
        monotonic() -> float

        Monotonic clock, cannot go backward.

    monotonic_ns(...)
        monotonic_ns() -> int

        Monotonic clock, cannot go backward, as nanoseconds.

    perf_counter(...)
        perf_counter() -> float

        Performance counter for benchmarking.

    perf_counter_ns(...)
        perf_counter_ns() -> int

        Performance counter for benchmarking as nanoseconds.

    process_time(...)
        process_time() -> float

        Process time for profiling: sum of the kernel and user-space CPU time.

    process_time_ns(...)
        process_time() -> int

        Process time for profiling as nanoseconds:
        sum of the kernel and user-space CPU time.

    sleep(...)
        sleep(seconds)

        Delay execution for a given number of seconds.  The argument may be
        a floating point number for subsecond precision.

    strftime(...)
        strftime(format[, tuple]) -> string

        Convert a time tuple to a string according to a format specification.
        See the library reference manual for formatting codes. When the time tuple
        is not present, current time as returned by localtime() is used.

        Commonly used format codes:

        %Y  Year with century as a decimal number.
        %m  Month as a decimal number [01,12].
        %d  Day of the month as a decimal number [01,31].
        %H  Hour (24-hour clock) as a decimal number [00,23].
        %M  Minute as a decimal number [00,59].
        %S  Second as a decimal number [00,61].
        %z  Time zone offset from UTC.
        %a  Locale's abbreviated weekday name.
        %A  Locale's full weekday name.
        %b  Locale's abbreviated month name.
        %B  Locale's full month name.
        %c  Locale's appropriate date and time representation.
        %I  Hour (12-hour clock) as a decimal number [01,12].
        %p  Locale's equivalent of either AM or PM.

        Other codes may be available on your platform.  See documentation for
        the C library strftime function.

    strptime(...)
        strptime(string, format) -> struct_time

        Parse a string to a time tuple according to a format specification.
        See the library reference manual for formatting codes (same as
        strftime()).

        Commonly used format codes:

        %Y  Year with century as a decimal number.
        %m  Month as a decimal number [01,12].
        %d  Day of the month as a decimal number [01,31].
        %H  Hour (24-hour clock) as a decimal number [00,23].
        %M  Minute as a decimal number [00,59].
        %S  Second as a decimal number [00,61].
        %z  Time zone offset from UTC.
        %a  Locale's abbreviated weekday name.
        %A  Locale's full weekday name.
        %b  Locale's abbreviated month name.
        %B  Locale's full month name.
        %c  Locale's appropriate date and time representation.
        %I  Hour (12-hour clock) as a decimal number [01,12].
        %p  Locale's equivalent of either AM or PM.

        Other codes may be available on your platform.  See documentation for
        the C library strftime function.

    thread_time(...)
        thread_time() -> float

        Thread time for profiling: sum of the kernel and user-space CPU time.

    thread_time_ns(...)
        thread_time() -> int

        Thread time for profiling as nanoseconds:
        sum of the kernel and user-space CPU time.

    time(...)
        time() -> floating point number

        Return the current time in seconds since the Epoch.
        Fractions of a second may be present if the system clock provides them.

    time_ns(...)
        time_ns() -> int

        Return the current time in nanoseconds since the Epoch.

    tzset(...)
        tzset()

        Initialize, or reinitialize, the local timezone to the value stored in
        os.environ['TZ']. The TZ environment variable should be specified in
        standard Unix timezone format as documented in the tzset man page
        (eg. 'US/Eastern', 'Europe/Amsterdam'). Unknown timezones will silently
        fall back to UTC. If the TZ environment variable is not set, the local
        timezone is set to the systems best guess of wallclock time.
        Changing the TZ environment variable without calling tzset *may* change
        the local timezone used by methods such as localtime, but this behaviour
        should not be relied on.

DATA
    CLOCK_MONOTONIC = 6
    CLOCK_MONOTONIC_RAW = 4
    CLOCK_PROCESS_CPUTIME_ID = 12
    CLOCK_REALTIME = 0
    CLOCK_THREAD_CPUTIME_ID = 16
    CLOCK_UPTIME_RAW = 8
    altzone = 21600
    daylight = 0
    timezone = 21600
    tzname = ('CST', 'CST')

FILE
    (built-in)


None
