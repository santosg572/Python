Algunos métodos
=================


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
