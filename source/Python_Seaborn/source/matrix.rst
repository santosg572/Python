Help on module seaborn.matrix in seaborn:

NAME
    seaborn.matrix - Functions to visualize matrices of data.

FUNCTIONS
    clustermap(data, *, pivot_kws=None, method='average', metric='euclidean', z_score=None, standard_scale=None, figsize=(10, 10), cbar_kws=None, row_cluster=True, col_cluster=True, row_linkage=None, col_linkage=None, row_colors=None, col_colors=None, mask=None, dendrogram_ratio=0.2, colors_ratio=0.03, cbar_pos=(0.02, 0.8, 0.05, 0.18), tree_kws=None, **kwargs)
        Plot a matrix dataset as a hierarchically-clustered heatmap.

        This function requires scipy to be available.

        Parameters
        ----------
        data : 2D array-like
            Rectangular data for clustering. Cannot contain NAs.
        pivot_kws : dict, optional
            If `data` is a tidy dataframe, can provide keyword arguments for
            pivot to create a rectangular dataframe.
        method : str, optional
            Linkage method to use for calculating clusters. See
            :func:`scipy.cluster.hierarchy.linkage` documentation for more
            information.
        metric : str, optional
            Distance metric to use for the data. See
            :func:`scipy.spatial.distance.pdist` documentation for more options.
            To use different metrics (or methods) for rows and columns, you may
            construct each linkage matrix yourself and provide them as
            `{row,col}_linkage`.
        z_score : int or None, optional
            Either 0 (rows) or 1 (columns). Whether or not to calculate z-scores
            for the rows or the columns. Z scores are: z = (x - mean)/std, so
            values in each row (column) will get the mean of the row (column)
            subtracted, then divided by the standard deviation of the row (column).
            This ensures that each row (column) has mean of 0 and variance of 1.
        standard_scale : int or None, optional
            Either 0 (rows) or 1 (columns). Whether or not to standardize that
            dimension, meaning for each row or column, subtract the minimum and
            divide each by its maximum.
        figsize : tuple of (width, height), optional
            Overall size of the figure.
        cbar_kws : dict, optional
            Keyword arguments to pass to `cbar_kws` in :func:`heatmap`, e.g. to
            add a label to the colorbar.
        {row,col}_cluster : bool, optional
            If ``True``, cluster the {rows, columns}.
        {row,col}_linkage : :class:`numpy.ndarray`, optional
            Precomputed linkage matrix for the rows or columns. See
            :func:`scipy.cluster.hierarchy.linkage` for specific formats.
        {row,col}_colors : list-like or pandas DataFrame/Series, optional
            List of colors to label for either the rows or columns. Useful to evaluate
            whether samples within a group are clustered together. Can use nested lists or
            DataFrame for multiple color levels of labeling. If given as a
            :class:`pandas.DataFrame` or :class:`pandas.Series`, labels for the colors are
            extracted from the DataFrames column names or from the name of the Series.
            DataFrame/Series colors are also matched to the data by their index, ensuring
            colors are drawn in the correct order.
        mask : bool array or DataFrame, optional
            If passed, data will not be shown in cells where `mask` is True.
            Cells with missing values are automatically masked. Only used for
            visualizing, not for calculating.
        {dendrogram,colors}_ratio : float, or pair of floats, optional
            Proportion of the figure size devoted to the two marginal elements. If
            a pair is given, they correspond to (row, col) ratios.
        cbar_pos : tuple of (left, bottom, width, height), optional
            Position of the colorbar axes in the figure. Setting to ``None`` will
            disable the colorbar.
        tree_kws : dict, optional
            Parameters for the :class:`matplotlib.collections.LineCollection`
            that is used to plot the lines of the dendrogram tree.
        kwargs : other keyword arguments
            All other keyword arguments are passed to :func:`heatmap`.

        Returns
        -------
        :class:`ClusterGrid`
            A :class:`ClusterGrid` instance.

        See Also
        --------
        heatmap : Plot rectangular data as a color-encoded matrix.

        Notes
        -----
        The returned object has a ``savefig`` method that should be used if you
        want to save the figure object without clipping the dendrograms.

        To access the reordered row indices, use:
        ``clustergrid.dendrogram_row.reordered_ind``

        Column indices, use:
        ``clustergrid.dendrogram_col.reordered_ind``

        Examples
        --------

        .. include:: ../docstrings/clustermap.rst

    heatmap(data, *, vmin=None, vmax=None, cmap=None, center=None, robust=False, annot=None, fmt='.2g', annot_kws=None, linewidths=0, linecolor='white', cbar=True, cbar_kws=None, cbar_ax=None, square=False, xticklabels='auto', yticklabels='auto', mask=None, ax=None, **kwargs)
        Plot rectangular data as a color-encoded matrix.

        This is an Axes-level function and will draw the heatmap into the
        currently-active Axes if none is provided to the ``ax`` argument.  Part of
        this Axes space will be taken and used to plot a colormap, unless ``cbar``
        is False or a separate Axes is provided to ``cbar_ax``.

        Parameters
        ----------
        data : rectangular dataset
            2D dataset that can be coerced into an ndarray. If a Pandas DataFrame
            is provided, the index/column information will be used to label the
            columns and rows.
        vmin, vmax : floats, optional
            Values to anchor the colormap, otherwise they are inferred from the
            data and other keyword arguments.
        cmap : matplotlib colormap name or object, or list of colors, optional
            The mapping from data values to color space. If not provided, the
            default will depend on whether ``center`` is set.
        center : float, optional
            The value at which to center the colormap when plotting divergent data.
            Using this parameter will change the default ``cmap`` if none is
            specified.
        robust : bool, optional
            If True and ``vmin`` or ``vmax`` are absent, the colormap range is
            computed with robust quantiles instead of the extreme values.
        annot : bool or rectangular dataset, optional
            If True, write the data value in each cell. If an array-like with the
            same shape as ``data``, then use this to annotate the heatmap instead
            of the data. Note that DataFrames will match on position, not index.
        fmt : str, optional
            String formatting code to use when adding annotations.
        annot_kws : dict of key, value mappings, optional
            Keyword arguments for :meth:`matplotlib.axes.Axes.text` when ``annot``
            is True.
        linewidths : float, optional
            Width of the lines that will divide each cell.
        linecolor : color, optional
            Color of the lines that will divide each cell.
        cbar : bool, optional
            Whether to draw a colorbar.
        cbar_kws : dict of key, value mappings, optional
            Keyword arguments for :meth:`matplotlib.figure.Figure.colorbar`.
        cbar_ax : matplotlib Axes, optional
            Axes in which to draw the colorbar, otherwise take space from the
            main Axes.
        square : bool, optional
            If True, set the Axes aspect to "equal" so each cell will be
            square-shaped.
        xticklabels, yticklabels : "auto", bool, list-like, or int, optional
            If True, plot the column names of the dataframe. If False, don't plot
            the column names. If list-like, plot these alternate labels as the
            xticklabels. If an integer, use the column names but plot only every
            n label. If "auto", try to densely plot non-overlapping labels.
        mask : bool array or DataFrame, optional
            If passed, data will not be shown in cells where ``mask`` is True.
            Cells with missing values are automatically masked.
        ax : matplotlib Axes, optional
            Axes in which to draw the plot, otherwise use the currently-active
            Axes.
        kwargs : other keyword arguments
            All other keyword arguments are passed to
            :meth:`matplotlib.axes.Axes.pcolormesh`.

        Returns
        -------
        ax : matplotlib Axes
            Axes object with the heatmap.

        See Also
        --------
        clustermap : Plot a matrix using hierarchical clustering to arrange the
                     rows and columns.

        Examples
        --------

        .. include:: ../docstrings/heatmap.rst

DATA
    __all__ = ['heatmap', 'clustermap']

FILE
    /Users/leopoldogonzalez/miniconda3/lib/python3.12/site-packages/seaborn/matrix.py


