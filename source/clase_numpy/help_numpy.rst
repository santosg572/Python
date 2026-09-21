numpy
=====

&&&&&&&&&&&&&&&&&&&&&& amax &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

amax(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)
    Return the maximum of an array or maximum along an axis.

    `amax` is an alias of `~numpy.max`.

    See Also
    --------
    max : alias of this function
    ndarray.max : equivalent method

None
&&&&&&&&&&&&&&&&&&&&&& amin &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

amin(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)
    Return the minimum of an array or minimum along an axis.

    `amin` is an alias of `~numpy.min`.

    See Also
    --------
    min : alias of this function
    ndarray.min : equivalent method

None
&&&&&&&&&&&&&&&&&&&&&& angle &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

angle(z, deg=False)
    Return the angle of the complex argument.

    Parameters
    ----------
    z : array_like
        A complex number or sequence of complex numbers.
    deg : bool, optional
        Return angle in degrees if True, radians if False (default).

    Returns
    -------
    angle : ndarray or scalar
        The counterclockwise angle from the positive real axis on the complex
        plane in the range ``(-pi, pi]``, with dtype as numpy.float64.

        .. versionchanged:: 1.16.0
            This function works on subclasses of ndarray like `ma.array`.

    See Also
    --------
    arctan2
    absolute

    Notes
    -----
    Although the angle of the complex number 0 is undefined, ``numpy.angle(0)``
    returns the value 0.

    Examples
    --------
    >>> np.angle([1.0, 1.0j, 1+1j])               # in radians
    array([ 0.        ,  1.57079633,  0.78539816]) # may vary
    >>> np.angle(1+1j, deg=True)                  # in degrees
    45.0

None
&&&&&&&&&&&&&&&&&&&&&& append &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

append(arr, values, axis=None)
    Append values to the end of an array.

    Parameters
    ----------
    arr : array_like
        Values are appended to a copy of this array.
    values : array_like
        These values are appended to a copy of `arr`.  It must be of the
        correct shape (the same shape as `arr`, excluding `axis`).  If
        `axis` is not specified, `values` can be any shape and will be
        flattened before use.
    axis : int, optional
        The axis along which `values` are appended.  If `axis` is not
        given, both `arr` and `values` are flattened before use.

    Returns
    -------
    append : ndarray
        A copy of `arr` with `values` appended to `axis`.  Note that
        `append` does not occur in-place: a new array is allocated and
        filled.  If `axis` is None, `out` is a flattened array.

    See Also
    --------
    insert : Insert elements into an array.
    delete : Delete elements from an array.

    Examples
    --------
    >>> np.append([1, 2, 3], [[4, 5, 6], [7, 8, 9]])
    array([1, 2, 3, ..., 7, 8, 9])

    When `axis` is specified, `values` must have the correct shape.

    >>> np.append([[1, 2, 3], [4, 5, 6]], [[7, 8, 9]], axis=0)
    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])
    >>> np.append([[1, 2, 3], [4, 5, 6]], [7, 8, 9], axis=0)
    Traceback (most recent call last):
        ...
    ValueError: all the input arrays must have same number of dimensions, but
    the array at index 0 has 2 dimension(s) and the array at index 1 has 1
    dimension(s)

None
&&&&&&&&&&&&&&&&&&&&&& apply_along_axis &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

apply_along_axis(func1d, axis, arr, *args, **kwargs)
    Apply a function to 1-D slices along the given axis.

    Execute `func1d(a, *args, **kwargs)` where `func1d` operates on 1-D arrays
    and `a` is a 1-D slice of `arr` along `axis`.

    This is equivalent to (but faster than) the following use of `ndindex` and
    `s_`, which sets each of ``ii``, ``jj``, and ``kk`` to a tuple of indices::

        Ni, Nk = a.shape[:axis], a.shape[axis+1:]
        for ii in ndindex(Ni):
            for kk in ndindex(Nk):
                f = func1d(arr[ii + s_[:,] + kk])
                Nj = f.shape
                for jj in ndindex(Nj):
                    out[ii + jj + kk] = f[jj]

    Equivalently, eliminating the inner loop, this can be expressed as::

        Ni, Nk = a.shape[:axis], a.shape[axis+1:]
        for ii in ndindex(Ni):
            for kk in ndindex(Nk):
                out[ii + s_[...,] + kk] = func1d(arr[ii + s_[:,] + kk])

    Parameters
    ----------
    func1d : function (M,) -> (Nj...)
        This function should accept 1-D arrays. It is applied to 1-D
        slices of `arr` along the specified axis.
    axis : integer
        Axis along which `arr` is sliced.
    arr : ndarray (Ni..., M, Nk...)
        Input array.
    args : any
        Additional arguments to `func1d`.
    kwargs : any
        Additional named arguments to `func1d`.

        .. versionadded:: 1.9.0


    Returns
    -------
    out : ndarray  (Ni..., Nj..., Nk...)
        The output array. The shape of `out` is identical to the shape of
        `arr`, except along the `axis` dimension. This axis is removed, and
        replaced with new dimensions equal to the shape of the return value
        of `func1d`. So if `func1d` returns a scalar `out` will have one
        fewer dimensions than `arr`.

    See Also
    --------
    apply_over_axes : Apply a function repeatedly over multiple axes.

    Examples
    --------
    >>> def my_func(a):
    ...     """Average first and last element of a 1-D array"""
    ...     return (a[0] + a[-1]) * 0.5
    >>> b = np.array([[1,2,3], [4,5,6], [7,8,9]])
    >>> np.apply_along_axis(my_func, 0, b)
    array([4., 5., 6.])
    >>> np.apply_along_axis(my_func, 1, b)
    array([2.,  5.,  8.])

    For a function that returns a 1D array, the number of dimensions in
    `outarr` is the same as `arr`.

    >>> b = np.array([[8,1,7], [4,3,9], [5,2,6]])
    >>> np.apply_along_axis(sorted, 1, b)
    array([[1, 7, 8],
           [3, 4, 9],
           [2, 5, 6]])

    For a function that returns a higher dimensional array, those dimensions
    are inserted in place of the `axis` dimension.

    >>> b = np.array([[1,2,3], [4,5,6], [7,8,9]])
    >>> np.apply_along_axis(np.diag, -1, b)
    array([[[1, 0, 0],
            [0, 2, 0],
            [0, 0, 3]],
           [[4, 0, 0],
            [0, 5, 0],
            [0, 0, 6]],
           [[7, 0, 0],
            [0, 8, 0],
            [0, 0, 9]]])

None
&&&&&&&&&&&&&&&&&&&&&& argmax &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

argmax(a, axis=None, out=None, *, keepdims=<no value>)
    Returns the indices of the maximum values along an axis.

    Parameters
    ----------
    a : array_like
        Input array.
    axis : int, optional
        By default, the index is into the flattened array, otherwise
        along the specified axis.
    out : array, optional
        If provided, the result will be inserted into this array. It should
        be of the appropriate shape and dtype.
    keepdims : bool, optional
        If this is set to True, the axes which are reduced are left
        in the result as dimensions with size one. With this option,
        the result will broadcast correctly against the array.

        .. versionadded:: 1.22.0

    Returns
    -------
    index_array : ndarray of ints
        Array of indices into the array. It has the same shape as `a.shape`
        with the dimension along `axis` removed. If `keepdims` is set to True,
        then the size of `axis` will be 1 with the resulting array having same
        shape as `a.shape`.

    See Also
    --------
    ndarray.argmax, argmin
    amax : The maximum value along a given axis.
    unravel_index : Convert a flat index into an index tuple.
    take_along_axis : Apply ``np.expand_dims(index_array, axis)``
                      from argmax to an array as if by calling max.

    Notes
    -----
    In case of multiple occurrences of the maximum values, the indices
    corresponding to the first occurrence are returned.

    Examples
    --------
    >>> a = np.arange(6).reshape(2,3) + 10
    >>> a
    array([[10, 11, 12],
           [13, 14, 15]])
    >>> np.argmax(a)
    5
    >>> np.argmax(a, axis=0)
    array([1, 1, 1])
    >>> np.argmax(a, axis=1)
    array([2, 2])

    Indexes of the maximal elements of a N-dimensional array:

    >>> ind = np.unravel_index(np.argmax(a, axis=None), a.shape)
    >>> ind
    (1, 2)
    >>> a[ind]
    15

    >>> b = np.arange(6)
    >>> b[1] = 5
    >>> b
    array([0, 5, 2, 3, 4, 5])
    >>> np.argmax(b)  # Only the first occurrence is returned.
    1

    >>> x = np.array([[4,2,3], [1,0,3]])
    >>> index_array = np.argmax(x, axis=-1)
    >>> # Same as np.amax(x, axis=-1, keepdims=True)
    >>> np.take_along_axis(x, np.expand_dims(index_array, axis=-1), axis=-1)
    array([[4],
           [3]])
    >>> # Same as np.amax(x, axis=-1)
    >>> np.take_along_axis(x, np.expand_dims(index_array, axis=-1), axis=-1).squeeze(axis=-1)
    array([4, 3])

    Setting `keepdims` to `True`,

    >>> x = np.arange(24).reshape((2, 3, 4))
    >>> res = np.argmax(x, axis=1, keepdims=True)
    >>> res.shape
    (2, 1, 4)

None
&&&&&&&&&&&&&&&&&&&&&& argmin &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

argmin(a, axis=None, out=None, *, keepdims=<no value>)
    Returns the indices of the minimum values along an axis.

    Parameters
    ----------
    a : array_like
        Input array.
    axis : int, optional
        By default, the index is into the flattened array, otherwise
        along the specified axis.
    out : array, optional
        If provided, the result will be inserted into this array. It should
        be of the appropriate shape and dtype.
    keepdims : bool, optional
        If this is set to True, the axes which are reduced are left
        in the result as dimensions with size one. With this option,
        the result will broadcast correctly against the array.

        .. versionadded:: 1.22.0

    Returns
    -------
    index_array : ndarray of ints
        Array of indices into the array. It has the same shape as `a.shape`
        with the dimension along `axis` removed. If `keepdims` is set to True,
        then the size of `axis` will be 1 with the resulting array having same
        shape as `a.shape`.

    See Also
    --------
    ndarray.argmin, argmax
    amin : The minimum value along a given axis.
    unravel_index : Convert a flat index into an index tuple.
    take_along_axis : Apply ``np.expand_dims(index_array, axis)``
                      from argmin to an array as if by calling min.

    Notes
    -----
    In case of multiple occurrences of the minimum values, the indices
    corresponding to the first occurrence are returned.

    Examples
    --------
    >>> a = np.arange(6).reshape(2,3) + 10
    >>> a
    array([[10, 11, 12],
           [13, 14, 15]])
    >>> np.argmin(a)
    0
    >>> np.argmin(a, axis=0)
    array([0, 0, 0])
    >>> np.argmin(a, axis=1)
    array([0, 0])

    Indices of the minimum elements of a N-dimensional array:

    >>> ind = np.unravel_index(np.argmin(a, axis=None), a.shape)
    >>> ind
    (0, 0)
    >>> a[ind]
    10

    >>> b = np.arange(6) + 10
    >>> b[4] = 10
    >>> b
    array([10, 11, 12, 13, 10, 15])
    >>> np.argmin(b)  # Only the first occurrence is returned.
    0

    >>> x = np.array([[4,2,3], [1,0,3]])
    >>> index_array = np.argmin(x, axis=-1)
    >>> # Same as np.amin(x, axis=-1, keepdims=True)
    >>> np.take_along_axis(x, np.expand_dims(index_array, axis=-1), axis=-1)
    array([[2],
           [0]])
    >>> # Same as np.amax(x, axis=-1)
    >>> np.take_along_axis(x, np.expand_dims(index_array, axis=-1), axis=-1).squeeze(axis=-1)
    array([2, 0])

    Setting `keepdims` to `True`,

    >>> x = np.arange(24).reshape((2, 3, 4))
    >>> res = np.argmin(x, axis=1, keepdims=True)
    >>> res.shape
    (2, 1, 4)

None
&&&&&&&&&&&&&&&&&&&&&& around &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

around(a, decimals=0, out=None)
    Round an array to the given number of decimals.

    `around` is an alias of `~numpy.round`.

    See Also
    --------
    ndarray.round : equivalent method
    round : alias for this function
    ceil, fix, floor, rint, trunc

None
&&&&&&&&&&&&&&&&&&&&&& array &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on built-in function array in module numpy:

array(...)
    array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0,
          like=None)

    Create an array.

    Parameters
    ----------
    object : array_like
        An array, any object exposing the array interface, an object whose
        ``__array__`` method returns an array, or any (nested) sequence.
        If object is a scalar, a 0-dimensional array containing object is
        returned.
    dtype : data-type, optional
        The desired data-type for the array. If not given, NumPy will try to use
        a default ``dtype`` that can represent the values (by applying promotion
        rules when necessary.)
    copy : bool, optional
        If true (default), then the object is copied.  Otherwise, a copy will
        only be made if ``__array__`` returns a copy, if obj is a nested
        sequence, or if a copy is needed to satisfy any of the other
        requirements (``dtype``, ``order``, etc.).
    order : {'K', 'A', 'C', 'F'}, optional
        Specify the memory layout of the array. If object is not an array, the
        newly created array will be in C order (row major) unless 'F' is
        specified, in which case it will be in Fortran order (column major).
        If object is an array the following holds.

        ===== ========= ===================================================
        order  no copy                     copy=True
        ===== ========= ===================================================
        'K'   unchanged F & C order preserved, otherwise most similar order
        'A'   unchanged F order if input is F and not C, otherwise C order
        'C'   C order   C order
        'F'   F order   F order
        ===== ========= ===================================================

        When ``copy=False`` and a copy is made for other reasons, the result is
        the same as if ``copy=True``, with some exceptions for 'A', see the
        Notes section. The default order is 'K'.
    subok : bool, optional
        If True, then sub-classes will be passed-through, otherwise
        the returned array will be forced to be a base-class array (default).
    ndmin : int, optional
        Specifies the minimum number of dimensions that the resulting
        array should have.  Ones will be prepended to the shape as
        needed to meet this requirement.
    like : array_like, optional
        Reference object to allow the creation of arrays which are not
        NumPy arrays. If an array-like passed in as ``like`` supports
        the ``__array_function__`` protocol, the result will be defined
        by it. In this case, it ensures the creation of an array object
        compatible with that passed in via this argument.

        .. versionadded:: 1.20.0

    Returns
    -------
    out : ndarray
        An array object satisfying the specified requirements.

    See Also
    --------
    empty_like : Return an empty array with shape and type of input.
    ones_like : Return an array of ones with shape and type of input.
    zeros_like : Return an array of zeros with shape and type of input.
    full_like : Return a new array with shape of input filled with value.
    empty : Return a new uninitialized array.
    ones : Return a new array setting values to one.
    zeros : Return a new array setting values to zero.
    full : Return a new array of given shape filled with value.


    Notes
    -----
    When order is 'A' and ``object`` is an array in neither 'C' nor 'F' order,
    and a copy is forced by a change in dtype, then the order of the result is
    not necessarily 'C' as expected. This is likely a bug.

    Examples
    --------
    >>> np.array([1, 2, 3])
    array([1, 2, 3])

    Upcasting:

    >>> np.array([1, 2, 3.0])
    array([ 1.,  2.,  3.])

    More than one dimension:

    >>> np.array([[1, 2], [3, 4]])
    array([[1, 2],
           [3, 4]])

    Minimum dimensions 2:

    >>> np.array([1, 2, 3], ndmin=2)
    array([[1, 2, 3]])

    Type provided:

    >>> np.array([1, 2, 3], dtype=complex)
    array([ 1.+0.j,  2.+0.j,  3.+0.j])

    Data-type consisting of more than one element:

    >>> x = np.array([(1,2),(3,4)],dtype=[('a','<i4'),('b','<i4')])
    >>> x['a']
    array([1, 3])

    Creating an array from sub-classes:

    >>> np.array(np.mat('1 2; 3 4'))
    array([[1, 2],
           [3, 4]])

    >>> np.array(np.mat('1 2; 3 4'), subok=True)
    matrix([[1, 2],
            [3, 4]])

None
&&&&&&&&&&&&&&&&&&&&&& c_ &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on CClass in module numpy.lib.index_tricks object:

class CClass(AxisConcatenator)
 |  Translates slice objects to concatenation along the second axis.
 |
 |  This is short-hand for ``np.r_['-1,2,0', index expression]``, which is
 |  useful because of its common occurrence. In particular, arrays will be
 |  stacked along their last axis after being upgraded to at least 2-D with
 |  1's post-pended to the shape (column vectors made out of 1-D arrays).
 |
 |  See Also
 |  --------
 |  column_stack : Stack 1-D arrays as columns into a 2-D array.
 |  r_ : For more detailed documentation.
 |
 |  Examples
 |  --------
 |  >>> np.c_[np.array([1,2,3]), np.array([4,5,6])]
 |  array([[1, 4],
 |         [2, 5],
 |         [3, 6]])
 |  >>> np.c_[np.array([[1,2,3]]), 0, 0, np.array([[4,5,6]])]
 |  array([[1, 2, 3, ..., 4, 5, 6]])
 |
 |  Method resolution order:
 |      CClass
 |      AxisConcatenator
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from AxisConcatenator:
 |
 |  __getitem__(self, key)
 |
 |  __len__(self)
 |
 |  ----------------------------------------------------------------------
 |  Static methods inherited from AxisConcatenator:
 |
 |  concatenate(...)
 |      concatenate((a1, a2, ...), axis=0, out=None, dtype=None, casting="same_kind")
 |
 |      Join a sequence of arrays along an existing axis.
 |
 |      Parameters
 |      ----------
 |      a1, a2, ... : sequence of array_like
 |          The arrays must have the same shape, except in the dimension
 |          corresponding to `axis` (the first, by default).
 |      axis : int, optional
 |          The axis along which the arrays will be joined.  If axis is None,
 |          arrays are flattened before use.  Default is 0.
 |      out : ndarray, optional
 |          If provided, the destination to place the result. The shape must be
 |          correct, matching that of what concatenate would have returned if no
 |          out argument were specified.
 |      dtype : str or dtype
 |          If provided, the destination array will have this dtype. Cannot be
 |          provided together with `out`.
 |
 |          .. versionadded:: 1.20.0
 |
 |      casting : {'no', 'equiv', 'safe', 'same_kind', 'unsafe'}, optional
 |          Controls what kind of data casting may occur. Defaults to 'same_kind'.
 |
 |          .. versionadded:: 1.20.0
 |
 |      Returns
 |      -------
 |      res : ndarray
 |          The concatenated array.
 |
 |      See Also
 |      --------
 |      ma.concatenate : Concatenate function that preserves input masks.
 |      array_split : Split an array into multiple sub-arrays of equal or
 |                    near-equal size.
 |      split : Split array into a list of multiple sub-arrays of equal size.
 |      hsplit : Split array into multiple sub-arrays horizontally (column wise).
 |      vsplit : Split array into multiple sub-arrays vertically (row wise).
 |      dsplit : Split array into multiple sub-arrays along the 3rd axis (depth).
 |      stack : Stack a sequence of arrays along a new axis.
 |      block : Assemble arrays from blocks.
 |      hstack : Stack arrays in sequence horizontally (column wise).
 |      vstack : Stack arrays in sequence vertically (row wise).
 |      dstack : Stack arrays in sequence depth wise (along third dimension).
 |      column_stack : Stack 1-D arrays as columns into a 2-D array.
 |
 |      Notes
 |      -----
 |      When one or more of the arrays to be concatenated is a MaskedArray,
 |      this function will return a MaskedArray object instead of an ndarray,
 |      but the input masks are *not* preserved. In cases where a MaskedArray
 |      is expected as input, use the ma.concatenate function from the masked
 |      array module instead.
 |
 |      Examples
 |      --------
 |      >>> a = np.array([[1, 2], [3, 4]])
 |      >>> b = np.array([[5, 6]])
 |      >>> np.concatenate((a, b), axis=0)
 |      array([[1, 2],
 |             [3, 4],
 |             [5, 6]])
 |      >>> np.concatenate((a, b.T), axis=1)
 |      array([[1, 2, 5],
 |             [3, 4, 6]])
 |      >>> np.concatenate((a, b), axis=None)
 |      array([1, 2, 3, 4, 5, 6])
 |
 |      This function will not preserve masking of MaskedArray inputs.
 |
 |      >>> a = np.ma.arange(3)
 |      >>> a[1] = np.ma.masked
 |      >>> b = np.arange(2, 5)
 |      >>> a
 |      masked_array(data=[0, --, 2],
 |                   mask=[False,  True, False],
 |             fill_value=999999)
 |      >>> b
 |      array([2, 3, 4])
 |      >>> np.concatenate([a, b])
 |      masked_array(data=[0, 1, 2, 2, 3, 4],
 |                   mask=False,
 |             fill_value=999999)
 |      >>> np.ma.concatenate([a, b])
 |      masked_array(data=[0, --, 2, 2, 3, 4],
 |                   mask=[False,  True, False, False, False, False],
 |             fill_value=999999)
 |
 |  makemat = class matrix(ndarray)
 |   |  makemat(data, dtype=None, copy=True)
 |   |
 |   |  matrix(data, dtype=None, copy=True)
 |   |
 |   |  .. note:: It is no longer recommended to use this class, even for linear
 |   |            algebra. Instead use regular arrays. The class may be removed
 |   |            in the future.
 |   |
 |   |  Returns a matrix from an array-like object, or from a string of data.
 |   |  A matrix is a specialized 2-D array that retains its 2-D nature
 |   |  through operations.  It has certain special operators, such as ``*``
 |   |  (matrix multiplication) and ``**`` (matrix power).
 |   |
 |   |  Parameters
 |   |  ----------
 |   |  data : array_like or string
 |   |     If `data` is a string, it is interpreted as a matrix with commas
 |   |     or spaces separating columns, and semicolons separating rows.
 |   |  dtype : data-type
 |   |     Data-type of the output matrix.
 |   |  copy : bool
 |   |     If `data` is already an `ndarray`, then this flag determines
 |   |     whether the data is copied (the default), or whether a view is
 |   |     constructed.
 |   |
 |   |  See Also
 |   |  --------
 |   |  array
 |   |
 |   |  Examples
 |   |  --------
 |   |  >>> a = np.matrix('1 2; 3 4')
 |   |  >>> a
 |   |  matrix([[1, 2],
 |   |          [3, 4]])
 |   |
 |   |  >>> np.matrix([[1, 2], [3, 4]])
 |   |  matrix([[1, 2],
 |   |          [3, 4]])
 |   |
 |   |  Method resolution order:
 |   |      matrix
 |   |      ndarray
 |   |      builtins.object
 |   |
 |   |  Methods defined here:
 |   |
 |   |  __array_finalize__(self, obj)
 |   |      a.__array_finalize__(obj, /)
 |   |
 |   |      Present so subclasses can call super. Does nothing.
 |   |
 |   |  __getitem__(self, index)
 |   |      Return self[key].
 |   |
 |   |  __imul__(self, other)
 |   |      Return self*=value.
 |   |
 |   |  __ipow__(self, other)
 |   |      Return self**=value.
 |   |
 |   |  __mul__(self, other)
 |   |      Return self*value.
 |   |
 |   |  __pow__(self, other)
 |   |      Return pow(self, value, mod).
 |   |
 |   |  __rmul__(self, other)
 |   |      Return value*self.
 |   |
 |   |  __rpow__(self, other)
 |   |      Return pow(value, self, mod).
 |   |
 |   |  all(self, axis=None, out=None)
 |   |      Test whether all matrix elements along a given axis evaluate to True.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      See `numpy.all` for complete descriptions
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.all
 |   |
 |   |      Notes
 |   |      -----
 |   |      This is the same as `ndarray.all`, but it returns a `matrix` object.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.matrix(np.arange(12).reshape((3,4))); x
 |   |      matrix([[ 0,  1,  2,  3],
 |   |              [ 4,  5,  6,  7],
 |   |              [ 8,  9, 10, 11]])
 |   |      >>> y = x[0]; y
 |   |      matrix([[0, 1, 2, 3]])
 |   |      >>> (x == y)
 |   |      matrix([[ True,  True,  True,  True],
 |   |              [False, False, False, False],
 |   |              [False, False, False, False]])
 |   |      >>> (x == y).all()
 |   |      False
 |   |      >>> (x == y).all(0)
 |   |      matrix([[False, False, False, False]])
 |   |      >>> (x == y).all(1)
 |   |      matrix([[ True],
 |   |              [False],
 |   |              [False]])
 |   |
 |   |  any(self, axis=None, out=None)
 |   |      Test whether any array element along a given axis evaluates to True.
 |   |
 |   |      Refer to `numpy.any` for full documentation.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      axis : int, optional
 |   |          Axis along which logical OR is performed
 |   |      out : ndarray, optional
 |   |          Output to existing array instead of creating new one, must have
 |   |          same shape as expected output
 |   |
 |   |      Returns
 |   |      -------
 |   |          any : bool, ndarray
 |   |              Returns a single bool if `axis` is ``None``; otherwise,
 |   |              returns `ndarray`
 |   |
 |   |  argmax(self, axis=None, out=None)
 |   |      Indexes of the maximum values along an axis.
 |   |
 |   |      Return the indexes of the first occurrences of the maximum values
 |   |      along the specified axis.  If axis is None, the index is for the
 |   |      flattened matrix.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      See `numpy.argmax` for complete descriptions
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.argmax
 |   |
 |   |      Notes
 |   |      -----
 |   |      This is the same as `ndarray.argmax`, but returns a `matrix` object
 |   |      where `ndarray.argmax` would return an `ndarray`.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.matrix(np.arange(12).reshape((3,4))); x
 |   |      matrix([[ 0,  1,  2,  3],
 |   |              [ 4,  5,  6,  7],
 |   |              [ 8,  9, 10, 11]])
 |   |      >>> x.argmax()
 |   |      11
 |   |      >>> x.argmax(0)
 |   |      matrix([[2, 2, 2, 2]])
 |   |      >>> x.argmax(1)
 |   |      matrix([[3],
 |   |              [3],
 |   |              [3]])
 |   |
 |   |  argmin(self, axis=None, out=None)
 |   |      Indexes of the minimum values along an axis.
 |   |
 |   |      Return the indexes of the first occurrences of the minimum values
 |   |      along the specified axis.  If axis is None, the index is for the
 |   |      flattened matrix.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      See `numpy.argmin` for complete descriptions.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.argmin
 |   |
 |   |      Notes
 |   |      -----
 |   |      This is the same as `ndarray.argmin`, but returns a `matrix` object
 |   |      where `ndarray.argmin` would return an `ndarray`.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = -np.matrix(np.arange(12).reshape((3,4))); x
 |   |      matrix([[  0,  -1,  -2,  -3],
 |   |              [ -4,  -5,  -6,  -7],
 |   |              [ -8,  -9, -10, -11]])
 |   |      >>> x.argmin()
 |   |      11
 |   |      >>> x.argmin(0)
 |   |      matrix([[2, 2, 2, 2]])
 |   |      >>> x.argmin(1)
 |   |      matrix([[3],
 |   |              [3],
 |   |              [3]])
 |   |
 |   |  flatten(self, order='C')
 |   |      Return a flattened copy of the matrix.
 |   |
 |   |      All `N` elements of the matrix are placed into a single row.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      order : {'C', 'F', 'A', 'K'}, optional
 |   |          'C' means to flatten in row-major (C-style) order. 'F' means to
 |   |          flatten in column-major (Fortran-style) order. 'A' means to
 |   |          flatten in column-major order if `m` is Fortran *contiguous* in
 |   |          memory, row-major order otherwise. 'K' means to flatten `m` in
 |   |          the order the elements occur in memory. The default is 'C'.
 |   |
 |   |      Returns
 |   |      -------
 |   |      y : matrix
 |   |          A copy of the matrix, flattened to a `(1, N)` matrix where `N`
 |   |          is the number of elements in the original matrix.
 |   |
 |   |      See Also
 |   |      --------
 |   |      ravel : Return a flattened array.
 |   |      flat : A 1-D flat iterator over the matrix.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> m = np.matrix([[1,2], [3,4]])
 |   |      >>> m.flatten()
 |   |      matrix([[1, 2, 3, 4]])
 |   |      >>> m.flatten('F')
 |   |      matrix([[1, 3, 2, 4]])
 |   |
 |   |  getA = A(self)
 |   |      Return `self` as an `ndarray` object.
 |   |
 |   |      Equivalent to ``np.asarray(self)``.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      None
 |   |
 |   |      Returns
 |   |      -------
 |   |      ret : ndarray
 |   |          `self` as an `ndarray`
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.matrix(np.arange(12).reshape((3,4))); x
 |   |      matrix([[ 0,  1,  2,  3],
 |   |              [ 4,  5,  6,  7],
 |   |              [ 8,  9, 10, 11]])
 |   |      >>> x.getA()
 |   |      array([[ 0,  1,  2,  3],
 |   |             [ 4,  5,  6,  7],
 |   |             [ 8,  9, 10, 11]])
 |   |
 |   |  getA1 = A1(self)
 |   |      Return `self` as a flattened `ndarray`.
 |   |
 |   |      Equivalent to ``np.asarray(x).ravel()``
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      None
 |   |
 |   |      Returns
 |   |      -------
 |   |      ret : ndarray
 |   |          `self`, 1-D, as an `ndarray`
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.matrix(np.arange(12).reshape((3,4))); x
 |   |      matrix([[ 0,  1,  2,  3],
 |   |              [ 4,  5,  6,  7],
 |   |              [ 8,  9, 10, 11]])
 |   |      >>> x.getA1()
 |   |      array([ 0,  1,  2, ...,  9, 10, 11])
 |   |
 |   |  getH = H(self)
 |   |      Returns the (complex) conjugate transpose of `self`.
 |   |
 |   |      Equivalent to ``np.transpose(self)`` if `self` is real-valued.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      None
 |   |
 |   |      Returns
 |   |      -------
 |   |      ret : matrix object
 |   |          complex conjugate transpose of `self`
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.matrix(np.arange(12).reshape((3,4)))
 |   |      >>> z = x - 1j*x; z
 |   |      matrix([[  0. +0.j,   1. -1.j,   2. -2.j,   3. -3.j],
 |   |              [  4. -4.j,   5. -5.j,   6. -6.j,   7. -7.j],
 |   |              [  8. -8.j,   9. -9.j,  10.-10.j,  11.-11.j]])
 |   |      >>> z.getH()
 |   |      matrix([[ 0. -0.j,  4. +4.j,  8. +8.j],
 |   |              [ 1. +1.j,  5. +5.j,  9. +9.j],
 |   |              [ 2. +2.j,  6. +6.j, 10.+10.j],
 |   |              [ 3. +3.j,  7. +7.j, 11.+11.j]])
 |   |
 |   |  getI = I(self)
 |   |      Returns the (multiplicative) inverse of invertible `self`.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      None
 |   |
 |   |      Returns
 |   |      -------
 |   |      ret : matrix object
 |   |          If `self` is non-singular, `ret` is such that ``ret * self`` ==
 |   |          ``self * ret`` == ``np.matrix(np.eye(self[0,:].size))`` all return
 |   |          ``True``.
 |   |
 |   |      Raises
 |   |      ------
 |   |      numpy.linalg.LinAlgError: Singular matrix
 |   |          If `self` is singular.
 |   |
 |   |      See Also
 |   |      --------
 |   |      linalg.inv
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> m = np.matrix('[1, 2; 3, 4]'); m
 |   |      matrix([[1, 2],
 |   |              [3, 4]])
 |   |      >>> m.getI()
 |   |      matrix([[-2. ,  1. ],
 |   |              [ 1.5, -0.5]])
 |   |      >>> m.getI() * m
 |   |      matrix([[ 1.,  0.], # may vary
 |   |              [ 0.,  1.]])
 |   |
 |   |  getT = T(self)
 |   |      Returns the transpose of the matrix.
 |   |
 |   |      Does *not* conjugate!  For the complex conjugate transpose, use ``.H``.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      None
 |   |
 |   |      Returns
 |   |      -------
 |   |      ret : matrix object
 |   |          The (non-conjugated) transpose of the matrix.
 |   |
 |   |      See Also
 |   |      --------
 |   |      transpose, getH
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> m = np.matrix('[1, 2; 3, 4]')
 |   |      >>> m
 |   |      matrix([[1, 2],
 |   |              [3, 4]])
 |   |      >>> m.getT()
 |   |      matrix([[1, 3],
 |   |              [2, 4]])
 |   |
 |   |  max(self, axis=None, out=None)
 |   |      Return the maximum value along an axis.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      See `amax` for complete descriptions
 |   |
 |   |      See Also
 |   |      --------
 |   |      amax, ndarray.max
 |   |
 |   |      Notes
 |   |      -----
 |   |      This is the same as `ndarray.max`, but returns a `matrix` object
 |   |      where `ndarray.max` would return an ndarray.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.matrix(np.arange(12).reshape((3,4))); x
 |   |      matrix([[ 0,  1,  2,  3],
 |   |              [ 4,  5,  6,  7],
 |   |              [ 8,  9, 10, 11]])
 |   |      >>> x.max()
 |   |      11
 |   |      >>> x.max(0)
 |   |      matrix([[ 8,  9, 10, 11]])
 |   |      >>> x.max(1)
 |   |      matrix([[ 3],
 |   |              [ 7],
 |   |              [11]])
 |   |
 |   |  mean(self, axis=None, dtype=None, out=None)
 |   |      Returns the average of the matrix elements along the given axis.
 |   |
 |   |      Refer to `numpy.mean` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.mean
 |   |
 |   |      Notes
 |   |      -----
 |   |      Same as `ndarray.mean` except that, where that returns an `ndarray`,
 |   |      this returns a `matrix` object.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.matrix(np.arange(12).reshape((3, 4)))
 |   |      >>> x
 |   |      matrix([[ 0,  1,  2,  3],
 |   |              [ 4,  5,  6,  7],
 |   |              [ 8,  9, 10, 11]])
 |   |      >>> x.mean()
 |   |      5.5
 |   |      >>> x.mean(0)
 |   |      matrix([[4., 5., 6., 7.]])
 |   |      >>> x.mean(1)
 |   |      matrix([[ 1.5],
 |   |              [ 5.5],
 |   |              [ 9.5]])
 |   |
 |   |  min(self, axis=None, out=None)
 |   |      Return the minimum value along an axis.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      See `amin` for complete descriptions.
 |   |
 |   |      See Also
 |   |      --------
 |   |      amin, ndarray.min
 |   |
 |   |      Notes
 |   |      -----
 |   |      This is the same as `ndarray.min`, but returns a `matrix` object
 |   |      where `ndarray.min` would return an ndarray.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = -np.matrix(np.arange(12).reshape((3,4))); x
 |   |      matrix([[  0,  -1,  -2,  -3],
 |   |              [ -4,  -5,  -6,  -7],
 |   |              [ -8,  -9, -10, -11]])
 |   |      >>> x.min()
 |   |      -11
 |   |      >>> x.min(0)
 |   |      matrix([[ -8,  -9, -10, -11]])
 |   |      >>> x.min(1)
 |   |      matrix([[ -3],
 |   |              [ -7],
 |   |              [-11]])
 |   |
 |   |  prod(self, axis=None, dtype=None, out=None)
 |   |      Return the product of the array elements over the given axis.
 |   |
 |   |      Refer to `prod` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      prod, ndarray.prod
 |   |
 |   |      Notes
 |   |      -----
 |   |      Same as `ndarray.prod`, except, where that returns an `ndarray`, this
 |   |      returns a `matrix` object instead.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.matrix(np.arange(12).reshape((3,4))); x
 |   |      matrix([[ 0,  1,  2,  3],
 |   |              [ 4,  5,  6,  7],
 |   |              [ 8,  9, 10, 11]])
 |   |      >>> x.prod()
 |   |      0
 |   |      >>> x.prod(0)
 |   |      matrix([[  0,  45, 120, 231]])
 |   |      >>> x.prod(1)
 |   |      matrix([[   0],
 |   |              [ 840],
 |   |              [7920]])
 |   |
 |   |  ptp(self, axis=None, out=None)
 |   |      Peak-to-peak (maximum - minimum) value along the given axis.
 |   |
 |   |      Refer to `numpy.ptp` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.ptp
 |   |
 |   |      Notes
 |   |      -----
 |   |      Same as `ndarray.ptp`, except, where that would return an `ndarray` object,
 |   |      this returns a `matrix` object.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.matrix(np.arange(12).reshape((3,4))); x
 |   |      matrix([[ 0,  1,  2,  3],
 |   |              [ 4,  5,  6,  7],
 |   |              [ 8,  9, 10, 11]])
 |   |      >>> x.ptp()
 |   |      11
 |   |      >>> x.ptp(0)
 |   |      matrix([[8, 8, 8, 8]])
 |   |      >>> x.ptp(1)
 |   |      matrix([[3],
 |   |              [3],
 |   |              [3]])
 |   |
 |   |  ravel(self, order='C')
 |   |      Return a flattened matrix.
 |   |
 |   |      Refer to `numpy.ravel` for more documentation.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      order : {'C', 'F', 'A', 'K'}, optional
 |   |          The elements of `m` are read using this index order. 'C' means to
 |   |          index the elements in C-like order, with the last axis index
 |   |          changing fastest, back to the first axis index changing slowest.
 |   |          'F' means to index the elements in Fortran-like index order, with
 |   |          the first index changing fastest, and the last index changing
 |   |          slowest. Note that the 'C' and 'F' options take no account of the
 |   |          memory layout of the underlying array, and only refer to the order
 |   |          of axis indexing.  'A' means to read the elements in Fortran-like
 |   |          index order if `m` is Fortran *contiguous* in memory, C-like order
 |   |          otherwise.  'K' means to read the elements in the order they occur
 |   |          in memory, except for reversing the data when strides are negative.
 |   |          By default, 'C' index order is used.
 |   |
 |   |      Returns
 |   |      -------
 |   |      ret : matrix
 |   |          Return the matrix flattened to shape `(1, N)` where `N`
 |   |          is the number of elements in the original matrix.
 |   |          A copy is made only if necessary.
 |   |
 |   |      See Also
 |   |      --------
 |   |      matrix.flatten : returns a similar output matrix but always a copy
 |   |      matrix.flat : a flat iterator on the array.
 |   |      numpy.ravel : related function which returns an ndarray
 |   |
 |   |  squeeze(self, axis=None)
 |   |      Return a possibly reshaped matrix.
 |   |
 |   |      Refer to `numpy.squeeze` for more documentation.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      axis : None or int or tuple of ints, optional
 |   |          Selects a subset of the axes of length one in the shape.
 |   |          If an axis is selected with shape entry greater than one,
 |   |          an error is raised.
 |   |
 |   |      Returns
 |   |      -------
 |   |      squeezed : matrix
 |   |          The matrix, but as a (1, N) matrix if it had shape (N, 1).
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.squeeze : related function
 |   |
 |   |      Notes
 |   |      -----
 |   |      If `m` has a single column then that column is returned
 |   |      as the single row of a matrix.  Otherwise `m` is returned.
 |   |      The returned matrix is always either `m` itself or a view into `m`.
 |   |      Supplying an axis keyword argument will not affect the returned matrix
 |   |      but it may cause an error to be raised.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> c = np.matrix([[1], [2]])
 |   |      >>> c
 |   |      matrix([[1],
 |   |              [2]])
 |   |      >>> c.squeeze()
 |   |      matrix([[1, 2]])
 |   |      >>> r = c.T
 |   |      >>> r
 |   |      matrix([[1, 2]])
 |   |      >>> r.squeeze()
 |   |      matrix([[1, 2]])
 |   |      >>> m = np.matrix([[1, 2], [3, 4]])
 |   |      >>> m.squeeze()
 |   |      matrix([[1, 2],
 |   |              [3, 4]])
 |   |
 |   |  std(self, axis=None, dtype=None, out=None, ddof=0)
 |   |      Return the standard deviation of the array elements along the given axis.
 |   |
 |   |      Refer to `numpy.std` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.std
 |   |
 |   |      Notes
 |   |      -----
 |   |      This is the same as `ndarray.std`, except that where an `ndarray` would
 |   |      be returned, a `matrix` object is returned instead.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.matrix(np.arange(12).reshape((3, 4)))
 |   |      >>> x
 |   |      matrix([[ 0,  1,  2,  3],
 |   |              [ 4,  5,  6,  7],
 |   |              [ 8,  9, 10, 11]])
 |   |      >>> x.std()
 |   |      3.4520525295346629 # may vary
 |   |      >>> x.std(0)
 |   |      matrix([[ 3.26598632,  3.26598632,  3.26598632,  3.26598632]]) # may vary
 |   |      >>> x.std(1)
 |   |      matrix([[ 1.11803399],
 |   |              [ 1.11803399],
 |   |              [ 1.11803399]])
 |   |
 |   |  sum(self, axis=None, dtype=None, out=None)
 |   |      Returns the sum of the matrix elements, along the given axis.
 |   |
 |   |      Refer to `numpy.sum` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.sum
 |   |
 |   |      Notes
 |   |      -----
 |   |      This is the same as `ndarray.sum`, except that where an `ndarray` would
 |   |      be returned, a `matrix` object is returned instead.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.matrix([[1, 2], [4, 3]])
 |   |      >>> x.sum()
 |   |      10
 |   |      >>> x.sum(axis=1)
 |   |      matrix([[3],
 |   |              [7]])
 |   |      >>> x.sum(axis=1, dtype='float')
 |   |      matrix([[3.],
 |   |              [7.]])
 |   |      >>> out = np.zeros((2, 1), dtype='float')
 |   |      >>> x.sum(axis=1, dtype='float', out=np.asmatrix(out))
 |   |      matrix([[3.],
 |   |              [7.]])
 |   |
 |   |  tolist(self)
 |   |      Return the matrix as a (possibly nested) list.
 |   |
 |   |      See `ndarray.tolist` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      ndarray.tolist
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.matrix(np.arange(12).reshape((3,4))); x
 |   |      matrix([[ 0,  1,  2,  3],
 |   |              [ 4,  5,  6,  7],
 |   |              [ 8,  9, 10, 11]])
 |   |      >>> x.tolist()
 |   |      [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
 |   |
 |   |  var(self, axis=None, dtype=None, out=None, ddof=0)
 |   |      Returns the variance of the matrix elements, along the given axis.
 |   |
 |   |      Refer to `numpy.var` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.var
 |   |
 |   |      Notes
 |   |      -----
 |   |      This is the same as `ndarray.var`, except that where an `ndarray` would
 |   |      be returned, a `matrix` object is returned instead.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.matrix(np.arange(12).reshape((3, 4)))
 |   |      >>> x
 |   |      matrix([[ 0,  1,  2,  3],
 |   |              [ 4,  5,  6,  7],
 |   |              [ 8,  9, 10, 11]])
 |   |      >>> x.var()
 |   |      11.916666666666666
 |   |      >>> x.var(0)
 |   |      matrix([[ 10.66666667,  10.66666667,  10.66666667,  10.66666667]]) # may vary
 |   |      >>> x.var(1)
 |   |      matrix([[1.25],
 |   |              [1.25],
 |   |              [1.25]])
 |   |
 |   |  ----------------------------------------------------------------------
 |   |  Static methods defined here:
 |   |
 |   |  __new__(subtype, data, dtype=None, copy=True)
 |   |      Create and return a new object.  See help(type) for accurate signature.
 |   |
 |   |  ----------------------------------------------------------------------
 |   |  Readonly properties defined here:
 |   |
 |   |  A
 |   |      Return `self` as an `ndarray` object.
 |   |
 |   |      Equivalent to ``np.asarray(self)``.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      None
 |   |
 |   |      Returns
 |   |      -------
 |   |      ret : ndarray
 |   |          `self` as an `ndarray`
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.matrix(np.arange(12).reshape((3,4))); x
 |   |      matrix([[ 0,  1,  2,  3],
 |   |              [ 4,  5,  6,  7],
 |   |              [ 8,  9, 10, 11]])
 |   |      >>> x.getA()
 |   |      array([[ 0,  1,  2,  3],
 |   |             [ 4,  5,  6,  7],
 |   |             [ 8,  9, 10, 11]])
 |   |
 |   |  A1
 |   |      Return `self` as a flattened `ndarray`.
 |   |
 |   |      Equivalent to ``np.asarray(x).ravel()``
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      None
 |   |
 |   |      Returns
 |   |      -------
 |   |      ret : ndarray
 |   |          `self`, 1-D, as an `ndarray`
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.matrix(np.arange(12).reshape((3,4))); x
 |   |      matrix([[ 0,  1,  2,  3],
 |   |              [ 4,  5,  6,  7],
 |   |              [ 8,  9, 10, 11]])
 |   |      >>> x.getA1()
 |   |      array([ 0,  1,  2, ...,  9, 10, 11])
 |   |
 |   |  H
 |   |      Returns the (complex) conjugate transpose of `self`.
 |   |
 |   |      Equivalent to ``np.transpose(self)`` if `self` is real-valued.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      None
 |   |
 |   |      Returns
 |   |      -------
 |   |      ret : matrix object
 |   |          complex conjugate transpose of `self`
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.matrix(np.arange(12).reshape((3,4)))
 |   |      >>> z = x - 1j*x; z
 |   |      matrix([[  0. +0.j,   1. -1.j,   2. -2.j,   3. -3.j],
 |   |              [  4. -4.j,   5. -5.j,   6. -6.j,   7. -7.j],
 |   |              [  8. -8.j,   9. -9.j,  10.-10.j,  11.-11.j]])
 |   |      >>> z.getH()
 |   |      matrix([[ 0. -0.j,  4. +4.j,  8. +8.j],
 |   |              [ 1. +1.j,  5. +5.j,  9. +9.j],
 |   |              [ 2. +2.j,  6. +6.j, 10.+10.j],
 |   |              [ 3. +3.j,  7. +7.j, 11.+11.j]])
 |   |
 |   |  I
 |   |      Returns the (multiplicative) inverse of invertible `self`.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      None
 |   |
 |   |      Returns
 |   |      -------
 |   |      ret : matrix object
 |   |          If `self` is non-singular, `ret` is such that ``ret * self`` ==
 |   |          ``self * ret`` == ``np.matrix(np.eye(self[0,:].size))`` all return
 |   |          ``True``.
 |   |
 |   |      Raises
 |   |      ------
 |   |      numpy.linalg.LinAlgError: Singular matrix
 |   |          If `self` is singular.
 |   |
 |   |      See Also
 |   |      --------
 |   |      linalg.inv
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> m = np.matrix('[1, 2; 3, 4]'); m
 |   |      matrix([[1, 2],
 |   |              [3, 4]])
 |   |      >>> m.getI()
 |   |      matrix([[-2. ,  1. ],
 |   |              [ 1.5, -0.5]])
 |   |      >>> m.getI() * m
 |   |      matrix([[ 1.,  0.], # may vary
 |   |              [ 0.,  1.]])
 |   |
 |   |  T
 |   |      Returns the transpose of the matrix.
 |   |
 |   |      Does *not* conjugate!  For the complex conjugate transpose, use ``.H``.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      None
 |   |
 |   |      Returns
 |   |      -------
 |   |      ret : matrix object
 |   |          The (non-conjugated) transpose of the matrix.
 |   |
 |   |      See Also
 |   |      --------
 |   |      transpose, getH
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> m = np.matrix('[1, 2; 3, 4]')
 |   |      >>> m
 |   |      matrix([[1, 2],
 |   |              [3, 4]])
 |   |      >>> m.getT()
 |   |      matrix([[1, 3],
 |   |              [2, 4]])
 |   |
 |   |  ----------------------------------------------------------------------
 |   |  Data descriptors defined here:
 |   |
 |   |  __dict__
 |   |      dictionary for instance variables
 |   |
 |   |  ----------------------------------------------------------------------
 |   |  Data and other attributes defined here:
 |   |
 |   |  __annotations__ = {}
 |   |
 |   |  __array_priority__ = 10.0
 |   |
 |   |  ----------------------------------------------------------------------
 |   |  Methods inherited from ndarray:
 |   |
 |   |  __abs__(self, /)
 |   |      abs(self)
 |   |
 |   |  __add__(self, value, /)
 |   |      Return self+value.
 |   |
 |   |  __and__(self, value, /)
 |   |      Return self&value.
 |   |
 |   |  __array__(...)
 |   |      a.__array__([dtype], /)
 |   |
 |   |      Returns either a new reference to self if dtype is not given or a new array
 |   |      of provided data type if dtype is different from the current dtype of the
 |   |      array.
 |   |
 |   |  __array_function__(...)
 |   |
 |   |  __array_prepare__(...)
 |   |      a.__array_prepare__(array[, context], /)
 |   |
 |   |      Returns a view of `array` with the same type as self.
 |   |
 |   |  __array_ufunc__(...)
 |   |
 |   |  __array_wrap__(...)
 |   |      a.__array_wrap__(array[, context], /)
 |   |
 |   |      Returns a view of `array` with the same type as self.
 |   |
 |   |  __bool__(self, /)
 |   |      True if self else False
 |   |
 |   |  __buffer__(self, flags, /)
 |   |      Return a buffer object that exposes the underlying memory of the object.
 |   |
 |   |  __complex__(...)
 |   |
 |   |  __contains__(self, key, /)
 |   |      Return bool(key in self).
 |   |
 |   |  __copy__(...)
 |   |      a.__copy__()
 |   |
 |   |      Used if :func:`copy.copy` is called on an array. Returns a copy of the array.
 |   |
 |   |      Equivalent to ``a.copy(order='K')``.
 |   |
 |   |  __deepcopy__(...)
 |   |      a.__deepcopy__(memo, /)
 |   |
 |   |      Used if :func:`copy.deepcopy` is called on an array.
 |   |
 |   |  __delitem__(self, key, /)
 |   |      Delete self[key].
 |   |
 |   |  __divmod__(self, value, /)
 |   |      Return divmod(self, value).
 |   |
 |   |  __dlpack__(...)
 |   |      a.__dlpack__(*, stream=None)
 |   |
 |   |      DLPack Protocol: Part of the Array API.
 |   |
 |   |  __dlpack_device__(...)
 |   |      a.__dlpack_device__()
 |   |
 |   |      DLPack Protocol: Part of the Array API.
 |   |
 |   |  __eq__(self, value, /)
 |   |      Return self==value.
 |   |
 |   |  __float__(self, /)
 |   |      float(self)
 |   |
 |   |  __floordiv__(self, value, /)
 |   |      Return self//value.
 |   |
 |   |  __format__(...)
 |   |      Default object formatter.
 |   |
 |   |      Return str(self) if format_spec is empty. Raise TypeError otherwise.
 |   |
 |   |  __ge__(self, value, /)
 |   |      Return self>=value.
 |   |
 |   |  __gt__(self, value, /)
 |   |      Return self>value.
 |   |
 |   |  __iadd__(self, value, /)
 |   |      Return self+=value.
 |   |
 |   |  __iand__(self, value, /)
 |   |      Return self&=value.
 |   |
 |   |  __ifloordiv__(self, value, /)
 |   |      Return self//=value.
 |   |
 |   |  __ilshift__(self, value, /)
 |   |      Return self<<=value.
 |   |
 |   |  __imatmul__(self, value, /)
 |   |      Return self@=value.
 |   |
 |   |  __imod__(self, value, /)
 |   |      Return self%=value.
 |   |
 |   |  __index__(self, /)
 |   |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |   |
 |   |  __int__(self, /)
 |   |      int(self)
 |   |
 |   |  __invert__(self, /)
 |   |      ~self
 |   |
 |   |  __ior__(self, value, /)
 |   |      Return self|=value.
 |   |
 |   |  __irshift__(self, value, /)
 |   |      Return self>>=value.
 |   |
 |   |  __isub__(self, value, /)
 |   |      Return self-=value.
 |   |
 |   |  __iter__(self, /)
 |   |      Implement iter(self).
 |   |
 |   |  __itruediv__(self, value, /)
 |   |      Return self/=value.
 |   |
 |   |  __ixor__(self, value, /)
 |   |      Return self^=value.
 |   |
 |   |  __le__(self, value, /)
 |   |      Return self<=value.
 |   |
 |   |  __len__(self, /)
 |   |      Return len(self).
 |   |
 |   |  __lshift__(self, value, /)
 |   |      Return self<<value.
 |   |
 |   |  __lt__(self, value, /)
 |   |      Return self<value.
 |   |
 |   |  __matmul__(self, value, /)
 |   |      Return self@value.
 |   |
 |   |  __mod__(self, value, /)
 |   |      Return self%value.
 |   |
 |   |  __ne__(self, value, /)
 |   |      Return self!=value.
 |   |
 |   |  __neg__(self, /)
 |   |      -self
 |   |
 |   |  __or__(self, value, /)
 |   |      Return self|value.
 |   |
 |   |  __pos__(self, /)
 |   |      +self
 |   |
 |   |  __radd__(self, value, /)
 |   |      Return value+self.
 |   |
 |   |  __rand__(self, value, /)
 |   |      Return value&self.
 |   |
 |   |  __rdivmod__(self, value, /)
 |   |      Return divmod(value, self).
 |   |
 |   |  __reduce__(...)
 |   |      a.__reduce__()
 |   |
 |   |      For pickling.
 |   |
 |   |  __reduce_ex__(...)
 |   |      Helper for pickle.
 |   |
 |   |  __repr__(self, /)
 |   |      Return repr(self).
 |   |
 |   |  __rfloordiv__(self, value, /)
 |   |      Return value//self.
 |   |
 |   |  __rlshift__(self, value, /)
 |   |      Return value<<self.
 |   |
 |   |  __rmatmul__(self, value, /)
 |   |      Return value@self.
 |   |
 |   |  __rmod__(self, value, /)
 |   |      Return value%self.
 |   |
 |   |  __ror__(self, value, /)
 |   |      Return value|self.
 |   |
 |   |  __rrshift__(self, value, /)
 |   |      Return value>>self.
 |   |
 |   |  __rshift__(self, value, /)
 |   |      Return self>>value.
 |   |
 |   |  __rsub__(self, value, /)
 |   |      Return value-self.
 |   |
 |   |  __rtruediv__(self, value, /)
 |   |      Return value/self.
 |   |
 |   |  __rxor__(self, value, /)
 |   |      Return value^self.
 |   |
 |   |  __setitem__(self, key, value, /)
 |   |      Set self[key] to value.
 |   |
 |   |  __setstate__(...)
 |   |      a.__setstate__(state, /)
 |   |
 |   |      For unpickling.
 |   |
 |   |      The `state` argument must be a sequence that contains the following
 |   |      elements:
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      version : int
 |   |          optional pickle version. If omitted defaults to 0.
 |   |      shape : tuple
 |   |      dtype : data-type
 |   |      isFortran : bool
 |   |      rawdata : string or list
 |   |          a binary string with the data (or a list if 'a' is an object array)
 |   |
 |   |  __sizeof__(...)
 |   |      Size of object in memory, in bytes.
 |   |
 |   |  __str__(self, /)
 |   |      Return str(self).
 |   |
 |   |  __sub__(self, value, /)
 |   |      Return self-value.
 |   |
 |   |  __truediv__(self, value, /)
 |   |      Return self/value.
 |   |
 |   |  __xor__(self, value, /)
 |   |      Return self^value.
 |   |
 |   |  argpartition(...)
 |   |      a.argpartition(kth, axis=-1, kind='introselect', order=None)
 |   |
 |   |      Returns the indices that would partition this array.
 |   |
 |   |      Refer to `numpy.argpartition` for full documentation.
 |   |
 |   |      .. versionadded:: 1.8.0
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.argpartition : equivalent function
 |   |
 |   |  argsort(...)
 |   |      a.argsort(axis=-1, kind=None, order=None)
 |   |
 |   |      Returns the indices that would sort this array.
 |   |
 |   |      Refer to `numpy.argsort` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.argsort : equivalent function
 |   |
 |   |  astype(...)
 |   |      a.astype(dtype, order='K', casting='unsafe', subok=True, copy=True)
 |   |
 |   |      Copy of the array, cast to a specified type.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      dtype : str or dtype
 |   |          Typecode or data-type to which the array is cast.
 |   |      order : {'C', 'F', 'A', 'K'}, optional
 |   |          Controls the memory layout order of the result.
 |   |          'C' means C order, 'F' means Fortran order, 'A'
 |   |          means 'F' order if all the arrays are Fortran contiguous,
 |   |          'C' order otherwise, and 'K' means as close to the
 |   |          order the array elements appear in memory as possible.
 |   |          Default is 'K'.
 |   |      casting : {'no', 'equiv', 'safe', 'same_kind', 'unsafe'}, optional
 |   |          Controls what kind of data casting may occur. Defaults to 'unsafe'
 |   |          for backwards compatibility.
 |   |
 |   |            * 'no' means the data types should not be cast at all.
 |   |            * 'equiv' means only byte-order changes are allowed.
 |   |            * 'safe' means only casts which can preserve values are allowed.
 |   |            * 'same_kind' means only safe casts or casts within a kind,
 |   |              like float64 to float32, are allowed.
 |   |            * 'unsafe' means any data conversions may be done.
 |   |      subok : bool, optional
 |   |          If True, then sub-classes will be passed-through (default), otherwise
 |   |          the returned array will be forced to be a base-class array.
 |   |      copy : bool, optional
 |   |          By default, astype always returns a newly allocated array. If this
 |   |          is set to false, and the `dtype`, `order`, and `subok`
 |   |          requirements are satisfied, the input array is returned instead
 |   |          of a copy.
 |   |
 |   |      Returns
 |   |      -------
 |   |      arr_t : ndarray
 |   |          Unless `copy` is False and the other conditions for returning the input
 |   |          array are satisfied (see description for `copy` input parameter), `arr_t`
 |   |          is a new array of the same shape as the input array, with dtype, order
 |   |          given by `dtype`, `order`.
 |   |
 |   |      Notes
 |   |      -----
 |   |      .. versionchanged:: 1.17.0
 |   |         Casting between a simple data type and a structured one is possible only
 |   |         for "unsafe" casting.  Casting to multiple fields is allowed, but
 |   |         casting from multiple fields is not.
 |   |
 |   |      .. versionchanged:: 1.9.0
 |   |         Casting from numeric to string types in 'safe' casting mode requires
 |   |         that the string dtype length is long enough to store the max
 |   |         integer/float value converted.
 |   |
 |   |      Raises
 |   |      ------
 |   |      ComplexWarning
 |   |          When casting from complex to float or int. To avoid this,
 |   |          one should use ``a.real.astype(t)``.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.array([1, 2, 2.5])
 |   |      >>> x
 |   |      array([1. ,  2. ,  2.5])
 |   |
 |   |      >>> x.astype(int)
 |   |      array([1, 2, 2])
 |   |
 |   |  byteswap(...)
 |   |      a.byteswap(inplace=False)
 |   |
 |   |      Swap the bytes of the array elements
 |   |
 |   |      Toggle between low-endian and big-endian data representation by
 |   |      returning a byteswapped array, optionally swapped in-place.
 |   |      Arrays of byte-strings are not swapped. The real and imaginary
 |   |      parts of a complex number are swapped individually.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      inplace : bool, optional
 |   |          If ``True``, swap bytes in-place, default is ``False``.
 |   |
 |   |      Returns
 |   |      -------
 |   |      out : ndarray
 |   |          The byteswapped array. If `inplace` is ``True``, this is
 |   |          a view to self.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> A = np.array([1, 256, 8755], dtype=np.int16)
 |   |      >>> list(map(hex, A))
 |   |      ['0x1', '0x100', '0x2233']
 |   |      >>> A.byteswap(inplace=True)
 |   |      array([  256,     1, 13090], dtype=int16)
 |   |      >>> list(map(hex, A))
 |   |      ['0x100', '0x1', '0x3322']
 |   |
 |   |      Arrays of byte-strings are not swapped
 |   |
 |   |      >>> A = np.array([b'ceg', b'fac'])
 |   |      >>> A.byteswap()
 |   |      array([b'ceg', b'fac'], dtype='|S3')
 |   |
 |   |      ``A.newbyteorder().byteswap()`` produces an array with the same values
 |   |        but different representation in memory
 |   |
 |   |      >>> A = np.array([1, 2, 3])
 |   |      >>> A.view(np.uint8)
 |   |      array([1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0,
 |   |             0, 0], dtype=uint8)
 |   |      >>> A.newbyteorder().byteswap(inplace=True)
 |   |      array([1, 2, 3])
 |   |      >>> A.view(np.uint8)
 |   |      array([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0,
 |   |             0, 3], dtype=uint8)
 |   |
 |   |  choose(...)
 |   |      a.choose(choices, out=None, mode='raise')
 |   |
 |   |      Use an index array to construct a new array from a set of choices.
 |   |
 |   |      Refer to `numpy.choose` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.choose : equivalent function
 |   |
 |   |  clip(...)
 |   |      a.clip(min=None, max=None, out=None, **kwargs)
 |   |
 |   |      Return an array whose values are limited to ``[min, max]``.
 |   |      One of max or min must be given.
 |   |
 |   |      Refer to `numpy.clip` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.clip : equivalent function
 |   |
 |   |  compress(...)
 |   |      a.compress(condition, axis=None, out=None)
 |   |
 |   |      Return selected slices of this array along given axis.
 |   |
 |   |      Refer to `numpy.compress` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.compress : equivalent function
 |   |
 |   |  conj(...)
 |   |      a.conj()
 |   |
 |   |      Complex-conjugate all elements.
 |   |
 |   |      Refer to `numpy.conjugate` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.conjugate : equivalent function
 |   |
 |   |  conjugate(...)
 |   |      a.conjugate()
 |   |
 |   |      Return the complex conjugate, element-wise.
 |   |
 |   |      Refer to `numpy.conjugate` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.conjugate : equivalent function
 |   |
 |   |  copy(...)
 |   |      a.copy(order='C')
 |   |
 |   |      Return a copy of the array.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      order : {'C', 'F', 'A', 'K'}, optional
 |   |          Controls the memory layout of the copy. 'C' means C-order,
 |   |          'F' means F-order, 'A' means 'F' if `a` is Fortran contiguous,
 |   |          'C' otherwise. 'K' means match the layout of `a` as closely
 |   |          as possible. (Note that this function and :func:`numpy.copy` are very
 |   |          similar but have different default values for their order=
 |   |          arguments, and this function always passes sub-classes through.)
 |   |
 |   |      See also
 |   |      --------
 |   |      numpy.copy : Similar function with different default behavior
 |   |      numpy.copyto
 |   |
 |   |      Notes
 |   |      -----
 |   |      This function is the preferred method for creating an array copy.  The
 |   |      function :func:`numpy.copy` is similar, but it defaults to using order 'K',
 |   |      and will not pass sub-classes through by default.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.array([[1,2,3],[4,5,6]], order='F')
 |   |
 |   |      >>> y = x.copy()
 |   |
 |   |      >>> x.fill(0)
 |   |
 |   |      >>> x
 |   |      array([[0, 0, 0],
 |   |             [0, 0, 0]])
 |   |
 |   |      >>> y
 |   |      array([[1, 2, 3],
 |   |             [4, 5, 6]])
 |   |
 |   |      >>> y.flags['C_CONTIGUOUS']
 |   |      True
 |   |
 |   |  cumprod(...)
 |   |      a.cumprod(axis=None, dtype=None, out=None)
 |   |
 |   |      Return the cumulative product of the elements along the given axis.
 |   |
 |   |      Refer to `numpy.cumprod` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.cumprod : equivalent function
 |   |
 |   |  cumsum(...)
 |   |      a.cumsum(axis=None, dtype=None, out=None)
 |   |
 |   |      Return the cumulative sum of the elements along the given axis.
 |   |
 |   |      Refer to `numpy.cumsum` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.cumsum : equivalent function
 |   |
 |   |  diagonal(...)
 |   |      a.diagonal(offset=0, axis1=0, axis2=1)
 |   |
 |   |      Return specified diagonals. In NumPy 1.9 the returned array is a
 |   |      read-only view instead of a copy as in previous NumPy versions.  In
 |   |      a future version the read-only restriction will be removed.
 |   |
 |   |      Refer to :func:`numpy.diagonal` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.diagonal : equivalent function
 |   |
 |   |  dot(...)
 |   |
 |   |  dump(...)
 |   |      a.dump(file)
 |   |
 |   |      Dump a pickle of the array to the specified file.
 |   |      The array can be read back with pickle.load or numpy.load.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      file : str or Path
 |   |          A string naming the dump file.
 |   |
 |   |          .. versionchanged:: 1.17.0
 |   |              `pathlib.Path` objects are now accepted.
 |   |
 |   |  dumps(...)
 |   |      a.dumps()
 |   |
 |   |      Returns the pickle of the array as a string.
 |   |      pickle.loads will convert the string back to an array.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      None
 |   |
 |   |  fill(...)
 |   |      a.fill(value)
 |   |
 |   |      Fill the array with a scalar value.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      value : scalar
 |   |          All elements of `a` will be assigned this value.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> a = np.array([1, 2])
 |   |      >>> a.fill(0)
 |   |      >>> a
 |   |      array([0, 0])
 |   |      >>> a = np.empty(2)
 |   |      >>> a.fill(1)
 |   |      >>> a
 |   |      array([1.,  1.])
 |   |
 |   |      Fill expects a scalar value and always behaves the same as assigning
 |   |      to a single array element.  The following is a rare example where this
 |   |      distinction is important:
 |   |
 |   |      >>> a = np.array([None, None], dtype=object)
 |   |      >>> a[0] = np.array(3)
 |   |      >>> a
 |   |      array([array(3), None], dtype=object)
 |   |      >>> a.fill(np.array(3))
 |   |      >>> a
 |   |      array([array(3), array(3)], dtype=object)
 |   |
 |   |      Where other forms of assignments will unpack the array being assigned:
 |   |
 |   |      >>> a[...] = np.array(3)
 |   |      >>> a
 |   |      array([3, 3], dtype=object)
 |   |
 |   |  getfield(...)
 |   |      a.getfield(dtype, offset=0)
 |   |
 |   |      Returns a field of the given array as a certain type.
 |   |
 |   |      A field is a view of the array data with a given data-type. The values in
 |   |      the view are determined by the given type and the offset into the current
 |   |      array in bytes. The offset needs to be such that the view dtype fits in the
 |   |      array dtype; for example an array of dtype complex128 has 16-byte elements.
 |   |      If taking a view with a 32-bit integer (4 bytes), the offset needs to be
 |   |      between 0 and 12 bytes.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      dtype : str or dtype
 |   |          The data type of the view. The dtype size of the view can not be larger
 |   |          than that of the array itself.
 |   |      offset : int
 |   |          Number of bytes to skip before beginning the element view.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.diag([1.+1.j]*2)
 |   |      >>> x[1, 1] = 2 + 4.j
 |   |      >>> x
 |   |      array([[1.+1.j,  0.+0.j],
 |   |             [0.+0.j,  2.+4.j]])
 |   |      >>> x.getfield(np.float64)
 |   |      array([[1.,  0.],
 |   |             [0.,  2.]])
 |   |
 |   |      By choosing an offset of 8 bytes we can select the complex part of the
 |   |      array for our view:
 |   |
 |   |      >>> x.getfield(np.float64, offset=8)
 |   |      array([[1.,  0.],
 |   |             [0.,  4.]])
 |   |
 |   |  item(...)
 |   |      a.item(*args)
 |   |
 |   |      Copy an element of an array to a standard Python scalar and return it.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      \*args : Arguments (variable number and type)
 |   |
 |   |          * none: in this case, the method only works for arrays
 |   |            with one element (`a.size == 1`), which element is
 |   |            copied into a standard Python scalar object and returned.
 |   |
 |   |          * int_type: this argument is interpreted as a flat index into
 |   |            the array, specifying which element to copy and return.
 |   |
 |   |          * tuple of int_types: functions as does a single int_type argument,
 |   |            except that the argument is interpreted as an nd-index into the
 |   |            array.
 |   |
 |   |      Returns
 |   |      -------
 |   |      z : Standard Python scalar object
 |   |          A copy of the specified element of the array as a suitable
 |   |          Python scalar
 |   |
 |   |      Notes
 |   |      -----
 |   |      When the data type of `a` is longdouble or clongdouble, item() returns
 |   |      a scalar array object because there is no available Python scalar that
 |   |      would not lose information. Void arrays return a buffer object for item(),
 |   |      unless fields are defined, in which case a tuple is returned.
 |   |
 |   |      `item` is very similar to a[args], except, instead of an array scalar,
 |   |      a standard Python scalar is returned. This can be useful for speeding up
 |   |      access to elements of the array and doing arithmetic on elements of the
 |   |      array using Python's optimized math.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> np.random.seed(123)
 |   |      >>> x = np.random.randint(9, size=(3, 3))
 |   |      >>> x
 |   |      array([[2, 2, 6],
 |   |             [1, 3, 6],
 |   |             [1, 0, 1]])
 |   |      >>> x.item(3)
 |   |      1
 |   |      >>> x.item(7)
 |   |      0
 |   |      >>> x.item((0, 1))
 |   |      2
 |   |      >>> x.item((2, 2))
 |   |      1
 |   |
 |   |  itemset(...)
 |   |      a.itemset(*args)
 |   |
 |   |      Insert scalar into an array (scalar is cast to array's dtype, if possible)
 |   |
 |   |      There must be at least 1 argument, and define the last argument
 |   |      as *item*.  Then, ``a.itemset(*args)`` is equivalent to but faster
 |   |      than ``a[args] = item``.  The item should be a scalar value and `args`
 |   |      must select a single item in the array `a`.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      \*args : Arguments
 |   |          If one argument: a scalar, only used in case `a` is of size 1.
 |   |          If two arguments: the last argument is the value to be set
 |   |          and must be a scalar, the first argument specifies a single array
 |   |          element location. It is either an int or a tuple.
 |   |
 |   |      Notes
 |   |      -----
 |   |      Compared to indexing syntax, `itemset` provides some speed increase
 |   |      for placing a scalar into a particular location in an `ndarray`,
 |   |      if you must do this.  However, generally this is discouraged:
 |   |      among other problems, it complicates the appearance of the code.
 |   |      Also, when using `itemset` (and `item`) inside a loop, be sure
 |   |      to assign the methods to a local variable to avoid the attribute
 |   |      look-up at each loop iteration.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> np.random.seed(123)
 |   |      >>> x = np.random.randint(9, size=(3, 3))
 |   |      >>> x
 |   |      array([[2, 2, 6],
 |   |             [1, 3, 6],
 |   |             [1, 0, 1]])
 |   |      >>> x.itemset(4, 0)
 |   |      >>> x.itemset((2, 2), 9)
 |   |      >>> x
 |   |      array([[2, 2, 6],
 |   |             [1, 0, 6],
 |   |             [1, 0, 9]])
 |   |
 |   |  newbyteorder(...)
 |   |      arr.newbyteorder(new_order='S', /)
 |   |
 |   |      Return the array with the same data viewed with a different byte order.
 |   |
 |   |      Equivalent to::
 |   |
 |   |          arr.view(arr.dtype.newbytorder(new_order))
 |   |
 |   |      Changes are also made in all fields and sub-arrays of the array data
 |   |      type.
 |   |
 |   |
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      new_order : string, optional
 |   |          Byte order to force; a value from the byte order specifications
 |   |          below. `new_order` codes can be any of:
 |   |
 |   |          * 'S' - swap dtype from current to opposite endian
 |   |          * {'<', 'little'} - little endian
 |   |          * {'>', 'big'} - big endian
 |   |          * {'=', 'native'} - native order, equivalent to `sys.byteorder`
 |   |          * {'|', 'I'} - ignore (no change to byte order)
 |   |
 |   |          The default value ('S') results in swapping the current
 |   |          byte order.
 |   |
 |   |
 |   |      Returns
 |   |      -------
 |   |      new_arr : array
 |   |          New array object with the dtype reflecting given change to the
 |   |          byte order.
 |   |
 |   |  nonzero(...)
 |   |      a.nonzero()
 |   |
 |   |      Return the indices of the elements that are non-zero.
 |   |
 |   |      Refer to `numpy.nonzero` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.nonzero : equivalent function
 |   |
 |   |  partition(...)
 |   |      a.partition(kth, axis=-1, kind='introselect', order=None)
 |   |
 |   |      Rearranges the elements in the array in such a way that the value of the
 |   |      element in kth position is in the position it would be in a sorted array.
 |   |      All elements smaller than the kth element are moved before this element and
 |   |      all equal or greater are moved behind it. The ordering of the elements in
 |   |      the two partitions is undefined.
 |   |
 |   |      .. versionadded:: 1.8.0
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      kth : int or sequence of ints
 |   |          Element index to partition by. The kth element value will be in its
 |   |          final sorted position and all smaller elements will be moved before it
 |   |          and all equal or greater elements behind it.
 |   |          The order of all elements in the partitions is undefined.
 |   |          If provided with a sequence of kth it will partition all elements
 |   |          indexed by kth of them into their sorted position at once.
 |   |
 |   |          .. deprecated:: 1.22.0
 |   |              Passing booleans as index is deprecated.
 |   |      axis : int, optional
 |   |          Axis along which to sort. Default is -1, which means sort along the
 |   |          last axis.
 |   |      kind : {'introselect'}, optional
 |   |          Selection algorithm. Default is 'introselect'.
 |   |      order : str or list of str, optional
 |   |          When `a` is an array with fields defined, this argument specifies
 |   |          which fields to compare first, second, etc. A single field can
 |   |          be specified as a string, and not all fields need to be specified,
 |   |          but unspecified fields will still be used, in the order in which
 |   |          they come up in the dtype, to break ties.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.partition : Return a partitioned copy of an array.
 |   |      argpartition : Indirect partition.
 |   |      sort : Full sort.
 |   |
 |   |      Notes
 |   |      -----
 |   |      See ``np.partition`` for notes on the different algorithms.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> a = np.array([3, 4, 2, 1])
 |   |      >>> a.partition(3)
 |   |      >>> a
 |   |      array([2, 1, 3, 4])
 |   |
 |   |      >>> a.partition((1, 3))
 |   |      >>> a
 |   |      array([1, 2, 3, 4])
 |   |
 |   |  put(...)
 |   |      a.put(indices, values, mode='raise')
 |   |
 |   |      Set ``a.flat[n] = values[n]`` for all `n` in indices.
 |   |
 |   |      Refer to `numpy.put` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.put : equivalent function
 |   |
 |   |  repeat(...)
 |   |      a.repeat(repeats, axis=None)
 |   |
 |   |      Repeat elements of an array.
 |   |
 |   |      Refer to `numpy.repeat` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.repeat : equivalent function
 |   |
 |   |  reshape(...)
 |   |      a.reshape(shape, order='C')
 |   |
 |   |      Returns an array containing the same data with a new shape.
 |   |
 |   |      Refer to `numpy.reshape` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.reshape : equivalent function
 |   |
 |   |      Notes
 |   |      -----
 |   |      Unlike the free function `numpy.reshape`, this method on `ndarray` allows
 |   |      the elements of the shape parameter to be passed in as separate arguments.
 |   |      For example, ``a.reshape(10, 11)`` is equivalent to
 |   |      ``a.reshape((10, 11))``.
 |   |
 |   |  resize(...)
 |   |      a.resize(new_shape, refcheck=True)
 |   |
 |   |      Change shape and size of array in-place.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      new_shape : tuple of ints, or `n` ints
 |   |          Shape of resized array.
 |   |      refcheck : bool, optional
 |   |          If False, reference count will not be checked. Default is True.
 |   |
 |   |      Returns
 |   |      -------
 |   |      None
 |   |
 |   |      Raises
 |   |      ------
 |   |      ValueError
 |   |          If `a` does not own its own data or references or views to it exist,
 |   |          and the data memory must be changed.
 |   |          PyPy only: will always raise if the data memory must be changed, since
 |   |          there is no reliable way to determine if references or views to it
 |   |          exist.
 |   |
 |   |      SystemError
 |   |          If the `order` keyword argument is specified. This behaviour is a
 |   |          bug in NumPy.
 |   |
 |   |      See Also
 |   |      --------
 |   |      resize : Return a new array with the specified shape.
 |   |
 |   |      Notes
 |   |      -----
 |   |      This reallocates space for the data area if necessary.
 |   |
 |   |      Only contiguous arrays (data elements consecutive in memory) can be
 |   |      resized.
 |   |
 |   |      The purpose of the reference count check is to make sure you
 |   |      do not use this array as a buffer for another Python object and then
 |   |      reallocate the memory. However, reference counts can increase in
 |   |      other ways so if you are sure that you have not shared the memory
 |   |      for this array with another Python object, then you may safely set
 |   |      `refcheck` to False.
 |   |
 |   |      Examples
 |   |      --------
 |   |      Shrinking an array: array is flattened (in the order that the data are
 |   |      stored in memory), resized, and reshaped:
 |   |
 |   |      >>> a = np.array([[0, 1], [2, 3]], order='C')
 |   |      >>> a.resize((2, 1))
 |   |      >>> a
 |   |      array([[0],
 |   |             [1]])
 |   |
 |   |      >>> a = np.array([[0, 1], [2, 3]], order='F')
 |   |      >>> a.resize((2, 1))
 |   |      >>> a
 |   |      array([[0],
 |   |             [2]])
 |   |
 |   |      Enlarging an array: as above, but missing entries are filled with zeros:
 |   |
 |   |      >>> b = np.array([[0, 1], [2, 3]])
 |   |      >>> b.resize(2, 3) # new_shape parameter doesn't have to be a tuple
 |   |      >>> b
 |   |      array([[0, 1, 2],
 |   |             [3, 0, 0]])
 |   |
 |   |      Referencing an array prevents resizing...
 |   |
 |   |      >>> c = a
 |   |      >>> a.resize((1, 1))
 |   |      Traceback (most recent call last):
 |   |      ...
 |   |      ValueError: cannot resize an array that references or is referenced ...
 |   |
 |   |      Unless `refcheck` is False:
 |   |
 |   |      >>> a.resize((1, 1), refcheck=False)
 |   |      >>> a
 |   |      array([[0]])
 |   |      >>> c
 |   |      array([[0]])
 |   |
 |   |  round(...)
 |   |      a.round(decimals=0, out=None)
 |   |
 |   |      Return `a` with each element rounded to the given number of decimals.
 |   |
 |   |      Refer to `numpy.around` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.around : equivalent function
 |   |
 |   |  searchsorted(...)
 |   |      a.searchsorted(v, side='left', sorter=None)
 |   |
 |   |      Find indices where elements of v should be inserted in a to maintain order.
 |   |
 |   |      For full documentation, see `numpy.searchsorted`
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.searchsorted : equivalent function
 |   |
 |   |  setfield(...)
 |   |      a.setfield(val, dtype, offset=0)
 |   |
 |   |      Put a value into a specified place in a field defined by a data-type.
 |   |
 |   |      Place `val` into `a`'s field defined by `dtype` and beginning `offset`
 |   |      bytes into the field.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      val : object
 |   |          Value to be placed in field.
 |   |      dtype : dtype object
 |   |          Data-type of the field in which to place `val`.
 |   |      offset : int, optional
 |   |          The number of bytes into the field at which to place `val`.
 |   |
 |   |      Returns
 |   |      -------
 |   |      None
 |   |
 |   |      See Also
 |   |      --------
 |   |      getfield
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.eye(3)
 |   |      >>> x.getfield(np.float64)
 |   |      array([[1.,  0.,  0.],
 |   |             [0.,  1.,  0.],
 |   |             [0.,  0.,  1.]])
 |   |      >>> x.setfield(3, np.int32)
 |   |      >>> x.getfield(np.int32)
 |   |      array([[3, 3, 3],
 |   |             [3, 3, 3],
 |   |             [3, 3, 3]], dtype=int32)
 |   |      >>> x
 |   |      array([[1.0e+000, 1.5e-323, 1.5e-323],
 |   |             [1.5e-323, 1.0e+000, 1.5e-323],
 |   |             [1.5e-323, 1.5e-323, 1.0e+000]])
 |   |      >>> x.setfield(np.eye(3), np.int32)
 |   |      >>> x
 |   |      array([[1.,  0.,  0.],
 |   |             [0.,  1.,  0.],
 |   |             [0.,  0.,  1.]])
 |   |
 |   |  setflags(...)
 |   |      a.setflags(write=None, align=None, uic=None)
 |   |
 |   |      Set array flags WRITEABLE, ALIGNED, WRITEBACKIFCOPY,
 |   |      respectively.
 |   |
 |   |      These Boolean-valued flags affect how numpy interprets the memory
 |   |      area used by `a` (see Notes below). The ALIGNED flag can only
 |   |      be set to True if the data is actually aligned according to the type.
 |   |      The WRITEBACKIFCOPY and flag can never be set
 |   |      to True. The flag WRITEABLE can only be set to True if the array owns its
 |   |      own memory, or the ultimate owner of the memory exposes a writeable buffer
 |   |      interface, or is a string. (The exception for string is made so that
 |   |      unpickling can be done without copying memory.)
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      write : bool, optional
 |   |          Describes whether or not `a` can be written to.
 |   |      align : bool, optional
 |   |          Describes whether or not `a` is aligned properly for its type.
 |   |      uic : bool, optional
 |   |          Describes whether or not `a` is a copy of another "base" array.
 |   |
 |   |      Notes
 |   |      -----
 |   |      Array flags provide information about how the memory area used
 |   |      for the array is to be interpreted. There are 7 Boolean flags
 |   |      in use, only four of which can be changed by the user:
 |   |      WRITEBACKIFCOPY, WRITEABLE, and ALIGNED.
 |   |
 |   |      WRITEABLE (W) the data area can be written to;
 |   |
 |   |      ALIGNED (A) the data and strides are aligned appropriately for the hardware
 |   |      (as determined by the compiler);
 |   |
 |   |      WRITEBACKIFCOPY (X) this array is a copy of some other array (referenced
 |   |      by .base). When the C-API function PyArray_ResolveWritebackIfCopy is
 |   |      called, the base array will be updated with the contents of this array.
 |   |
 |   |      All flags can be accessed using the single (upper case) letter as well
 |   |      as the full name.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> y = np.array([[3, 1, 7],
 |   |      ...               [2, 0, 0],
 |   |      ...               [8, 5, 9]])
 |   |      >>> y
 |   |      array([[3, 1, 7],
 |   |             [2, 0, 0],
 |   |             [8, 5, 9]])
 |   |      >>> y.flags
 |   |        C_CONTIGUOUS : True
 |   |        F_CONTIGUOUS : False
 |   |        OWNDATA : True
 |   |        WRITEABLE : True
 |   |        ALIGNED : True
 |   |        WRITEBACKIFCOPY : False
 |   |      >>> y.setflags(write=0, align=0)
 |   |      >>> y.flags
 |   |        C_CONTIGUOUS : True
 |   |        F_CONTIGUOUS : False
 |   |        OWNDATA : True
 |   |        WRITEABLE : False
 |   |        ALIGNED : False
 |   |        WRITEBACKIFCOPY : False
 |   |      >>> y.setflags(uic=1)
 |   |      Traceback (most recent call last):
 |   |        File "<stdin>", line 1, in <module>
 |   |      ValueError: cannot set WRITEBACKIFCOPY flag to True
 |   |
 |   |  sort(...)
 |   |      a.sort(axis=-1, kind=None, order=None)
 |   |
 |   |      Sort an array in-place. Refer to `numpy.sort` for full documentation.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      axis : int, optional
 |   |          Axis along which to sort. Default is -1, which means sort along the
 |   |          last axis.
 |   |      kind : {'quicksort', 'mergesort', 'heapsort', 'stable'}, optional
 |   |          Sorting algorithm. The default is 'quicksort'. Note that both 'stable'
 |   |          and 'mergesort' use timsort under the covers and, in general, the
 |   |          actual implementation will vary with datatype. The 'mergesort' option
 |   |          is retained for backwards compatibility.
 |   |
 |   |          .. versionchanged:: 1.15.0
 |   |             The 'stable' option was added.
 |   |
 |   |      order : str or list of str, optional
 |   |          When `a` is an array with fields defined, this argument specifies
 |   |          which fields to compare first, second, etc.  A single field can
 |   |          be specified as a string, and not all fields need be specified,
 |   |          but unspecified fields will still be used, in the order in which
 |   |          they come up in the dtype, to break ties.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.sort : Return a sorted copy of an array.
 |   |      numpy.argsort : Indirect sort.
 |   |      numpy.lexsort : Indirect stable sort on multiple keys.
 |   |      numpy.searchsorted : Find elements in sorted array.
 |   |      numpy.partition: Partial sort.
 |   |
 |   |      Notes
 |   |      -----
 |   |      See `numpy.sort` for notes on the different sorting algorithms.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> a = np.array([[1,4], [3,1]])
 |   |      >>> a.sort(axis=1)
 |   |      >>> a
 |   |      array([[1, 4],
 |   |             [1, 3]])
 |   |      >>> a.sort(axis=0)
 |   |      >>> a
 |   |      array([[1, 3],
 |   |             [1, 4]])
 |   |
 |   |      Use the `order` keyword to specify a field to use when sorting a
 |   |      structured array:
 |   |
 |   |      >>> a = np.array([('a', 2), ('c', 1)], dtype=[('x', 'S1'), ('y', int)])
 |   |      >>> a.sort(order='y')
 |   |      >>> a
 |   |      array([(b'c', 1), (b'a', 2)],
 |   |            dtype=[('x', 'S1'), ('y', '<i8')])
 |   |
 |   |  swapaxes(...)
 |   |      a.swapaxes(axis1, axis2)
 |   |
 |   |      Return a view of the array with `axis1` and `axis2` interchanged.
 |   |
 |   |      Refer to `numpy.swapaxes` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.swapaxes : equivalent function
 |   |
 |   |  take(...)
 |   |      a.take(indices, axis=None, out=None, mode='raise')
 |   |
 |   |      Return an array formed from the elements of `a` at the given indices.
 |   |
 |   |      Refer to `numpy.take` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.take : equivalent function
 |   |
 |   |  tobytes(...)
 |   |      a.tobytes(order='C')
 |   |
 |   |      Construct Python bytes containing the raw data bytes in the array.
 |   |
 |   |      Constructs Python bytes showing a copy of the raw contents of
 |   |      data memory. The bytes object is produced in C-order by default.
 |   |      This behavior is controlled by the ``order`` parameter.
 |   |
 |   |      .. versionadded:: 1.9.0
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      order : {'C', 'F', 'A'}, optional
 |   |          Controls the memory layout of the bytes object. 'C' means C-order,
 |   |          'F' means F-order, 'A' (short for *Any*) means 'F' if `a` is
 |   |          Fortran contiguous, 'C' otherwise. Default is 'C'.
 |   |
 |   |      Returns
 |   |      -------
 |   |      s : bytes
 |   |          Python bytes exhibiting a copy of `a`'s raw data.
 |   |
 |   |      See also
 |   |      --------
 |   |      frombuffer
 |   |          Inverse of this operation, construct a 1-dimensional array from Python
 |   |          bytes.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.array([[0, 1], [2, 3]], dtype='<u2')
 |   |      >>> x.tobytes()
 |   |      b'\x00\x00\x01\x00\x02\x00\x03\x00'
 |   |      >>> x.tobytes('C') == x.tobytes()
 |   |      True
 |   |      >>> x.tobytes('F')
 |   |      b'\x00\x00\x02\x00\x01\x00\x03\x00'
 |   |
 |   |  tofile(...)
 |   |      a.tofile(fid, sep="", format="%s")
 |   |
 |   |      Write array to a file as text or binary (default).
 |   |
 |   |      Data is always written in 'C' order, independent of the order of `a`.
 |   |      The data produced by this method can be recovered using the function
 |   |      fromfile().
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      fid : file or str or Path
 |   |          An open file object, or a string containing a filename.
 |   |
 |   |          .. versionchanged:: 1.17.0
 |   |              `pathlib.Path` objects are now accepted.
 |   |
 |   |      sep : str
 |   |          Separator between array items for text output.
 |   |          If "" (empty), a binary file is written, equivalent to
 |   |          ``file.write(a.tobytes())``.
 |   |      format : str
 |   |          Format string for text file output.
 |   |          Each entry in the array is formatted to text by first converting
 |   |          it to the closest Python type, and then using "format" % item.
 |   |
 |   |      Notes
 |   |      -----
 |   |      This is a convenience function for quick storage of array data.
 |   |      Information on endianness and precision is lost, so this method is not a
 |   |      good choice for files intended to archive data or transport data between
 |   |      machines with different endianness. Some of these problems can be overcome
 |   |      by outputting the data as text files, at the expense of speed and file
 |   |      size.
 |   |
 |   |      When fid is a file object, array contents are directly written to the
 |   |      file, bypassing the file object's ``write`` method. As a result, tofile
 |   |      cannot be used with files objects supporting compression (e.g., GzipFile)
 |   |      or file-like objects that do not support ``fileno()`` (e.g., BytesIO).
 |   |
 |   |  tostring(...)
 |   |      a.tostring(order='C')
 |   |
 |   |      A compatibility alias for `tobytes`, with exactly the same behavior.
 |   |
 |   |      Despite its name, it returns `bytes` not `str`\ s.
 |   |
 |   |      .. deprecated:: 1.19.0
 |   |
 |   |  trace(...)
 |   |      a.trace(offset=0, axis1=0, axis2=1, dtype=None, out=None)
 |   |
 |   |      Return the sum along diagonals of the array.
 |   |
 |   |      Refer to `numpy.trace` for full documentation.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.trace : equivalent function
 |   |
 |   |  transpose(...)
 |   |      a.transpose(*axes)
 |   |
 |   |      Returns a view of the array with axes transposed.
 |   |
 |   |      Refer to `numpy.transpose` for full documentation.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      axes : None, tuple of ints, or `n` ints
 |   |
 |   |       * None or no argument: reverses the order of the axes.
 |   |
 |   |       * tuple of ints: `i` in the `j`-th place in the tuple means that the
 |   |         array's `i`-th axis becomes the transposed array's `j`-th axis.
 |   |
 |   |       * `n` ints: same as an n-tuple of the same ints (this form is
 |   |         intended simply as a "convenience" alternative to the tuple form).
 |   |
 |   |      Returns
 |   |      -------
 |   |      p : ndarray
 |   |          View of the array with its axes suitably permuted.
 |   |
 |   |      See Also
 |   |      --------
 |   |      transpose : Equivalent function.
 |   |      ndarray.T : Array property returning the array transposed.
 |   |      ndarray.reshape : Give a new shape to an array without changing its data.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> a = np.array([[1, 2], [3, 4]])
 |   |      >>> a
 |   |      array([[1, 2],
 |   |             [3, 4]])
 |   |      >>> a.transpose()
 |   |      array([[1, 3],
 |   |             [2, 4]])
 |   |      >>> a.transpose((1, 0))
 |   |      array([[1, 3],
 |   |             [2, 4]])
 |   |      >>> a.transpose(1, 0)
 |   |      array([[1, 3],
 |   |             [2, 4]])
 |   |
 |   |      >>> a = np.array([1, 2, 3, 4])
 |   |      >>> a
 |   |      array([1, 2, 3, 4])
 |   |      >>> a.transpose()
 |   |      array([1, 2, 3, 4])
 |   |
 |   |  view(...)
 |   |      a.view([dtype][, type])
 |   |
 |   |      New view of array with the same data.
 |   |
 |   |      .. note::
 |   |          Passing None for ``dtype`` is different from omitting the parameter,
 |   |          since the former invokes ``dtype(None)`` which is an alias for
 |   |          ``dtype('float_')``.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      dtype : data-type or ndarray sub-class, optional
 |   |          Data-type descriptor of the returned view, e.g., float32 or int16.
 |   |          Omitting it results in the view having the same data-type as `a`.
 |   |          This argument can also be specified as an ndarray sub-class, which
 |   |          then specifies the type of the returned object (this is equivalent to
 |   |          setting the ``type`` parameter).
 |   |      type : Python type, optional
 |   |          Type of the returned view, e.g., ndarray or matrix.  Again, omission
 |   |          of the parameter results in type preservation.
 |   |
 |   |      Notes
 |   |      -----
 |   |      ``a.view()`` is used two different ways:
 |   |
 |   |      ``a.view(some_dtype)`` or ``a.view(dtype=some_dtype)`` constructs a view
 |   |      of the array's memory with a different data-type.  This can cause a
 |   |      reinterpretation of the bytes of memory.
 |   |
 |   |      ``a.view(ndarray_subclass)`` or ``a.view(type=ndarray_subclass)`` just
 |   |      returns an instance of `ndarray_subclass` that looks at the same array
 |   |      (same shape, dtype, etc.)  This does not cause a reinterpretation of the
 |   |      memory.
 |   |
 |   |      For ``a.view(some_dtype)``, if ``some_dtype`` has a different number of
 |   |      bytes per entry than the previous dtype (for example, converting a regular
 |   |      array to a structured array), then the last axis of ``a`` must be
 |   |      contiguous. This axis will be resized in the result.
 |   |
 |   |      .. versionchanged:: 1.23.0
 |   |         Only the last axis needs to be contiguous. Previously, the entire array
 |   |         had to be C-contiguous.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.array([(1, 2)], dtype=[('a', np.int8), ('b', np.int8)])
 |   |
 |   |      Viewing array data using a different type and dtype:
 |   |
 |   |      >>> y = x.view(dtype=np.int16, type=np.matrix)
 |   |      >>> y
 |   |      matrix([[513]], dtype=int16)
 |   |      >>> print(type(y))
 |   |      <class 'numpy.matrix'>
 |   |
 |   |      Creating a view on a structured array so it can be used in calculations
 |   |
 |   |      >>> x = np.array([(1, 2),(3,4)], dtype=[('a', np.int8), ('b', np.int8)])
 |   |      >>> xv = x.view(dtype=np.int8).reshape(-1,2)
 |   |      >>> xv
 |   |      array([[1, 2],
 |   |             [3, 4]], dtype=int8)
 |   |      >>> xv.mean(0)
 |   |      array([2.,  3.])
 |   |
 |   |      Making changes to the view changes the underlying array
 |   |
 |   |      >>> xv[0,1] = 20
 |   |      >>> x
 |   |      array([(1, 20), (3,  4)], dtype=[('a', 'i1'), ('b', 'i1')])
 |   |
 |   |      Using a view to convert an array to a recarray:
 |   |
 |   |      >>> z = x.view(np.recarray)
 |   |      >>> z.a
 |   |      array([1, 3], dtype=int8)
 |   |
 |   |      Views share data:
 |   |
 |   |      >>> x[0] = (9, 10)
 |   |      >>> z[0]
 |   |      (9, 10)
 |   |
 |   |      Views that change the dtype size (bytes per entry) should normally be
 |   |      avoided on arrays defined by slices, transposes, fortran-ordering, etc.:
 |   |
 |   |      >>> x = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int16)
 |   |      >>> y = x[:, ::2]
 |   |      >>> y
 |   |      array([[1, 3],
 |   |             [4, 6]], dtype=int16)
 |   |      >>> y.view(dtype=[('width', np.int16), ('length', np.int16)])
 |   |      Traceback (most recent call last):
 |   |          ...
 |   |      ValueError: To change to a dtype of a different size, the last axis must be contiguous
 |   |      >>> z = y.copy()
 |   |      >>> z.view(dtype=[('width', np.int16), ('length', np.int16)])
 |   |      array([[(1, 3)],
 |   |             [(4, 6)]], dtype=[('width', '<i2'), ('length', '<i2')])
 |   |
 |   |      However, views that change dtype are totally fine for arrays with a
 |   |      contiguous last axis, even if the rest of the axes are not C-contiguous:
 |   |
 |   |      >>> x = np.arange(2 * 3 * 4, dtype=np.int8).reshape(2, 3, 4)
 |   |      >>> x.transpose(1, 0, 2).view(np.int16)
 |   |      array([[[ 256,  770],
 |   |              [3340, 3854]],
 |   |      <BLANKLINE>
 |   |             [[1284, 1798],
 |   |              [4368, 4882]],
 |   |      <BLANKLINE>
 |   |             [[2312, 2826],
 |   |              [5396, 5910]]], dtype=int16)
 |   |
 |   |  ----------------------------------------------------------------------
 |   |  Class methods inherited from ndarray:
 |   |
 |   |  __class_getitem__(...) from builtins.type
 |   |      a.__class_getitem__(item, /)
 |   |
 |   |      Return a parametrized wrapper around the `~numpy.ndarray` type.
 |   |
 |   |      .. versionadded:: 1.22
 |   |
 |   |      Returns
 |   |      -------
 |   |      alias : types.GenericAlias
 |   |          A parametrized `~numpy.ndarray` type.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> from typing import Any
 |   |      >>> import numpy as np
 |   |
 |   |      >>> np.ndarray[Any, np.dtype[Any]]
 |   |      numpy.ndarray[typing.Any, numpy.dtype[typing.Any]]
 |   |
 |   |      See Also
 |   |      --------
 |   |      :pep:`585` : Type hinting generics in standard collections.
 |   |      numpy.typing.NDArray : An ndarray alias :term:`generic <generic type>`
 |   |                          w.r.t. its `dtype.type <numpy.dtype.type>`.
 |   |
 |   |  ----------------------------------------------------------------------
 |   |  Data descriptors inherited from ndarray:
 |   |
 |   |  __array_interface__
 |   |      Array protocol: Python side.
 |   |
 |   |  __array_struct__
 |   |      Array protocol: C-struct side.
 |   |
 |   |  base
 |   |      Base object if memory is from some other object.
 |   |
 |   |      Examples
 |   |      --------
 |   |      The base of an array that owns its memory is None:
 |   |
 |   |      >>> x = np.array([1,2,3,4])
 |   |      >>> x.base is None
 |   |      True
 |   |
 |   |      Slicing creates a view, whose memory is shared with x:
 |   |
 |   |      >>> y = x[2:]
 |   |      >>> y.base is x
 |   |      True
 |   |
 |   |  ctypes
 |   |      An object to simplify the interaction of the array with the ctypes
 |   |      module.
 |   |
 |   |      This attribute creates an object that makes it easier to use arrays
 |   |      when calling shared libraries with the ctypes module. The returned
 |   |      object has, among others, data, shape, and strides attributes (see
 |   |      Notes below) which themselves return ctypes objects that can be used
 |   |      as arguments to a shared library.
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      None
 |   |
 |   |      Returns
 |   |      -------
 |   |      c : Python object
 |   |          Possessing attributes data, shape, strides, etc.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.ctypeslib
 |   |
 |   |      Notes
 |   |      -----
 |   |      Below are the public attributes of this object which were documented
 |   |      in "Guide to NumPy" (we have omitted undocumented public attributes,
 |   |      as well as documented private attributes):
 |   |
 |   |      .. autoattribute:: numpy.core._internal._ctypes.data
 |   |          :noindex:
 |   |
 |   |      .. autoattribute:: numpy.core._internal._ctypes.shape
 |   |          :noindex:
 |   |
 |   |      .. autoattribute:: numpy.core._internal._ctypes.strides
 |   |          :noindex:
 |   |
 |   |      .. automethod:: numpy.core._internal._ctypes.data_as
 |   |          :noindex:
 |   |
 |   |      .. automethod:: numpy.core._internal._ctypes.shape_as
 |   |          :noindex:
 |   |
 |   |      .. automethod:: numpy.core._internal._ctypes.strides_as
 |   |          :noindex:
 |   |
 |   |      If the ctypes module is not available, then the ctypes attribute
 |   |      of array objects still returns something useful, but ctypes objects
 |   |      are not returned and errors may be raised instead. In particular,
 |   |      the object will still have the ``as_parameter`` attribute which will
 |   |      return an integer equal to the data attribute.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> import ctypes
 |   |      >>> x = np.array([[0, 1], [2, 3]], dtype=np.int32)
 |   |      >>> x
 |   |      array([[0, 1],
 |   |             [2, 3]], dtype=int32)
 |   |      >>> x.ctypes.data
 |   |      31962608 # may vary
 |   |      >>> x.ctypes.data_as(ctypes.POINTER(ctypes.c_uint32))
 |   |      <__main__.LP_c_uint object at 0x7ff2fc1fc200> # may vary
 |   |      >>> x.ctypes.data_as(ctypes.POINTER(ctypes.c_uint32)).contents
 |   |      c_uint(0)
 |   |      >>> x.ctypes.data_as(ctypes.POINTER(ctypes.c_uint64)).contents
 |   |      c_ulong(4294967296)
 |   |      >>> x.ctypes.shape
 |   |      <numpy.core._internal.c_long_Array_2 object at 0x7ff2fc1fce60> # may vary
 |   |      >>> x.ctypes.strides
 |   |      <numpy.core._internal.c_long_Array_2 object at 0x7ff2fc1ff320> # may vary
 |   |
 |   |  data
 |   |      Python buffer object pointing to the start of the array's data.
 |   |
 |   |  dtype
 |   |      Data-type of the array's elements.
 |   |
 |   |      .. warning::
 |   |
 |   |          Setting ``arr.dtype`` is discouraged and may be deprecated in the
 |   |          future.  Setting will replace the ``dtype`` without modifying the
 |   |          memory (see also `ndarray.view` and `ndarray.astype`).
 |   |
 |   |      Parameters
 |   |      ----------
 |   |      None
 |   |
 |   |      Returns
 |   |      -------
 |   |      d : numpy dtype object
 |   |
 |   |      See Also
 |   |      --------
 |   |      ndarray.astype : Cast the values contained in the array to a new data-type.
 |   |      ndarray.view : Create a view of the same data but a different data-type.
 |   |      numpy.dtype
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x
 |   |      array([[0, 1],
 |   |             [2, 3]])
 |   |      >>> x.dtype
 |   |      dtype('int32')
 |   |      >>> type(x.dtype)
 |   |      <type 'numpy.dtype'>
 |   |
 |   |  flags
 |   |      Information about the memory layout of the array.
 |   |
 |   |      Attributes
 |   |      ----------
 |   |      C_CONTIGUOUS (C)
 |   |          The data is in a single, C-style contiguous segment.
 |   |      F_CONTIGUOUS (F)
 |   |          The data is in a single, Fortran-style contiguous segment.
 |   |      OWNDATA (O)
 |   |          The array owns the memory it uses or borrows it from another object.
 |   |      WRITEABLE (W)
 |   |          The data area can be written to.  Setting this to False locks
 |   |          the data, making it read-only.  A view (slice, etc.) inherits WRITEABLE
 |   |          from its base array at creation time, but a view of a writeable
 |   |          array may be subsequently locked while the base array remains writeable.
 |   |          (The opposite is not true, in that a view of a locked array may not
 |   |          be made writeable.  However, currently, locking a base object does not
 |   |          lock any views that already reference it, so under that circumstance it
 |   |          is possible to alter the contents of a locked array via a previously
 |   |          created writeable view onto it.)  Attempting to change a non-writeable
 |   |          array raises a RuntimeError exception.
 |   |      ALIGNED (A)
 |   |          The data and all elements are aligned appropriately for the hardware.
 |   |      WRITEBACKIFCOPY (X)
 |   |          This array is a copy of some other array. The C-API function
 |   |          PyArray_ResolveWritebackIfCopy must be called before deallocating
 |   |          to the base array will be updated with the contents of this array.
 |   |      FNC
 |   |          F_CONTIGUOUS and not C_CONTIGUOUS.
 |   |      FORC
 |   |          F_CONTIGUOUS or C_CONTIGUOUS (one-segment test).
 |   |      BEHAVED (B)
 |   |          ALIGNED and WRITEABLE.
 |   |      CARRAY (CA)
 |   |          BEHAVED and C_CONTIGUOUS.
 |   |      FARRAY (FA)
 |   |          BEHAVED and F_CONTIGUOUS and not C_CONTIGUOUS.
 |   |
 |   |      Notes
 |   |      -----
 |   |      The `flags` object can be accessed dictionary-like (as in ``a.flags['WRITEABLE']``),
 |   |      or by using lowercased attribute names (as in ``a.flags.writeable``). Short flag
 |   |      names are only supported in dictionary access.
 |   |
 |   |      Only the WRITEBACKIFCOPY, WRITEABLE, and ALIGNED flags can be
 |   |      changed by the user, via direct assignment to the attribute or dictionary
 |   |      entry, or by calling `ndarray.setflags`.
 |   |
 |   |      The array flags cannot be set arbitrarily:
 |   |
 |   |      - WRITEBACKIFCOPY can only be set ``False``.
 |   |      - ALIGNED can only be set ``True`` if the data is truly aligned.
 |   |      - WRITEABLE can only be set ``True`` if the array owns its own memory
 |   |        or the ultimate owner of the memory exposes a writeable buffer
 |   |        interface or is a string.
 |   |
 |   |      Arrays can be both C-style and Fortran-style contiguous simultaneously.
 |   |      This is clear for 1-dimensional arrays, but can also be true for higher
 |   |      dimensional arrays.
 |   |
 |   |      Even for contiguous arrays a stride for a given dimension
 |   |      ``arr.strides[dim]`` may be *arbitrary* if ``arr.shape[dim] == 1``
 |   |      or the array has no elements.
 |   |      It does *not* generally hold that ``self.strides[-1] == self.itemsize``
 |   |      for C-style contiguous arrays or ``self.strides[0] == self.itemsize`` for
 |   |      Fortran-style contiguous arrays is true.
 |   |
 |   |  flat
 |   |      A 1-D iterator over the array.
 |   |
 |   |      This is a `numpy.flatiter` instance, which acts similarly to, but is not
 |   |      a subclass of, Python's built-in iterator object.
 |   |
 |   |      See Also
 |   |      --------
 |   |      flatten : Return a copy of the array collapsed into one dimension.
 |   |
 |   |      flatiter
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.arange(1, 7).reshape(2, 3)
 |   |      >>> x
 |   |      array([[1, 2, 3],
 |   |             [4, 5, 6]])
 |   |      >>> x.flat[3]
 |   |      4
 |   |      >>> x.T
 |   |      array([[1, 4],
 |   |             [2, 5],
 |   |             [3, 6]])
 |   |      >>> x.T.flat[3]
 |   |      5
 |   |      >>> type(x.flat)
 |   |      <class 'numpy.flatiter'>
 |   |
 |   |      An assignment example:
 |   |
 |   |      >>> x.flat = 3; x
 |   |      array([[3, 3, 3],
 |   |             [3, 3, 3]])
 |   |      >>> x.flat[[1,4]] = 1; x
 |   |      array([[3, 1, 3],
 |   |             [3, 1, 3]])
 |   |
 |   |  imag
 |   |      The imaginary part of the array.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.sqrt([1+0j, 0+1j])
 |   |      >>> x.imag
 |   |      array([ 0.        ,  0.70710678])
 |   |      >>> x.imag.dtype
 |   |      dtype('float64')
 |   |
 |   |  itemsize
 |   |      Length of one array element in bytes.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.array([1,2,3], dtype=np.float64)
 |   |      >>> x.itemsize
 |   |      8
 |   |      >>> x = np.array([1,2,3], dtype=np.complex128)
 |   |      >>> x.itemsize
 |   |      16
 |   |
 |   |  nbytes
 |   |      Total bytes consumed by the elements of the array.
 |   |
 |   |      Notes
 |   |      -----
 |   |      Does not include memory consumed by non-element attributes of the
 |   |      array object.
 |   |
 |   |      See Also
 |   |      --------
 |   |      sys.getsizeof
 |   |          Memory consumed by the object itself without parents in case view.
 |   |          This does include memory consumed by non-element attributes.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.zeros((3,5,2), dtype=np.complex128)
 |   |      >>> x.nbytes
 |   |      480
 |   |      >>> np.prod(x.shape) * x.itemsize
 |   |      480
 |   |
 |   |  ndim
 |   |      Number of array dimensions.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.array([1, 2, 3])
 |   |      >>> x.ndim
 |   |      1
 |   |      >>> y = np.zeros((2, 3, 4))
 |   |      >>> y.ndim
 |   |      3
 |   |
 |   |  real
 |   |      The real part of the array.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.sqrt([1+0j, 0+1j])
 |   |      >>> x.real
 |   |      array([ 1.        ,  0.70710678])
 |   |      >>> x.real.dtype
 |   |      dtype('float64')
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.real : equivalent function
 |   |
 |   |  shape
 |   |      Tuple of array dimensions.
 |   |
 |   |      The shape property is usually used to get the current shape of an array,
 |   |      but may also be used to reshape the array in-place by assigning a tuple of
 |   |      array dimensions to it.  As with `numpy.reshape`, one of the new shape
 |   |      dimensions can be -1, in which case its value is inferred from the size of
 |   |      the array and the remaining dimensions. Reshaping an array in-place will
 |   |      fail if a copy is required.
 |   |
 |   |      .. warning::
 |   |
 |   |          Setting ``arr.shape`` is discouraged and may be deprecated in the
 |   |          future.  Using `ndarray.reshape` is the preferred approach.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.array([1, 2, 3, 4])
 |   |      >>> x.shape
 |   |      (4,)
 |   |      >>> y = np.zeros((2, 3, 4))
 |   |      >>> y.shape
 |   |      (2, 3, 4)
 |   |      >>> y.shape = (3, 8)
 |   |      >>> y
 |   |      array([[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
 |   |             [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
 |   |             [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]])
 |   |      >>> y.shape = (3, 6)
 |   |      Traceback (most recent call last):
 |   |        File "<stdin>", line 1, in <module>
 |   |      ValueError: total size of new array must be unchanged
 |   |      >>> np.zeros((4,2))[::2].shape = (-1,)
 |   |      Traceback (most recent call last):
 |   |        File "<stdin>", line 1, in <module>
 |   |      AttributeError: Incompatible shape for in-place modification. Use
 |   |      `.reshape()` to make a copy with the desired shape.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.shape : Equivalent getter function.
 |   |      numpy.reshape : Function similar to setting ``shape``.
 |   |      ndarray.reshape : Method similar to setting ``shape``.
 |   |
 |   |  size
 |   |      Number of elements in the array.
 |   |
 |   |      Equal to ``np.prod(a.shape)``, i.e., the product of the array's
 |   |      dimensions.
 |   |
 |   |      Notes
 |   |      -----
 |   |      `a.size` returns a standard arbitrary precision Python integer. This
 |   |      may not be the case with other methods of obtaining the same value
 |   |      (like the suggested ``np.prod(a.shape)``, which returns an instance
 |   |      of ``np.int_``), and may be relevant if the value is used further in
 |   |      calculations that may overflow a fixed size integer type.
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> x = np.zeros((3, 5, 2), dtype=np.complex128)
 |   |      >>> x.size
 |   |      30
 |   |      >>> np.prod(x.shape)
 |   |      30
 |   |
 |   |  strides
 |   |      Tuple of bytes to step in each dimension when traversing an array.
 |   |
 |   |      The byte offset of element ``(i[0], i[1], ..., i[n])`` in an array `a`
 |   |      is::
 |   |
 |   |          offset = sum(np.array(i) * a.strides)
 |   |
 |   |      A more detailed explanation of strides can be found in the
 |   |      "ndarray.rst" file in the NumPy reference guide.
 |   |
 |   |      .. warning::
 |   |
 |   |          Setting ``arr.strides`` is discouraged and may be deprecated in the
 |   |          future.  `numpy.lib.stride_tricks.as_strided` should be preferred
 |   |          to create a new view of the same data in a safer way.
 |   |
 |   |      Notes
 |   |      -----
 |   |      Imagine an array of 32-bit integers (each 4 bytes)::
 |   |
 |   |        x = np.array([[0, 1, 2, 3, 4],
 |   |                      [5, 6, 7, 8, 9]], dtype=np.int32)
 |   |
 |   |      This array is stored in memory as 40 bytes, one after the other
 |   |      (known as a contiguous block of memory).  The strides of an array tell
 |   |      us how many bytes we have to skip in memory to move to the next position
 |   |      along a certain axis.  For example, we have to skip 4 bytes (1 value) to
 |   |      move to the next column, but 20 bytes (5 values) to get to the same
 |   |      position in the next row.  As such, the strides for the array `x` will be
 |   |      ``(20, 4)``.
 |   |
 |   |      See Also
 |   |      --------
 |   |      numpy.lib.stride_tricks.as_strided
 |   |
 |   |      Examples
 |   |      --------
 |   |      >>> y = np.reshape(np.arange(2*3*4), (2,3,4))
 |   |      >>> y
 |   |      array([[[ 0,  1,  2,  3],
 |   |              [ 4,  5,  6,  7],
 |   |              [ 8,  9, 10, 11]],
 |   |             [[12, 13, 14, 15],
 |   |              [16, 17, 18, 19],
 |   |              [20, 21, 22, 23]]])
 |   |      >>> y.strides
 |   |      (48, 16, 4)
 |   |      >>> y[1,1,1]
 |   |      17
 |   |      >>> offset=sum(y.strides * np.array((1,1,1)))
 |   |      >>> offset/y.itemsize
 |   |      17
 |   |
 |   |      >>> x = np.reshape(np.arange(5*6*7*8), (5,6,7,8)).transpose(2,3,1,0)
 |   |      >>> x.strides
 |   |      (32, 4, 224, 1344)
 |   |      >>> i = np.array([3,5,2,2])
 |   |      >>> offset = sum(i * x.strides)
 |   |      >>> x[3,5,2,2]
 |   |      813
 |   |      >>> offset / x.itemsize
 |   |      813
 |   |
 |   |  ----------------------------------------------------------------------
 |   |  Data and other attributes inherited from ndarray:
 |   |
 |   |  __hash__ = None
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from AxisConcatenator:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object

None
&&&&&&&&&&&&&&&&&&&&&& choose &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

choose(a, choices, out=None, mode='raise')
    Construct an array from an index array and a list of arrays to choose from.

    First of all, if confused or uncertain, definitely look at the Examples -
    in its full generality, this function is less simple than it might
    seem from the following code description (below ndi =
    `numpy.lib.index_tricks`):

    ``np.choose(a,c) == np.array([c[a[I]][I] for I in ndi.ndindex(a.shape)])``.

    But this omits some subtleties.  Here is a fully general summary:

    Given an "index" array (`a`) of integers and a sequence of ``n`` arrays
    (`choices`), `a` and each choice array are first broadcast, as necessary,
    to arrays of a common shape; calling these *Ba* and *Bchoices[i], i =
    0,...,n-1* we have that, necessarily, ``Ba.shape == Bchoices[i].shape``
    for each ``i``.  Then, a new array with shape ``Ba.shape`` is created as
    follows:

    * if ``mode='raise'`` (the default), then, first of all, each element of
      ``a`` (and thus ``Ba``) must be in the range ``[0, n-1]``; now, suppose
      that ``i`` (in that range) is the value at the ``(j0, j1, ..., jm)``
      position in ``Ba`` - then the value at the same position in the new array
      is the value in ``Bchoices[i]`` at that same position;

    * if ``mode='wrap'``, values in `a` (and thus `Ba`) may be any (signed)
      integer; modular arithmetic is used to map integers outside the range
      `[0, n-1]` back into that range; and then the new array is constructed
      as above;

    * if ``mode='clip'``, values in `a` (and thus ``Ba``) may be any (signed)
      integer; negative integers are mapped to 0; values greater than ``n-1``
      are mapped to ``n-1``; and then the new array is constructed as above.

    Parameters
    ----------
    a : int array
        This array must contain integers in ``[0, n-1]``, where ``n`` is the
        number of choices, unless ``mode=wrap`` or ``mode=clip``, in which
        cases any integers are permissible.
    choices : sequence of arrays
        Choice arrays. `a` and all of the choices must be broadcastable to the
        same shape.  If `choices` is itself an array (not recommended), then
        its outermost dimension (i.e., the one corresponding to
        ``choices.shape[0]``) is taken as defining the "sequence".
    out : array, optional
        If provided, the result will be inserted into this array. It should
        be of the appropriate shape and dtype. Note that `out` is always
        buffered if ``mode='raise'``; use other modes for better performance.
    mode : {'raise' (default), 'wrap', 'clip'}, optional
        Specifies how indices outside ``[0, n-1]`` will be treated:

          * 'raise' : an exception is raised
          * 'wrap' : value becomes value mod ``n``
          * 'clip' : values < 0 are mapped to 0, values > n-1 are mapped to n-1

    Returns
    -------
    merged_array : array
        The merged result.

    Raises
    ------
    ValueError: shape mismatch
        If `a` and each choice array are not all broadcastable to the same
        shape.

    See Also
    --------
    ndarray.choose : equivalent method
    numpy.take_along_axis : Preferable if `choices` is an array

    Notes
    -----
    To reduce the chance of misinterpretation, even though the following
    "abuse" is nominally supported, `choices` should neither be, nor be
    thought of as, a single array, i.e., the outermost sequence-like container
    should be either a list or a tuple.

    Examples
    --------

    >>> choices = [[0, 1, 2, 3], [10, 11, 12, 13],
    ...   [20, 21, 22, 23], [30, 31, 32, 33]]
    >>> np.choose([2, 3, 1, 0], choices
    ... # the first element of the result will be the first element of the
    ... # third (2+1) "array" in choices, namely, 20; the second element
    ... # will be the second element of the fourth (3+1) choice array, i.e.,
    ... # 31, etc.
    ... )
    array([20, 31, 12,  3])
    >>> np.choose([2, 4, 1, 0], choices, mode='clip') # 4 goes to 3 (4-1)
    array([20, 31, 12,  3])
    >>> # because there are 4 choice arrays
    >>> np.choose([2, 4, 1, 0], choices, mode='wrap') # 4 goes to (4 mod 4)
    array([20,  1, 12,  3])
    >>> # i.e., 0

    A couple examples illustrating how choose broadcasts:

    >>> a = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
    >>> choices = [-10, 10]
    >>> np.choose(a, choices)
    array([[ 10, -10,  10],
           [-10,  10, -10],
           [ 10, -10,  10]])

    >>> # With thanks to Anne Archibald
    >>> a = np.array([0, 1]).reshape((2,1,1))
    >>> c1 = np.array([1, 2, 3]).reshape((1,3,1))
    >>> c2 = np.array([-1, -2, -3, -4, -5]).reshape((1,1,5))
    >>> np.choose(a, (c1, c2)) # result is 2x3x5, res[0,:,:]=c1, res[1,:,:]=c2
    array([[[ 1,  1,  1,  1,  1],
            [ 2,  2,  2,  2,  2],
            [ 3,  3,  3,  3,  3]],
           [[-1, -2, -3, -4, -5],
            [-1, -2, -3, -4, -5],
            [-1, -2, -3, -4, -5]]])

None
&&&&&&&&&&&&&&&&&&&&&& concatenate &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

concatenate(...)
    concatenate((a1, a2, ...), axis=0, out=None, dtype=None, casting="same_kind")

    Join a sequence of arrays along an existing axis.

    Parameters
    ----------
    a1, a2, ... : sequence of array_like
        The arrays must have the same shape, except in the dimension
        corresponding to `axis` (the first, by default).
    axis : int, optional
        The axis along which the arrays will be joined.  If axis is None,
        arrays are flattened before use.  Default is 0.
    out : ndarray, optional
        If provided, the destination to place the result. The shape must be
        correct, matching that of what concatenate would have returned if no
        out argument were specified.
    dtype : str or dtype
        If provided, the destination array will have this dtype. Cannot be
        provided together with `out`.

        .. versionadded:: 1.20.0

    casting : {'no', 'equiv', 'safe', 'same_kind', 'unsafe'}, optional
        Controls what kind of data casting may occur. Defaults to 'same_kind'.

        .. versionadded:: 1.20.0

    Returns
    -------
    res : ndarray
        The concatenated array.

    See Also
    --------
    ma.concatenate : Concatenate function that preserves input masks.
    array_split : Split an array into multiple sub-arrays of equal or
                  near-equal size.
    split : Split array into a list of multiple sub-arrays of equal size.
    hsplit : Split array into multiple sub-arrays horizontally (column wise).
    vsplit : Split array into multiple sub-arrays vertically (row wise).
    dsplit : Split array into multiple sub-arrays along the 3rd axis (depth).
    stack : Stack a sequence of arrays along a new axis.
    block : Assemble arrays from blocks.
    hstack : Stack arrays in sequence horizontally (column wise).
    vstack : Stack arrays in sequence vertically (row wise).
    dstack : Stack arrays in sequence depth wise (along third dimension).
    column_stack : Stack 1-D arrays as columns into a 2-D array.

    Notes
    -----
    When one or more of the arrays to be concatenated is a MaskedArray,
    this function will return a MaskedArray object instead of an ndarray,
    but the input masks are *not* preserved. In cases where a MaskedArray
    is expected as input, use the ma.concatenate function from the masked
    array module instead.

    Examples
    --------
    >>> a = np.array([[1, 2], [3, 4]])
    >>> b = np.array([[5, 6]])
    >>> np.concatenate((a, b), axis=0)
    array([[1, 2],
           [3, 4],
           [5, 6]])
    >>> np.concatenate((a, b.T), axis=1)
    array([[1, 2, 5],
           [3, 4, 6]])
    >>> np.concatenate((a, b), axis=None)
    array([1, 2, 3, 4, 5, 6])

    This function will not preserve masking of MaskedArray inputs.

    >>> a = np.ma.arange(3)
    >>> a[1] = np.ma.masked
    >>> b = np.arange(2, 5)
    >>> a
    masked_array(data=[0, --, 2],
                 mask=[False,  True, False],
           fill_value=999999)
    >>> b
    array([2, 3, 4])
    >>> np.concatenate([a, b])
    masked_array(data=[0, 1, 2, 2, 3, 4],
                 mask=False,
           fill_value=999999)
    >>> np.ma.concatenate([a, b])
    masked_array(data=[0, --, 2, 2, 3, 4],
                 mask=[False,  True, False, False, False, False],
           fill_value=999999)

None
&&&&&&&&&&&&&&&&&&&&&& copy &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

copy(a, order='K', subok=False)
    Return an array copy of the given object.

    Parameters
    ----------
    a : array_like
        Input data.
    order : {'C', 'F', 'A', 'K'}, optional
        Controls the memory layout of the copy. 'C' means C-order,
        'F' means F-order, 'A' means 'F' if `a` is Fortran contiguous,
        'C' otherwise. 'K' means match the layout of `a` as closely
        as possible. (Note that this function and :meth:`ndarray.copy` are very
        similar, but have different default values for their order=
        arguments.)
    subok : bool, optional
        If True, then sub-classes will be passed-through, otherwise the
        returned array will be forced to be a base-class array (defaults to False).

        .. versionadded:: 1.19.0

    Returns
    -------
    arr : ndarray
        Array interpretation of `a`.

    See Also
    --------
    ndarray.copy : Preferred method for creating an array copy

    Notes
    -----
    This is equivalent to:

    >>> np.array(a, copy=True)  #doctest: +SKIP

    Examples
    --------
    Create an array x, with a reference y and a copy z:

    >>> x = np.array([1, 2, 3])
    >>> y = x
    >>> z = np.copy(x)

    Note that, when we modify x, y changes, but not z:

    >>> x[0] = 10
    >>> x[0] == y[0]
    True
    >>> x[0] == z[0]
    False

    Note that, np.copy clears previously set WRITEABLE=False flag.

    >>> a = np.array([1, 2, 3])
    >>> a.flags["WRITEABLE"] = False
    >>> b = np.copy(a)
    >>> b.flags["WRITEABLE"]
    True
    >>> b[0] = 3
    >>> b
    array([3, 2, 3])

    Note that np.copy is a shallow copy and will not copy object
    elements within arrays. This is mainly important for arrays
    containing Python objects. The new array will contain the
    same object which may lead to surprises if that object can
    be modified (is mutable):

    >>> a = np.array([1, 'm', [2, 3, 4]], dtype=object)
    >>> b = np.copy(a)
    >>> b[2][0] = 10
    >>> a
    array([1, 'm', list([10, 3, 4])], dtype=object)

    To ensure all elements within an ``object`` array are copied,
    use `copy.deepcopy`:

    >>> import copy
    >>> a = np.array([1, 'm', [2, 3, 4]], dtype=object)
    >>> c = copy.deepcopy(a)
    >>> c[2][0] = 10
    >>> c
    array([1, 'm', list([10, 3, 4])], dtype=object)
    >>> a
    array([1, 'm', list([2, 3, 4])], dtype=object)

None
&&&&&&&&&&&&&&&&&&&&&& corrcoef &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

corrcoef(x, y=None, rowvar=True, bias=<no value>, ddof=<no value>, *, dtype=None)
    Return Pearson product-moment correlation coefficients.

    Please refer to the documentation for `cov` for more detail.  The
    relationship between the correlation coefficient matrix, `R`, and the
    covariance matrix, `C`, is

    .. math:: R_{ij} = \frac{ C_{ij} } { \sqrt{ C_{ii} C_{jj} } }

    The values of `R` are between -1 and 1, inclusive.

    Parameters
    ----------
    x : array_like
        A 1-D or 2-D array containing multiple variables and observations.
        Each row of `x` represents a variable, and each column a single
        observation of all those variables. Also see `rowvar` below.
    y : array_like, optional
        An additional set of variables and observations. `y` has the same
        shape as `x`.
    rowvar : bool, optional
        If `rowvar` is True (default), then each row represents a
        variable, with observations in the columns. Otherwise, the relationship
        is transposed: each column represents a variable, while the rows
        contain observations.
    bias : _NoValue, optional
        Has no effect, do not use.

        .. deprecated:: 1.10.0
    ddof : _NoValue, optional
        Has no effect, do not use.

        .. deprecated:: 1.10.0
    dtype : data-type, optional
        Data-type of the result. By default, the return data-type will have
        at least `numpy.float64` precision.

        .. versionadded:: 1.20

    Returns
    -------
    R : ndarray
        The correlation coefficient matrix of the variables.

    See Also
    --------
    cov : Covariance matrix

    Notes
    -----
    Due to floating point rounding the resulting array may not be Hermitian,
    the diagonal elements may not be 1, and the elements may not satisfy the
    inequality abs(a) <= 1. The real and imaginary parts are clipped to the
    interval [-1,  1] in an attempt to improve on that situation but is not
    much help in the complex case.

    This function accepts but discards arguments `bias` and `ddof`.  This is
    for backwards compatibility with previous versions of this function.  These
    arguments had no effect on the return values of the function and can be
    safely ignored in this and previous versions of numpy.

    Examples
    --------
    In this example we generate two random arrays, ``xarr`` and ``yarr``, and
    compute the row-wise and column-wise Pearson correlation coefficients,
    ``R``. Since ``rowvar`` is  true by  default, we first find the row-wise
    Pearson correlation coefficients between the variables of ``xarr``.

    >>> import numpy as np
    >>> rng = np.random.default_rng(seed=42)
    >>> xarr = rng.random((3, 3))
    >>> xarr
    array([[0.77395605, 0.43887844, 0.85859792],
           [0.69736803, 0.09417735, 0.97562235],
           [0.7611397 , 0.78606431, 0.12811363]])
    >>> R1 = np.corrcoef(xarr)
    >>> R1
    array([[ 1.        ,  0.99256089, -0.68080986],
           [ 0.99256089,  1.        , -0.76492172],
           [-0.68080986, -0.76492172,  1.        ]])

    If we add another set of variables and observations ``yarr``, we can
    compute the row-wise Pearson correlation coefficients between the
    variables in ``xarr`` and ``yarr``.

    >>> yarr = rng.random((3, 3))
    >>> yarr
    array([[0.45038594, 0.37079802, 0.92676499],
           [0.64386512, 0.82276161, 0.4434142 ],
           [0.22723872, 0.55458479, 0.06381726]])
    >>> R2 = np.corrcoef(xarr, yarr)
    >>> R2
    array([[ 1.        ,  0.99256089, -0.68080986,  0.75008178, -0.934284  ,
            -0.99004057],
           [ 0.99256089,  1.        , -0.76492172,  0.82502011, -0.97074098,
            -0.99981569],
           [-0.68080986, -0.76492172,  1.        , -0.99507202,  0.89721355,
             0.77714685],
           [ 0.75008178,  0.82502011, -0.99507202,  1.        , -0.93657855,
            -0.83571711],
           [-0.934284  , -0.97074098,  0.89721355, -0.93657855,  1.        ,
             0.97517215],
           [-0.99004057, -0.99981569,  0.77714685, -0.83571711,  0.97517215,
             1.        ]])

    Finally if we use the option ``rowvar=False``, the columns are now
    being treated as the variables and we will find the column-wise Pearson
    correlation coefficients between variables in ``xarr`` and ``yarr``.

    >>> R3 = np.corrcoef(xarr, yarr, rowvar=False)
    >>> R3
    array([[ 1.        ,  0.77598074, -0.47458546, -0.75078643, -0.9665554 ,
             0.22423734],
           [ 0.77598074,  1.        , -0.92346708, -0.99923895, -0.58826587,
            -0.44069024],
           [-0.47458546, -0.92346708,  1.        ,  0.93773029,  0.23297648,
             0.75137473],
           [-0.75078643, -0.99923895,  0.93773029,  1.        ,  0.55627469,
             0.47536961],
           [-0.9665554 , -0.58826587,  0.23297648,  0.55627469,  1.        ,
            -0.46666491],
           [ 0.22423734, -0.44069024,  0.75137473,  0.47536961, -0.46666491,
             1.        ]])

None
&&&&&&&&&&&&&&&&&&&&&& cos &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on ufunc:

cos = <ufunc 'cos'>
    cos(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])

    Cosine element-wise.

    Parameters
    ----------
    x : array_like
        Input array in radians.
    out : ndarray, None, or tuple of ndarray and None, optional
        A location into which the result is stored. If provided, it must have
        a shape that the inputs broadcast to. If not provided or None,
        a freshly-allocated array is returned. A tuple (possible only as a
        keyword argument) must have length equal to the number of outputs.
    where : array_like, optional
        This condition is broadcast over the input. At locations where the
        condition is True, the `out` array will be set to the ufunc result.
        Elsewhere, the `out` array will retain its original value.
        Note that if an uninitialized `out` array is created via the default
        ``out=None``, locations within it where the condition is False will
        remain uninitialized.
    **kwargs
        For other keyword-only arguments, see the
        :ref:`ufunc docs <ufuncs.kwargs>`.

    Returns
    -------
    y : ndarray
        The corresponding cosine values.
        This is a scalar if `x` is a scalar.

    Notes
    -----
    If `out` is provided, the function writes the result into it,
    and returns a reference to `out`.  (See Examples)

    References
    ----------
    M. Abramowitz and I. A. Stegun, Handbook of Mathematical Functions.
    New York, NY: Dover, 1972.

    Examples
    --------
    >>> np.cos(np.array([0, np.pi/2, np.pi]))
    array([  1.00000000e+00,   6.12303177e-17,  -1.00000000e+00])
    >>>
    >>> # Example of providing the optional output parameter
    >>> out1 = np.array([0], dtype='d')
    >>> out2 = np.cos([0.1], out1)
    >>> out2 is out1
    True
    >>>
    >>> # Example of ValueError due to provision of shape mis-matched `out`
    >>> np.cos(np.zeros((3,3)),np.zeros((2,2)))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: operands could not be broadcast together with shapes (3,3) (2,2)

None
&&&&&&&&&&&&&&&&&&&&&& cumsum &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

cumsum(a, axis=None, dtype=None, out=None)
    Return the cumulative sum of the elements along a given axis.

    Parameters
    ----------
    a : array_like
        Input array.
    axis : int, optional
        Axis along which the cumulative sum is computed. The default
        (None) is to compute the cumsum over the flattened array.
    dtype : dtype, optional
        Type of the returned array and of the accumulator in which the
        elements are summed.  If `dtype` is not specified, it defaults
        to the dtype of `a`, unless `a` has an integer dtype with a
        precision less than that of the default platform integer.  In
        that case, the default platform integer is used.
    out : ndarray, optional
        Alternative output array in which to place the result. It must
        have the same shape and buffer length as the expected output
        but the type will be cast if necessary. See :ref:`ufuncs-output-type` for
        more details.

    Returns
    -------
    cumsum_along_axis : ndarray.
        A new array holding the result is returned unless `out` is
        specified, in which case a reference to `out` is returned. The
        result has the same size as `a`, and the same shape as `a` if
        `axis` is not None or `a` is a 1-d array.

    See Also
    --------
    sum : Sum array elements.
    trapz : Integration of array values using the composite trapezoidal rule.
    diff : Calculate the n-th discrete difference along given axis.

    Notes
    -----
    Arithmetic is modular when using integer types, and no error is
    raised on overflow.

    ``cumsum(a)[-1]`` may not be equal to ``sum(a)`` for floating-point
    values since ``sum`` may use a pairwise summation routine, reducing
    the roundoff-error. See `sum` for more information.

    Examples
    --------
    >>> a = np.array([[1,2,3], [4,5,6]])
    >>> a
    array([[1, 2, 3],
           [4, 5, 6]])
    >>> np.cumsum(a)
    array([ 1,  3,  6, 10, 15, 21])
    >>> np.cumsum(a, dtype=float)     # specifies type of output value(s)
    array([  1.,   3.,   6.,  10.,  15.,  21.])

    >>> np.cumsum(a,axis=0)      # sum over rows for each of the 3 columns
    array([[1, 2, 3],
           [5, 7, 9]])
    >>> np.cumsum(a,axis=1)      # sum over columns for each of the 2 rows
    array([[ 1,  3,  6],
           [ 4,  9, 15]])

    ``cumsum(b)[-1]`` may not be equal to ``sum(b)``

    >>> b = np.array([1, 2e-9, 3e-9] * 1000000)
    >>> b.cumsum()[-1]
    1000000.0050045159
    >>> b.sum()
    1000000.0050000029

None
&&&&&&&&&&&&&&&&&&&&&& degrees &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on ufunc:

degrees = <ufunc 'degrees'>
    degrees(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])

    Convert angles from radians to degrees.

    Parameters
    ----------
    x : array_like
        Input array in radians.
    out : ndarray, None, or tuple of ndarray and None, optional
        A location into which the result is stored. If provided, it must have
        a shape that the inputs broadcast to. If not provided or None,
        a freshly-allocated array is returned. A tuple (possible only as a
        keyword argument) must have length equal to the number of outputs.
    where : array_like, optional
        This condition is broadcast over the input. At locations where the
        condition is True, the `out` array will be set to the ufunc result.
        Elsewhere, the `out` array will retain its original value.
        Note that if an uninitialized `out` array is created via the default
        ``out=None``, locations within it where the condition is False will
        remain uninitialized.
    **kwargs
        For other keyword-only arguments, see the
        :ref:`ufunc docs <ufuncs.kwargs>`.

    Returns
    -------
    y : ndarray of floats
        The corresponding degree values; if `out` was supplied this is a
        reference to it.
        This is a scalar if `x` is a scalar.

    See Also
    --------
    rad2deg : equivalent function

    Examples
    --------
    Convert a radian array to degrees

    >>> rad = np.arange(12.)*np.pi/6
    >>> np.degrees(rad)
    array([   0.,   30.,   60.,   90.,  120.,  150.,  180.,  210.,  240.,
            270.,  300.,  330.])

    >>> out = np.zeros((rad.shape))
    >>> r = np.degrees(rad, out)
    >>> np.all(r == out)
    True

None
&&&&&&&&&&&&&&&&&&&&&& e &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on float object:

class float(object)
 |  float(x=0, /)
 |
 |  Convert a string or number to a floating point number, if possible.
 |
 |  Methods defined here:
 |
 |  __abs__(self, /)
 |      abs(self)
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __bool__(self, /)
 |      True if self else False
 |
 |  __ceil__(self, /)
 |      Return the ceiling as an Integral.
 |
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __float__(self, /)
 |      float(self)
 |
 |  __floor__(self, /)
 |      Return the floor as an Integral.
 |
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |
 |  __format__(self, format_spec, /)
 |      Formats the float according to format_spec.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __getnewargs__(self, /)
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
 |
 |  __int__(self, /)
 |      int(self)
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __mod__(self, value, /)
 |      Return self%value.
 |
 |  __mul__(self, value, /)
 |      Return self*value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __neg__(self, /)
 |      -self
 |
 |  __pos__(self, /)
 |      +self
 |
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |
 |  __radd__(self, value, /)
 |      Return value+self.
 |
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |
 |  __rmod__(self, value, /)
 |      Return value%self.
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __round__(self, ndigits=None, /)
 |      Return the Integral closest to x, rounding half toward even.
 |
 |      When an argument is passed, work like built-in round(x, ndigits).
 |
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |
 |  __rsub__(self, value, /)
 |      Return value-self.
 |
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |
 |  __sub__(self, value, /)
 |      Return self-value.
 |
 |  __truediv__(self, value, /)
 |      Return self/value.
 |
 |  __trunc__(self, /)
 |      Return the Integral closest to x between 0 and x.
 |
 |  as_integer_ratio(self, /)
 |      Return a pair of integers, whose ratio is exactly equal to the original float.
 |
 |      The ratio is in lowest terms and has a positive denominator.  Raise
 |      OverflowError on infinities and a ValueError on NaNs.
 |
 |      >>> (10.0).as_integer_ratio()
 |      (10, 1)
 |      >>> (0.0).as_integer_ratio()
 |      (0, 1)
 |      >>> (-.25).as_integer_ratio()
 |      (-1, 4)
 |
 |  conjugate(self, /)
 |      Return self, the complex conjugate of any float.
 |
 |  hex(self, /)
 |      Return a hexadecimal representation of a floating-point number.
 |
 |      >>> (-0.1).hex()
 |      '-0x1.999999999999ap-4'
 |      >>> 3.14159.hex()
 |      '0x1.921f9f01b866ep+1'
 |
 |  is_integer(self, /)
 |      Return True if the float is an integer.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __getformat__(typestr, /) from builtins.type
 |      You probably don't want to use this function.
 |
 |        typestr
 |          Must be 'double' or 'float'.
 |
 |      It exists mainly to be used in Python's test suite.
 |
 |      This function returns whichever of 'unknown', 'IEEE, big-endian' or 'IEEE,
 |      little-endian' best describes the format of floating point numbers used by the
 |      C type named by typestr.
 |
 |  fromhex(string, /) from builtins.type
 |      Create a floating-point number from a hexadecimal string.
 |
 |      >>> float.fromhex('0x1.ffffp10')
 |      2047.984375
 |      >>> float.fromhex('-0x1p-1074')
 |      -5e-324
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
 |  imag
 |      the imaginary part of a complex number
 |
 |  real
 |      the real part of a complex number

None
&&&&&&&&&&&&&&&&&&&&&& exp &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on ufunc:

exp = <ufunc 'exp'>
    exp(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])

    Calculate the exponential of all elements in the input array.

    Parameters
    ----------
    x : array_like
        Input values.
    out : ndarray, None, or tuple of ndarray and None, optional
        A location into which the result is stored. If provided, it must have
        a shape that the inputs broadcast to. If not provided or None,
        a freshly-allocated array is returned. A tuple (possible only as a
        keyword argument) must have length equal to the number of outputs.
    where : array_like, optional
        This condition is broadcast over the input. At locations where the
        condition is True, the `out` array will be set to the ufunc result.
        Elsewhere, the `out` array will retain its original value.
        Note that if an uninitialized `out` array is created via the default
        ``out=None``, locations within it where the condition is False will
        remain uninitialized.
    **kwargs
        For other keyword-only arguments, see the
        :ref:`ufunc docs <ufuncs.kwargs>`.

    Returns
    -------
    out : ndarray or scalar
        Output array, element-wise exponential of `x`.
        This is a scalar if `x` is a scalar.

    See Also
    --------
    expm1 : Calculate ``exp(x) - 1`` for all elements in the array.
    exp2  : Calculate ``2**x`` for all elements in the array.

    Notes
    -----
    The irrational number ``e`` is also known as Euler's number.  It is
    approximately 2.718281, and is the base of the natural logarithm,
    ``ln`` (this means that, if :math:`x = \ln y = \log_e y`,
    then :math:`e^x = y`. For real input, ``exp(x)`` is always positive.

    For complex arguments, ``x = a + ib``, we can write
    :math:`e^x = e^a e^{ib}`.  The first term, :math:`e^a`, is already
    known (it is the real argument, described above).  The second term,
    :math:`e^{ib}`, is :math:`\cos b + i \sin b`, a function with
    magnitude 1 and a periodic phase.

    References
    ----------
    .. [1] Wikipedia, "Exponential function",
           https://en.wikipedia.org/wiki/Exponential_function
    .. [2] M. Abramovitz and I. A. Stegun, "Handbook of Mathematical Functions
           with Formulas, Graphs, and Mathematical Tables," Dover, 1964, p. 69,
           https://personal.math.ubc.ca/~cbm/aands/page_69.htm

    Examples
    --------
    Plot the magnitude and phase of ``exp(x)`` in the complex plane:

    >>> import matplotlib.pyplot as plt

    >>> x = np.linspace(-2*np.pi, 2*np.pi, 100)
    >>> xx = x + 1j * x[:, np.newaxis] # a + ib over complex plane
    >>> out = np.exp(xx)

    >>> plt.subplot(121)
    >>> plt.imshow(np.abs(out),
    ...            extent=[-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi], cmap='gray')
    >>> plt.title('Magnitude of exp(x)')

    >>> plt.subplot(122)
    >>> plt.imshow(np.angle(out),
    ...            extent=[-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi], cmap='hsv')
    >>> plt.title('Phase (angle) of exp(x)')
    >>> plt.show()

None
&&&&&&&&&&&&&&&&&&&&&& fft &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on package numpy.fft in numpy:

NAME
    numpy.fft

DESCRIPTION
    Discrete Fourier Transform (:mod:`numpy.fft`)
    =============================================

    .. currentmodule:: numpy.fft

    The SciPy module `scipy.fft` is a more comprehensive superset
    of ``numpy.fft``, which includes only a basic set of routines.

    Standard FFTs
    -------------

    .. autosummary::
       :toctree: generated/

       fft       Discrete Fourier transform.
       ifft      Inverse discrete Fourier transform.
       fft2      Discrete Fourier transform in two dimensions.
       ifft2     Inverse discrete Fourier transform in two dimensions.
       fftn      Discrete Fourier transform in N-dimensions.
       ifftn     Inverse discrete Fourier transform in N dimensions.

    Real FFTs
    ---------

    .. autosummary::
       :toctree: generated/

       rfft      Real discrete Fourier transform.
       irfft     Inverse real discrete Fourier transform.
       rfft2     Real discrete Fourier transform in two dimensions.
       irfft2    Inverse real discrete Fourier transform in two dimensions.
       rfftn     Real discrete Fourier transform in N dimensions.
       irfftn    Inverse real discrete Fourier transform in N dimensions.

    Hermitian FFTs
    --------------

    .. autosummary::
       :toctree: generated/

       hfft      Hermitian discrete Fourier transform.
       ihfft     Inverse Hermitian discrete Fourier transform.

    Helper routines
    ---------------

    .. autosummary::
       :toctree: generated/

       fftfreq   Discrete Fourier Transform sample frequencies.
       rfftfreq  DFT sample frequencies (for usage with rfft, irfft).
       fftshift  Shift zero-frequency component to center of spectrum.
       ifftshift Inverse of fftshift.


    Background information
    ----------------------

    Fourier analysis is fundamentally a method for expressing a function as a
    sum of periodic components, and for recovering the function from those
    components.  When both the function and its Fourier transform are
    replaced with discretized counterparts, it is called the discrete Fourier
    transform (DFT).  The DFT has become a mainstay of numerical computing in
    part because of a very fast algorithm for computing it, called the Fast
    Fourier Transform (FFT), which was known to Gauss (1805) and was brought
    to light in its current form by Cooley and Tukey [CT]_.  Press et al. [NR]_
    provide an accessible introduction to Fourier analysis and its
    applications.

    Because the discrete Fourier transform separates its input into
    components that contribute at discrete frequencies, it has a great number
    of applications in digital signal processing, e.g., for filtering, and in
    this context the discretized input to the transform is customarily
    referred to as a *signal*, which exists in the *time domain*.  The output
    is called a *spectrum* or *transform* and exists in the *frequency
    domain*.

    Implementation details
    ----------------------

    There are many ways to define the DFT, varying in the sign of the
    exponent, normalization, etc.  In this implementation, the DFT is defined
    as

    .. math::
       A_k =  \sum_{m=0}^{n-1} a_m \exp\left\{-2\pi i{mk \over n}\right\}
       \qquad k = 0,\ldots,n-1.

    The DFT is in general defined for complex inputs and outputs, and a
    single-frequency component at linear frequency :math:`f` is
    represented by a complex exponential
    :math:`a_m = \exp\{2\pi i\,f m\Delta t\}`, where :math:`\Delta t`
    is the sampling interval.

    The values in the result follow so-called "standard" order: If ``A =
    fft(a, n)``, then ``A[0]`` contains the zero-frequency term (the sum of
    the signal), which is always purely real for real inputs. Then ``A[1:n/2]``
    contains the positive-frequency terms, and ``A[n/2+1:]`` contains the
    negative-frequency terms, in order of decreasingly negative frequency.
    For an even number of input points, ``A[n/2]`` represents both positive and
    negative Nyquist frequency, and is also purely real for real input.  For
    an odd number of input points, ``A[(n-1)/2]`` contains the largest positive
    frequency, while ``A[(n+1)/2]`` contains the largest negative frequency.
    The routine ``np.fft.fftfreq(n)`` returns an array giving the frequencies
    of corresponding elements in the output.  The routine
    ``np.fft.fftshift(A)`` shifts transforms and their frequencies to put the
    zero-frequency components in the middle, and ``np.fft.ifftshift(A)`` undoes
    that shift.

    When the input `a` is a time-domain signal and ``A = fft(a)``, ``np.abs(A)``
    is its amplitude spectrum and ``np.abs(A)**2`` is its power spectrum.
    The phase spectrum is obtained by ``np.angle(A)``.

    The inverse DFT is defined as

    .. math::
       a_m = \frac{1}{n}\sum_{k=0}^{n-1}A_k\exp\left\{2\pi i{mk\over n}\right\}
       \qquad m = 0,\ldots,n-1.

    It differs from the forward transform by the sign of the exponential
    argument and the default normalization by :math:`1/n`.

    Type Promotion
    --------------

    `numpy.fft` promotes ``float32`` and ``complex64`` arrays to ``float64`` and
    ``complex128`` arrays respectively. For an FFT implementation that does not
    promote input arrays, see `scipy.fftpack`.

    Normalization
    -------------

    The argument ``norm`` indicates which direction of the pair of direct/inverse
    transforms is scaled and with what normalization factor.
    The default normalization (``"backward"``) has the direct (forward) transforms
    unscaled and the inverse (backward) transforms scaled by :math:`1/n`. It is
    possible to obtain unitary transforms by setting the keyword argument ``norm``
    to ``"ortho"`` so that both direct and inverse transforms are scaled by
    :math:`1/\sqrt{n}`. Finally, setting the keyword argument ``norm`` to
    ``"forward"`` has the direct transforms scaled by :math:`1/n` and the inverse
    transforms unscaled (i.e. exactly opposite to the default ``"backward"``).
    `None` is an alias of the default option ``"backward"`` for backward
    compatibility.

    Real and Hermitian transforms
    -----------------------------

    When the input is purely real, its transform is Hermitian, i.e., the
    component at frequency :math:`f_k` is the complex conjugate of the
    component at frequency :math:`-f_k`, which means that for real
    inputs there is no information in the negative frequency components that
    is not already available from the positive frequency components.
    The family of `rfft` functions is
    designed to operate on real inputs, and exploits this symmetry by
    computing only the positive frequency components, up to and including the
    Nyquist frequency.  Thus, ``n`` input points produce ``n/2+1`` complex
    output points.  The inverses of this family assumes the same symmetry of
    its input, and for an output of ``n`` points uses ``n/2+1`` input points.

    Correspondingly, when the spectrum is purely real, the signal is
    Hermitian.  The `hfft` family of functions exploits this symmetry by
    using ``n/2+1`` complex points in the input (time) domain for ``n`` real
    points in the frequency domain.

    In higher dimensions, FFTs are used, e.g., for image analysis and
    filtering.  The computational efficiency of the FFT means that it can
    also be a faster way to compute large convolutions, using the property
    that a convolution in the time domain is equivalent to a point-by-point
    multiplication in the frequency domain.

    Higher dimensions
    -----------------

    In two dimensions, the DFT is defined as

    .. math::
       A_{kl} =  \sum_{m=0}^{M-1} \sum_{n=0}^{N-1}
       a_{mn}\exp\left\{-2\pi i \left({mk\over M}+{nl\over N}\right)\right\}
       \qquad k = 0, \ldots, M-1;\quad l = 0, \ldots, N-1,

    which extends in the obvious way to higher dimensions, and the inverses
    in higher dimensions also extend in the same way.

    References
    ----------

    .. [CT] Cooley, James W., and John W. Tukey, 1965, "An algorithm for the
            machine calculation of complex Fourier series," *Math. Comput.*
            19: 297-301.

    .. [NR] Press, W., Teukolsky, S., Vetterline, W.T., and Flannery, B.P.,
            2007, *Numerical Recipes: The Art of Scientific Computing*, ch.
            12-13.  Cambridge Univ. Press, Cambridge, UK.

    Examples
    --------

    For examples, see the various functions.

PACKAGE CONTENTS
    _pocketfft
    _pocketfft_internal
    helper
    tests (package)

FUNCTIONS
    fft(a, n=None, axis=-1, norm=None)
        Compute the one-dimensional discrete Fourier Transform.

        This function computes the one-dimensional *n*-point discrete Fourier
        Transform (DFT) with the efficient Fast Fourier Transform (FFT)
        algorithm [CT].

        Parameters
        ----------
        a : array_like
            Input array, can be complex.
        n : int, optional
            Length of the transformed axis of the output.
            If `n` is smaller than the length of the input, the input is cropped.
            If it is larger, the input is padded with zeros.  If `n` is not given,
            the length of the input along the axis specified by `axis` is used.
        axis : int, optional
            Axis over which to compute the FFT.  If not given, the last axis is
            used.
        norm : {"backward", "ortho", "forward"}, optional
            .. versionadded:: 1.10.0

            Normalization mode (see `numpy.fft`). Default is "backward".
            Indicates which direction of the forward/backward pair of transforms
            is scaled and with what normalization factor.

            .. versionadded:: 1.20.0

                The "backward", "forward" values were added.

        Returns
        -------
        out : complex ndarray
            The truncated or zero-padded input, transformed along the axis
            indicated by `axis`, or the last one if `axis` is not specified.

        Raises
        ------
        IndexError
            If `axis` is not a valid axis of `a`.

        See Also
        --------
        numpy.fft : for definition of the DFT and conventions used.
        ifft : The inverse of `fft`.
        fft2 : The two-dimensional FFT.
        fftn : The *n*-dimensional FFT.
        rfftn : The *n*-dimensional FFT of real input.
        fftfreq : Frequency bins for given FFT parameters.

        Notes
        -----
        FFT (Fast Fourier Transform) refers to a way the discrete Fourier
        Transform (DFT) can be calculated efficiently, by using symmetries in the
        calculated terms.  The symmetry is highest when `n` is a power of 2, and
        the transform is therefore most efficient for these sizes.

        The DFT is defined, with the conventions used in this implementation, in
        the documentation for the `numpy.fft` module.

        References
        ----------
        .. [CT] Cooley, James W., and John W. Tukey, 1965, "An algorithm for the
                machine calculation of complex Fourier series," *Math. Comput.*
                19: 297-301.

        Examples
        --------
        >>> np.fft.fft(np.exp(2j * np.pi * np.arange(8) / 8))
        array([-2.33486982e-16+1.14423775e-17j,  8.00000000e+00-1.25557246e-15j,
                2.33486982e-16+2.33486982e-16j,  0.00000000e+00+1.22464680e-16j,
               -1.14423775e-17+2.33486982e-16j,  0.00000000e+00+5.20784380e-16j,
                1.14423775e-17+1.14423775e-17j,  0.00000000e+00+1.22464680e-16j])

        In this example, real input has an FFT which is Hermitian, i.e., symmetric
        in the real part and anti-symmetric in the imaginary part, as described in
        the `numpy.fft` documentation:

        >>> import matplotlib.pyplot as plt
        >>> t = np.arange(256)
        >>> sp = np.fft.fft(np.sin(t))
        >>> freq = np.fft.fftfreq(t.shape[-1])
        >>> plt.plot(freq, sp.real, freq, sp.imag)
        [<matplotlib.lines.Line2D object at 0x...>, <matplotlib.lines.Line2D object at 0x...>]
        >>> plt.show()

    fft2(a, s=None, axes=(-2, -1), norm=None)
        Compute the 2-dimensional discrete Fourier Transform.

        This function computes the *n*-dimensional discrete Fourier Transform
        over any axes in an *M*-dimensional array by means of the
        Fast Fourier Transform (FFT).  By default, the transform is computed over
        the last two axes of the input array, i.e., a 2-dimensional FFT.

        Parameters
        ----------
        a : array_like
            Input array, can be complex
        s : sequence of ints, optional
            Shape (length of each transformed axis) of the output
            (``s[0]`` refers to axis 0, ``s[1]`` to axis 1, etc.).
            This corresponds to ``n`` for ``fft(x, n)``.
            Along each axis, if the given shape is smaller than that of the input,
            the input is cropped.  If it is larger, the input is padded with zeros.
            if `s` is not given, the shape of the input along the axes specified
            by `axes` is used.
        axes : sequence of ints, optional
            Axes over which to compute the FFT.  If not given, the last two
            axes are used.  A repeated index in `axes` means the transform over
            that axis is performed multiple times.  A one-element sequence means
            that a one-dimensional FFT is performed.
        norm : {"backward", "ortho", "forward"}, optional
            .. versionadded:: 1.10.0

            Normalization mode (see `numpy.fft`). Default is "backward".
            Indicates which direction of the forward/backward pair of transforms
            is scaled and with what normalization factor.

            .. versionadded:: 1.20.0

                The "backward", "forward" values were added.

        Returns
        -------
        out : complex ndarray
            The truncated or zero-padded input, transformed along the axes
            indicated by `axes`, or the last two axes if `axes` is not given.

        Raises
        ------
        ValueError
            If `s` and `axes` have different length, or `axes` not given and
            ``len(s) != 2``.
        IndexError
            If an element of `axes` is larger than than the number of axes of `a`.

        See Also
        --------
        numpy.fft : Overall view of discrete Fourier transforms, with definitions
             and conventions used.
        ifft2 : The inverse two-dimensional FFT.
        fft : The one-dimensional FFT.
        fftn : The *n*-dimensional FFT.
        fftshift : Shifts zero-frequency terms to the center of the array.
            For two-dimensional input, swaps first and third quadrants, and second
            and fourth quadrants.

        Notes
        -----
        `fft2` is just `fftn` with a different default for `axes`.

        The output, analogously to `fft`, contains the term for zero frequency in
        the low-order corner of the transformed axes, the positive frequency terms
        in the first half of these axes, the term for the Nyquist frequency in the
        middle of the axes and the negative frequency terms in the second half of
        the axes, in order of decreasingly negative frequency.

        See `fftn` for details and a plotting example, and `numpy.fft` for
        definitions and conventions used.


        Examples
        --------
        >>> a = np.mgrid[:5, :5][0]
        >>> np.fft.fft2(a)
        array([[ 50.  +0.j        ,   0.  +0.j        ,   0.  +0.j        , # may vary
                  0.  +0.j        ,   0.  +0.j        ],
               [-12.5+17.20477401j,   0.  +0.j        ,   0.  +0.j        ,
                  0.  +0.j        ,   0.  +0.j        ],
               [-12.5 +4.0614962j ,   0.  +0.j        ,   0.  +0.j        ,
                  0.  +0.j        ,   0.  +0.j        ],
               [-12.5 -4.0614962j ,   0.  +0.j        ,   0.  +0.j        ,
                  0.  +0.j        ,   0.  +0.j        ],
               [-12.5-17.20477401j,   0.  +0.j        ,   0.  +0.j        ,
                  0.  +0.j        ,   0.  +0.j        ]])

    fftfreq(n, d=1.0)
        Return the Discrete Fourier Transform sample frequencies.

        The returned float array `f` contains the frequency bin centers in cycles
        per unit of the sample spacing (with zero at the start).  For instance, if
        the sample spacing is in seconds, then the frequency unit is cycles/second.

        Given a window length `n` and a sample spacing `d`::

          f = [0, 1, ...,   n/2-1,     -n/2, ..., -1] / (d*n)   if n is even
          f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (d*n)   if n is odd

        Parameters
        ----------
        n : int
            Window length.
        d : scalar, optional
            Sample spacing (inverse of the sampling rate). Defaults to 1.

        Returns
        -------
        f : ndarray
            Array of length `n` containing the sample frequencies.

        Examples
        --------
        >>> signal = np.array([-2, 8, 6, 4, 1, 0, 3, 5], dtype=float)
        >>> fourier = np.fft.fft(signal)
        >>> n = signal.size
        >>> timestep = 0.1
        >>> freq = np.fft.fftfreq(n, d=timestep)
        >>> freq
        array([ 0.  ,  1.25,  2.5 , ..., -3.75, -2.5 , -1.25])

    fftn(a, s=None, axes=None, norm=None)
        Compute the N-dimensional discrete Fourier Transform.

        This function computes the *N*-dimensional discrete Fourier Transform over
        any number of axes in an *M*-dimensional array by means of the Fast Fourier
        Transform (FFT).

        Parameters
        ----------
        a : array_like
            Input array, can be complex.
        s : sequence of ints, optional
            Shape (length of each transformed axis) of the output
            (``s[0]`` refers to axis 0, ``s[1]`` to axis 1, etc.).
            This corresponds to ``n`` for ``fft(x, n)``.
            Along any axis, if the given shape is smaller than that of the input,
            the input is cropped.  If it is larger, the input is padded with zeros.
            if `s` is not given, the shape of the input along the axes specified
            by `axes` is used.
        axes : sequence of ints, optional
            Axes over which to compute the FFT.  If not given, the last ``len(s)``
            axes are used, or all axes if `s` is also not specified.
            Repeated indices in `axes` means that the transform over that axis is
            performed multiple times.
        norm : {"backward", "ortho", "forward"}, optional
            .. versionadded:: 1.10.0

            Normalization mode (see `numpy.fft`). Default is "backward".
            Indicates which direction of the forward/backward pair of transforms
            is scaled and with what normalization factor.

            .. versionadded:: 1.20.0

                The "backward", "forward" values were added.

        Returns
        -------
        out : complex ndarray
            The truncated or zero-padded input, transformed along the axes
            indicated by `axes`, or by a combination of `s` and `a`,
            as explained in the parameters section above.

        Raises
        ------
        ValueError
            If `s` and `axes` have different length.
        IndexError
            If an element of `axes` is larger than than the number of axes of `a`.

        See Also
        --------
        numpy.fft : Overall view of discrete Fourier transforms, with definitions
            and conventions used.
        ifftn : The inverse of `fftn`, the inverse *n*-dimensional FFT.
        fft : The one-dimensional FFT, with definitions and conventions used.
        rfftn : The *n*-dimensional FFT of real input.
        fft2 : The two-dimensional FFT.
        fftshift : Shifts zero-frequency terms to centre of array

        Notes
        -----
        The output, analogously to `fft`, contains the term for zero frequency in
        the low-order corner of all axes, the positive frequency terms in the
        first half of all axes, the term for the Nyquist frequency in the middle
        of all axes and the negative frequency terms in the second half of all
        axes, in order of decreasingly negative frequency.

        See `numpy.fft` for details, definitions and conventions used.

        Examples
        --------
        >>> a = np.mgrid[:3, :3, :3][0]
        >>> np.fft.fftn(a, axes=(1, 2))
        array([[[ 0.+0.j,   0.+0.j,   0.+0.j], # may vary
                [ 0.+0.j,   0.+0.j,   0.+0.j],
                [ 0.+0.j,   0.+0.j,   0.+0.j]],
               [[ 9.+0.j,   0.+0.j,   0.+0.j],
                [ 0.+0.j,   0.+0.j,   0.+0.j],
                [ 0.+0.j,   0.+0.j,   0.+0.j]],
               [[18.+0.j,   0.+0.j,   0.+0.j],
                [ 0.+0.j,   0.+0.j,   0.+0.j],
                [ 0.+0.j,   0.+0.j,   0.+0.j]]])
        >>> np.fft.fftn(a, (2, 2), axes=(0, 1))
        array([[[ 2.+0.j,  2.+0.j,  2.+0.j], # may vary
                [ 0.+0.j,  0.+0.j,  0.+0.j]],
               [[-2.+0.j, -2.+0.j, -2.+0.j],
                [ 0.+0.j,  0.+0.j,  0.+0.j]]])

        >>> import matplotlib.pyplot as plt
        >>> [X, Y] = np.meshgrid(2 * np.pi * np.arange(200) / 12,
        ...                      2 * np.pi * np.arange(200) / 34)
        >>> S = np.sin(X) + np.cos(Y) + np.random.uniform(0, 1, X.shape)
        >>> FS = np.fft.fftn(S)
        >>> plt.imshow(np.log(np.abs(np.fft.fftshift(FS))**2))
        <matplotlib.image.AxesImage object at 0x...>
        >>> plt.show()

    fftshift(x, axes=None)
        Shift the zero-frequency component to the center of the spectrum.

        This function swaps half-spaces for all axes listed (defaults to all).
        Note that ``y[0]`` is the Nyquist component only if ``len(x)`` is even.

        Parameters
        ----------
        x : array_like
            Input array.
        axes : int or shape tuple, optional
            Axes over which to shift.  Default is None, which shifts all axes.

        Returns
        -------
        y : ndarray
            The shifted array.

        See Also
        --------
        ifftshift : The inverse of `fftshift`.

        Examples
        --------
        >>> freqs = np.fft.fftfreq(10, 0.1)
        >>> freqs
        array([ 0.,  1.,  2., ..., -3., -2., -1.])
        >>> np.fft.fftshift(freqs)
        array([-5., -4., -3., -2., -1.,  0.,  1.,  2.,  3.,  4.])

        Shift the zero-frequency component only along the second axis:

        >>> freqs = np.fft.fftfreq(9, d=1./9).reshape(3, 3)
        >>> freqs
        array([[ 0.,  1.,  2.],
               [ 3.,  4., -4.],
               [-3., -2., -1.]])
        >>> np.fft.fftshift(freqs, axes=(1,))
        array([[ 2.,  0.,  1.],
               [-4.,  3.,  4.],
               [-1., -3., -2.]])

    hfft(a, n=None, axis=-1, norm=None)
        Compute the FFT of a signal that has Hermitian symmetry, i.e., a real
        spectrum.

        Parameters
        ----------
        a : array_like
            The input array.
        n : int, optional
            Length of the transformed axis of the output. For `n` output
            points, ``n//2 + 1`` input points are necessary.  If the input is
            longer than this, it is cropped.  If it is shorter than this, it is
            padded with zeros.  If `n` is not given, it is taken to be ``2*(m-1)``
            where ``m`` is the length of the input along the axis specified by
            `axis`.
        axis : int, optional
            Axis over which to compute the FFT. If not given, the last
            axis is used.
        norm : {"backward", "ortho", "forward"}, optional
            .. versionadded:: 1.10.0

            Normalization mode (see `numpy.fft`). Default is "backward".
            Indicates which direction of the forward/backward pair of transforms
            is scaled and with what normalization factor.

            .. versionadded:: 1.20.0

                The "backward", "forward" values were added.

        Returns
        -------
        out : ndarray
            The truncated or zero-padded input, transformed along the axis
            indicated by `axis`, or the last one if `axis` is not specified.
            The length of the transformed axis is `n`, or, if `n` is not given,
            ``2*m - 2`` where ``m`` is the length of the transformed axis of
            the input. To get an odd number of output points, `n` must be
            specified, for instance as ``2*m - 1`` in the typical case,

        Raises
        ------
        IndexError
            If `axis` is not a valid axis of `a`.

        See also
        --------
        rfft : Compute the one-dimensional FFT for real input.
        ihfft : The inverse of `hfft`.

        Notes
        -----
        `hfft`/`ihfft` are a pair analogous to `rfft`/`irfft`, but for the
        opposite case: here the signal has Hermitian symmetry in the time
        domain and is real in the frequency domain. So here it's `hfft` for
        which you must supply the length of the result if it is to be odd.

        * even: ``ihfft(hfft(a, 2*len(a) - 2)) == a``, within roundoff error,
        * odd: ``ihfft(hfft(a, 2*len(a) - 1)) == a``, within roundoff error.

        The correct interpretation of the hermitian input depends on the length of
        the original data, as given by `n`. This is because each input shape could
        correspond to either an odd or even length signal. By default, `hfft`
        assumes an even output length which puts the last entry at the Nyquist
        frequency; aliasing with its symmetric counterpart. By Hermitian symmetry,
        the value is thus treated as purely real. To avoid losing information, the
        shape of the full signal **must** be given.

        Examples
        --------
        >>> signal = np.array([1, 2, 3, 4, 3, 2])
        >>> np.fft.fft(signal)
        array([15.+0.j,  -4.+0.j,   0.+0.j,  -1.-0.j,   0.+0.j,  -4.+0.j]) # may vary
        >>> np.fft.hfft(signal[:4]) # Input first half of signal
        array([15.,  -4.,   0.,  -1.,   0.,  -4.])
        >>> np.fft.hfft(signal, 6)  # Input entire signal and truncate
        array([15.,  -4.,   0.,  -1.,   0.,  -4.])


        >>> signal = np.array([[1, 1.j], [-1.j, 2]])
        >>> np.conj(signal.T) - signal   # check Hermitian symmetry
        array([[ 0.-0.j,  -0.+0.j], # may vary
               [ 0.+0.j,  0.-0.j]])
        >>> freq_spectrum = np.fft.hfft(signal)
        >>> freq_spectrum
        array([[ 1.,  1.],
               [ 2., -2.]])

    ifft(a, n=None, axis=-1, norm=None)
        Compute the one-dimensional inverse discrete Fourier Transform.

        This function computes the inverse of the one-dimensional *n*-point
        discrete Fourier transform computed by `fft`.  In other words,
        ``ifft(fft(a)) == a`` to within numerical accuracy.
        For a general description of the algorithm and definitions,
        see `numpy.fft`.

        The input should be ordered in the same way as is returned by `fft`,
        i.e.,

        * ``a[0]`` should contain the zero frequency term,
        * ``a[1:n//2]`` should contain the positive-frequency terms,
        * ``a[n//2 + 1:]`` should contain the negative-frequency terms, in
          increasing order starting from the most negative frequency.

        For an even number of input points, ``A[n//2]`` represents the sum of
        the values at the positive and negative Nyquist frequencies, as the two
        are aliased together. See `numpy.fft` for details.

        Parameters
        ----------
        a : array_like
            Input array, can be complex.
        n : int, optional
            Length of the transformed axis of the output.
            If `n` is smaller than the length of the input, the input is cropped.
            If it is larger, the input is padded with zeros.  If `n` is not given,
            the length of the input along the axis specified by `axis` is used.
            See notes about padding issues.
        axis : int, optional
            Axis over which to compute the inverse DFT.  If not given, the last
            axis is used.
        norm : {"backward", "ortho", "forward"}, optional
            .. versionadded:: 1.10.0

            Normalization mode (see `numpy.fft`). Default is "backward".
            Indicates which direction of the forward/backward pair of transforms
            is scaled and with what normalization factor.

            .. versionadded:: 1.20.0

                The "backward", "forward" values were added.

        Returns
        -------
        out : complex ndarray
            The truncated or zero-padded input, transformed along the axis
            indicated by `axis`, or the last one if `axis` is not specified.

        Raises
        ------
        IndexError
            If `axis` is not a valid axis of `a`.

        See Also
        --------
        numpy.fft : An introduction, with definitions and general explanations.
        fft : The one-dimensional (forward) FFT, of which `ifft` is the inverse
        ifft2 : The two-dimensional inverse FFT.
        ifftn : The n-dimensional inverse FFT.

        Notes
        -----
        If the input parameter `n` is larger than the size of the input, the input
        is padded by appending zeros at the end.  Even though this is the common
        approach, it might lead to surprising results.  If a different padding is
        desired, it must be performed before calling `ifft`.

        Examples
        --------
        >>> np.fft.ifft([0, 4, 0, 0])
        array([ 1.+0.j,  0.+1.j, -1.+0.j,  0.-1.j]) # may vary

        Create and plot a band-limited signal with random phases:

        >>> import matplotlib.pyplot as plt
        >>> t = np.arange(400)
        >>> n = np.zeros((400,), dtype=complex)
        >>> n[40:60] = np.exp(1j*np.random.uniform(0, 2*np.pi, (20,)))
        >>> s = np.fft.ifft(n)
        >>> plt.plot(t, s.real, label='real')
        [<matplotlib.lines.Line2D object at ...>]
        >>> plt.plot(t, s.imag, '--', label='imaginary')
        [<matplotlib.lines.Line2D object at ...>]
        >>> plt.legend()
        <matplotlib.legend.Legend object at ...>
        >>> plt.show()

    ifft2(a, s=None, axes=(-2, -1), norm=None)
        Compute the 2-dimensional inverse discrete Fourier Transform.

        This function computes the inverse of the 2-dimensional discrete Fourier
        Transform over any number of axes in an M-dimensional array by means of
        the Fast Fourier Transform (FFT).  In other words, ``ifft2(fft2(a)) == a``
        to within numerical accuracy.  By default, the inverse transform is
        computed over the last two axes of the input array.

        The input, analogously to `ifft`, should be ordered in the same way as is
        returned by `fft2`, i.e. it should have the term for zero frequency
        in the low-order corner of the two axes, the positive frequency terms in
        the first half of these axes, the term for the Nyquist frequency in the
        middle of the axes and the negative frequency terms in the second half of
        both axes, in order of decreasingly negative frequency.

        Parameters
        ----------
        a : array_like
            Input array, can be complex.
        s : sequence of ints, optional
            Shape (length of each axis) of the output (``s[0]`` refers to axis 0,
            ``s[1]`` to axis 1, etc.).  This corresponds to `n` for ``ifft(x, n)``.
            Along each axis, if the given shape is smaller than that of the input,
            the input is cropped.  If it is larger, the input is padded with zeros.
            if `s` is not given, the shape of the input along the axes specified
            by `axes` is used.  See notes for issue on `ifft` zero padding.
        axes : sequence of ints, optional
            Axes over which to compute the FFT.  If not given, the last two
            axes are used.  A repeated index in `axes` means the transform over
            that axis is performed multiple times.  A one-element sequence means
            that a one-dimensional FFT is performed.
        norm : {"backward", "ortho", "forward"}, optional
            .. versionadded:: 1.10.0

            Normalization mode (see `numpy.fft`). Default is "backward".
            Indicates which direction of the forward/backward pair of transforms
            is scaled and with what normalization factor.

            .. versionadded:: 1.20.0

                The "backward", "forward" values were added.

        Returns
        -------
        out : complex ndarray
            The truncated or zero-padded input, transformed along the axes
            indicated by `axes`, or the last two axes if `axes` is not given.

        Raises
        ------
        ValueError
            If `s` and `axes` have different length, or `axes` not given and
            ``len(s) != 2``.
        IndexError
            If an element of `axes` is larger than than the number of axes of `a`.

        See Also
        --------
        numpy.fft : Overall view of discrete Fourier transforms, with definitions
             and conventions used.
        fft2 : The forward 2-dimensional FFT, of which `ifft2` is the inverse.
        ifftn : The inverse of the *n*-dimensional FFT.
        fft : The one-dimensional FFT.
        ifft : The one-dimensional inverse FFT.

        Notes
        -----
        `ifft2` is just `ifftn` with a different default for `axes`.

        See `ifftn` for details and a plotting example, and `numpy.fft` for
        definition and conventions used.

        Zero-padding, analogously with `ifft`, is performed by appending zeros to
        the input along the specified dimension.  Although this is the common
        approach, it might lead to surprising results.  If another form of zero
        padding is desired, it must be performed before `ifft2` is called.

        Examples
        --------
        >>> a = 4 * np.eye(4)
        >>> np.fft.ifft2(a)
        array([[1.+0.j,  0.+0.j,  0.+0.j,  0.+0.j], # may vary
               [0.+0.j,  0.+0.j,  0.+0.j,  1.+0.j],
               [0.+0.j,  0.+0.j,  1.+0.j,  0.+0.j],
               [0.+0.j,  1.+0.j,  0.+0.j,  0.+0.j]])

    ifftn(a, s=None, axes=None, norm=None)
        Compute the N-dimensional inverse discrete Fourier Transform.

        This function computes the inverse of the N-dimensional discrete
        Fourier Transform over any number of axes in an M-dimensional array by
        means of the Fast Fourier Transform (FFT).  In other words,
        ``ifftn(fftn(a)) == a`` to within numerical accuracy.
        For a description of the definitions and conventions used, see `numpy.fft`.

        The input, analogously to `ifft`, should be ordered in the same way as is
        returned by `fftn`, i.e. it should have the term for zero frequency
        in all axes in the low-order corner, the positive frequency terms in the
        first half of all axes, the term for the Nyquist frequency in the middle
        of all axes and the negative frequency terms in the second half of all
        axes, in order of decreasingly negative frequency.

        Parameters
        ----------
        a : array_like
            Input array, can be complex.
        s : sequence of ints, optional
            Shape (length of each transformed axis) of the output
            (``s[0]`` refers to axis 0, ``s[1]`` to axis 1, etc.).
            This corresponds to ``n`` for ``ifft(x, n)``.
            Along any axis, if the given shape is smaller than that of the input,
            the input is cropped.  If it is larger, the input is padded with zeros.
            if `s` is not given, the shape of the input along the axes specified
            by `axes` is used.  See notes for issue on `ifft` zero padding.
        axes : sequence of ints, optional
            Axes over which to compute the IFFT.  If not given, the last ``len(s)``
            axes are used, or all axes if `s` is also not specified.
            Repeated indices in `axes` means that the inverse transform over that
            axis is performed multiple times.
        norm : {"backward", "ortho", "forward"}, optional
            .. versionadded:: 1.10.0

            Normalization mode (see `numpy.fft`). Default is "backward".
            Indicates which direction of the forward/backward pair of transforms
            is scaled and with what normalization factor.

            .. versionadded:: 1.20.0

                The "backward", "forward" values were added.

        Returns
        -------
        out : complex ndarray
            The truncated or zero-padded input, transformed along the axes
            indicated by `axes`, or by a combination of `s` or `a`,
            as explained in the parameters section above.

        Raises
        ------
        ValueError
            If `s` and `axes` have different length.
        IndexError
            If an element of `axes` is larger than than the number of axes of `a`.

        See Also
        --------
        numpy.fft : Overall view of discrete Fourier transforms, with definitions
             and conventions used.
        fftn : The forward *n*-dimensional FFT, of which `ifftn` is the inverse.
        ifft : The one-dimensional inverse FFT.
        ifft2 : The two-dimensional inverse FFT.
        ifftshift : Undoes `fftshift`, shifts zero-frequency terms to beginning
            of array.

        Notes
        -----
        See `numpy.fft` for definitions and conventions used.

        Zero-padding, analogously with `ifft`, is performed by appending zeros to
        the input along the specified dimension.  Although this is the common
        approach, it might lead to surprising results.  If another form of zero
        padding is desired, it must be performed before `ifftn` is called.

        Examples
        --------
        >>> a = np.eye(4)
        >>> np.fft.ifftn(np.fft.fftn(a, axes=(0,)), axes=(1,))
        array([[1.+0.j,  0.+0.j,  0.+0.j,  0.+0.j], # may vary
               [0.+0.j,  1.+0.j,  0.+0.j,  0.+0.j],
               [0.+0.j,  0.+0.j,  1.+0.j,  0.+0.j],
               [0.+0.j,  0.+0.j,  0.+0.j,  1.+0.j]])


        Create and plot an image with band-limited frequency content:

        >>> import matplotlib.pyplot as plt
        >>> n = np.zeros((200,200), dtype=complex)
        >>> n[60:80, 20:40] = np.exp(1j*np.random.uniform(0, 2*np.pi, (20, 20)))
        >>> im = np.fft.ifftn(n).real
        >>> plt.imshow(im)
        <matplotlib.image.AxesImage object at 0x...>
        >>> plt.show()

    ifftshift(x, axes=None)
        The inverse of `fftshift`. Although identical for even-length `x`, the
        functions differ by one sample for odd-length `x`.

        Parameters
        ----------
        x : array_like
            Input array.
        axes : int or shape tuple, optional
            Axes over which to calculate.  Defaults to None, which shifts all axes.

        Returns
        -------
        y : ndarray
            The shifted array.

        See Also
        --------
        fftshift : Shift zero-frequency component to the center of the spectrum.

        Examples
        --------
        >>> freqs = np.fft.fftfreq(9, d=1./9).reshape(3, 3)
        >>> freqs
        array([[ 0.,  1.,  2.],
               [ 3.,  4., -4.],
               [-3., -2., -1.]])
        >>> np.fft.ifftshift(np.fft.fftshift(freqs))
        array([[ 0.,  1.,  2.],
               [ 3.,  4., -4.],
               [-3., -2., -1.]])

    ihfft(a, n=None, axis=-1, norm=None)
        Compute the inverse FFT of a signal that has Hermitian symmetry.

        Parameters
        ----------
        a : array_like
            Input array.
        n : int, optional
            Length of the inverse FFT, the number of points along
            transformation axis in the input to use.  If `n` is smaller than
            the length of the input, the input is cropped.  If it is larger,
            the input is padded with zeros. If `n` is not given, the length of
            the input along the axis specified by `axis` is used.
        axis : int, optional
            Axis over which to compute the inverse FFT. If not given, the last
            axis is used.
        norm : {"backward", "ortho", "forward"}, optional
            .. versionadded:: 1.10.0

            Normalization mode (see `numpy.fft`). Default is "backward".
            Indicates which direction of the forward/backward pair of transforms
            is scaled and with what normalization factor.

            .. versionadded:: 1.20.0

                The "backward", "forward" values were added.

        Returns
        -------
        out : complex ndarray
            The truncated or zero-padded input, transformed along the axis
            indicated by `axis`, or the last one if `axis` is not specified.
            The length of the transformed axis is ``n//2 + 1``.

        See also
        --------
        hfft, irfft

        Notes
        -----
        `hfft`/`ihfft` are a pair analogous to `rfft`/`irfft`, but for the
        opposite case: here the signal has Hermitian symmetry in the time
        domain and is real in the frequency domain. So here it's `hfft` for
        which you must supply the length of the result if it is to be odd:

        * even: ``ihfft(hfft(a, 2*len(a) - 2)) == a``, within roundoff error,
        * odd: ``ihfft(hfft(a, 2*len(a) - 1)) == a``, within roundoff error.

        Examples
        --------
        >>> spectrum = np.array([ 15, -4, 0, -1, 0, -4])
        >>> np.fft.ifft(spectrum)
        array([1.+0.j,  2.+0.j,  3.+0.j,  4.+0.j,  3.+0.j,  2.+0.j]) # may vary
        >>> np.fft.ihfft(spectrum)
        array([ 1.-0.j,  2.-0.j,  3.-0.j,  4.-0.j]) # may vary

    irfft(a, n=None, axis=-1, norm=None)
        Computes the inverse of `rfft`.

        This function computes the inverse of the one-dimensional *n*-point
        discrete Fourier Transform of real input computed by `rfft`.
        In other words, ``irfft(rfft(a), len(a)) == a`` to within numerical
        accuracy. (See Notes below for why ``len(a)`` is necessary here.)

        The input is expected to be in the form returned by `rfft`, i.e. the
        real zero-frequency term followed by the complex positive frequency terms
        in order of increasing frequency.  Since the discrete Fourier Transform of
        real input is Hermitian-symmetric, the negative frequency terms are taken
        to be the complex conjugates of the corresponding positive frequency terms.

        Parameters
        ----------
        a : array_like
            The input array.
        n : int, optional
            Length of the transformed axis of the output.
            For `n` output points, ``n//2+1`` input points are necessary.  If the
            input is longer than this, it is cropped.  If it is shorter than this,
            it is padded with zeros.  If `n` is not given, it is taken to be
            ``2*(m-1)`` where ``m`` is the length of the input along the axis
            specified by `axis`.
        axis : int, optional
            Axis over which to compute the inverse FFT. If not given, the last
            axis is used.
        norm : {"backward", "ortho", "forward"}, optional
            .. versionadded:: 1.10.0

            Normalization mode (see `numpy.fft`). Default is "backward".
            Indicates which direction of the forward/backward pair of transforms
            is scaled and with what normalization factor.

            .. versionadded:: 1.20.0

                The "backward", "forward" values were added.

        Returns
        -------
        out : ndarray
            The truncated or zero-padded input, transformed along the axis
            indicated by `axis`, or the last one if `axis` is not specified.
            The length of the transformed axis is `n`, or, if `n` is not given,
            ``2*(m-1)`` where ``m`` is the length of the transformed axis of the
            input. To get an odd number of output points, `n` must be specified.

        Raises
        ------
        IndexError
            If `axis` is not a valid axis of `a`.

        See Also
        --------
        numpy.fft : For definition of the DFT and conventions used.
        rfft : The one-dimensional FFT of real input, of which `irfft` is inverse.
        fft : The one-dimensional FFT.
        irfft2 : The inverse of the two-dimensional FFT of real input.
        irfftn : The inverse of the *n*-dimensional FFT of real input.

        Notes
        -----
        Returns the real valued `n`-point inverse discrete Fourier transform
        of `a`, where `a` contains the non-negative frequency terms of a
        Hermitian-symmetric sequence. `n` is the length of the result, not the
        input.

        If you specify an `n` such that `a` must be zero-padded or truncated, the
        extra/removed values will be added/removed at high frequencies. One can
        thus resample a series to `m` points via Fourier interpolation by:
        ``a_resamp = irfft(rfft(a), m)``.

        The correct interpretation of the hermitian input depends on the length of
        the original data, as given by `n`. This is because each input shape could
        correspond to either an odd or even length signal. By default, `irfft`
        assumes an even output length which puts the last entry at the Nyquist
        frequency; aliasing with its symmetric counterpart. By Hermitian symmetry,
        the value is thus treated as purely real. To avoid losing information, the
        correct length of the real input **must** be given.

        Examples
        --------
        >>> np.fft.ifft([1, -1j, -1, 1j])
        array([0.+0.j,  1.+0.j,  0.+0.j,  0.+0.j]) # may vary
        >>> np.fft.irfft([1, -1j, -1])
        array([0.,  1.,  0.,  0.])

        Notice how the last term in the input to the ordinary `ifft` is the
        complex conjugate of the second term, and the output has zero imaginary
        part everywhere.  When calling `irfft`, the negative frequencies are not
        specified, and the output array is purely real.

    irfft2(a, s=None, axes=(-2, -1), norm=None)
        Computes the inverse of `rfft2`.

        Parameters
        ----------
        a : array_like
            The input array
        s : sequence of ints, optional
            Shape of the real output to the inverse FFT.
        axes : sequence of ints, optional
            The axes over which to compute the inverse fft.
            Default is the last two axes.
        norm : {"backward", "ortho", "forward"}, optional
            .. versionadded:: 1.10.0

            Normalization mode (see `numpy.fft`). Default is "backward".
            Indicates which direction of the forward/backward pair of transforms
            is scaled and with what normalization factor.

            .. versionadded:: 1.20.0

                The "backward", "forward" values were added.

        Returns
        -------
        out : ndarray
            The result of the inverse real 2-D FFT.

        See Also
        --------
        rfft2 : The forward two-dimensional FFT of real input,
                of which `irfft2` is the inverse.
        rfft : The one-dimensional FFT for real input.
        irfft : The inverse of the one-dimensional FFT of real input.
        irfftn : Compute the inverse of the N-dimensional FFT of real input.

        Notes
        -----
        This is really `irfftn` with different defaults.
        For more details see `irfftn`.

        Examples
        --------
        >>> a = np.mgrid[:5, :5][0]
        >>> A = np.fft.rfft2(a)
        >>> np.fft.irfft2(A, s=a.shape)
        array([[0., 0., 0., 0., 0.],
               [1., 1., 1., 1., 1.],
               [2., 2., 2., 2., 2.],
               [3., 3., 3., 3., 3.],
               [4., 4., 4., 4., 4.]])

    irfftn(a, s=None, axes=None, norm=None)
        Computes the inverse of `rfftn`.

        This function computes the inverse of the N-dimensional discrete
        Fourier Transform for real input over any number of axes in an
        M-dimensional array by means of the Fast Fourier Transform (FFT).  In
        other words, ``irfftn(rfftn(a), a.shape) == a`` to within numerical
        accuracy. (The ``a.shape`` is necessary like ``len(a)`` is for `irfft`,
        and for the same reason.)

        The input should be ordered in the same way as is returned by `rfftn`,
        i.e. as for `irfft` for the final transformation axis, and as for `ifftn`
        along all the other axes.

        Parameters
        ----------
        a : array_like
            Input array.
        s : sequence of ints, optional
            Shape (length of each transformed axis) of the output
            (``s[0]`` refers to axis 0, ``s[1]`` to axis 1, etc.). `s` is also the
            number of input points used along this axis, except for the last axis,
            where ``s[-1]//2+1`` points of the input are used.
            Along any axis, if the shape indicated by `s` is smaller than that of
            the input, the input is cropped.  If it is larger, the input is padded
            with zeros. If `s` is not given, the shape of the input along the axes
            specified by axes is used. Except for the last axis which is taken to
            be ``2*(m-1)`` where ``m`` is the length of the input along that axis.
        axes : sequence of ints, optional
            Axes over which to compute the inverse FFT. If not given, the last
            `len(s)` axes are used, or all axes if `s` is also not specified.
            Repeated indices in `axes` means that the inverse transform over that
            axis is performed multiple times.
        norm : {"backward", "ortho", "forward"}, optional
            .. versionadded:: 1.10.0

            Normalization mode (see `numpy.fft`). Default is "backward".
            Indicates which direction of the forward/backward pair of transforms
            is scaled and with what normalization factor.

            .. versionadded:: 1.20.0

                The "backward", "forward" values were added.

        Returns
        -------
        out : ndarray
            The truncated or zero-padded input, transformed along the axes
            indicated by `axes`, or by a combination of `s` or `a`,
            as explained in the parameters section above.
            The length of each transformed axis is as given by the corresponding
            element of `s`, or the length of the input in every axis except for the
            last one if `s` is not given.  In the final transformed axis the length
            of the output when `s` is not given is ``2*(m-1)`` where ``m`` is the
            length of the final transformed axis of the input.  To get an odd
            number of output points in the final axis, `s` must be specified.

        Raises
        ------
        ValueError
            If `s` and `axes` have different length.
        IndexError
            If an element of `axes` is larger than than the number of axes of `a`.

        See Also
        --------
        rfftn : The forward n-dimensional FFT of real input,
                of which `ifftn` is the inverse.
        fft : The one-dimensional FFT, with definitions and conventions used.
        irfft : The inverse of the one-dimensional FFT of real input.
        irfft2 : The inverse of the two-dimensional FFT of real input.

        Notes
        -----
        See `fft` for definitions and conventions used.

        See `rfft` for definitions and conventions used for real input.

        The correct interpretation of the hermitian input depends on the shape of
        the original data, as given by `s`. This is because each input shape could
        correspond to either an odd or even length signal. By default, `irfftn`
        assumes an even output length which puts the last entry at the Nyquist
        frequency; aliasing with its symmetric counterpart. When performing the
        final complex to real transform, the last value is thus treated as purely
        real. To avoid losing information, the correct shape of the real input
        **must** be given.

        Examples
        --------
        >>> a = np.zeros((3, 2, 2))
        >>> a[0, 0, 0] = 3 * 2 * 2
        >>> np.fft.irfftn(a)
        array([[[1.,  1.],
                [1.,  1.]],
               [[1.,  1.],
                [1.,  1.]],
               [[1.,  1.],
                [1.,  1.]]])

    rfft(a, n=None, axis=-1, norm=None)
        Compute the one-dimensional discrete Fourier Transform for real input.

        This function computes the one-dimensional *n*-point discrete Fourier
        Transform (DFT) of a real-valued array by means of an efficient algorithm
        called the Fast Fourier Transform (FFT).

        Parameters
        ----------
        a : array_like
            Input array
        n : int, optional
            Number of points along transformation axis in the input to use.
            If `n` is smaller than the length of the input, the input is cropped.
            If it is larger, the input is padded with zeros. If `n` is not given,
            the length of the input along the axis specified by `axis` is used.
        axis : int, optional
            Axis over which to compute the FFT. If not given, the last axis is
            used.
        norm : {"backward", "ortho", "forward"}, optional
            .. versionadded:: 1.10.0

            Normalization mode (see `numpy.fft`). Default is "backward".
            Indicates which direction of the forward/backward pair of transforms
            is scaled and with what normalization factor.

            .. versionadded:: 1.20.0

                The "backward", "forward" values were added.

        Returns
        -------
        out : complex ndarray
            The truncated or zero-padded input, transformed along the axis
            indicated by `axis`, or the last one if `axis` is not specified.
            If `n` is even, the length of the transformed axis is ``(n/2)+1``.
            If `n` is odd, the length is ``(n+1)/2``.

        Raises
        ------
        IndexError
            If `axis` is not a valid axis of `a`.

        See Also
        --------
        numpy.fft : For definition of the DFT and conventions used.
        irfft : The inverse of `rfft`.
        fft : The one-dimensional FFT of general (complex) input.
        fftn : The *n*-dimensional FFT.
        rfftn : The *n*-dimensional FFT of real input.

        Notes
        -----
        When the DFT is computed for purely real input, the output is
        Hermitian-symmetric, i.e. the negative frequency terms are just the complex
        conjugates of the corresponding positive-frequency terms, and the
        negative-frequency terms are therefore redundant.  This function does not
        compute the negative frequency terms, and the length of the transformed
        axis of the output is therefore ``n//2 + 1``.

        When ``A = rfft(a)`` and fs is the sampling frequency, ``A[0]`` contains
        the zero-frequency term 0*fs, which is real due to Hermitian symmetry.

        If `n` is even, ``A[-1]`` contains the term representing both positive
        and negative Nyquist frequency (+fs/2 and -fs/2), and must also be purely
        real. If `n` is odd, there is no term at fs/2; ``A[-1]`` contains
        the largest positive frequency (fs/2*(n-1)/n), and is complex in the
        general case.

        If the input `a` contains an imaginary part, it is silently discarded.

        Examples
        --------
        >>> np.fft.fft([0, 1, 0, 0])
        array([ 1.+0.j,  0.-1.j, -1.+0.j,  0.+1.j]) # may vary
        >>> np.fft.rfft([0, 1, 0, 0])
        array([ 1.+0.j,  0.-1.j, -1.+0.j]) # may vary

        Notice how the final element of the `fft` output is the complex conjugate
        of the second element, for real input. For `rfft`, this symmetry is
        exploited to compute only the non-negative frequency terms.

    rfft2(a, s=None, axes=(-2, -1), norm=None)
        Compute the 2-dimensional FFT of a real array.

        Parameters
        ----------
        a : array
            Input array, taken to be real.
        s : sequence of ints, optional
            Shape of the FFT.
        axes : sequence of ints, optional
            Axes over which to compute the FFT.
        norm : {"backward", "ortho", "forward"}, optional
            .. versionadded:: 1.10.0

            Normalization mode (see `numpy.fft`). Default is "backward".
            Indicates which direction of the forward/backward pair of transforms
            is scaled and with what normalization factor.

            .. versionadded:: 1.20.0

                The "backward", "forward" values were added.

        Returns
        -------
        out : ndarray
            The result of the real 2-D FFT.

        See Also
        --------
        rfftn : Compute the N-dimensional discrete Fourier Transform for real
                input.

        Notes
        -----
        This is really just `rfftn` with different default behavior.
        For more details see `rfftn`.

        Examples
        --------
        >>> a = np.mgrid[:5, :5][0]
        >>> np.fft.rfft2(a)
        array([[ 50.  +0.j        ,   0.  +0.j        ,   0.  +0.j        ],
               [-12.5+17.20477401j,   0.  +0.j        ,   0.  +0.j        ],
               [-12.5 +4.0614962j ,   0.  +0.j        ,   0.  +0.j        ],
               [-12.5 -4.0614962j ,   0.  +0.j        ,   0.  +0.j        ],
               [-12.5-17.20477401j,   0.  +0.j        ,   0.  +0.j        ]])

    rfftfreq(n, d=1.0)
        Return the Discrete Fourier Transform sample frequencies
        (for usage with rfft, irfft).

        The returned float array `f` contains the frequency bin centers in cycles
        per unit of the sample spacing (with zero at the start).  For instance, if
        the sample spacing is in seconds, then the frequency unit is cycles/second.

        Given a window length `n` and a sample spacing `d`::

          f = [0, 1, ...,     n/2-1,     n/2] / (d*n)   if n is even
          f = [0, 1, ..., (n-1)/2-1, (n-1)/2] / (d*n)   if n is odd

        Unlike `fftfreq` (but like `scipy.fftpack.rfftfreq`)
        the Nyquist frequency component is considered to be positive.

        Parameters
        ----------
        n : int
            Window length.
        d : scalar, optional
            Sample spacing (inverse of the sampling rate). Defaults to 1.

        Returns
        -------
        f : ndarray
            Array of length ``n//2 + 1`` containing the sample frequencies.

        Examples
        --------
        >>> signal = np.array([-2, 8, 6, 4, 1, 0, 3, 5, -3, 4], dtype=float)
        >>> fourier = np.fft.rfft(signal)
        >>> n = signal.size
        >>> sample_rate = 100
        >>> freq = np.fft.fftfreq(n, d=1./sample_rate)
        >>> freq
        array([  0.,  10.,  20., ..., -30., -20., -10.])
        >>> freq = np.fft.rfftfreq(n, d=1./sample_rate)
        >>> freq
        array([  0.,  10.,  20.,  30.,  40.,  50.])

    rfftn(a, s=None, axes=None, norm=None)
        Compute the N-dimensional discrete Fourier Transform for real input.

        This function computes the N-dimensional discrete Fourier Transform over
        any number of axes in an M-dimensional real array by means of the Fast
        Fourier Transform (FFT).  By default, all axes are transformed, with the
        real transform performed over the last axis, while the remaining
        transforms are complex.

        Parameters
        ----------
        a : array_like
            Input array, taken to be real.
        s : sequence of ints, optional
            Shape (length along each transformed axis) to use from the input.
            (``s[0]`` refers to axis 0, ``s[1]`` to axis 1, etc.).
            The final element of `s` corresponds to `n` for ``rfft(x, n)``, while
            for the remaining axes, it corresponds to `n` for ``fft(x, n)``.
            Along any axis, if the given shape is smaller than that of the input,
            the input is cropped.  If it is larger, the input is padded with zeros.
            if `s` is not given, the shape of the input along the axes specified
            by `axes` is used.
        axes : sequence of ints, optional
            Axes over which to compute the FFT.  If not given, the last ``len(s)``
            axes are used, or all axes if `s` is also not specified.
        norm : {"backward", "ortho", "forward"}, optional
            .. versionadded:: 1.10.0

            Normalization mode (see `numpy.fft`). Default is "backward".
            Indicates which direction of the forward/backward pair of transforms
            is scaled and with what normalization factor.

            .. versionadded:: 1.20.0

                The "backward", "forward" values were added.

        Returns
        -------
        out : complex ndarray
            The truncated or zero-padded input, transformed along the axes
            indicated by `axes`, or by a combination of `s` and `a`,
            as explained in the parameters section above.
            The length of the last axis transformed will be ``s[-1]//2+1``,
            while the remaining transformed axes will have lengths according to
            `s`, or unchanged from the input.

        Raises
        ------
        ValueError
            If `s` and `axes` have different length.
        IndexError
            If an element of `axes` is larger than than the number of axes of `a`.

        See Also
        --------
        irfftn : The inverse of `rfftn`, i.e. the inverse of the n-dimensional FFT
             of real input.
        fft : The one-dimensional FFT, with definitions and conventions used.
        rfft : The one-dimensional FFT of real input.
        fftn : The n-dimensional FFT.
        rfft2 : The two-dimensional FFT of real input.

        Notes
        -----
        The transform for real input is performed over the last transformation
        axis, as by `rfft`, then the transform over the remaining axes is
        performed as by `fftn`.  The order of the output is as for `rfft` for the
        final transformation axis, and as for `fftn` for the remaining
        transformation axes.

        See `fft` for details, definitions and conventions used.

        Examples
        --------
        >>> a = np.ones((2, 2, 2))
        >>> np.fft.rfftn(a)
        array([[[8.+0.j,  0.+0.j], # may vary
                [0.+0.j,  0.+0.j]],
               [[0.+0.j,  0.+0.j],
                [0.+0.j,  0.+0.j]]])

        >>> np.fft.rfftn(a, axes=(2, 0))
        array([[[4.+0.j,  0.+0.j], # may vary
                [4.+0.j,  0.+0.j]],
               [[0.+0.j,  0.+0.j],
                [0.+0.j,  0.+0.j]]])

DATA
    __all__ = ['fft', 'ifft', 'rfft', 'irfft', 'hfft', 'ihfft', 'rfftn', '...

FILE
    /Users/leopoldogonzalez/miniconda3/lib/python3.12/site-packages/numpy/fft/__init__.py


None
&&&&&&&&&&&&&&&&&&&&&& fix &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

fix(x, out=None)
    Round to nearest integer towards zero.

    Round an array of floats element-wise to nearest integer towards zero.
    The rounded values are returned as floats.

    Parameters
    ----------
    x : array_like
        An array of floats to be rounded
    out : ndarray, optional
        A location into which the result is stored. If provided, it must have
        a shape that the input broadcasts to. If not provided or None, a
        freshly-allocated array is returned.

    Returns
    -------
    out : ndarray of floats
        A float array with the same dimensions as the input.
        If second argument is not supplied then a float array is returned
        with the rounded values.

        If a second argument is supplied the result is stored there.
        The return value `out` is then a reference to that array.

    See Also
    --------
    rint, trunc, floor, ceil
    around : Round to given number of decimals

    Examples
    --------
    >>> np.fix(3.14)
    3.0
    >>> np.fix(3)
    3.0
    >>> np.fix([2.1, 2.9, -2.1, -2.9])
    array([ 2.,  2., -2., -2.])

None
&&&&&&&&&&&&&&&&&&&&&& fmax &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on ufunc:

fmax = <ufunc 'fmax'>
    fmax(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])

    Element-wise maximum of array elements.

    Compare two arrays and return a new array containing the element-wise
    maxima. If one of the elements being compared is a NaN, then the
    non-nan element is returned. If both elements are NaNs then the first
    is returned.  The latter distinction is important for complex NaNs,
    which are defined as at least one of the real or imaginary parts being
    a NaN. The net effect is that NaNs are ignored when possible.

    Parameters
    ----------
    x1, x2 : array_like
        The arrays holding the elements to be compared.
        If ``x1.shape != x2.shape``, they must be broadcastable to a common
        shape (which becomes the shape of the output).
    out : ndarray, None, or tuple of ndarray and None, optional
        A location into which the result is stored. If provided, it must have
        a shape that the inputs broadcast to. If not provided or None,
        a freshly-allocated array is returned. A tuple (possible only as a
        keyword argument) must have length equal to the number of outputs.
    where : array_like, optional
        This condition is broadcast over the input. At locations where the
        condition is True, the `out` array will be set to the ufunc result.
        Elsewhere, the `out` array will retain its original value.
        Note that if an uninitialized `out` array is created via the default
        ``out=None``, locations within it where the condition is False will
        remain uninitialized.
    **kwargs
        For other keyword-only arguments, see the
        :ref:`ufunc docs <ufuncs.kwargs>`.

    Returns
    -------
    y : ndarray or scalar
        The maximum of `x1` and `x2`, element-wise.
        This is a scalar if both `x1` and `x2` are scalars.

    See Also
    --------
    fmin :
        Element-wise minimum of two arrays, ignores NaNs.
    maximum :
        Element-wise maximum of two arrays, propagates NaNs.
    amax :
        The maximum value of an array along a given axis, propagates NaNs.
    nanmax :
        The maximum value of an array along a given axis, ignores NaNs.

    minimum, amin, nanmin

    Notes
    -----
    .. versionadded:: 1.3.0

    The fmax is equivalent to ``np.where(x1 >= x2, x1, x2)`` when neither
    x1 nor x2 are NaNs, but it is faster and does proper broadcasting.

    Examples
    --------
    >>> np.fmax([2, 3, 4], [1, 5, 2])
    array([ 2.,  5.,  4.])

    >>> np.fmax(np.eye(2), [0.5, 2])
    array([[ 1. ,  2. ],
           [ 0.5,  2. ]])

    >>> np.fmax([np.nan, 0, np.nan],[0, np.nan, np.nan])
    array([ 0.,  0., nan])

None
&&&&&&&&&&&&&&&&&&&&&& fmin &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on ufunc:

fmin = <ufunc 'fmin'>
    fmin(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])

    Element-wise minimum of array elements.

    Compare two arrays and return a new array containing the element-wise
    minima. If one of the elements being compared is a NaN, then the
    non-nan element is returned. If both elements are NaNs then the first
    is returned.  The latter distinction is important for complex NaNs,
    which are defined as at least one of the real or imaginary parts being
    a NaN. The net effect is that NaNs are ignored when possible.

    Parameters
    ----------
    x1, x2 : array_like
        The arrays holding the elements to be compared.
        If ``x1.shape != x2.shape``, they must be broadcastable to a common
        shape (which becomes the shape of the output).
    out : ndarray, None, or tuple of ndarray and None, optional
        A location into which the result is stored. If provided, it must have
        a shape that the inputs broadcast to. If not provided or None,
        a freshly-allocated array is returned. A tuple (possible only as a
        keyword argument) must have length equal to the number of outputs.
    where : array_like, optional
        This condition is broadcast over the input. At locations where the
        condition is True, the `out` array will be set to the ufunc result.
        Elsewhere, the `out` array will retain its original value.
        Note that if an uninitialized `out` array is created via the default
        ``out=None``, locations within it where the condition is False will
        remain uninitialized.
    **kwargs
        For other keyword-only arguments, see the
        :ref:`ufunc docs <ufuncs.kwargs>`.

    Returns
    -------
    y : ndarray or scalar
        The minimum of `x1` and `x2`, element-wise.
        This is a scalar if both `x1` and `x2` are scalars.

    See Also
    --------
    fmax :
        Element-wise maximum of two arrays, ignores NaNs.
    minimum :
        Element-wise minimum of two arrays, propagates NaNs.
    amin :
        The minimum value of an array along a given axis, propagates NaNs.
    nanmin :
        The minimum value of an array along a given axis, ignores NaNs.

    maximum, amax, nanmax

    Notes
    -----
    .. versionadded:: 1.3.0

    The fmin is equivalent to ``np.where(x1 <= x2, x1, x2)`` when neither
    x1 nor x2 are NaNs, but it is faster and does proper broadcasting.

    Examples
    --------
    >>> np.fmin([2, 3, 4], [1, 5, 2])
    array([1, 3, 2])

    >>> np.fmin(np.eye(2), [0.5, 2])
    array([[ 0.5,  0. ],
           [ 0. ,  1. ]])

    >>> np.fmin([np.nan, 0, np.nan],[0, np.nan, np.nan])
    array([ 0.,  0., nan])

None
&&&&&&&&&&&&&&&&&&&&&& histogram &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

histogram(a, bins=10, range=None, density=None, weights=None)
    Compute the histogram of a dataset.

    Parameters
    ----------
    a : array_like
        Input data. The histogram is computed over the flattened array.
    bins : int or sequence of scalars or str, optional
        If `bins` is an int, it defines the number of equal-width
        bins in the given range (10, by default). If `bins` is a
        sequence, it defines a monotonically increasing array of bin edges,
        including the rightmost edge, allowing for non-uniform bin widths.

        .. versionadded:: 1.11.0

        If `bins` is a string, it defines the method used to calculate the
        optimal bin width, as defined by `histogram_bin_edges`.

    range : (float, float), optional
        The lower and upper range of the bins.  If not provided, range
        is simply ``(a.min(), a.max())``.  Values outside the range are
        ignored. The first element of the range must be less than or
        equal to the second. `range` affects the automatic bin
        computation as well. While bin width is computed to be optimal
        based on the actual data within `range`, the bin count will fill
        the entire range including portions containing no data.
    weights : array_like, optional
        An array of weights, of the same shape as `a`.  Each value in
        `a` only contributes its associated weight towards the bin count
        (instead of 1). If `density` is True, the weights are
        normalized, so that the integral of the density over the range
        remains 1.
    density : bool, optional
        If ``False``, the result will contain the number of samples in
        each bin. If ``True``, the result is the value of the
        probability *density* function at the bin, normalized such that
        the *integral* over the range is 1. Note that the sum of the
        histogram values will not be equal to 1 unless bins of unity
        width are chosen; it is not a probability *mass* function.

    Returns
    -------
    hist : array
        The values of the histogram. See `density` and `weights` for a
        description of the possible semantics.
    bin_edges : array of dtype float
        Return the bin edges ``(length(hist)+1)``.


    See Also
    --------
    histogramdd, bincount, searchsorted, digitize, histogram_bin_edges

    Notes
    -----
    All but the last (righthand-most) bin is half-open.  In other words,
    if `bins` is::

      [1, 2, 3, 4]

    then the first bin is ``[1, 2)`` (including 1, but excluding 2) and
    the second ``[2, 3)``.  The last bin, however, is ``[3, 4]``, which
    *includes* 4.


    Examples
    --------
    >>> np.histogram([1, 2, 1], bins=[0, 1, 2, 3])
    (array([0, 2, 1]), array([0, 1, 2, 3]))
    >>> np.histogram(np.arange(4), bins=np.arange(5), density=True)
    (array([0.25, 0.25, 0.25, 0.25]), array([0, 1, 2, 3, 4]))
    >>> np.histogram([[1, 2, 1], [1, 0, 1]], bins=[0,1,2,3])
    (array([1, 4, 1]), array([0, 1, 2, 3]))

    >>> a = np.arange(5)
    >>> hist, bin_edges = np.histogram(a, density=True)
    >>> hist
    array([0.5, 0. , 0.5, 0. , 0. , 0.5, 0. , 0.5, 0. , 0.5])
    >>> hist.sum()
    2.4999999999999996
    >>> np.sum(hist * np.diff(bin_edges))
    1.0

    .. versionadded:: 1.11.0

    Automated Bin Selection Methods example, using 2 peak random data
    with 2000 points:

    >>> import matplotlib.pyplot as plt
    >>> rng = np.random.RandomState(10)  # deterministic random data
    >>> a = np.hstack((rng.normal(size=1000),
    ...                rng.normal(loc=5, scale=2, size=1000)))
    >>> _ = plt.hist(a, bins='auto')  # arguments are passed to np.histogram
    >>> plt.title("Histogram with 'auto' bins")
    Text(0.5, 1.0, "Histogram with 'auto' bins")
    >>> plt.show()

None
&&&&&&&&&&&&&&&&&&&&&& inf &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on float object:

class float(object)
 |  float(x=0, /)
 |
 |  Convert a string or number to a floating point number, if possible.
 |
 |  Methods defined here:
 |
 |  __abs__(self, /)
 |      abs(self)
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __bool__(self, /)
 |      True if self else False
 |
 |  __ceil__(self, /)
 |      Return the ceiling as an Integral.
 |
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __float__(self, /)
 |      float(self)
 |
 |  __floor__(self, /)
 |      Return the floor as an Integral.
 |
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |
 |  __format__(self, format_spec, /)
 |      Formats the float according to format_spec.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __getnewargs__(self, /)
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
 |
 |  __int__(self, /)
 |      int(self)
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __mod__(self, value, /)
 |      Return self%value.
 |
 |  __mul__(self, value, /)
 |      Return self*value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __neg__(self, /)
 |      -self
 |
 |  __pos__(self, /)
 |      +self
 |
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |
 |  __radd__(self, value, /)
 |      Return value+self.
 |
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |
 |  __rmod__(self, value, /)
 |      Return value%self.
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __round__(self, ndigits=None, /)
 |      Return the Integral closest to x, rounding half toward even.
 |
 |      When an argument is passed, work like built-in round(x, ndigits).
 |
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |
 |  __rsub__(self, value, /)
 |      Return value-self.
 |
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |
 |  __sub__(self, value, /)
 |      Return self-value.
 |
 |  __truediv__(self, value, /)
 |      Return self/value.
 |
 |  __trunc__(self, /)
 |      Return the Integral closest to x between 0 and x.
 |
 |  as_integer_ratio(self, /)
 |      Return a pair of integers, whose ratio is exactly equal to the original float.
 |
 |      The ratio is in lowest terms and has a positive denominator.  Raise
 |      OverflowError on infinities and a ValueError on NaNs.
 |
 |      >>> (10.0).as_integer_ratio()
 |      (10, 1)
 |      >>> (0.0).as_integer_ratio()
 |      (0, 1)
 |      >>> (-.25).as_integer_ratio()
 |      (-1, 4)
 |
 |  conjugate(self, /)
 |      Return self, the complex conjugate of any float.
 |
 |  hex(self, /)
 |      Return a hexadecimal representation of a floating-point number.
 |
 |      >>> (-0.1).hex()
 |      '-0x1.999999999999ap-4'
 |      >>> 3.14159.hex()
 |      '0x1.921f9f01b866ep+1'
 |
 |  is_integer(self, /)
 |      Return True if the float is an integer.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __getformat__(typestr, /) from builtins.type
 |      You probably don't want to use this function.
 |
 |        typestr
 |          Must be 'double' or 'float'.
 |
 |      It exists mainly to be used in Python's test suite.
 |
 |      This function returns whichever of 'unknown', 'IEEE, big-endian' or 'IEEE,
 |      little-endian' best describes the format of floating point numbers used by the
 |      C type named by typestr.
 |
 |  fromhex(string, /) from builtins.type
 |      Create a floating-point number from a hexadecimal string.
 |
 |      >>> float.fromhex('0x1.ffffp10')
 |      2047.984375
 |      >>> float.fromhex('-0x1p-1074')
 |      -5e-324
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
 |  imag
 |      the imaginary part of a complex number
 |
 |  real
 |      the real part of a complex number

None
&&&&&&&&&&&&&&&&&&&&&& infty &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on float object:

class float(object)
 |  float(x=0, /)
 |
 |  Convert a string or number to a floating point number, if possible.
 |
 |  Methods defined here:
 |
 |  __abs__(self, /)
 |      abs(self)
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __bool__(self, /)
 |      True if self else False
 |
 |  __ceil__(self, /)
 |      Return the ceiling as an Integral.
 |
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __float__(self, /)
 |      float(self)
 |
 |  __floor__(self, /)
 |      Return the floor as an Integral.
 |
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |
 |  __format__(self, format_spec, /)
 |      Formats the float according to format_spec.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __getnewargs__(self, /)
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
 |
 |  __int__(self, /)
 |      int(self)
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __mod__(self, value, /)
 |      Return self%value.
 |
 |  __mul__(self, value, /)
 |      Return self*value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __neg__(self, /)
 |      -self
 |
 |  __pos__(self, /)
 |      +self
 |
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |
 |  __radd__(self, value, /)
 |      Return value+self.
 |
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |
 |  __rmod__(self, value, /)
 |      Return value%self.
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __round__(self, ndigits=None, /)
 |      Return the Integral closest to x, rounding half toward even.
 |
 |      When an argument is passed, work like built-in round(x, ndigits).
 |
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |
 |  __rsub__(self, value, /)
 |      Return value-self.
 |
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |
 |  __sub__(self, value, /)
 |      Return self-value.
 |
 |  __truediv__(self, value, /)
 |      Return self/value.
 |
 |  __trunc__(self, /)
 |      Return the Integral closest to x between 0 and x.
 |
 |  as_integer_ratio(self, /)
 |      Return a pair of integers, whose ratio is exactly equal to the original float.
 |
 |      The ratio is in lowest terms and has a positive denominator.  Raise
 |      OverflowError on infinities and a ValueError on NaNs.
 |
 |      >>> (10.0).as_integer_ratio()
 |      (10, 1)
 |      >>> (0.0).as_integer_ratio()
 |      (0, 1)
 |      >>> (-.25).as_integer_ratio()
 |      (-1, 4)
 |
 |  conjugate(self, /)
 |      Return self, the complex conjugate of any float.
 |
 |  hex(self, /)
 |      Return a hexadecimal representation of a floating-point number.
 |
 |      >>> (-0.1).hex()
 |      '-0x1.999999999999ap-4'
 |      >>> 3.14159.hex()
 |      '0x1.921f9f01b866ep+1'
 |
 |  is_integer(self, /)
 |      Return True if the float is an integer.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __getformat__(typestr, /) from builtins.type
 |      You probably don't want to use this function.
 |
 |        typestr
 |          Must be 'double' or 'float'.
 |
 |      It exists mainly to be used in Python's test suite.
 |
 |      This function returns whichever of 'unknown', 'IEEE, big-endian' or 'IEEE,
 |      little-endian' best describes the format of floating point numbers used by the
 |      C type named by typestr.
 |
 |  fromhex(string, /) from builtins.type
 |      Create a floating-point number from a hexadecimal string.
 |
 |      >>> float.fromhex('0x1.ffffp10')
 |      2047.984375
 |      >>> float.fromhex('-0x1p-1074')
 |      -5e-324
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
 |  imag
 |      the imaginary part of a complex number
 |
 |  real
 |      the real part of a complex number

None
&&&&&&&&&&&&&&&&&&&&&& isnan &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on ufunc:

isnan = <ufunc 'isnan'>
    isnan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])

    Test element-wise for NaN and return result as a boolean array.

    Parameters
    ----------
    x : array_like
        Input array.
    out : ndarray, None, or tuple of ndarray and None, optional
        A location into which the result is stored. If provided, it must have
        a shape that the inputs broadcast to. If not provided or None,
        a freshly-allocated array is returned. A tuple (possible only as a
        keyword argument) must have length equal to the number of outputs.
    where : array_like, optional
        This condition is broadcast over the input. At locations where the
        condition is True, the `out` array will be set to the ufunc result.
        Elsewhere, the `out` array will retain its original value.
        Note that if an uninitialized `out` array is created via the default
        ``out=None``, locations within it where the condition is False will
        remain uninitialized.
    **kwargs
        For other keyword-only arguments, see the
        :ref:`ufunc docs <ufuncs.kwargs>`.

    Returns
    -------
    y : ndarray or bool
        True where ``x`` is NaN, false otherwise.
        This is a scalar if `x` is a scalar.

    See Also
    --------
    isinf, isneginf, isposinf, isfinite, isnat

    Notes
    -----
    NumPy uses the IEEE Standard for Binary Floating-Point for Arithmetic
    (IEEE 754). This means that Not a Number is not equivalent to infinity.

    Examples
    --------
    >>> np.isnan(np.nan)
    True
    >>> np.isnan(np.inf)
    False
    >>> np.isnan([np.log(-1.),1.,np.log(0)])
    array([ True, False, False])

None
&&&&&&&&&&&&&&&&&&&&&& log &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on ufunc:

log = <ufunc 'log'>
    log(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])

    Natural logarithm, element-wise.

    The natural logarithm `log` is the inverse of the exponential function,
    so that `log(exp(x)) = x`. The natural logarithm is logarithm in base
    `e`.

    Parameters
    ----------
    x : array_like
        Input value.
    out : ndarray, None, or tuple of ndarray and None, optional
        A location into which the result is stored. If provided, it must have
        a shape that the inputs broadcast to. If not provided or None,
        a freshly-allocated array is returned. A tuple (possible only as a
        keyword argument) must have length equal to the number of outputs.
    where : array_like, optional
        This condition is broadcast over the input. At locations where the
        condition is True, the `out` array will be set to the ufunc result.
        Elsewhere, the `out` array will retain its original value.
        Note that if an uninitialized `out` array is created via the default
        ``out=None``, locations within it where the condition is False will
        remain uninitialized.
    **kwargs
        For other keyword-only arguments, see the
        :ref:`ufunc docs <ufuncs.kwargs>`.

    Returns
    -------
    y : ndarray
        The natural logarithm of `x`, element-wise.
        This is a scalar if `x` is a scalar.

    See Also
    --------
    log10, log2, log1p, emath.log

    Notes
    -----
    Logarithm is a multivalued function: for each `x` there is an infinite
    number of `z` such that `exp(z) = x`. The convention is to return the
    `z` whose imaginary part lies in `(-pi, pi]`.

    For real-valued input data types, `log` always returns real output. For
    each value that cannot be expressed as a real number or infinity, it
    yields ``nan`` and sets the `invalid` floating point error flag.

    For complex-valued input, `log` is a complex analytical function that
    has a branch cut `[-inf, 0]` and is continuous from above on it. `log`
    handles the floating-point negative zero as an infinitesimal negative
    number, conforming to the C99 standard.

    In the cases where the input has a negative real part and a very small
    negative complex part (approaching 0), the result is so close to `-pi`
    that it evaluates to exactly `-pi`.

    References
    ----------
    .. [1] M. Abramowitz and I.A. Stegun, "Handbook of Mathematical Functions",
           10th printing, 1964, pp. 67.
           https://personal.math.ubc.ca/~cbm/aands/page_67.htm
    .. [2] Wikipedia, "Logarithm". https://en.wikipedia.org/wiki/Logarithm

    Examples
    --------
    >>> np.log([1, np.e, np.e**2, 0])
    array([  0.,   1.,   2., -Inf])

None
&&&&&&&&&&&&&&&&&&&&&& log10 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on ufunc:

log10 = <ufunc 'log10'>
    log10(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])

    Return the base 10 logarithm of the input array, element-wise.

    Parameters
    ----------
    x : array_like
        Input values.
    out : ndarray, None, or tuple of ndarray and None, optional
        A location into which the result is stored. If provided, it must have
        a shape that the inputs broadcast to. If not provided or None,
        a freshly-allocated array is returned. A tuple (possible only as a
        keyword argument) must have length equal to the number of outputs.
    where : array_like, optional
        This condition is broadcast over the input. At locations where the
        condition is True, the `out` array will be set to the ufunc result.
        Elsewhere, the `out` array will retain its original value.
        Note that if an uninitialized `out` array is created via the default
        ``out=None``, locations within it where the condition is False will
        remain uninitialized.
    **kwargs
        For other keyword-only arguments, see the
        :ref:`ufunc docs <ufuncs.kwargs>`.

    Returns
    -------
    y : ndarray
        The logarithm to the base 10 of `x`, element-wise. NaNs are
        returned where x is negative.
        This is a scalar if `x` is a scalar.

    See Also
    --------
    emath.log10

    Notes
    -----
    Logarithm is a multivalued function: for each `x` there is an infinite
    number of `z` such that `10**z = x`. The convention is to return the
    `z` whose imaginary part lies in `(-pi, pi]`.

    For real-valued input data types, `log10` always returns real output.
    For each value that cannot be expressed as a real number or infinity,
    it yields ``nan`` and sets the `invalid` floating point error flag.

    For complex-valued input, `log10` is a complex analytical function that
    has a branch cut `[-inf, 0]` and is continuous from above on it.
    `log10` handles the floating-point negative zero as an infinitesimal
    negative number, conforming to the C99 standard.

    In the cases where the input has a negative real part and a very small
    negative complex part (approaching 0), the result is so close to `-pi`
    that it evaluates to exactly `-pi`.

    References
    ----------
    .. [1] M. Abramowitz and I.A. Stegun, "Handbook of Mathematical Functions",
           10th printing, 1964, pp. 67.
           https://personal.math.ubc.ca/~cbm/aands/page_67.htm
    .. [2] Wikipedia, "Logarithm". https://en.wikipedia.org/wiki/Logarithm

    Examples
    --------
    >>> np.log10([1e-15, -3.])
    array([-15.,  nan])

None
&&&&&&&&&&&&&&&&&&&&&& max &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

max(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)
    Return the maximum of an array or maximum along an axis.

    Parameters
    ----------
    a : array_like
        Input data.
    axis : None or int or tuple of ints, optional
        Axis or axes along which to operate.  By default, flattened input is
        used.

        .. versionadded:: 1.7.0

        If this is a tuple of ints, the maximum is selected over multiple axes,
        instead of a single axis or all the axes as before.
    out : ndarray, optional
        Alternative output array in which to place the result.  Must
        be of the same shape and buffer length as the expected output.
        See :ref:`ufuncs-output-type` for more details.

    keepdims : bool, optional
        If this is set to True, the axes which are reduced are left
        in the result as dimensions with size one. With this option,
        the result will broadcast correctly against the input array.

        If the default value is passed, then `keepdims` will not be
        passed through to the ``max`` method of sub-classes of
        `ndarray`, however any non-default value will be.  If the
        sub-class' method does not implement `keepdims` any
        exceptions will be raised.

    initial : scalar, optional
        The minimum value of an output element. Must be present to allow
        computation on empty slice. See `~numpy.ufunc.reduce` for details.

        .. versionadded:: 1.15.0

    where : array_like of bool, optional
        Elements to compare for the maximum. See `~numpy.ufunc.reduce`
        for details.

        .. versionadded:: 1.17.0

    Returns
    -------
    max : ndarray or scalar
        Maximum of `a`. If `axis` is None, the result is a scalar value.
        If `axis` is an int, the result is an array of dimension
        ``a.ndim - 1``. If `axis` is a tuple, the result is an array of
        dimension ``a.ndim - len(axis)``.

    See Also
    --------
    amin :
        The minimum value of an array along a given axis, propagating any NaNs.
    nanmax :
        The maximum value of an array along a given axis, ignoring any NaNs.
    maximum :
        Element-wise maximum of two arrays, propagating any NaNs.
    fmax :
        Element-wise maximum of two arrays, ignoring any NaNs.
    argmax :
        Return the indices of the maximum values.

    nanmin, minimum, fmin

    Notes
    -----
    NaN values are propagated, that is if at least one item is NaN, the
    corresponding max value will be NaN as well. To ignore NaN values
    (MATLAB behavior), please use nanmax.

    Don't use `~numpy.max` for element-wise comparison of 2 arrays; when
    ``a.shape[0]`` is 2, ``maximum(a[0], a[1])`` is faster than
    ``max(a, axis=0)``.

    Examples
    --------
    >>> a = np.arange(4).reshape((2,2))
    >>> a
    array([[0, 1],
           [2, 3]])
    >>> np.max(a)           # Maximum of the flattened array
    3
    >>> np.max(a, axis=0)   # Maxima along the first axis
    array([2, 3])
    >>> np.max(a, axis=1)   # Maxima along the second axis
    array([1, 3])
    >>> np.max(a, where=[False, True], initial=-1, axis=0)
    array([-1,  3])
    >>> b = np.arange(5, dtype=float)
    >>> b[2] = np.NaN
    >>> np.max(b)
    nan
    >>> np.max(b, where=~np.isnan(b), initial=-1)
    4.0
    >>> np.nanmax(b)
    4.0

    You can use an initial value to compute the maximum of an empty slice, or
    to initialize it to a different value:

    >>> np.max([[-50], [10]], axis=-1, initial=0)
    array([ 0, 10])

    Notice that the initial value is used as one of the elements for which the
    maximum is determined, unlike for the default argument Python's max
    function, which is only used for empty iterables.

    >>> np.max([5], initial=6)
    6
    >>> max([5], default=6)
    5

None
&&&&&&&&&&&&&&&&&&&&&& mean &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

mean(a, axis=None, dtype=None, out=None, keepdims=<no value>, *, where=<no value>)
    Compute the arithmetic mean along the specified axis.

    Returns the average of the array elements.  The average is taken over
    the flattened array by default, otherwise over the specified axis.
    `float64` intermediate and return values are used for integer inputs.

    Parameters
    ----------
    a : array_like
        Array containing numbers whose mean is desired. If `a` is not an
        array, a conversion is attempted.
    axis : None or int or tuple of ints, optional
        Axis or axes along which the means are computed. The default is to
        compute the mean of the flattened array.

        .. versionadded:: 1.7.0

        If this is a tuple of ints, a mean is performed over multiple axes,
        instead of a single axis or all the axes as before.
    dtype : data-type, optional
        Type to use in computing the mean.  For integer inputs, the default
        is `float64`; for floating point inputs, it is the same as the
        input dtype.
    out : ndarray, optional
        Alternate output array in which to place the result.  The default
        is ``None``; if provided, it must have the same shape as the
        expected output, but the type will be cast if necessary.
        See :ref:`ufuncs-output-type` for more details.

    keepdims : bool, optional
        If this is set to True, the axes which are reduced are left
        in the result as dimensions with size one. With this option,
        the result will broadcast correctly against the input array.

        If the default value is passed, then `keepdims` will not be
        passed through to the `mean` method of sub-classes of
        `ndarray`, however any non-default value will be.  If the
        sub-class' method does not implement `keepdims` any
        exceptions will be raised.

    where : array_like of bool, optional
        Elements to include in the mean. See `~numpy.ufunc.reduce` for details.

        .. versionadded:: 1.20.0

    Returns
    -------
    m : ndarray, see dtype parameter above
        If `out=None`, returns a new array containing the mean values,
        otherwise a reference to the output array is returned.

    See Also
    --------
    average : Weighted average
    std, var, nanmean, nanstd, nanvar

    Notes
    -----
    The arithmetic mean is the sum of the elements along the axis divided
    by the number of elements.

    Note that for floating-point input, the mean is computed using the
    same precision the input has.  Depending on the input data, this can
    cause the results to be inaccurate, especially for `float32` (see
    example below).  Specifying a higher-precision accumulator using the
    `dtype` keyword can alleviate this issue.

    By default, `float16` results are computed using `float32` intermediates
    for extra precision.

    Examples
    --------
    >>> a = np.array([[1, 2], [3, 4]])
    >>> np.mean(a)
    2.5
    >>> np.mean(a, axis=0)
    array([2., 3.])
    >>> np.mean(a, axis=1)
    array([1.5, 3.5])

    In single precision, `mean` can be inaccurate:

    >>> a = np.zeros((2, 512*512), dtype=np.float32)
    >>> a[0, :] = 1.0
    >>> a[1, :] = 0.1
    >>> np.mean(a)
    0.54999924

    Computing the mean in float64 is more accurate:

    >>> np.mean(a, dtype=np.float64)
    0.55000000074505806 # may vary

    Specifying a where argument:

    >>> a = np.array([[5, 9, 13], [14, 10, 12], [11, 15, 19]])
    >>> np.mean(a)
    12.0
    >>> np.mean(a, where=[[True], [False], [False]])
    9.0

None
&&&&&&&&&&&&&&&&&&&&&& median &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

median(a, axis=None, out=None, overwrite_input=False, keepdims=False)
    Compute the median along the specified axis.

    Returns the median of the array elements.

    Parameters
    ----------
    a : array_like
        Input array or object that can be converted to an array.
    axis : {int, sequence of int, None}, optional
        Axis or axes along which the medians are computed. The default
        is to compute the median along a flattened version of the array.
        A sequence of axes is supported since version 1.9.0.
    out : ndarray, optional
        Alternative output array in which to place the result. It must
        have the same shape and buffer length as the expected output,
        but the type (of the output) will be cast if necessary.
    overwrite_input : bool, optional
       If True, then allow use of memory of input array `a` for
       calculations. The input array will be modified by the call to
       `median`. This will save memory when you do not need to preserve
       the contents of the input array. Treat the input as undefined,
       but it will probably be fully or partially sorted. Default is
       False. If `overwrite_input` is ``True`` and `a` is not already an
       `ndarray`, an error will be raised.
    keepdims : bool, optional
        If this is set to True, the axes which are reduced are left
        in the result as dimensions with size one. With this option,
        the result will broadcast correctly against the original `arr`.

        .. versionadded:: 1.9.0

    Returns
    -------
    median : ndarray
        A new array holding the result. If the input contains integers
        or floats smaller than ``float64``, then the output data-type is
        ``np.float64``.  Otherwise, the data-type of the output is the
        same as that of the input. If `out` is specified, that array is
        returned instead.

    See Also
    --------
    mean, percentile

    Notes
    -----
    Given a vector ``V`` of length ``N``, the median of ``V`` is the
    middle value of a sorted copy of ``V``, ``V_sorted`` - i
    e., ``V_sorted[(N-1)/2]``, when ``N`` is odd, and the average of the
    two middle values of ``V_sorted`` when ``N`` is even.

    Examples
    --------
    >>> a = np.array([[10, 7, 4], [3, 2, 1]])
    >>> a
    array([[10,  7,  4],
           [ 3,  2,  1]])
    >>> np.median(a)
    3.5
    >>> np.median(a, axis=0)
    array([6.5, 4.5, 2.5])
    >>> np.median(a, axis=1)
    array([7.,  2.])
    >>> m = np.median(a, axis=0)
    >>> out = np.zeros_like(m)
    >>> np.median(a, axis=0, out=m)
    array([6.5,  4.5,  2.5])
    >>> m
    array([6.5,  4.5,  2.5])
    >>> b = a.copy()
    >>> np.median(b, axis=1, overwrite_input=True)
    array([7.,  2.])
    >>> assert not np.all(a==b)
    >>> b = a.copy()
    >>> np.median(b, axis=None, overwrite_input=True)
    3.5
    >>> assert not np.all(a==b)

None
&&&&&&&&&&&&&&&&&&&&&& min &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

min(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)
    Return the minimum of an array or minimum along an axis.

    Parameters
    ----------
    a : array_like
        Input data.
    axis : None or int or tuple of ints, optional
        Axis or axes along which to operate.  By default, flattened input is
        used.

        .. versionadded:: 1.7.0

        If this is a tuple of ints, the minimum is selected over multiple axes,
        instead of a single axis or all the axes as before.
    out : ndarray, optional
        Alternative output array in which to place the result.  Must
        be of the same shape and buffer length as the expected output.
        See :ref:`ufuncs-output-type` for more details.

    keepdims : bool, optional
        If this is set to True, the axes which are reduced are left
        in the result as dimensions with size one. With this option,
        the result will broadcast correctly against the input array.

        If the default value is passed, then `keepdims` will not be
        passed through to the ``min`` method of sub-classes of
        `ndarray`, however any non-default value will be.  If the
        sub-class' method does not implement `keepdims` any
        exceptions will be raised.

    initial : scalar, optional
        The maximum value of an output element. Must be present to allow
        computation on empty slice. See `~numpy.ufunc.reduce` for details.

        .. versionadded:: 1.15.0

    where : array_like of bool, optional
        Elements to compare for the minimum. See `~numpy.ufunc.reduce`
        for details.

        .. versionadded:: 1.17.0

    Returns
    -------
    min : ndarray or scalar
        Minimum of `a`. If `axis` is None, the result is a scalar value.
        If `axis` is an int, the result is an array of dimension
        ``a.ndim - 1``.  If `axis` is a tuple, the result is an array of
        dimension ``a.ndim - len(axis)``.

    See Also
    --------
    amax :
        The maximum value of an array along a given axis, propagating any NaNs.
    nanmin :
        The minimum value of an array along a given axis, ignoring any NaNs.
    minimum :
        Element-wise minimum of two arrays, propagating any NaNs.
    fmin :
        Element-wise minimum of two arrays, ignoring any NaNs.
    argmin :
        Return the indices of the minimum values.

    nanmax, maximum, fmax

    Notes
    -----
    NaN values are propagated, that is if at least one item is NaN, the
    corresponding min value will be NaN as well. To ignore NaN values
    (MATLAB behavior), please use nanmin.

    Don't use `~numpy.min` for element-wise comparison of 2 arrays; when
    ``a.shape[0]`` is 2, ``minimum(a[0], a[1])`` is faster than
    ``min(a, axis=0)``.

    Examples
    --------
    >>> a = np.arange(4).reshape((2,2))
    >>> a
    array([[0, 1],
           [2, 3]])
    >>> np.min(a)           # Minimum of the flattened array
    0
    >>> np.min(a, axis=0)   # Minima along the first axis
    array([0, 1])
    >>> np.min(a, axis=1)   # Minima along the second axis
    array([0, 2])
    >>> np.min(a, where=[False, True], initial=10, axis=0)
    array([10,  1])

    >>> b = np.arange(5, dtype=float)
    >>> b[2] = np.NaN
    >>> np.min(b)
    nan
    >>> np.min(b, where=~np.isnan(b), initial=10)
    0.0
    >>> np.nanmin(b)
    0.0

    >>> np.min([[-50], [10]], axis=-1, initial=0)
    array([-50,   0])

    Notice that the initial value is used as one of the elements for which the
    minimum is determined, unlike for the default argument Python's max
    function, which is only used for empty iterables.

    Notice that this isn't the same as Python's ``default`` argument.

    >>> np.min([6], initial=5)
    5
    >>> min([6], default=5)
    6

None
&&&&&&&&&&&&&&&&&&&&&& ndim &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

ndim(a)
    Return the number of dimensions of an array.

    Parameters
    ----------
    a : array_like
        Input array.  If it is not already an ndarray, a conversion is
        attempted.

    Returns
    -------
    number_of_dimensions : int
        The number of dimensions in `a`.  Scalars are zero-dimensional.

    See Also
    --------
    ndarray.ndim : equivalent method
    shape : dimensions of array
    ndarray.shape : dimensions of array

    Examples
    --------
    >>> np.ndim([[1,2,3],[4,5,6]])
    2
    >>> np.ndim(np.array([[1,2,3],[4,5,6]]))
    2
    >>> np.ndim(1)
    0

None
&&&&&&&&&&&&&&&&&&&&&& ndindex &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on class ndindex in module numpy:

class ndindex(builtins.object)
 |  ndindex(*shape)
 |
 |  An N-dimensional iterator object to index arrays.
 |
 |  Given the shape of an array, an `ndindex` instance iterates over
 |  the N-dimensional index of the array. At each iteration a tuple
 |  of indices is returned, the last dimension is iterated over first.
 |
 |  Parameters
 |  ----------
 |  shape : ints, or a single tuple of ints
 |      The size of each dimension of the array can be passed as
 |      individual parameters or as the elements of a tuple.
 |
 |  See Also
 |  --------
 |  ndenumerate, flatiter
 |
 |  Examples
 |  --------
 |  Dimensions as individual arguments
 |
 |  >>> for index in np.ndindex(3, 2, 1):
 |  ...     print(index)
 |  (0, 0, 0)
 |  (0, 1, 0)
 |  (1, 0, 0)
 |  (1, 1, 0)
 |  (2, 0, 0)
 |  (2, 1, 0)
 |
 |  Same dimensions - but in a tuple ``(3, 2, 1)``
 |
 |  >>> for index in np.ndindex((3, 2, 1)):
 |  ...     print(index)
 |  (0, 0, 0)
 |  (0, 1, 0)
 |  (1, 0, 0)
 |  (1, 1, 0)
 |  (2, 0, 0)
 |  (2, 1, 0)
 |
 |  Methods defined here:
 |
 |  __init__(self, *shape)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __iter__(self)
 |
 |  __next__(self)
 |      Standard iterator method, updates the index and returns the index
 |      tuple.
 |
 |      Returns
 |      -------
 |      val : tuple of ints
 |          Returns a tuple containing the indices of the current
 |          iteration.
 |
 |  ndincr(self)
 |      Increment the multi-dimensional index by one.
 |
 |      This method is for backward compatibility only: do not use.
 |
 |      .. deprecated:: 1.20.0
 |          This method has been advised against since numpy 1.8.0, but only
 |          started emitting DeprecationWarning as of this version.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object

None
&&&&&&&&&&&&&&&&&&&&&& ones &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on function ones in module numpy:

ones(shape, dtype=None, order='C', *, like=None)
    Return a new array of given shape and type, filled with ones.

    Parameters
    ----------
    shape : int or sequence of ints
        Shape of the new array, e.g., ``(2, 3)`` or ``2``.
    dtype : data-type, optional
        The desired data-type for the array, e.g., `numpy.int8`.  Default is
        `numpy.float64`.
    order : {'C', 'F'}, optional, default: C
        Whether to store multi-dimensional data in row-major
        (C-style) or column-major (Fortran-style) order in
        memory.
    like : array_like, optional
        Reference object to allow the creation of arrays which are not
        NumPy arrays. If an array-like passed in as ``like`` supports
        the ``__array_function__`` protocol, the result will be defined
        by it. In this case, it ensures the creation of an array object
        compatible with that passed in via this argument.

        .. versionadded:: 1.20.0

    Returns
    -------
    out : ndarray
        Array of ones with the given shape, dtype, and order.

    See Also
    --------
    ones_like : Return an array of ones with shape and type of input.
    empty : Return a new uninitialized array.
    zeros : Return a new array setting values to zero.
    full : Return a new array of given shape filled with value.


    Examples
    --------
    >>> np.ones(5)
    array([1., 1., 1., 1., 1.])

    >>> np.ones((5,), dtype=int)
    array([1, 1, 1, 1, 1])

    >>> np.ones((2, 1))
    array([[1.],
           [1.]])

    >>> s = (2,2)
    >>> np.ones(s)
    array([[1.,  1.],
           [1.,  1.]])

None
&&&&&&&&&&&&&&&&&&&&&& pi &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on float object:

class float(object)
 |  float(x=0, /)
 |
 |  Convert a string or number to a floating point number, if possible.
 |
 |  Methods defined here:
 |
 |  __abs__(self, /)
 |      abs(self)
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __bool__(self, /)
 |      True if self else False
 |
 |  __ceil__(self, /)
 |      Return the ceiling as an Integral.
 |
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __float__(self, /)
 |      float(self)
 |
 |  __floor__(self, /)
 |      Return the floor as an Integral.
 |
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |
 |  __format__(self, format_spec, /)
 |      Formats the float according to format_spec.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __getnewargs__(self, /)
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
 |
 |  __int__(self, /)
 |      int(self)
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __mod__(self, value, /)
 |      Return self%value.
 |
 |  __mul__(self, value, /)
 |      Return self*value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __neg__(self, /)
 |      -self
 |
 |  __pos__(self, /)
 |      +self
 |
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |
 |  __radd__(self, value, /)
 |      Return value+self.
 |
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |
 |  __rmod__(self, value, /)
 |      Return value%self.
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __round__(self, ndigits=None, /)
 |      Return the Integral closest to x, rounding half toward even.
 |
 |      When an argument is passed, work like built-in round(x, ndigits).
 |
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |
 |  __rsub__(self, value, /)
 |      Return value-self.
 |
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |
 |  __sub__(self, value, /)
 |      Return self-value.
 |
 |  __truediv__(self, value, /)
 |      Return self/value.
 |
 |  __trunc__(self, /)
 |      Return the Integral closest to x between 0 and x.
 |
 |  as_integer_ratio(self, /)
 |      Return a pair of integers, whose ratio is exactly equal to the original float.
 |
 |      The ratio is in lowest terms and has a positive denominator.  Raise
 |      OverflowError on infinities and a ValueError on NaNs.
 |
 |      >>> (10.0).as_integer_ratio()
 |      (10, 1)
 |      >>> (0.0).as_integer_ratio()
 |      (0, 1)
 |      >>> (-.25).as_integer_ratio()
 |      (-1, 4)
 |
 |  conjugate(self, /)
 |      Return self, the complex conjugate of any float.
 |
 |  hex(self, /)
 |      Return a hexadecimal representation of a floating-point number.
 |
 |      >>> (-0.1).hex()
 |      '-0x1.999999999999ap-4'
 |      >>> 3.14159.hex()
 |      '0x1.921f9f01b866ep+1'
 |
 |  is_integer(self, /)
 |      Return True if the float is an integer.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __getformat__(typestr, /) from builtins.type
 |      You probably don't want to use this function.
 |
 |        typestr
 |          Must be 'double' or 'float'.
 |
 |      It exists mainly to be used in Python's test suite.
 |
 |      This function returns whichever of 'unknown', 'IEEE, big-endian' or 'IEEE,
 |      little-endian' best describes the format of floating point numbers used by the
 |      C type named by typestr.
 |
 |  fromhex(string, /) from builtins.type
 |      Create a floating-point number from a hexadecimal string.
 |
 |      >>> float.fromhex('0x1.ffffp10')
 |      2047.984375
 |      >>> float.fromhex('-0x1p-1074')
 |      -5e-324
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
 |  imag
 |      the imaginary part of a complex number
 |
 |  real
 |      the real part of a complex number

None
&&&&&&&&&&&&&&&&&&&&&& quantile &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

quantile(a, q, axis=None, out=None, overwrite_input=False, method='linear', keepdims=False, *, interpolation=None)
    Compute the q-th quantile of the data along the specified axis.

    .. versionadded:: 1.15.0

    Parameters
    ----------
    a : array_like of real numbers
        Input array or object that can be converted to an array.
    q : array_like of float
        Probability or sequence of probabilities for the quantiles to compute.
        Values must be between 0 and 1 inclusive.
    axis : {int, tuple of int, None}, optional
        Axis or axes along which the quantiles are computed. The default is
        to compute the quantile(s) along a flattened version of the array.
    out : ndarray, optional
        Alternative output array in which to place the result. It must have
        the same shape and buffer length as the expected output, but the
        type (of the output) will be cast if necessary.
    overwrite_input : bool, optional
        If True, then allow the input array `a` to be modified by
        intermediate calculations, to save memory. In this case, the
        contents of the input `a` after this function completes is
        undefined.
    method : str, optional
        This parameter specifies the method to use for estimating the
        quantile.  There are many different methods, some unique to NumPy.
        See the notes for explanation.  The options sorted by their R type
        as summarized in the H&F paper [1]_ are:

        1. 'inverted_cdf'
        2. 'averaged_inverted_cdf'
        3. 'closest_observation'
        4. 'interpolated_inverted_cdf'
        5. 'hazen'
        6. 'weibull'
        7. 'linear'  (default)
        8. 'median_unbiased'
        9. 'normal_unbiased'

        The first three methods are discontinuous.  NumPy further defines the
        following discontinuous variations of the default 'linear' (7.) option:

        * 'lower'
        * 'higher',
        * 'midpoint'
        * 'nearest'

        .. versionchanged:: 1.22.0
            This argument was previously called "interpolation" and only
            offered the "linear" default and last four options.

    keepdims : bool, optional
        If this is set to True, the axes which are reduced are left in
        the result as dimensions with size one. With this option, the
        result will broadcast correctly against the original array `a`.

    interpolation : str, optional
        Deprecated name for the method keyword argument.

        .. deprecated:: 1.22.0

    Returns
    -------
    quantile : scalar or ndarray
        If `q` is a single probability and `axis=None`, then the result
        is a scalar. If multiple probabilies levels are given, first axis of
        the result corresponds to the quantiles. The other axes are
        the axes that remain after the reduction of `a`. If the input
        contains integers or floats smaller than ``float64``, the output
        data-type is ``float64``. Otherwise, the output data-type is the
        same as that of the input. If `out` is specified, that array is
        returned instead.

    See Also
    --------
    mean
    percentile : equivalent to quantile, but with q in the range [0, 100].
    median : equivalent to ``quantile(..., 0.5)``
    nanquantile

    Notes
    -----
    Given a vector ``V`` of length ``n``, the q-th quantile of ``V`` is
    the value ``q`` of the way from the minimum to the maximum in a
    sorted copy of ``V``. The values and distances of the two nearest
    neighbors as well as the `method` parameter will determine the
    quantile if the normalized ranking does not match the location of
    ``q`` exactly. This function is the same as the median if ``q=0.5``, the
    same as the minimum if ``q=0.0`` and the same as the maximum if
    ``q=1.0``.

    The optional `method` parameter specifies the method to use when the
    desired quantile lies between two indexes ``i`` and ``j = i + 1``.
    In that case, we first determine ``i + g``, a virtual index that lies
    between ``i`` and ``j``, where  ``i`` is the floor and ``g`` is the
    fractional part of the index. The final result is, then, an interpolation
    of ``a[i]`` and ``a[j]`` based on ``g``. During the computation of ``g``,
    ``i`` and ``j`` are modified using correction constants ``alpha`` and
    ``beta`` whose choices depend on the ``method`` used. Finally, note that
    since Python uses 0-based indexing, the code subtracts another 1 from the
    index internally.

    The following formula determines the virtual index ``i + g``, the location
    of the quantile in the sorted sample:

    .. math::
        i + g = q * ( n - alpha - beta + 1 ) + alpha

    The different methods then work as follows

    inverted_cdf:
        method 1 of H&F [1]_.
        This method gives discontinuous results:

        * if g > 0 ; then take j
        * if g = 0 ; then take i

    averaged_inverted_cdf:
        method 2 of H&F [1]_.
        This method gives discontinuous results:

        * if g > 0 ; then take j
        * if g = 0 ; then average between bounds

    closest_observation:
        method 3 of H&F [1]_.
        This method gives discontinuous results:

        * if g > 0 ; then take j
        * if g = 0 and index is odd ; then take j
        * if g = 0 and index is even ; then take i

    interpolated_inverted_cdf:
        method 4 of H&F [1]_.
        This method gives continuous results using:

        * alpha = 0
        * beta = 1

    hazen:
        method 5 of H&F [1]_.
        This method gives continuous results using:

        * alpha = 1/2
        * beta = 1/2

    weibull:
        method 6 of H&F [1]_.
        This method gives continuous results using:

        * alpha = 0
        * beta = 0

    linear:
        method 7 of H&F [1]_.
        This method gives continuous results using:

        * alpha = 1
        * beta = 1

    median_unbiased:
        method 8 of H&F [1]_.
        This method is probably the best method if the sample
        distribution function is unknown (see reference).
        This method gives continuous results using:

        * alpha = 1/3
        * beta = 1/3

    normal_unbiased:
        method 9 of H&F [1]_.
        This method is probably the best method if the sample
        distribution function is known to be normal.
        This method gives continuous results using:

        * alpha = 3/8
        * beta = 3/8

    lower:
        NumPy method kept for backwards compatibility.
        Takes ``i`` as the interpolation point.

    higher:
        NumPy method kept for backwards compatibility.
        Takes ``j`` as the interpolation point.

    nearest:
        NumPy method kept for backwards compatibility.
        Takes ``i`` or ``j``, whichever is nearest.

    midpoint:
        NumPy method kept for backwards compatibility.
        Uses ``(i + j) / 2``.

    Examples
    --------
    >>> a = np.array([[10, 7, 4], [3, 2, 1]])
    >>> a
    array([[10,  7,  4],
           [ 3,  2,  1]])
    >>> np.quantile(a, 0.5)
    3.5
    >>> np.quantile(a, 0.5, axis=0)
    array([6.5, 4.5, 2.5])
    >>> np.quantile(a, 0.5, axis=1)
    array([7.,  2.])
    >>> np.quantile(a, 0.5, axis=1, keepdims=True)
    array([[7.],
           [2.]])
    >>> m = np.quantile(a, 0.5, axis=0)
    >>> out = np.zeros_like(m)
    >>> np.quantile(a, 0.5, axis=0, out=out)
    array([6.5, 4.5, 2.5])
    >>> m
    array([6.5, 4.5, 2.5])
    >>> b = a.copy()
    >>> np.quantile(b, 0.5, axis=1, overwrite_input=True)
    array([7.,  2.])
    >>> assert not np.all(a == b)

    See also `numpy.percentile` for a visualization of most methods.

    References
    ----------
    .. [1] R. J. Hyndman and Y. Fan,
       "Sample quantiles in statistical packages,"
       The American Statistician, 50(4), pp. 361-365, 1996

None
&&&&&&&&&&&&&&&&&&&&&& radians &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on ufunc:

radians = <ufunc 'radians'>
    radians(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])

    Convert angles from degrees to radians.

    Parameters
    ----------
    x : array_like
        Input array in degrees.
    out : ndarray, None, or tuple of ndarray and None, optional
        A location into which the result is stored. If provided, it must have
        a shape that the inputs broadcast to. If not provided or None,
        a freshly-allocated array is returned. A tuple (possible only as a
        keyword argument) must have length equal to the number of outputs.
    where : array_like, optional
        This condition is broadcast over the input. At locations where the
        condition is True, the `out` array will be set to the ufunc result.
        Elsewhere, the `out` array will retain its original value.
        Note that if an uninitialized `out` array is created via the default
        ``out=None``, locations within it where the condition is False will
        remain uninitialized.
    **kwargs
        For other keyword-only arguments, see the
        :ref:`ufunc docs <ufuncs.kwargs>`.

    Returns
    -------
    y : ndarray
        The corresponding radian values.
        This is a scalar if `x` is a scalar.

    See Also
    --------
    deg2rad : equivalent function

    Examples
    --------
    Convert a degree array to radians

    >>> deg = np.arange(12.) * 30.
    >>> np.radians(deg)
    array([ 0.        ,  0.52359878,  1.04719755,  1.57079633,  2.0943951 ,
            2.61799388,  3.14159265,  3.66519143,  4.1887902 ,  4.71238898,
            5.23598776,  5.75958653])

    >>> out = np.zeros((deg.shape))
    >>> ret = np.radians(deg, out)
    >>> ret is out
    True

None
&&&&&&&&&&&&&&&&&&&&&& random &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on package numpy.random in numpy:

NAME
    numpy.random

DESCRIPTION
    ========================
    Random Number Generation
    ========================

    Use ``default_rng()`` to create a `Generator` and call its methods.

    =============== =========================================================
    Generator
    --------------- ---------------------------------------------------------
    Generator       Class implementing all of the random number distributions
    default_rng     Default constructor for ``Generator``
    =============== =========================================================

    ============================================= ===
    BitGenerator Streams that work with Generator
    --------------------------------------------- ---
    MT19937
    PCG64
    PCG64DXSM
    Philox
    SFC64
    ============================================= ===

    ============================================= ===
    Getting entropy to initialize a BitGenerator
    --------------------------------------------- ---
    SeedSequence
    ============================================= ===


    Legacy
    ------

    For backwards compatibility with previous versions of numpy before 1.17, the
    various aliases to the global `RandomState` methods are left alone and do not
    use the new `Generator` API.

    ==================== =========================================================
    Utility functions
    -------------------- ---------------------------------------------------------
    random               Uniformly distributed floats over ``[0, 1)``
    bytes                Uniformly distributed random bytes.
    permutation          Randomly permute a sequence / generate a random sequence.
    shuffle              Randomly permute a sequence in place.
    choice               Random sample from 1-D array.
    ==================== =========================================================

    ==================== =========================================================
    Compatibility
    functions - removed
    in the new API
    -------------------- ---------------------------------------------------------
    rand                 Uniformly distributed values.
    randn                Normally distributed values.
    ranf                 Uniformly distributed floating point numbers.
    random_integers      Uniformly distributed integers in a given range.
                         (deprecated, use ``integers(..., closed=True)`` instead)
    random_sample        Alias for `random_sample`
    randint              Uniformly distributed integers in a given range
    seed                 Seed the legacy random number generator.
    ==================== =========================================================

    ==================== =========================================================
    Univariate
    distributions
    -------------------- ---------------------------------------------------------
    beta                 Beta distribution over ``[0, 1]``.
    binomial             Binomial distribution.
    chisquare            :math:`\chi^2` distribution.
    exponential          Exponential distribution.
    f                    F (Fisher-Snedecor) distribution.
    gamma                Gamma distribution.
    geometric            Geometric distribution.
    gumbel               Gumbel distribution.
    hypergeometric       Hypergeometric distribution.
    laplace              Laplace distribution.
    logistic             Logistic distribution.
    lognormal            Log-normal distribution.
    logseries            Logarithmic series distribution.
    negative_binomial    Negative binomial distribution.
    noncentral_chisquare Non-central chi-square distribution.
    noncentral_f         Non-central F distribution.
    normal               Normal / Gaussian distribution.
    pareto               Pareto distribution.
    poisson              Poisson distribution.
    power                Power distribution.
    rayleigh             Rayleigh distribution.
    triangular           Triangular distribution.
    uniform              Uniform distribution.
    vonmises             Von Mises circular distribution.
    wald                 Wald (inverse Gaussian) distribution.
    weibull              Weibull distribution.
    zipf                 Zipf's distribution over ranked data.
    ==================== =========================================================

    ==================== ==========================================================
    Multivariate
    distributions
    -------------------- ----------------------------------------------------------
    dirichlet            Multivariate generalization of Beta distribution.
    multinomial          Multivariate generalization of the binomial distribution.
    multivariate_normal  Multivariate generalization of the normal distribution.
    ==================== ==========================================================

    ==================== =========================================================
    Standard
    distributions
    -------------------- ---------------------------------------------------------
    standard_cauchy      Standard Cauchy-Lorentz distribution.
    standard_exponential Standard exponential distribution.
    standard_gamma       Standard Gamma distribution.
    standard_normal      Standard normal distribution.
    standard_t           Standard Student's t-distribution.
    ==================== =========================================================

    ==================== =========================================================
    Internal functions
    -------------------- ---------------------------------------------------------
    get_state            Get tuple representing internal state of generator.
    set_state            Set state of generator.
    ==================== =========================================================

PACKAGE CONTENTS
    _bounded_integers
    _common
    _generator
    _mt19937
    _pcg64
    _philox
    _pickle
    _sfc64
    bit_generator
    mtrand
    tests (package)

CLASSES
    builtins.object
        numpy.random._generator.Generator
        numpy.random.bit_generator.BitGenerator
            numpy.random._mt19937.MT19937
            numpy.random._pcg64.PCG64
            numpy.random._pcg64.PCG64DXSM
            numpy.random._philox.Philox
            numpy.random._sfc64.SFC64
        numpy.random.bit_generator.SeedSequence
        numpy.random.mtrand.RandomState

    class BitGenerator(builtins.object)
     |  BitGenerator(seed=None)
     |
     |  Base Class for generic BitGenerators, which provide a stream
     |  of random bits based on different algorithms. Must be overridden.
     |
     |  Parameters
     |  ----------
     |  seed : {None, int, array_like[ints], SeedSequence}, optional
     |      A seed to initialize the `BitGenerator`. If None, then fresh,
     |      unpredictable entropy will be pulled from the OS. If an ``int`` or
     |      ``array_like[ints]`` is passed, then it will be passed to
     |      `~numpy.random.SeedSequence` to derive the initial `BitGenerator` state.
     |      One may also pass in a `SeedSequence` instance.
     |      All integer values must be non-negative.
     |
     |  Attributes
     |  ----------
     |  lock : threading.Lock
     |      Lock instance that is shared so that the same BitGenerator can
     |      be used in multiple Generators without corrupting the state. Code that
     |      generates values from a bit generator should hold the bit generator's
     |      lock.
     |
     |  See Also
     |  --------
     |  SeedSequence
     |
     |  Methods defined here:
     |
     |  __getstate__(...)
     |      Helper for pickle.
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __setstate__(...)
     |
     |  random_raw(...)
     |      random_raw(self, size=None)
     |
     |      Return randoms as generated by the underlying BitGenerator
     |
     |      Parameters
     |      ----------
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  Default is None, in which case a
     |          single value is returned.
     |      output : bool, optional
     |          Output values.  Used for performance testing since the generated
     |          values are not returned.
     |
     |      Returns
     |      -------
     |      out : uint or ndarray
     |          Drawn samples.
     |
     |      Notes
     |      -----
     |      This method directly exposes the raw underlying pseudo-random
     |      number generator. All values are returned as unsigned 64-bit
     |      values irrespective of the number of bits produced by the PRNG.
     |
     |      See the class docstring for the number of bits returned.
     |
     |  spawn(...)
     |      spawn(n_children)
     |
     |      Create new independent child bit generators.
     |
     |      See :ref:`seedsequence-spawn` for additional notes on spawning
     |      children.  Some bit generators also implement ``jumped``
     |      as a different approach for creating independent streams.
     |
     |      .. versionadded:: 1.25.0
     |
     |      Parameters
     |      ----------
     |      n_children : int
     |
     |      Returns
     |      -------
     |      child_bit_generators : list of BitGenerators
     |
     |      Raises
     |      ------
     |      TypeError
     |          When the underlying SeedSequence does not implement spawning.
     |
     |      See Also
     |      --------
     |      random.Generator.spawn, random.SeedSequence.spawn :
     |          Equivalent method on the generator and seed sequence.
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
     |  capsule
     |
     |  cffi
     |      CFFI interface
     |
     |      Returns
     |      -------
     |      interface : namedtuple
     |          Named tuple containing CFFI wrapper
     |
     |          * state_address - Memory address of the state struct
     |          * state - pointer to the state struct
     |          * next_uint64 - function pointer to produce 64 bit integers
     |          * next_uint32 - function pointer to produce 32 bit integers
     |          * next_double - function pointer to produce doubles
     |          * bitgen - pointer to the bit generator struct
     |
     |  ctypes
     |      ctypes interface
     |
     |      Returns
     |      -------
     |      interface : namedtuple
     |          Named tuple containing ctypes wrapper
     |
     |          * state_address - Memory address of the state struct
     |          * state - pointer to the state struct
     |          * next_uint64 - function pointer to produce 64 bit integers
     |          * next_uint32 - function pointer to produce 32 bit integers
     |          * next_double - function pointer to produce doubles
     |          * bitgen - pointer to the bit generator struct
     |
     |  lock
     |
     |  seed_seq
     |      Get the seed sequence used to initialize the bit generator.
     |
     |      .. versionadded:: 1.25.0
     |
     |      Returns
     |      -------
     |      seed_seq : ISeedSequence
     |          The SeedSequence object used to initialize the BitGenerator.
     |          This is normally a `np.random.SeedSequence` instance.
     |
     |  state
     |      Get or set the PRNG state
     |
     |      The base BitGenerator.state must be overridden by a subclass
     |
     |      Returns
     |      -------
     |      state : dict
     |          Dictionary containing the information required to describe the
     |          state of the PRNG

    class Generator(builtins.object)
     |  Generator(bit_generator)
     |
     |  Container for the BitGenerators.
     |
     |  ``Generator`` exposes a number of methods for generating random
     |  numbers drawn from a variety of probability distributions. In addition to
     |  the distribution-specific arguments, each method takes a keyword argument
     |  `size` that defaults to ``None``. If `size` is ``None``, then a single
     |  value is generated and returned. If `size` is an integer, then a 1-D
     |  array filled with generated values is returned. If `size` is a tuple,
     |  then an array with that shape is filled and returned.
     |
     |  The function :func:`numpy.random.default_rng` will instantiate
     |  a `Generator` with numpy's default `BitGenerator`.
     |
     |  **No Compatibility Guarantee**
     |
     |  ``Generator`` does not provide a version compatibility guarantee. In
     |  particular, as better algorithms evolve the bit stream may change.
     |
     |  Parameters
     |  ----------
     |  bit_generator : BitGenerator
     |      BitGenerator to use as the core generator.
     |
     |  Notes
     |  -----
     |  The Python stdlib module `random` contains pseudo-random number generator
     |  with a number of methods that are similar to the ones available in
     |  ``Generator``. It uses Mersenne Twister, and this bit generator can
     |  be accessed using ``MT19937``. ``Generator``, besides being
     |  NumPy-aware, has the advantage that it provides a much larger number
     |  of probability distributions to choose from.
     |
     |  Examples
     |  --------
     |  >>> from numpy.random import Generator, PCG64
     |  >>> rng = Generator(PCG64())
     |  >>> rng.standard_normal()
     |  -0.203  # random
     |
     |  See Also
     |  --------
     |  default_rng : Recommended constructor for `Generator`.
     |
     |  Methods defined here:
     |
     |  __getstate__(...)
     |      Helper for pickle.
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __repr__(...)
     |      Return repr(self).
     |
     |  __setstate__(...)
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  beta(...)
     |      beta(a, b, size=None)
     |
     |      Draw samples from a Beta distribution.
     |
     |      The Beta distribution is a special case of the Dirichlet distribution,
     |      and is related to the Gamma distribution.  It has the probability
     |      distribution function
     |
     |      .. math:: f(x; a,b) = \frac{1}{B(\alpha, \beta)} x^{\alpha - 1}
     |                                                       (1 - x)^{\beta - 1},
     |
     |      where the normalization, B, is the beta function,
     |
     |      .. math:: B(\alpha, \beta) = \int_0^1 t^{\alpha - 1}
     |                                   (1 - t)^{\beta - 1} dt.
     |
     |      It is often seen in Bayesian inference and order statistics.
     |
     |      Parameters
     |      ----------
     |      a : float or array_like of floats
     |          Alpha, positive (>0).
     |      b : float or array_like of floats
     |          Beta, positive (>0).
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``a`` and ``b`` are both scalars.
     |          Otherwise, ``np.broadcast(a, b).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized beta distribution.
     |
     |  binomial(...)
     |      binomial(n, p, size=None)
     |
     |      Draw samples from a binomial distribution.
     |
     |      Samples are drawn from a binomial distribution with specified
     |      parameters, n trials and p probability of success where
     |      n an integer >= 0 and p is in the interval [0,1]. (n may be
     |      input as a float, but it is truncated to an integer in use)
     |
     |      Parameters
     |      ----------
     |      n : int or array_like of ints
     |          Parameter of the distribution, >= 0. Floats are also accepted,
     |          but they will be truncated to integers.
     |      p : float or array_like of floats
     |          Parameter of the distribution, >= 0 and <=1.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``n`` and ``p`` are both scalars.
     |          Otherwise, ``np.broadcast(n, p).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized binomial distribution, where
     |          each sample is equal to the number of successes over the n trials.
     |
     |      See Also
     |      --------
     |      scipy.stats.binom : probability density function, distribution or
     |          cumulative density function, etc.
     |
     |      Notes
     |      -----
     |      The probability density for the binomial distribution is
     |
     |      .. math:: P(N) = \binom{n}{N}p^N(1-p)^{n-N},
     |
     |      where :math:`n` is the number of trials, :math:`p` is the probability
     |      of success, and :math:`N` is the number of successes.
     |
     |      When estimating the standard error of a proportion in a population by
     |      using a random sample, the normal distribution works well unless the
     |      product p*n <=5, where p = population proportion estimate, and n =
     |      number of samples, in which case the binomial distribution is used
     |      instead. For example, a sample of 15 people shows 4 who are left
     |      handed, and 11 who are right handed. Then p = 4/15 = 27%. 0.27*15 = 4,
     |      so the binomial distribution should be used in this case.
     |
     |      References
     |      ----------
     |      .. [1] Dalgaard, Peter, "Introductory Statistics with R",
     |             Springer-Verlag, 2002.
     |      .. [2] Glantz, Stanton A. "Primer of Biostatistics.", McGraw-Hill,
     |             Fifth Edition, 2002.
     |      .. [3] Lentner, Marvin, "Elementary Applied Statistics", Bogden
     |             and Quigley, 1972.
     |      .. [4] Weisstein, Eric W. "Binomial Distribution." From MathWorld--A
     |             Wolfram Web Resource.
     |             http://mathworld.wolfram.com/BinomialDistribution.html
     |      .. [5] Wikipedia, "Binomial distribution",
     |             https://en.wikipedia.org/wiki/Binomial_distribution
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> rng = np.random.default_rng()
     |      >>> n, p = 10, .5  # number of trials, probability of each trial
     |      >>> s = rng.binomial(n, p, 1000)
     |      # result of flipping a coin 10 times, tested 1000 times.
     |
     |      A real world example. A company drills 9 wild-cat oil exploration
     |      wells, each with an estimated probability of success of 0.1. All nine
     |      wells fail. What is the probability of that happening?
     |
     |      Let's do 20,000 trials of the model, and count the number that
     |      generate zero positive results.
     |
     |      >>> sum(rng.binomial(9, 0.1, 20000) == 0)/20000.
     |      # answer = 0.38885, or 39%.
     |
     |  bytes(...)
     |      bytes(length)
     |
     |      Return random bytes.
     |
     |      Parameters
     |      ----------
     |      length : int
     |          Number of random bytes.
     |
     |      Returns
     |      -------
     |      out : bytes
     |          String of length `length`.
     |
     |      Examples
     |      --------
     |      >>> np.random.default_rng().bytes(10)
     |      b'\xfeC\x9b\x86\x17\xf2\xa1\xafcp' # random
     |
     |  chisquare(...)
     |      chisquare(df, size=None)
     |
     |      Draw samples from a chi-square distribution.
     |
     |      When `df` independent random variables, each with standard normal
     |      distributions (mean 0, variance 1), are squared and summed, the
     |      resulting distribution is chi-square (see Notes).  This distribution
     |      is often used in hypothesis testing.
     |
     |      Parameters
     |      ----------
     |      df : float or array_like of floats
     |           Number of degrees of freedom, must be > 0.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``df`` is a scalar.  Otherwise,
     |          ``np.array(df).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized chi-square distribution.
     |
     |      Raises
     |      ------
     |      ValueError
     |          When `df` <= 0 or when an inappropriate `size` (e.g. ``size=-1``)
     |          is given.
     |
     |      Notes
     |      -----
     |      The variable obtained by summing the squares of `df` independent,
     |      standard normally distributed random variables:
     |
     |      .. math:: Q = \sum_{i=0}^{\mathtt{df}} X^2_i
     |
     |      is chi-square distributed, denoted
     |
     |      .. math:: Q \sim \chi^2_k.
     |
     |      The probability density function of the chi-squared distribution is
     |
     |      .. math:: p(x) = \frac{(1/2)^{k/2}}{\Gamma(k/2)}
     |                       x^{k/2 - 1} e^{-x/2},
     |
     |      where :math:`\Gamma` is the gamma function,
     |
     |      .. math:: \Gamma(x) = \int_0^{-\infty} t^{x - 1} e^{-t} dt.
     |
     |      References
     |      ----------
     |      .. [1] NIST "Engineering Statistics Handbook"
     |             https://www.itl.nist.gov/div898/handbook/eda/section3/eda3666.htm
     |
     |      Examples
     |      --------
     |      >>> np.random.default_rng().chisquare(2,4)
     |      array([ 1.89920014,  9.00867716,  3.13710533,  5.62318272]) # random
     |
     |  choice(...)
     |      choice(a, size=None, replace=True, p=None, axis=0, shuffle=True)
     |
     |      Generates a random sample from a given array
     |
     |      Parameters
     |      ----------
     |      a : {array_like, int}
     |          If an ndarray, a random sample is generated from its elements.
     |          If an int, the random sample is generated from np.arange(a).
     |      size : {int, tuple[int]}, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn from the 1-d `a`. If `a` has more
     |          than one dimension, the `size` shape will be inserted into the
     |          `axis` dimension, so the output ``ndim`` will be ``a.ndim - 1 +
     |          len(size)``. Default is None, in which case a single value is
     |          returned.
     |      replace : bool, optional
     |          Whether the sample is with or without replacement. Default is True,
     |          meaning that a value of ``a`` can be selected multiple times.
     |      p : 1-D array_like, optional
     |          The probabilities associated with each entry in a.
     |          If not given, the sample assumes a uniform distribution over all
     |          entries in ``a``.
     |      axis : int, optional
     |          The axis along which the selection is performed. The default, 0,
     |          selects by row.
     |      shuffle : bool, optional
     |          Whether the sample is shuffled when sampling without replacement.
     |          Default is True, False provides a speedup.
     |
     |      Returns
     |      -------
     |      samples : single item or ndarray
     |          The generated random samples
     |
     |      Raises
     |      ------
     |      ValueError
     |          If a is an int and less than zero, if p is not 1-dimensional, if
     |          a is array-like with a size 0, if p is not a vector of
     |          probabilities, if a and p have different lengths, or if
     |          replace=False and the sample size is greater than the population
     |          size.
     |
     |      See Also
     |      --------
     |      integers, shuffle, permutation
     |
     |      Notes
     |      -----
     |      Setting user-specified probabilities through ``p`` uses a more general but less
     |      efficient sampler than the default. The general sampler produces a different sample
     |      than the optimized sampler even if each element of ``p`` is 1 / len(a).
     |
     |      Examples
     |      --------
     |      Generate a uniform random sample from np.arange(5) of size 3:
     |
     |      >>> rng = np.random.default_rng()
     |      >>> rng.choice(5, 3)
     |      array([0, 3, 4]) # random
     |      >>> #This is equivalent to rng.integers(0,5,3)
     |
     |      Generate a non-uniform random sample from np.arange(5) of size 3:
     |
     |      >>> rng.choice(5, 3, p=[0.1, 0, 0.3, 0.6, 0])
     |      array([3, 3, 0]) # random
     |
     |      Generate a uniform random sample from np.arange(5) of size 3 without
     |      replacement:
     |
     |      >>> rng.choice(5, 3, replace=False)
     |      array([3,1,0]) # random
     |      >>> #This is equivalent to rng.permutation(np.arange(5))[:3]
     |
     |      Generate a uniform random sample from a 2-D array along the first
     |      axis (the default), without replacement:
     |
     |      >>> rng.choice([[0, 1, 2], [3, 4, 5], [6, 7, 8]], 2, replace=False)
     |      array([[3, 4, 5], # random
     |             [0, 1, 2]])
     |
     |      Generate a non-uniform random sample from np.arange(5) of size
     |      3 without replacement:
     |
     |      >>> rng.choice(5, 3, replace=False, p=[0.1, 0, 0.3, 0.6, 0])
     |      array([2, 3, 0]) # random
     |
     |      Any of the above can be repeated with an arbitrary array-like
     |      instead of just integers. For instance:
     |
     |      >>> aa_milne_arr = ['pooh', 'rabbit', 'piglet', 'Christopher']
     |      >>> rng.choice(aa_milne_arr, 5, p=[0.5, 0.1, 0.1, 0.3])
     |      array(['pooh', 'pooh', 'pooh', 'Christopher', 'piglet'], # random
     |            dtype='<U11')
     |
     |  dirichlet(...)
     |      dirichlet(alpha, size=None)
     |
     |      Draw samples from the Dirichlet distribution.
     |
     |      Draw `size` samples of dimension k from a Dirichlet distribution. A
     |      Dirichlet-distributed random variable can be seen as a multivariate
     |      generalization of a Beta distribution. The Dirichlet distribution
     |      is a conjugate prior of a multinomial distribution in Bayesian
     |      inference.
     |
     |      Parameters
     |      ----------
     |      alpha : sequence of floats, length k
     |          Parameter of the distribution (length ``k`` for sample of
     |          length ``k``).
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n)``, then
     |          ``m * n * k`` samples are drawn.  Default is None, in which case a
     |          vector of length ``k`` is returned.
     |
     |      Returns
     |      -------
     |      samples : ndarray,
     |          The drawn samples, of shape ``(size, k)``.
     |
     |      Raises
     |      ------
     |      ValueError
     |          If any value in ``alpha`` is less than zero
     |
     |      Notes
     |      -----
     |      The Dirichlet distribution is a distribution over vectors
     |      :math:`x` that fulfil the conditions :math:`x_i>0` and
     |      :math:`\sum_{i=1}^k x_i = 1`.
     |
     |      The probability density function :math:`p` of a
     |      Dirichlet-distributed random vector :math:`X` is
     |      proportional to
     |
     |      .. math:: p(x) \propto \prod_{i=1}^{k}{x^{\alpha_i-1}_i},
     |
     |      where :math:`\alpha` is a vector containing the positive
     |      concentration parameters.
     |
     |      The method uses the following property for computation: let :math:`Y`
     |      be a random vector which has components that follow a standard gamma
     |      distribution, then :math:`X = \frac{1}{\sum_{i=1}^k{Y_i}} Y`
     |      is Dirichlet-distributed
     |
     |      References
     |      ----------
     |      .. [1] David McKay, "Information Theory, Inference and Learning
     |             Algorithms," chapter 23,
     |             http://www.inference.org.uk/mackay/itila/
     |      .. [2] Wikipedia, "Dirichlet distribution",
     |             https://en.wikipedia.org/wiki/Dirichlet_distribution
     |
     |      Examples
     |      --------
     |      Taking an example cited in Wikipedia, this distribution can be used if
     |      one wanted to cut strings (each of initial length 1.0) into K pieces
     |      with different lengths, where each piece had, on average, a designated
     |      average length, but allowing some variation in the relative sizes of
     |      the pieces.
     |
     |      >>> s = np.random.default_rng().dirichlet((10, 5, 3), 20).transpose()
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> plt.barh(range(20), s[0])
     |      >>> plt.barh(range(20), s[1], left=s[0], color='g')
     |      >>> plt.barh(range(20), s[2], left=s[0]+s[1], color='r')
     |      >>> plt.title("Lengths of Strings")
     |
     |  exponential(...)
     |      exponential(scale=1.0, size=None)
     |
     |      Draw samples from an exponential distribution.
     |
     |      Its probability density function is
     |
     |      .. math:: f(x; \frac{1}{\beta}) = \frac{1}{\beta} \exp(-\frac{x}{\beta}),
     |
     |      for ``x > 0`` and 0 elsewhere. :math:`\beta` is the scale parameter,
     |      which is the inverse of the rate parameter :math:`\lambda = 1/\beta`.
     |      The rate parameter is an alternative, widely used parameterization
     |      of the exponential distribution [3]_.
     |
     |      The exponential distribution is a continuous analogue of the
     |      geometric distribution.  It describes many common situations, such as
     |      the size of raindrops measured over many rainstorms [1]_, or the time
     |      between page requests to Wikipedia [2]_.
     |
     |      Parameters
     |      ----------
     |      scale : float or array_like of floats
     |          The scale parameter, :math:`\beta = 1/\lambda`. Must be
     |          non-negative.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``scale`` is a scalar.  Otherwise,
     |          ``np.array(scale).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized exponential distribution.
     |
     |      Examples
     |      --------
     |      A real world example: Assume a company has 10000 customer support
     |      agents and the average time between customer calls is 4 minutes.
     |
     |      >>> n = 10000
     |      >>> time_between_calls = np.random.default_rng().exponential(scale=4, size=n)
     |
     |      What is the probability that a customer will call in the next
     |      4 to 5 minutes?
     |
     |      >>> x = ((time_between_calls < 5).sum())/n
     |      >>> y = ((time_between_calls < 4).sum())/n
     |      >>> x-y
     |      0.08 # may vary
     |
     |      References
     |      ----------
     |      .. [1] Peyton Z. Peebles Jr., "Probability, Random Variables and
     |             Random Signal Principles", 4th ed, 2001, p. 57.
     |      .. [2] Wikipedia, "Poisson process",
     |             https://en.wikipedia.org/wiki/Poisson_process
     |      .. [3] Wikipedia, "Exponential distribution",
     |             https://en.wikipedia.org/wiki/Exponential_distribution
     |
     |  f(...)
     |      f(dfnum, dfden, size=None)
     |
     |      Draw samples from an F distribution.
     |
     |      Samples are drawn from an F distribution with specified parameters,
     |      `dfnum` (degrees of freedom in numerator) and `dfden` (degrees of
     |      freedom in denominator), where both parameters must be greater than
     |      zero.
     |
     |      The random variate of the F distribution (also known as the
     |      Fisher distribution) is a continuous probability distribution
     |      that arises in ANOVA tests, and is the ratio of two chi-square
     |      variates.
     |
     |      Parameters
     |      ----------
     |      dfnum : float or array_like of floats
     |          Degrees of freedom in numerator, must be > 0.
     |      dfden : float or array_like of float
     |          Degrees of freedom in denominator, must be > 0.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``dfnum`` and ``dfden`` are both scalars.
     |          Otherwise, ``np.broadcast(dfnum, dfden).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized Fisher distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.f : probability density function, distribution or
     |          cumulative density function, etc.
     |
     |      Notes
     |      -----
     |      The F statistic is used to compare in-group variances to between-group
     |      variances. Calculating the distribution depends on the sampling, and
     |      so it is a function of the respective degrees of freedom in the
     |      problem.  The variable `dfnum` is the number of samples minus one, the
     |      between-groups degrees of freedom, while `dfden` is the within-groups
     |      degrees of freedom, the sum of the number of samples in each group
     |      minus the number of groups.
     |
     |      References
     |      ----------
     |      .. [1] Glantz, Stanton A. "Primer of Biostatistics.", McGraw-Hill,
     |             Fifth Edition, 2002.
     |      .. [2] Wikipedia, "F-distribution",
     |             https://en.wikipedia.org/wiki/F-distribution
     |
     |      Examples
     |      --------
     |      An example from Glantz[1], pp 47-40:
     |
     |      Two groups, children of diabetics (25 people) and children from people
     |      without diabetes (25 controls). Fasting blood glucose was measured,
     |      case group had a mean value of 86.1, controls had a mean value of
     |      82.2. Standard deviations were 2.09 and 2.49 respectively. Are these
     |      data consistent with the null hypothesis that the parents diabetic
     |      status does not affect their children's blood glucose levels?
     |      Calculating the F statistic from the data gives a value of 36.01.
     |
     |      Draw samples from the distribution:
     |
     |      >>> dfnum = 1. # between group degrees of freedom
     |      >>> dfden = 48. # within groups degrees of freedom
     |      >>> s = np.random.default_rng().f(dfnum, dfden, 1000)
     |
     |      The lower bound for the top 1% of the samples is :
     |
     |      >>> np.sort(s)[-10]
     |      7.61988120985 # random
     |
     |      So there is about a 1% chance that the F statistic will exceed 7.62,
     |      the measured value is 36, so the null hypothesis is rejected at the 1%
     |      level.
     |
     |  gamma(...)
     |      gamma(shape, scale=1.0, size=None)
     |
     |      Draw samples from a Gamma distribution.
     |
     |      Samples are drawn from a Gamma distribution with specified parameters,
     |      `shape` (sometimes designated "k") and `scale` (sometimes designated
     |      "theta"), where both parameters are > 0.
     |
     |      Parameters
     |      ----------
     |      shape : float or array_like of floats
     |          The shape of the gamma distribution. Must be non-negative.
     |      scale : float or array_like of floats, optional
     |          The scale of the gamma distribution. Must be non-negative.
     |          Default is equal to 1.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``shape`` and ``scale`` are both scalars.
     |          Otherwise, ``np.broadcast(shape, scale).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized gamma distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.gamma : probability density function, distribution or
     |          cumulative density function, etc.
     |
     |      Notes
     |      -----
     |      The probability density for the Gamma distribution is
     |
     |      .. math:: p(x) = x^{k-1}\frac{e^{-x/\theta}}{\theta^k\Gamma(k)},
     |
     |      where :math:`k` is the shape and :math:`\theta` the scale,
     |      and :math:`\Gamma` is the Gamma function.
     |
     |      The Gamma distribution is often used to model the times to failure of
     |      electronic components, and arises naturally in processes for which the
     |      waiting times between Poisson distributed events are relevant.
     |
     |      References
     |      ----------
     |      .. [1] Weisstein, Eric W. "Gamma Distribution." From MathWorld--A
     |             Wolfram Web Resource.
     |             http://mathworld.wolfram.com/GammaDistribution.html
     |      .. [2] Wikipedia, "Gamma distribution",
     |             https://en.wikipedia.org/wiki/Gamma_distribution
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> shape, scale = 2., 2.  # mean=4, std=2*sqrt(2)
     |      >>> s = np.random.default_rng().gamma(shape, scale, 1000)
     |
     |      Display the histogram of the samples, along with
     |      the probability density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> import scipy.special as sps  # doctest: +SKIP
     |      >>> count, bins, ignored = plt.hist(s, 50, density=True)
     |      >>> y = bins**(shape-1)*(np.exp(-bins/scale) /  # doctest: +SKIP
     |      ...                      (sps.gamma(shape)*scale**shape))
     |      >>> plt.plot(bins, y, linewidth=2, color='r')  # doctest: +SKIP
     |      >>> plt.show()
     |
     |  geometric(...)
     |      geometric(p, size=None)
     |
     |      Draw samples from the geometric distribution.
     |
     |      Bernoulli trials are experiments with one of two outcomes:
     |      success or failure (an example of such an experiment is flipping
     |      a coin).  The geometric distribution models the number of trials
     |      that must be run in order to achieve success.  It is therefore
     |      supported on the positive integers, ``k = 1, 2, ...``.
     |
     |      The probability mass function of the geometric distribution is
     |
     |      .. math:: f(k) = (1 - p)^{k - 1} p
     |
     |      where `p` is the probability of success of an individual trial.
     |
     |      Parameters
     |      ----------
     |      p : float or array_like of floats
     |          The probability of success of an individual trial.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``p`` is a scalar.  Otherwise,
     |          ``np.array(p).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized geometric distribution.
     |
     |      Examples
     |      --------
     |      Draw ten thousand values from the geometric distribution,
     |      with the probability of an individual success equal to 0.35:
     |
     |      >>> z = np.random.default_rng().geometric(p=0.35, size=10000)
     |
     |      How many trials succeeded after a single run?
     |
     |      >>> (z == 1).sum() / 10000.
     |      0.34889999999999999 # random
     |
     |  gumbel(...)
     |      gumbel(loc=0.0, scale=1.0, size=None)
     |
     |      Draw samples from a Gumbel distribution.
     |
     |      Draw samples from a Gumbel distribution with specified location and
     |      scale.  For more information on the Gumbel distribution, see
     |      Notes and References below.
     |
     |      Parameters
     |      ----------
     |      loc : float or array_like of floats, optional
     |          The location of the mode of the distribution. Default is 0.
     |      scale : float or array_like of floats, optional
     |          The scale parameter of the distribution. Default is 1. Must be non-
     |          negative.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``loc`` and ``scale`` are both scalars.
     |          Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized Gumbel distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.gumbel_l
     |      scipy.stats.gumbel_r
     |      scipy.stats.genextreme
     |      weibull
     |
     |      Notes
     |      -----
     |      The Gumbel (or Smallest Extreme Value (SEV) or the Smallest Extreme
     |      Value Type I) distribution is one of a class of Generalized Extreme
     |      Value (GEV) distributions used in modeling extreme value problems.
     |      The Gumbel is a special case of the Extreme Value Type I distribution
     |      for maximums from distributions with "exponential-like" tails.
     |
     |      The probability density for the Gumbel distribution is
     |
     |      .. math:: p(x) = \frac{e^{-(x - \mu)/ \beta}}{\beta} e^{ -e^{-(x - \mu)/
     |                \beta}},
     |
     |      where :math:`\mu` is the mode, a location parameter, and
     |      :math:`\beta` is the scale parameter.
     |
     |      The Gumbel (named for German mathematician Emil Julius Gumbel) was used
     |      very early in the hydrology literature, for modeling the occurrence of
     |      flood events. It is also used for modeling maximum wind speed and
     |      rainfall rates.  It is a "fat-tailed" distribution - the probability of
     |      an event in the tail of the distribution is larger than if one used a
     |      Gaussian, hence the surprisingly frequent occurrence of 100-year
     |      floods. Floods were initially modeled as a Gaussian process, which
     |      underestimated the frequency of extreme events.
     |
     |      It is one of a class of extreme value distributions, the Generalized
     |      Extreme Value (GEV) distributions, which also includes the Weibull and
     |      Frechet.
     |
     |      The function has a mean of :math:`\mu + 0.57721\beta` and a variance
     |      of :math:`\frac{\pi^2}{6}\beta^2`.
     |
     |      References
     |      ----------
     |      .. [1] Gumbel, E. J., "Statistics of Extremes,"
     |             New York: Columbia University Press, 1958.
     |      .. [2] Reiss, R.-D. and Thomas, M., "Statistical Analysis of Extreme
     |             Values from Insurance, Finance, Hydrology and Other Fields,"
     |             Basel: Birkhauser Verlag, 2001.
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> rng = np.random.default_rng()
     |      >>> mu, beta = 0, 0.1 # location and scale
     |      >>> s = rng.gumbel(mu, beta, 1000)
     |
     |      Display the histogram of the samples, along with
     |      the probability density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> count, bins, ignored = plt.hist(s, 30, density=True)
     |      >>> plt.plot(bins, (1/beta)*np.exp(-(bins - mu)/beta)
     |      ...          * np.exp( -np.exp( -(bins - mu) /beta) ),
     |      ...          linewidth=2, color='r')
     |      >>> plt.show()
     |
     |      Show how an extreme value distribution can arise from a Gaussian process
     |      and compare to a Gaussian:
     |
     |      >>> means = []
     |      >>> maxima = []
     |      >>> for i in range(0,1000) :
     |      ...    a = rng.normal(mu, beta, 1000)
     |      ...    means.append(a.mean())
     |      ...    maxima.append(a.max())
     |      >>> count, bins, ignored = plt.hist(maxima, 30, density=True)
     |      >>> beta = np.std(maxima) * np.sqrt(6) / np.pi
     |      >>> mu = np.mean(maxima) - 0.57721*beta
     |      >>> plt.plot(bins, (1/beta)*np.exp(-(bins - mu)/beta)
     |      ...          * np.exp(-np.exp(-(bins - mu)/beta)),
     |      ...          linewidth=2, color='r')
     |      >>> plt.plot(bins, 1/(beta * np.sqrt(2 * np.pi))
     |      ...          * np.exp(-(bins - mu)**2 / (2 * beta**2)),
     |      ...          linewidth=2, color='g')
     |      >>> plt.show()
     |
     |  hypergeometric(...)
     |      hypergeometric(ngood, nbad, nsample, size=None)
     |
     |      Draw samples from a Hypergeometric distribution.
     |
     |      Samples are drawn from a hypergeometric distribution with specified
     |      parameters, `ngood` (ways to make a good selection), `nbad` (ways to make
     |      a bad selection), and `nsample` (number of items sampled, which is less
     |      than or equal to the sum ``ngood + nbad``).
     |
     |      Parameters
     |      ----------
     |      ngood : int or array_like of ints
     |          Number of ways to make a good selection.  Must be nonnegative and
     |          less than 10**9.
     |      nbad : int or array_like of ints
     |          Number of ways to make a bad selection.  Must be nonnegative and
     |          less than 10**9.
     |      nsample : int or array_like of ints
     |          Number of items sampled.  Must be nonnegative and less than
     |          ``ngood + nbad``.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if `ngood`, `nbad`, and `nsample`
     |          are all scalars.  Otherwise, ``np.broadcast(ngood, nbad, nsample).size``
     |          samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized hypergeometric distribution. Each
     |          sample is the number of good items within a randomly selected subset of
     |          size `nsample` taken from a set of `ngood` good items and `nbad` bad items.
     |
     |      See Also
     |      --------
     |      multivariate_hypergeometric : Draw samples from the multivariate
     |          hypergeometric distribution.
     |      scipy.stats.hypergeom : probability density function, distribution or
     |          cumulative density function, etc.
     |
     |      Notes
     |      -----
     |      The probability density for the Hypergeometric distribution is
     |
     |      .. math:: P(x) = \frac{\binom{g}{x}\binom{b}{n-x}}{\binom{g+b}{n}},
     |
     |      where :math:`0 \le x \le n` and :math:`n-b \le x \le g`
     |
     |      for P(x) the probability of ``x`` good results in the drawn sample,
     |      g = `ngood`, b = `nbad`, and n = `nsample`.
     |
     |      Consider an urn with black and white marbles in it, `ngood` of them
     |      are black and `nbad` are white. If you draw `nsample` balls without
     |      replacement, then the hypergeometric distribution describes the
     |      distribution of black balls in the drawn sample.
     |
     |      Note that this distribution is very similar to the binomial
     |      distribution, except that in this case, samples are drawn without
     |      replacement, whereas in the Binomial case samples are drawn with
     |      replacement (or the sample space is infinite). As the sample space
     |      becomes large, this distribution approaches the binomial.
     |
     |      The arguments `ngood` and `nbad` each must be less than `10**9`. For
     |      extremely large arguments, the algorithm that is used to compute the
     |      samples [4]_ breaks down because of loss of precision in floating point
     |      calculations.  For such large values, if `nsample` is not also large,
     |      the distribution can be approximated with the binomial distribution,
     |      `binomial(n=nsample, p=ngood/(ngood + nbad))`.
     |
     |      References
     |      ----------
     |      .. [1] Lentner, Marvin, "Elementary Applied Statistics", Bogden
     |             and Quigley, 1972.
     |      .. [2] Weisstein, Eric W. "Hypergeometric Distribution." From
     |             MathWorld--A Wolfram Web Resource.
     |             http://mathworld.wolfram.com/HypergeometricDistribution.html
     |      .. [3] Wikipedia, "Hypergeometric distribution",
     |             https://en.wikipedia.org/wiki/Hypergeometric_distribution
     |      .. [4] Stadlober, Ernst, "The ratio of uniforms approach for generating
     |             discrete random variates", Journal of Computational and Applied
     |             Mathematics, 31, pp. 181-189 (1990).
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> rng = np.random.default_rng()
     |      >>> ngood, nbad, nsamp = 100, 2, 10
     |      # number of good, number of bad, and number of samples
     |      >>> s = rng.hypergeometric(ngood, nbad, nsamp, 1000)
     |      >>> from matplotlib.pyplot import hist
     |      >>> hist(s)
     |      #   note that it is very unlikely to grab both bad items
     |
     |      Suppose you have an urn with 15 white and 15 black marbles.
     |      If you pull 15 marbles at random, how likely is it that
     |      12 or more of them are one color?
     |
     |      >>> s = rng.hypergeometric(15, 15, 15, 100000)
     |      >>> sum(s>=12)/100000. + sum(s<=3)/100000.
     |      #   answer = 0.003 ... pretty unlikely!
     |
     |  integers(...)
     |      integers(low, high=None, size=None, dtype=np.int64, endpoint=False)
     |
     |      Return random integers from `low` (inclusive) to `high` (exclusive), or
     |      if endpoint=True, `low` (inclusive) to `high` (inclusive). Replaces
     |      `RandomState.randint` (with endpoint=False) and
     |      `RandomState.random_integers` (with endpoint=True)
     |
     |      Return random integers from the "discrete uniform" distribution of
     |      the specified dtype. If `high` is None (the default), then results are
     |      from 0 to `low`.
     |
     |      Parameters
     |      ----------
     |      low : int or array-like of ints
     |          Lowest (signed) integers to be drawn from the distribution (unless
     |          ``high=None``, in which case this parameter is 0 and this value is
     |          used for `high`).
     |      high : int or array-like of ints, optional
     |          If provided, one above the largest (signed) integer to be drawn
     |          from the distribution (see above for behavior if ``high=None``).
     |          If array-like, must contain integer values
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  Default is None, in which case a
     |          single value is returned.
     |      dtype : dtype, optional
     |          Desired dtype of the result. Byteorder must be native.
     |          The default value is np.int64.
     |      endpoint : bool, optional
     |          If true, sample from the interval [low, high] instead of the
     |          default [low, high)
     |          Defaults to False
     |
     |      Returns
     |      -------
     |      out : int or ndarray of ints
     |          `size`-shaped array of random integers from the appropriate
     |          distribution, or a single such random int if `size` not provided.
     |
     |      Notes
     |      -----
     |      When using broadcasting with uint64 dtypes, the maximum value (2**64)
     |      cannot be represented as a standard integer type. The high array (or
     |      low if high is None) must have object dtype, e.g., array([2**64]).
     |
     |      Examples
     |      --------
     |      >>> rng = np.random.default_rng()
     |      >>> rng.integers(2, size=10)
     |      array([1, 0, 0, 0, 1, 1, 0, 0, 1, 0])  # random
     |      >>> rng.integers(1, size=10)
     |      array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
     |
     |      Generate a 2 x 4 array of ints between 0 and 4, inclusive:
     |
     |      >>> rng.integers(5, size=(2, 4))
     |      array([[4, 0, 2, 1],
     |             [3, 2, 2, 0]])  # random
     |
     |      Generate a 1 x 3 array with 3 different upper bounds
     |
     |      >>> rng.integers(1, [3, 5, 10])
     |      array([2, 2, 9])  # random
     |
     |      Generate a 1 by 3 array with 3 different lower bounds
     |
     |      >>> rng.integers([1, 5, 7], 10)
     |      array([9, 8, 7])  # random
     |
     |      Generate a 2 by 4 array using broadcasting with dtype of uint8
     |
     |      >>> rng.integers([1, 3, 5, 7], [[10], [20]], dtype=np.uint8)
     |      array([[ 8,  6,  9,  7],
     |             [ 1, 16,  9, 12]], dtype=uint8)  # random
     |
     |      References
     |      ----------
     |      .. [1] Daniel Lemire., "Fast Random Integer Generation in an Interval",
     |             ACM Transactions on Modeling and Computer Simulation 29 (1), 2019,
     |             http://arxiv.org/abs/1805.10941.
     |
     |  laplace(...)
     |      laplace(loc=0.0, scale=1.0, size=None)
     |
     |      Draw samples from the Laplace or double exponential distribution with
     |      specified location (or mean) and scale (decay).
     |
     |      The Laplace distribution is similar to the Gaussian/normal distribution,
     |      but is sharper at the peak and has fatter tails. It represents the
     |      difference between two independent, identically distributed exponential
     |      random variables.
     |
     |      Parameters
     |      ----------
     |      loc : float or array_like of floats, optional
     |          The position, :math:`\mu`, of the distribution peak. Default is 0.
     |      scale : float or array_like of floats, optional
     |          :math:`\lambda`, the exponential decay. Default is 1. Must be non-
     |          negative.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``loc`` and ``scale`` are both scalars.
     |          Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized Laplace distribution.
     |
     |      Notes
     |      -----
     |      It has the probability density function
     |
     |      .. math:: f(x; \mu, \lambda) = \frac{1}{2\lambda}
     |                                     \exp\left(-\frac{|x - \mu|}{\lambda}\right).
     |
     |      The first law of Laplace, from 1774, states that the frequency
     |      of an error can be expressed as an exponential function of the
     |      absolute magnitude of the error, which leads to the Laplace
     |      distribution. For many problems in economics and health
     |      sciences, this distribution seems to model the data better
     |      than the standard Gaussian distribution.
     |
     |      References
     |      ----------
     |      .. [1] Abramowitz, M. and Stegun, I. A. (Eds.). "Handbook of
     |             Mathematical Functions with Formulas, Graphs, and Mathematical
     |             Tables, 9th printing," New York: Dover, 1972.
     |      .. [2] Kotz, Samuel, et. al. "The Laplace Distribution and
     |             Generalizations, " Birkhauser, 2001.
     |      .. [3] Weisstein, Eric W. "Laplace Distribution."
     |             From MathWorld--A Wolfram Web Resource.
     |             http://mathworld.wolfram.com/LaplaceDistribution.html
     |      .. [4] Wikipedia, "Laplace distribution",
     |             https://en.wikipedia.org/wiki/Laplace_distribution
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution
     |
     |      >>> loc, scale = 0., 1.
     |      >>> s = np.random.default_rng().laplace(loc, scale, 1000)
     |
     |      Display the histogram of the samples, along with
     |      the probability density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> count, bins, ignored = plt.hist(s, 30, density=True)
     |      >>> x = np.arange(-8., 8., .01)
     |      >>> pdf = np.exp(-abs(x-loc)/scale)/(2.*scale)
     |      >>> plt.plot(x, pdf)
     |
     |      Plot Gaussian for comparison:
     |
     |      >>> g = (1/(scale * np.sqrt(2 * np.pi)) *
     |      ...      np.exp(-(x - loc)**2 / (2 * scale**2)))
     |      >>> plt.plot(x,g)
     |
     |  logistic(...)
     |      logistic(loc=0.0, scale=1.0, size=None)
     |
     |      Draw samples from a logistic distribution.
     |
     |      Samples are drawn from a logistic distribution with specified
     |      parameters, loc (location or mean, also median), and scale (>0).
     |
     |      Parameters
     |      ----------
     |      loc : float or array_like of floats, optional
     |          Parameter of the distribution. Default is 0.
     |      scale : float or array_like of floats, optional
     |          Parameter of the distribution. Must be non-negative.
     |          Default is 1.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``loc`` and ``scale`` are both scalars.
     |          Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized logistic distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.logistic : probability density function, distribution or
     |          cumulative density function, etc.
     |
     |      Notes
     |      -----
     |      The probability density for the Logistic distribution is
     |
     |      .. math:: P(x) = P(x) = \frac{e^{-(x-\mu)/s}}{s(1+e^{-(x-\mu)/s})^2},
     |
     |      where :math:`\mu` = location and :math:`s` = scale.
     |
     |      The Logistic distribution is used in Extreme Value problems where it
     |      can act as a mixture of Gumbel distributions, in Epidemiology, and by
     |      the World Chess Federation (FIDE) where it is used in the Elo ranking
     |      system, assuming the performance of each player is a logistically
     |      distributed random variable.
     |
     |      References
     |      ----------
     |      .. [1] Reiss, R.-D. and Thomas M. (2001), "Statistical Analysis of
     |             Extreme Values, from Insurance, Finance, Hydrology and Other
     |             Fields," Birkhauser Verlag, Basel, pp 132-133.
     |      .. [2] Weisstein, Eric W. "Logistic Distribution." From
     |             MathWorld--A Wolfram Web Resource.
     |             http://mathworld.wolfram.com/LogisticDistribution.html
     |      .. [3] Wikipedia, "Logistic-distribution",
     |             https://en.wikipedia.org/wiki/Logistic_distribution
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> loc, scale = 10, 1
     |      >>> s = np.random.default_rng().logistic(loc, scale, 10000)
     |      >>> import matplotlib.pyplot as plt
     |      >>> count, bins, ignored = plt.hist(s, bins=50)
     |
     |      #   plot against distribution
     |
     |      >>> def logist(x, loc, scale):
     |      ...     return np.exp((loc-x)/scale)/(scale*(1+np.exp((loc-x)/scale))**2)
     |      >>> lgst_val = logist(bins, loc, scale)
     |      >>> plt.plot(bins, lgst_val * count.max() / lgst_val.max())
     |      >>> plt.show()
     |
     |  lognormal(...)
     |      lognormal(mean=0.0, sigma=1.0, size=None)
     |
     |      Draw samples from a log-normal distribution.
     |
     |      Draw samples from a log-normal distribution with specified mean,
     |      standard deviation, and array shape.  Note that the mean and standard
     |      deviation are not the values for the distribution itself, but of the
     |      underlying normal distribution it is derived from.
     |
     |      Parameters
     |      ----------
     |      mean : float or array_like of floats, optional
     |          Mean value of the underlying normal distribution. Default is 0.
     |      sigma : float or array_like of floats, optional
     |          Standard deviation of the underlying normal distribution. Must be
     |          non-negative. Default is 1.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``mean`` and ``sigma`` are both scalars.
     |          Otherwise, ``np.broadcast(mean, sigma).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized log-normal distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.lognorm : probability density function, distribution,
     |          cumulative density function, etc.
     |
     |      Notes
     |      -----
     |      A variable `x` has a log-normal distribution if `log(x)` is normally
     |      distributed.  The probability density function for the log-normal
     |      distribution is:
     |
     |      .. math:: p(x) = \frac{1}{\sigma x \sqrt{2\pi}}
     |                       e^{(-\frac{(ln(x)-\mu)^2}{2\sigma^2})}
     |
     |      where :math:`\mu` is the mean and :math:`\sigma` is the standard
     |      deviation of the normally distributed logarithm of the variable.
     |      A log-normal distribution results if a random variable is the *product*
     |      of a large number of independent, identically-distributed variables in
     |      the same way that a normal distribution results if the variable is the
     |      *sum* of a large number of independent, identically-distributed
     |      variables.
     |
     |      References
     |      ----------
     |      .. [1] Limpert, E., Stahel, W. A., and Abbt, M., "Log-normal
     |             Distributions across the Sciences: Keys and Clues,"
     |             BioScience, Vol. 51, No. 5, May, 2001.
     |             https://stat.ethz.ch/~stahel/lognormal/bioscience.pdf
     |      .. [2] Reiss, R.D. and Thomas, M., "Statistical Analysis of Extreme
     |             Values," Basel: Birkhauser Verlag, 2001, pp. 31-32.
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> rng = np.random.default_rng()
     |      >>> mu, sigma = 3., 1. # mean and standard deviation
     |      >>> s = rng.lognormal(mu, sigma, 1000)
     |
     |      Display the histogram of the samples, along with
     |      the probability density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> count, bins, ignored = plt.hist(s, 100, density=True, align='mid')
     |
     |      >>> x = np.linspace(min(bins), max(bins), 10000)
     |      >>> pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
     |      ...        / (x * sigma * np.sqrt(2 * np.pi)))
     |
     |      >>> plt.plot(x, pdf, linewidth=2, color='r')
     |      >>> plt.axis('tight')
     |      >>> plt.show()
     |
     |      Demonstrate that taking the products of random samples from a uniform
     |      distribution can be fit well by a log-normal probability density
     |      function.
     |
     |      >>> # Generate a thousand samples: each is the product of 100 random
     |      >>> # values, drawn from a normal distribution.
     |      >>> rng = rng
     |      >>> b = []
     |      >>> for i in range(1000):
     |      ...    a = 10. + rng.standard_normal(100)
     |      ...    b.append(np.prod(a))
     |
     |      >>> b = np.array(b) / np.min(b) # scale values to be positive
     |      >>> count, bins, ignored = plt.hist(b, 100, density=True, align='mid')
     |      >>> sigma = np.std(np.log(b))
     |      >>> mu = np.mean(np.log(b))
     |
     |      >>> x = np.linspace(min(bins), max(bins), 10000)
     |      >>> pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
     |      ...        / (x * sigma * np.sqrt(2 * np.pi)))
     |
     |      >>> plt.plot(x, pdf, color='r', linewidth=2)
     |      >>> plt.show()
     |
     |  logseries(...)
     |      logseries(p, size=None)
     |
     |      Draw samples from a logarithmic series distribution.
     |
     |      Samples are drawn from a log series distribution with specified
     |      shape parameter, 0 <= ``p`` < 1.
     |
     |      Parameters
     |      ----------
     |      p : float or array_like of floats
     |          Shape parameter for the distribution.  Must be in the range [0, 1).
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``p`` is a scalar.  Otherwise,
     |          ``np.array(p).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized logarithmic series distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.logser : probability density function, distribution or
     |          cumulative density function, etc.
     |
     |      Notes
     |      -----
     |      The probability mass function for the Log Series distribution is
     |
     |      .. math:: P(k) = \frac{-p^k}{k \ln(1-p)},
     |
     |      where p = probability.
     |
     |      The log series distribution is frequently used to represent species
     |      richness and occurrence, first proposed by Fisher, Corbet, and
     |      Williams in 1943 [2].  It may also be used to model the numbers of
     |      occupants seen in cars [3].
     |
     |      References
     |      ----------
     |      .. [1] Buzas, Martin A.; Culver, Stephen J.,  Understanding regional
     |             species diversity through the log series distribution of
     |             occurrences: BIODIVERSITY RESEARCH Diversity & Distributions,
     |             Volume 5, Number 5, September 1999 , pp. 187-195(9).
     |      .. [2] Fisher, R.A,, A.S. Corbet, and C.B. Williams. 1943. The
     |             relation between the number of species and the number of
     |             individuals in a random sample of an animal population.
     |             Journal of Animal Ecology, 12:42-58.
     |      .. [3] D. J. Hand, F. Daly, D. Lunn, E. Ostrowski, A Handbook of Small
     |             Data Sets, CRC Press, 1994.
     |      .. [4] Wikipedia, "Logarithmic distribution",
     |             https://en.wikipedia.org/wiki/Logarithmic_distribution
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> a = .6
     |      >>> s = np.random.default_rng().logseries(a, 10000)
     |      >>> import matplotlib.pyplot as plt
     |      >>> count, bins, ignored = plt.hist(s)
     |
     |      #   plot against distribution
     |
     |      >>> def logseries(k, p):
     |      ...     return -p**k/(k*np.log(1-p))
     |      >>> plt.plot(bins, logseries(bins, a) * count.max()/
     |      ...          logseries(bins, a).max(), 'r')
     |      >>> plt.show()
     |
     |  multinomial(...)
     |      multinomial(n, pvals, size=None)
     |
     |      Draw samples from a multinomial distribution.
     |
     |      The multinomial distribution is a multivariate generalization of the
     |      binomial distribution.  Take an experiment with one of ``p``
     |      possible outcomes.  An example of such an experiment is throwing a dice,
     |      where the outcome can be 1 through 6.  Each sample drawn from the
     |      distribution represents `n` such experiments.  Its values,
     |      ``X_i = [X_0, X_1, ..., X_p]``, represent the number of times the
     |      outcome was ``i``.
     |
     |      Parameters
     |      ----------
     |      n : int or array-like of ints
     |          Number of experiments.
     |      pvals : array-like of floats
     |          Probabilities of each of the ``p`` different outcomes with shape
     |          ``(k0, k1, ..., kn, p)``. Each element ``pvals[i,j,...,:]`` must
     |          sum to 1 (however, the last element is always assumed to account
     |          for the remaining probability, as long as
     |          ``sum(pvals[..., :-1], axis=-1) <= 1.0``. Must have at least 1
     |          dimension where pvals.shape[-1] > 0.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn each with ``p`` elements. Default
     |          is None where the output size is determined by the broadcast shape
     |          of ``n`` and all by the final dimension of ``pvals``, which is
     |          denoted as ``b=(b0, b1, ..., bq)``. If size is not None, then it
     |          must be compatible with the broadcast shape ``b``. Specifically,
     |          size must have ``q`` or more elements and size[-(q-j):] must equal
     |          ``bj``.
     |
     |      Returns
     |      -------
     |      out : ndarray
     |          The drawn samples, of shape size, if provided. When size is
     |          provided, the output shape is size + (p,)  If not specified,
     |          the shape is determined by the broadcast shape of ``n`` and
     |          ``pvals``, ``(b0, b1, ..., bq)`` augmented with the dimension of
     |          the multinomial, ``p``, so that that output shape is
     |          ``(b0, b1, ..., bq, p)``.
     |
     |          Each entry ``out[i,j,...,:]`` is a ``p``-dimensional value drawn
     |          from the distribution.
     |
     |          .. versionchanged:: 1.22.0
     |              Added support for broadcasting `pvals` against `n`
     |
     |      Examples
     |      --------
     |      Throw a dice 20 times:
     |
     |      >>> rng = np.random.default_rng()
     |      >>> rng.multinomial(20, [1/6.]*6, size=1)
     |      array([[4, 1, 7, 5, 2, 1]])  # random
     |
     |      It landed 4 times on 1, once on 2, etc.
     |
     |      Now, throw the dice 20 times, and 20 times again:
     |
     |      >>> rng.multinomial(20, [1/6.]*6, size=2)
     |      array([[3, 4, 3, 3, 4, 3],
     |             [2, 4, 3, 4, 0, 7]])  # random
     |
     |      For the first run, we threw 3 times 1, 4 times 2, etc.  For the second,
     |      we threw 2 times 1, 4 times 2, etc.
     |
     |      Now, do one experiment throwing the dice 10 time, and 10 times again,
     |      and another throwing the dice 20 times, and 20 times again:
     |
     |      >>> rng.multinomial([[10], [20]], [1/6.]*6, size=(2, 2))
     |      array([[[2, 4, 0, 1, 2, 1],
     |              [1, 3, 0, 3, 1, 2]],
     |             [[1, 4, 4, 4, 4, 3],
     |              [3, 3, 2, 5, 5, 2]]])  # random
     |
     |      The first array shows the outcomes of throwing the dice 10 times, and
     |      the second shows the outcomes from throwing the dice 20 times.
     |
     |      A loaded die is more likely to land on number 6:
     |
     |      >>> rng.multinomial(100, [1/7.]*5 + [2/7.])
     |      array([11, 16, 14, 17, 16, 26])  # random
     |
     |      Simulate 10 throws of a 4-sided die and 20 throws of a 6-sided die
     |
     |      >>> rng.multinomial([10, 20],[[1/4]*4 + [0]*2, [1/6]*6])
     |      array([[2, 1, 4, 3, 0, 0],
     |             [3, 3, 3, 6, 1, 4]], dtype=int64)  # random
     |
     |      Generate categorical random variates from two categories where the
     |      first has 3 outcomes and the second has 2.
     |
     |      >>> rng.multinomial(1, [[.1, .5, .4 ], [.3, .7, .0]])
     |      array([[0, 0, 1],
     |             [0, 1, 0]], dtype=int64)  # random
     |
     |      ``argmax(axis=-1)`` is then used to return the categories.
     |
     |      >>> pvals = [[.1, .5, .4 ], [.3, .7, .0]]
     |      >>> rvs = rng.multinomial(1, pvals, size=(4,2))
     |      >>> rvs.argmax(axis=-1)
     |      array([[0, 1],
     |             [2, 0],
     |             [2, 1],
     |             [2, 0]], dtype=int64)  # random
     |
     |      The same output dimension can be produced using broadcasting.
     |
     |      >>> rvs = rng.multinomial([[1]] * 4, pvals)
     |      >>> rvs.argmax(axis=-1)
     |      array([[0, 1],
     |             [2, 0],
     |             [2, 1],
     |             [2, 0]], dtype=int64)  # random
     |
     |      The probability inputs should be normalized. As an implementation
     |      detail, the value of the last entry is ignored and assumed to take
     |      up any leftover probability mass, but this should not be relied on.
     |      A biased coin which has twice as much weight on one side as on the
     |      other should be sampled like so:
     |
     |      >>> rng.multinomial(100, [1.0 / 3, 2.0 / 3])  # RIGHT
     |      array([38, 62])  # random
     |
     |      not like:
     |
     |      >>> rng.multinomial(100, [1.0, 2.0])  # WRONG
     |      Traceback (most recent call last):
     |      ValueError: pvals < 0, pvals > 1 or pvals contains NaNs
     |
     |  multivariate_hypergeometric(...)
     |      multivariate_hypergeometric(colors, nsample, size=None,
     |                                  method='marginals')
     |
     |      Generate variates from a multivariate hypergeometric distribution.
     |
     |      The multivariate hypergeometric distribution is a generalization
     |      of the hypergeometric distribution.
     |
     |      Choose ``nsample`` items at random without replacement from a
     |      collection with ``N`` distinct types.  ``N`` is the length of
     |      ``colors``, and the values in ``colors`` are the number of occurrences
     |      of that type in the collection.  The total number of items in the
     |      collection is ``sum(colors)``.  Each random variate generated by this
     |      function is a vector of length ``N`` holding the counts of the
     |      different types that occurred in the ``nsample`` items.
     |
     |      The name ``colors`` comes from a common description of the
     |      distribution: it is the probability distribution of the number of
     |      marbles of each color selected without replacement from an urn
     |      containing marbles of different colors; ``colors[i]`` is the number
     |      of marbles in the urn with color ``i``.
     |
     |      Parameters
     |      ----------
     |      colors : sequence of integers
     |          The number of each type of item in the collection from which
     |          a sample is drawn.  The values in ``colors`` must be nonnegative.
     |          To avoid loss of precision in the algorithm, ``sum(colors)``
     |          must be less than ``10**9`` when `method` is "marginals".
     |      nsample : int
     |          The number of items selected.  ``nsample`` must not be greater
     |          than ``sum(colors)``.
     |      size : int or tuple of ints, optional
     |          The number of variates to generate, either an integer or a tuple
     |          holding the shape of the array of variates.  If the given size is,
     |          e.g., ``(k, m)``, then ``k * m`` variates are drawn, where one
     |          variate is a vector of length ``len(colors)``, and the return value
     |          has shape ``(k, m, len(colors))``.  If `size` is an integer, the
     |          output has shape ``(size, len(colors))``.  Default is None, in
     |          which case a single variate is returned as an array with shape
     |          ``(len(colors),)``.
     |      method : string, optional
     |          Specify the algorithm that is used to generate the variates.
     |          Must be 'count' or 'marginals' (the default).  See the Notes
     |          for a description of the methods.
     |
     |      Returns
     |      -------
     |      variates : ndarray
     |          Array of variates drawn from the multivariate hypergeometric
     |          distribution.
     |
     |      See Also
     |      --------
     |      hypergeometric : Draw samples from the (univariate) hypergeometric
     |          distribution.
     |
     |      Notes
     |      -----
     |      The two methods do not return the same sequence of variates.
     |
     |      The "count" algorithm is roughly equivalent to the following numpy
     |      code::
     |
     |          choices = np.repeat(np.arange(len(colors)), colors)
     |          selection = np.random.choice(choices, nsample, replace=False)
     |          variate = np.bincount(selection, minlength=len(colors))
     |
     |      The "count" algorithm uses a temporary array of integers with length
     |      ``sum(colors)``.
     |
     |      The "marginals" algorithm generates a variate by using repeated
     |      calls to the univariate hypergeometric sampler.  It is roughly
     |      equivalent to::
     |
     |          variate = np.zeros(len(colors), dtype=np.int64)
     |          # `remaining` is the cumulative sum of `colors` from the last
     |          # element to the first; e.g. if `colors` is [3, 1, 5], then
     |          # `remaining` is [9, 6, 5].
     |          remaining = np.cumsum(colors[::-1])[::-1]
     |          for i in range(len(colors)-1):
     |              if nsample < 1:
     |                  break
     |              variate[i] = hypergeometric(colors[i], remaining[i+1],
     |                                         nsample)
     |              nsample -= variate[i]
     |          variate[-1] = nsample
     |
     |      The default method is "marginals".  For some cases (e.g. when
     |      `colors` contains relatively small integers), the "count" method
     |      can be significantly faster than the "marginals" method.  If
     |      performance of the algorithm is important, test the two methods
     |      with typical inputs to decide which works best.
     |
     |      .. versionadded:: 1.18.0
     |
     |      Examples
     |      --------
     |      >>> colors = [16, 8, 4]
     |      >>> seed = 4861946401452
     |      >>> gen = np.random.Generator(np.random.PCG64(seed))
     |      >>> gen.multivariate_hypergeometric(colors, 6)
     |      array([5, 0, 1])
     |      >>> gen.multivariate_hypergeometric(colors, 6, size=3)
     |      array([[5, 0, 1],
     |             [2, 2, 2],
     |             [3, 3, 0]])
     |      >>> gen.multivariate_hypergeometric(colors, 6, size=(2, 2))
     |      array([[[3, 2, 1],
     |              [3, 2, 1]],
     |             [[4, 1, 1],
     |              [3, 2, 1]]])
     |
     |  multivariate_normal(...)
     |      multivariate_normal(mean, cov, size=None, check_valid='warn',
     |                          tol=1e-8, *, method='svd')
     |
     |      Draw random samples from a multivariate normal distribution.
     |
     |      The multivariate normal, multinormal or Gaussian distribution is a
     |      generalization of the one-dimensional normal distribution to higher
     |      dimensions.  Such a distribution is specified by its mean and
     |      covariance matrix.  These parameters are analogous to the mean
     |      (average or "center") and variance (the squared standard deviation,
     |      or "width") of the one-dimensional normal distribution.
     |
     |      Parameters
     |      ----------
     |      mean : 1-D array_like, of length N
     |          Mean of the N-dimensional distribution.
     |      cov : 2-D array_like, of shape (N, N)
     |          Covariance matrix of the distribution. It must be symmetric and
     |          positive-semidefinite for proper sampling.
     |      size : int or tuple of ints, optional
     |          Given a shape of, for example, ``(m,n,k)``, ``m*n*k`` samples are
     |          generated, and packed in an `m`-by-`n`-by-`k` arrangement.  Because
     |          each sample is `N`-dimensional, the output shape is ``(m,n,k,N)``.
     |          If no shape is specified, a single (`N`-D) sample is returned.
     |      check_valid : { 'warn', 'raise', 'ignore' }, optional
     |          Behavior when the covariance matrix is not positive semidefinite.
     |      tol : float, optional
     |          Tolerance when checking the singular values in covariance matrix.
     |          cov is cast to double before the check.
     |      method : { 'svd', 'eigh', 'cholesky'}, optional
     |          The cov input is used to compute a factor matrix A such that
     |          ``A @ A.T = cov``. This argument is used to select the method
     |          used to compute the factor matrix A. The default method 'svd' is
     |          the slowest, while 'cholesky' is the fastest but less robust than
     |          the slowest method. The method `eigh` uses eigen decomposition to
     |          compute A and is faster than svd but slower than cholesky.
     |
     |          .. versionadded:: 1.18.0
     |
     |      Returns
     |      -------
     |      out : ndarray
     |          The drawn samples, of shape *size*, if that was provided.  If not,
     |          the shape is ``(N,)``.
     |
     |          In other words, each entry ``out[i,j,...,:]`` is an N-dimensional
     |          value drawn from the distribution.
     |
     |      Notes
     |      -----
     |      The mean is a coordinate in N-dimensional space, which represents the
     |      location where samples are most likely to be generated.  This is
     |      analogous to the peak of the bell curve for the one-dimensional or
     |      univariate normal distribution.
     |
     |      Covariance indicates the level to which two variables vary together.
     |      From the multivariate normal distribution, we draw N-dimensional
     |      samples, :math:`X = [x_1, x_2, ... x_N]`.  The covariance matrix
     |      element :math:`C_{ij}` is the covariance of :math:`x_i` and :math:`x_j`.
     |      The element :math:`C_{ii}` is the variance of :math:`x_i` (i.e. its
     |      "spread").
     |
     |      Instead of specifying the full covariance matrix, popular
     |      approximations include:
     |
     |        - Spherical covariance (`cov` is a multiple of the identity matrix)
     |        - Diagonal covariance (`cov` has non-negative elements, and only on
     |          the diagonal)
     |
     |      This geometrical property can be seen in two dimensions by plotting
     |      generated data-points:
     |
     |      >>> mean = [0, 0]
     |      >>> cov = [[1, 0], [0, 100]]  # diagonal covariance
     |
     |      Diagonal covariance means that points are oriented along x or y-axis:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> x, y = np.random.default_rng().multivariate_normal(mean, cov, 5000).T
     |      >>> plt.plot(x, y, 'x')
     |      >>> plt.axis('equal')
     |      >>> plt.show()
     |
     |      Note that the covariance matrix must be positive semidefinite (a.k.a.
     |      nonnegative-definite). Otherwise, the behavior of this method is
     |      undefined and backwards compatibility is not guaranteed.
     |
     |      This function internally uses linear algebra routines, and thus results
     |      may not be identical (even up to precision) across architectures, OSes,
     |      or even builds. For example, this is likely if ``cov`` has multiple equal
     |      singular values and ``method`` is ``'svd'`` (default). In this case,
     |      ``method='cholesky'`` may be more robust.
     |
     |      References
     |      ----------
     |      .. [1] Papoulis, A., "Probability, Random Variables, and Stochastic
     |             Processes," 3rd ed., New York: McGraw-Hill, 1991.
     |      .. [2] Duda, R. O., Hart, P. E., and Stork, D. G., "Pattern
     |             Classification," 2nd ed., New York: Wiley, 2001.
     |
     |      Examples
     |      --------
     |      >>> mean = (1, 2)
     |      >>> cov = [[1, 0], [0, 1]]
     |      >>> rng = np.random.default_rng()
     |      >>> x = rng.multivariate_normal(mean, cov, (3, 3))
     |      >>> x.shape
     |      (3, 3, 2)
     |
     |      We can use a different method other than the default to factorize cov:
     |
     |      >>> y = rng.multivariate_normal(mean, cov, (3, 3), method='cholesky')
     |      >>> y.shape
     |      (3, 3, 2)
     |
     |      Here we generate 800 samples from the bivariate normal distribution
     |      with mean [0, 0] and covariance matrix [[6, -3], [-3, 3.5]].  The
     |      expected variances of the first and second components of the sample
     |      are 6 and 3.5, respectively, and the expected correlation
     |      coefficient is -3/sqrt(6*3.5) ≈ -0.65465.
     |
     |      >>> cov = np.array([[6, -3], [-3, 3.5]])
     |      >>> pts = rng.multivariate_normal([0, 0], cov, size=800)
     |
     |      Check that the mean, covariance, and correlation coefficient of the
     |      sample are close to the expected values:
     |
     |      >>> pts.mean(axis=0)
     |      array([ 0.0326911 , -0.01280782])  # may vary
     |      >>> np.cov(pts.T)
     |      array([[ 5.96202397, -2.85602287],
     |             [-2.85602287,  3.47613949]])  # may vary
     |      >>> np.corrcoef(pts.T)[0, 1]
     |      -0.6273591314603949  # may vary
     |
     |      We can visualize this data with a scatter plot.  The orientation
     |      of the point cloud illustrates the negative correlation of the
     |      components of this sample.
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> plt.plot(pts[:, 0], pts[:, 1], '.', alpha=0.5)
     |      >>> plt.axis('equal')
     |      >>> plt.grid()
     |      >>> plt.show()
     |
     |  negative_binomial(...)
     |      negative_binomial(n, p, size=None)
     |
     |      Draw samples from a negative binomial distribution.
     |
     |      Samples are drawn from a negative binomial distribution with specified
     |      parameters, `n` successes and `p` probability of success where `n`
     |      is > 0 and `p` is in the interval (0, 1].
     |
     |      Parameters
     |      ----------
     |      n : float or array_like of floats
     |          Parameter of the distribution, > 0.
     |      p : float or array_like of floats
     |          Parameter of the distribution. Must satisfy 0 < p <= 1.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``n`` and ``p`` are both scalars.
     |          Otherwise, ``np.broadcast(n, p).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized negative binomial distribution,
     |          where each sample is equal to N, the number of failures that
     |          occurred before a total of n successes was reached.
     |
     |      Notes
     |      -----
     |      The probability mass function of the negative binomial distribution is
     |
     |      .. math:: P(N;n,p) = \frac{\Gamma(N+n)}{N!\Gamma(n)}p^{n}(1-p)^{N},
     |
     |      where :math:`n` is the number of successes, :math:`p` is the
     |      probability of success, :math:`N+n` is the number of trials, and
     |      :math:`\Gamma` is the gamma function. When :math:`n` is an integer,
     |      :math:`\frac{\Gamma(N+n)}{N!\Gamma(n)} = \binom{N+n-1}{N}`, which is
     |      the more common form of this term in the pmf. The negative
     |      binomial distribution gives the probability of N failures given n
     |      successes, with a success on the last trial.
     |
     |      If one throws a die repeatedly until the third time a "1" appears,
     |      then the probability distribution of the number of non-"1"s that
     |      appear before the third "1" is a negative binomial distribution.
     |
     |      Because this method internally calls ``Generator.poisson`` with an
     |      intermediate random value, a ValueError is raised when the choice of
     |      :math:`n` and :math:`p` would result in the mean + 10 sigma of the sampled
     |      intermediate distribution exceeding the max acceptable value of the
     |      ``Generator.poisson`` method. This happens when :math:`p` is too low
     |      (a lot of failures happen for every success) and :math:`n` is too big (
     |      a lot of successes are allowed).
     |      Therefore, the :math:`n` and :math:`p` values must satisfy the constraint:
     |
     |      .. math:: n\frac{1-p}{p}+10n\sqrt{n}\frac{1-p}{p}<2^{63}-1-10\sqrt{2^{63}-1},
     |
     |      Where the left side of the equation is the derived mean + 10 sigma of
     |      a sample from the gamma distribution internally used as the :math:`lam`
     |      parameter of a poisson sample, and the right side of the equation is
     |      the constraint for maximum value of :math:`lam` in ``Generator.poisson``.
     |
     |      References
     |      ----------
     |      .. [1] Weisstein, Eric W. "Negative Binomial Distribution." From
     |             MathWorld--A Wolfram Web Resource.
     |             http://mathworld.wolfram.com/NegativeBinomialDistribution.html
     |      .. [2] Wikipedia, "Negative binomial distribution",
     |             https://en.wikipedia.org/wiki/Negative_binomial_distribution
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      A real world example. A company drills wild-cat oil
     |      exploration wells, each with an estimated probability of
     |      success of 0.1.  What is the probability of having one success
     |      for each successive well, that is what is the probability of a
     |      single success after drilling 5 wells, after 6 wells, etc.?
     |
     |      >>> s = np.random.default_rng().negative_binomial(1, 0.1, 100000)
     |      >>> for i in range(1, 11): # doctest: +SKIP
     |      ...    probability = sum(s<i) / 100000.
     |      ...    print(i, "wells drilled, probability of one success =", probability)
     |
     |  noncentral_chisquare(...)
     |      noncentral_chisquare(df, nonc, size=None)
     |
     |      Draw samples from a noncentral chi-square distribution.
     |
     |      The noncentral :math:`\chi^2` distribution is a generalization of
     |      the :math:`\chi^2` distribution.
     |
     |      Parameters
     |      ----------
     |      df : float or array_like of floats
     |          Degrees of freedom, must be > 0.
     |
     |          .. versionchanged:: 1.10.0
     |             Earlier NumPy versions required dfnum > 1.
     |      nonc : float or array_like of floats
     |          Non-centrality, must be non-negative.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``df`` and ``nonc`` are both scalars.
     |          Otherwise, ``np.broadcast(df, nonc).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized noncentral chi-square distribution.
     |
     |      Notes
     |      -----
     |      The probability density function for the noncentral Chi-square
     |      distribution is
     |
     |      .. math:: P(x;df,nonc) = \sum^{\infty}_{i=0}
     |                             \frac{e^{-nonc/2}(nonc/2)^{i}}{i!}
     |                             P_{Y_{df+2i}}(x),
     |
     |      where :math:`Y_{q}` is the Chi-square with q degrees of freedom.
     |
     |      References
     |      ----------
     |      .. [1] Wikipedia, "Noncentral chi-squared distribution"
     |             https://en.wikipedia.org/wiki/Noncentral_chi-squared_distribution
     |
     |      Examples
     |      --------
     |      Draw values from the distribution and plot the histogram
     |
     |      >>> rng = np.random.default_rng()
     |      >>> import matplotlib.pyplot as plt
     |      >>> values = plt.hist(rng.noncentral_chisquare(3, 20, 100000),
     |      ...                   bins=200, density=True)
     |      >>> plt.show()
     |
     |      Draw values from a noncentral chisquare with very small noncentrality,
     |      and compare to a chisquare.
     |
     |      >>> plt.figure()
     |      >>> values = plt.hist(rng.noncentral_chisquare(3, .0000001, 100000),
     |      ...                   bins=np.arange(0., 25, .1), density=True)
     |      >>> values2 = plt.hist(rng.chisquare(3, 100000),
     |      ...                    bins=np.arange(0., 25, .1), density=True)
     |      >>> plt.plot(values[1][0:-1], values[0]-values2[0], 'ob')
     |      >>> plt.show()
     |
     |      Demonstrate how large values of non-centrality lead to a more symmetric
     |      distribution.
     |
     |      >>> plt.figure()
     |      >>> values = plt.hist(rng.noncentral_chisquare(3, 20, 100000),
     |      ...                   bins=200, density=True)
     |      >>> plt.show()
     |
     |  noncentral_f(...)
     |      noncentral_f(dfnum, dfden, nonc, size=None)
     |
     |      Draw samples from the noncentral F distribution.
     |
     |      Samples are drawn from an F distribution with specified parameters,
     |      `dfnum` (degrees of freedom in numerator) and `dfden` (degrees of
     |      freedom in denominator), where both parameters > 1.
     |      `nonc` is the non-centrality parameter.
     |
     |      Parameters
     |      ----------
     |      dfnum : float or array_like of floats
     |          Numerator degrees of freedom, must be > 0.
     |
     |          .. versionchanged:: 1.14.0
     |             Earlier NumPy versions required dfnum > 1.
     |      dfden : float or array_like of floats
     |          Denominator degrees of freedom, must be > 0.
     |      nonc : float or array_like of floats
     |          Non-centrality parameter, the sum of the squares of the numerator
     |          means, must be >= 0.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``dfnum``, ``dfden``, and ``nonc``
     |          are all scalars.  Otherwise, ``np.broadcast(dfnum, dfden, nonc).size``
     |          samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized noncentral Fisher distribution.
     |
     |      Notes
     |      -----
     |      When calculating the power of an experiment (power = probability of
     |      rejecting the null hypothesis when a specific alternative is true) the
     |      non-central F statistic becomes important.  When the null hypothesis is
     |      true, the F statistic follows a central F distribution. When the null
     |      hypothesis is not true, then it follows a non-central F statistic.
     |
     |      References
     |      ----------
     |      .. [1] Weisstein, Eric W. "Noncentral F-Distribution."
     |             From MathWorld--A Wolfram Web Resource.
     |             http://mathworld.wolfram.com/NoncentralF-Distribution.html
     |      .. [2] Wikipedia, "Noncentral F-distribution",
     |             https://en.wikipedia.org/wiki/Noncentral_F-distribution
     |
     |      Examples
     |      --------
     |      In a study, testing for a specific alternative to the null hypothesis
     |      requires use of the Noncentral F distribution. We need to calculate the
     |      area in the tail of the distribution that exceeds the value of the F
     |      distribution for the null hypothesis.  We'll plot the two probability
     |      distributions for comparison.
     |
     |      >>> rng = np.random.default_rng()
     |      >>> dfnum = 3 # between group deg of freedom
     |      >>> dfden = 20 # within groups degrees of freedom
     |      >>> nonc = 3.0
     |      >>> nc_vals = rng.noncentral_f(dfnum, dfden, nonc, 1000000)
     |      >>> NF = np.histogram(nc_vals, bins=50, density=True)
     |      >>> c_vals = rng.f(dfnum, dfden, 1000000)
     |      >>> F = np.histogram(c_vals, bins=50, density=True)
     |      >>> import matplotlib.pyplot as plt
     |      >>> plt.plot(F[1][1:], F[0])
     |      >>> plt.plot(NF[1][1:], NF[0])
     |      >>> plt.show()
     |
     |  normal(...)
     |      normal(loc=0.0, scale=1.0, size=None)
     |
     |      Draw random samples from a normal (Gaussian) distribution.
     |
     |      The probability density function of the normal distribution, first
     |      derived by De Moivre and 200 years later by both Gauss and Laplace
     |      independently [2]_, is often called the bell curve because of
     |      its characteristic shape (see the example below).
     |
     |      The normal distributions occurs often in nature.  For example, it
     |      describes the commonly occurring distribution of samples influenced
     |      by a large number of tiny, random disturbances, each with its own
     |      unique distribution [2]_.
     |
     |      Parameters
     |      ----------
     |      loc : float or array_like of floats
     |          Mean ("centre") of the distribution.
     |      scale : float or array_like of floats
     |          Standard deviation (spread or "width") of the distribution. Must be
     |          non-negative.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``loc`` and ``scale`` are both scalars.
     |          Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized normal distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.norm : probability density function, distribution or
     |          cumulative density function, etc.
     |
     |      Notes
     |      -----
     |      The probability density for the Gaussian distribution is
     |
     |      .. math:: p(x) = \frac{1}{\sqrt{ 2 \pi \sigma^2 }}
     |                       e^{ - \frac{ (x - \mu)^2 } {2 \sigma^2} },
     |
     |      where :math:`\mu` is the mean and :math:`\sigma` the standard
     |      deviation. The square of the standard deviation, :math:`\sigma^2`,
     |      is called the variance.
     |
     |      The function has its peak at the mean, and its "spread" increases with
     |      the standard deviation (the function reaches 0.607 times its maximum at
     |      :math:`x + \sigma` and :math:`x - \sigma` [2]_).  This implies that
     |      :meth:`normal` is more likely to return samples lying close to the
     |      mean, rather than those far away.
     |
     |      References
     |      ----------
     |      .. [1] Wikipedia, "Normal distribution",
     |             https://en.wikipedia.org/wiki/Normal_distribution
     |      .. [2] P. R. Peebles Jr., "Central Limit Theorem" in "Probability,
     |             Random Variables and Random Signal Principles", 4th ed., 2001,
     |             pp. 51, 51, 125.
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> mu, sigma = 0, 0.1 # mean and standard deviation
     |      >>> s = np.random.default_rng().normal(mu, sigma, 1000)
     |
     |      Verify the mean and the variance:
     |
     |      >>> abs(mu - np.mean(s))
     |      0.0  # may vary
     |
     |      >>> abs(sigma - np.std(s, ddof=1))
     |      0.0  # may vary
     |
     |      Display the histogram of the samples, along with
     |      the probability density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> count, bins, ignored = plt.hist(s, 30, density=True)
     |      >>> plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
     |      ...                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
     |      ...          linewidth=2, color='r')
     |      >>> plt.show()
     |
     |      Two-by-four array of samples from the normal distribution with
     |      mean 3 and standard deviation 2.5:
     |
     |      >>> np.random.default_rng().normal(3, 2.5, size=(2, 4))
     |      array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random
     |             [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random
     |
     |  pareto(...)
     |      pareto(a, size=None)
     |
     |      Draw samples from a Pareto II or Lomax distribution with
     |      specified shape.
     |
     |      The Lomax or Pareto II distribution is a shifted Pareto
     |      distribution. The classical Pareto distribution can be
     |      obtained from the Lomax distribution by adding 1 and
     |      multiplying by the scale parameter ``m`` (see Notes).  The
     |      smallest value of the Lomax distribution is zero while for the
     |      classical Pareto distribution it is ``mu``, where the standard
     |      Pareto distribution has location ``mu = 1``.  Lomax can also
     |      be considered as a simplified version of the Generalized
     |      Pareto distribution (available in SciPy), with the scale set
     |      to one and the location set to zero.
     |
     |      The Pareto distribution must be greater than zero, and is
     |      unbounded above.  It is also known as the "80-20 rule".  In
     |      this distribution, 80 percent of the weights are in the lowest
     |      20 percent of the range, while the other 20 percent fill the
     |      remaining 80 percent of the range.
     |
     |      Parameters
     |      ----------
     |      a : float or array_like of floats
     |          Shape of the distribution. Must be positive.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``a`` is a scalar.  Otherwise,
     |          ``np.array(a).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized Pareto distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.lomax : probability density function, distribution or
     |          cumulative density function, etc.
     |      scipy.stats.genpareto : probability density function, distribution or
     |          cumulative density function, etc.
     |
     |      Notes
     |      -----
     |      The probability density for the Pareto distribution is
     |
     |      .. math:: p(x) = \frac{am^a}{x^{a+1}}
     |
     |      where :math:`a` is the shape and :math:`m` the scale.
     |
     |      The Pareto distribution, named after the Italian economist
     |      Vilfredo Pareto, is a power law probability distribution
     |      useful in many real world problems.  Outside the field of
     |      economics it is generally referred to as the Bradford
     |      distribution. Pareto developed the distribution to describe
     |      the distribution of wealth in an economy.  It has also found
     |      use in insurance, web page access statistics, oil field sizes,
     |      and many other problems, including the download frequency for
     |      projects in Sourceforge [1]_.  It is one of the so-called
     |      "fat-tailed" distributions.
     |
     |
     |      References
     |      ----------
     |      .. [1] Francis Hunt and Paul Johnson, On the Pareto Distribution of
     |             Sourceforge projects.
     |      .. [2] Pareto, V. (1896). Course of Political Economy. Lausanne.
     |      .. [3] Reiss, R.D., Thomas, M.(2001), Statistical Analysis of Extreme
     |             Values, Birkhauser Verlag, Basel, pp 23-30.
     |      .. [4] Wikipedia, "Pareto distribution",
     |             https://en.wikipedia.org/wiki/Pareto_distribution
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> a, m = 3., 2.  # shape and mode
     |      >>> s = (np.random.default_rng().pareto(a, 1000) + 1) * m
     |
     |      Display the histogram of the samples, along with the probability
     |      density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> count, bins, _ = plt.hist(s, 100, density=True)
     |      >>> fit = a*m**a / bins**(a+1)
     |      >>> plt.plot(bins, max(count)*fit/max(fit), linewidth=2, color='r')
     |      >>> plt.show()
     |
     |  permutation(...)
     |      permutation(x, axis=0)
     |
     |      Randomly permute a sequence, or return a permuted range.
     |
     |      Parameters
     |      ----------
     |      x : int or array_like
     |          If `x` is an integer, randomly permute ``np.arange(x)``.
     |          If `x` is an array, make a copy and shuffle the elements
     |          randomly.
     |      axis : int, optional
     |          The axis which `x` is shuffled along. Default is 0.
     |
     |      Returns
     |      -------
     |      out : ndarray
     |          Permuted sequence or array range.
     |
     |      Examples
     |      --------
     |      >>> rng = np.random.default_rng()
     |      >>> rng.permutation(10)
     |      array([1, 7, 4, 3, 0, 9, 2, 5, 8, 6]) # random
     |
     |      >>> rng.permutation([1, 4, 9, 12, 15])
     |      array([15,  1,  9,  4, 12]) # random
     |
     |      >>> arr = np.arange(9).reshape((3, 3))
     |      >>> rng.permutation(arr)
     |      array([[6, 7, 8], # random
     |             [0, 1, 2],
     |             [3, 4, 5]])
     |
     |      >>> rng.permutation("abc")
     |      Traceback (most recent call last):
     |          ...
     |      numpy.exceptions.AxisError: axis 0 is out of bounds for array of dimension 0
     |
     |      >>> arr = np.arange(9).reshape((3, 3))
     |      >>> rng.permutation(arr, axis=1)
     |      array([[0, 2, 1], # random
     |             [3, 5, 4],
     |             [6, 8, 7]])
     |
     |  permuted(...)
     |      permuted(x, axis=None, out=None)
     |
     |      Randomly permute `x` along axis `axis`.
     |
     |      Unlike `shuffle`, each slice along the given axis is shuffled
     |      independently of the others.
     |
     |      Parameters
     |      ----------
     |      x : array_like, at least one-dimensional
     |          Array to be shuffled.
     |      axis : int, optional
     |          Slices of `x` in this axis are shuffled. Each slice
     |          is shuffled independently of the others.  If `axis` is
     |          None, the flattened array is shuffled.
     |      out : ndarray, optional
     |          If given, this is the destination of the shuffled array.
     |          If `out` is None, a shuffled copy of the array is returned.
     |
     |      Returns
     |      -------
     |      ndarray
     |          If `out` is None, a shuffled copy of `x` is returned.
     |          Otherwise, the shuffled array is stored in `out`,
     |          and `out` is returned
     |
     |      See Also
     |      --------
     |      shuffle
     |      permutation
     |
     |      Notes
     |      -----
     |      An important distinction between methods ``shuffle``  and ``permuted`` is
     |      how they both treat the ``axis`` parameter which can be found at
     |      :ref:`generator-handling-axis-parameter`.
     |
     |      Examples
     |      --------
     |      Create a `numpy.random.Generator` instance:
     |
     |      >>> rng = np.random.default_rng()
     |
     |      Create a test array:
     |
     |      >>> x = np.arange(24).reshape(3, 8)
     |      >>> x
     |      array([[ 0,  1,  2,  3,  4,  5,  6,  7],
     |             [ 8,  9, 10, 11, 12, 13, 14, 15],
     |             [16, 17, 18, 19, 20, 21, 22, 23]])
     |
     |      Shuffle the rows of `x`:
     |
     |      >>> y = rng.permuted(x, axis=1)
     |      >>> y
     |      array([[ 4,  3,  6,  7,  1,  2,  5,  0],  # random
     |             [15, 10, 14,  9, 12, 11,  8, 13],
     |             [17, 16, 20, 21, 18, 22, 23, 19]])
     |
     |      `x` has not been modified:
     |
     |      >>> x
     |      array([[ 0,  1,  2,  3,  4,  5,  6,  7],
     |             [ 8,  9, 10, 11, 12, 13, 14, 15],
     |             [16, 17, 18, 19, 20, 21, 22, 23]])
     |
     |      To shuffle the rows of `x` in-place, pass `x` as the `out`
     |      parameter:
     |
     |      >>> y = rng.permuted(x, axis=1, out=x)
     |      >>> x
     |      array([[ 3,  0,  4,  7,  1,  6,  2,  5],  # random
     |             [ 8, 14, 13,  9, 12, 11, 15, 10],
     |             [17, 18, 16, 22, 19, 23, 20, 21]])
     |
     |      Note that when the ``out`` parameter is given, the return
     |      value is ``out``:
     |
     |      >>> y is x
     |      True
     |
     |  poisson(...)
     |      poisson(lam=1.0, size=None)
     |
     |      Draw samples from a Poisson distribution.
     |
     |      The Poisson distribution is the limit of the binomial distribution
     |      for large N.
     |
     |      Parameters
     |      ----------
     |      lam : float or array_like of floats
     |          Expected number of events occurring in a fixed-time interval,
     |          must be >= 0. A sequence must be broadcastable over the requested
     |          size.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``lam`` is a scalar. Otherwise,
     |          ``np.array(lam).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized Poisson distribution.
     |
     |      Notes
     |      -----
     |      The Poisson distribution
     |
     |      .. math:: f(k; \lambda)=\frac{\lambda^k e^{-\lambda}}{k!}
     |
     |      For events with an expected separation :math:`\lambda` the Poisson
     |      distribution :math:`f(k; \lambda)` describes the probability of
     |      :math:`k` events occurring within the observed
     |      interval :math:`\lambda`.
     |
     |      Because the output is limited to the range of the C int64 type, a
     |      ValueError is raised when `lam` is within 10 sigma of the maximum
     |      representable value.
     |
     |      References
     |      ----------
     |      .. [1] Weisstein, Eric W. "Poisson Distribution."
     |             From MathWorld--A Wolfram Web Resource.
     |             http://mathworld.wolfram.com/PoissonDistribution.html
     |      .. [2] Wikipedia, "Poisson distribution",
     |             https://en.wikipedia.org/wiki/Poisson_distribution
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> import numpy as np
     |      >>> rng = np.random.default_rng()
     |      >>> s = rng.poisson(5, 10000)
     |
     |      Display histogram of the sample:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> count, bins, ignored = plt.hist(s, 14, density=True)
     |      >>> plt.show()
     |
     |      Draw each 100 values for lambda 100 and 500:
     |
     |      >>> s = rng.poisson(lam=(100., 500.), size=(100, 2))
     |
     |  power(...)
     |      power(a, size=None)
     |
     |      Draws samples in [0, 1] from a power distribution with positive
     |      exponent a - 1.
     |
     |      Also known as the power function distribution.
     |
     |      Parameters
     |      ----------
     |      a : float or array_like of floats
     |          Parameter of the distribution. Must be non-negative.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``a`` is a scalar.  Otherwise,
     |          ``np.array(a).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized power distribution.
     |
     |      Raises
     |      ------
     |      ValueError
     |          If a <= 0.
     |
     |      Notes
     |      -----
     |      The probability density function is
     |
     |      .. math:: P(x; a) = ax^{a-1}, 0 \le x \le 1, a>0.
     |
     |      The power function distribution is just the inverse of the Pareto
     |      distribution. It may also be seen as a special case of the Beta
     |      distribution.
     |
     |      It is used, for example, in modeling the over-reporting of insurance
     |      claims.
     |
     |      References
     |      ----------
     |      .. [1] Christian Kleiber, Samuel Kotz, "Statistical size distributions
     |             in economics and actuarial sciences", Wiley, 2003.
     |      .. [2] Heckert, N. A. and Filliben, James J. "NIST Handbook 148:
     |             Dataplot Reference Manual, Volume 2: Let Subcommands and Library
     |             Functions", National Institute of Standards and Technology
     |             Handbook Series, June 2003.
     |             https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/powpdf.pdf
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> rng = np.random.default_rng()
     |      >>> a = 5. # shape
     |      >>> samples = 1000
     |      >>> s = rng.power(a, samples)
     |
     |      Display the histogram of the samples, along with
     |      the probability density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> count, bins, ignored = plt.hist(s, bins=30)
     |      >>> x = np.linspace(0, 1, 100)
     |      >>> y = a*x**(a-1.)
     |      >>> normed_y = samples*np.diff(bins)[0]*y
     |      >>> plt.plot(x, normed_y)
     |      >>> plt.show()
     |
     |      Compare the power function distribution to the inverse of the Pareto.
     |
     |      >>> from scipy import stats  # doctest: +SKIP
     |      >>> rvs = rng.power(5, 1000000)
     |      >>> rvsp = rng.pareto(5, 1000000)
     |      >>> xx = np.linspace(0,1,100)
     |      >>> powpdf = stats.powerlaw.pdf(xx,5)  # doctest: +SKIP
     |
     |      >>> plt.figure()
     |      >>> plt.hist(rvs, bins=50, density=True)
     |      >>> plt.plot(xx,powpdf,'r-')  # doctest: +SKIP
     |      >>> plt.title('power(5)')
     |
     |      >>> plt.figure()
     |      >>> plt.hist(1./(1.+rvsp), bins=50, density=True)
     |      >>> plt.plot(xx,powpdf,'r-')  # doctest: +SKIP
     |      >>> plt.title('inverse of 1 + Generator.pareto(5)')
     |
     |      >>> plt.figure()
     |      >>> plt.hist(1./(1.+rvsp), bins=50, density=True)
     |      >>> plt.plot(xx,powpdf,'r-')  # doctest: +SKIP
     |      >>> plt.title('inverse of stats.pareto(5)')
     |
     |  random(...)
     |      random(size=None, dtype=np.float64, out=None)
     |
     |      Return random floats in the half-open interval [0.0, 1.0).
     |
     |      Results are from the "continuous uniform" distribution over the
     |      stated interval.  To sample :math:`Unif[a, b), b > a` use `uniform`
     |      or multiply the output of `random` by ``(b - a)`` and add ``a``::
     |
     |          (b - a) * random() + a
     |
     |      Parameters
     |      ----------
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  Default is None, in which case a
     |          single value is returned.
     |      dtype : dtype, optional
     |          Desired dtype of the result, only `float64` and `float32` are supported.
     |          Byteorder must be native. The default value is np.float64.
     |      out : ndarray, optional
     |          Alternative output array in which to place the result. If size is not None,
     |          it must have the same shape as the provided size and must match the type of
     |          the output values.
     |
     |      Returns
     |      -------
     |      out : float or ndarray of floats
     |          Array of random floats of shape `size` (unless ``size=None``, in which
     |          case a single float is returned).
     |
     |      See Also
     |      --------
     |      uniform : Draw samples from the parameterized uniform distribution.
     |
     |      Examples
     |      --------
     |      >>> rng = np.random.default_rng()
     |      >>> rng.random()
     |      0.47108547995356098 # random
     |      >>> type(rng.random())
     |      <class 'float'>
     |      >>> rng.random((5,))
     |      array([ 0.30220482,  0.86820401,  0.1654503 ,  0.11659149,  0.54323428]) # random
     |
     |      Three-by-two array of random numbers from [-5, 0):
     |
     |      >>> 5 * rng.random((3, 2)) - 5
     |      array([[-3.99149989, -0.52338984], # random
     |             [-2.99091858, -0.79479508],
     |             [-1.23204345, -1.75224494]])
     |
     |  rayleigh(...)
     |      rayleigh(scale=1.0, size=None)
     |
     |      Draw samples from a Rayleigh distribution.
     |
     |      The :math:`\chi` and Weibull distributions are generalizations of the
     |      Rayleigh.
     |
     |      Parameters
     |      ----------
     |      scale : float or array_like of floats, optional
     |          Scale, also equals the mode. Must be non-negative. Default is 1.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``scale`` is a scalar.  Otherwise,
     |          ``np.array(scale).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized Rayleigh distribution.
     |
     |      Notes
     |      -----
     |      The probability density function for the Rayleigh distribution is
     |
     |      .. math:: P(x;scale) = \frac{x}{scale^2}e^{\frac{-x^2}{2 \cdotp scale^2}}
     |
     |      The Rayleigh distribution would arise, for example, if the East
     |      and North components of the wind velocity had identical zero-mean
     |      Gaussian distributions.  Then the wind speed would have a Rayleigh
     |      distribution.
     |
     |      References
     |      ----------
     |      .. [1] Brighton Webs Ltd., "Rayleigh Distribution,"
     |             https://web.archive.org/web/20090514091424/http://brighton-webs.co.uk:80/distributions/rayleigh.asp
     |      .. [2] Wikipedia, "Rayleigh distribution"
     |             https://en.wikipedia.org/wiki/Rayleigh_distribution
     |
     |      Examples
     |      --------
     |      Draw values from the distribution and plot the histogram
     |
     |      >>> from matplotlib.pyplot import hist
     |      >>> rng = np.random.default_rng()
     |      >>> values = hist(rng.rayleigh(3, 100000), bins=200, density=True)
     |
     |      Wave heights tend to follow a Rayleigh distribution. If the mean wave
     |      height is 1 meter, what fraction of waves are likely to be larger than 3
     |      meters?
     |
     |      >>> meanvalue = 1
     |      >>> modevalue = np.sqrt(2 / np.pi) * meanvalue
     |      >>> s = rng.rayleigh(modevalue, 1000000)
     |
     |      The percentage of waves larger than 3 meters is:
     |
     |      >>> 100.*sum(s>3)/1000000.
     |      0.087300000000000003 # random
     |
     |  shuffle(...)
     |      shuffle(x, axis=0)
     |
     |      Modify an array or sequence in-place by shuffling its contents.
     |
     |      The order of sub-arrays is changed but their contents remains the same.
     |
     |      Parameters
     |      ----------
     |      x : ndarray or MutableSequence
     |          The array, list or mutable sequence to be shuffled.
     |      axis : int, optional
     |          The axis which `x` is shuffled along. Default is 0.
     |          It is only supported on `ndarray` objects.
     |
     |      Returns
     |      -------
     |      None
     |
     |      See Also
     |      --------
     |      permuted
     |      permutation
     |
     |      Notes
     |      -----
     |      An important distinction between methods ``shuffle``  and ``permuted`` is
     |      how they both treat the ``axis`` parameter which can be found at
     |      :ref:`generator-handling-axis-parameter`.
     |
     |      Examples
     |      --------
     |      >>> rng = np.random.default_rng()
     |      >>> arr = np.arange(10)
     |      >>> arr
     |      array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
     |      >>> rng.shuffle(arr)
     |      >>> arr
     |      array([2, 0, 7, 5, 1, 4, 8, 9, 3, 6]) # random
     |
     |      >>> arr = np.arange(9).reshape((3, 3))
     |      >>> arr
     |      array([[0, 1, 2],
     |             [3, 4, 5],
     |             [6, 7, 8]])
     |      >>> rng.shuffle(arr)
     |      >>> arr
     |      array([[3, 4, 5], # random
     |             [6, 7, 8],
     |             [0, 1, 2]])
     |
     |      >>> arr = np.arange(9).reshape((3, 3))
     |      >>> arr
     |      array([[0, 1, 2],
     |             [3, 4, 5],
     |             [6, 7, 8]])
     |      >>> rng.shuffle(arr, axis=1)
     |      >>> arr
     |      array([[2, 0, 1], # random
     |             [5, 3, 4],
     |             [8, 6, 7]])
     |
     |  spawn(...)
     |      spawn(n_children)
     |
     |      Create new independent child generators.
     |
     |      See :ref:`seedsequence-spawn` for additional notes on spawning
     |      children.
     |
     |      .. versionadded:: 1.25.0
     |
     |      Parameters
     |      ----------
     |      n_children : int
     |
     |      Returns
     |      -------
     |      child_generators : list of Generators
     |
     |      Raises
     |      ------
     |      TypeError
     |          When the underlying SeedSequence does not implement spawning.
     |
     |      See Also
     |      --------
     |      random.BitGenerator.spawn, random.SeedSequence.spawn :
     |          Equivalent method on the bit generator and seed sequence.
     |      bit_generator :
     |          The bit generator instance used by the generator.
     |
     |      Examples
     |      --------
     |      Starting from a seeded default generator:
     |
     |      >>> # High quality entropy created with: f"0x{secrets.randbits(128):x}"
     |      >>> entropy = 0x3034c61a9ae04ff8cb62ab8ec2c4b501
     |      >>> rng = np.random.default_rng(entropy)
     |
     |      Create two new generators for example for parallel execution:
     |
     |      >>> child_rng1, child_rng2 = rng.spawn(2)
     |
     |      Drawn numbers from each are independent but derived from the initial
     |      seeding entropy:
     |
     |      >>> rng.uniform(), child_rng1.uniform(), child_rng2.uniform()
     |      (0.19029263503854454, 0.9475673279178444, 0.4702687338396767)
     |
     |      It is safe to spawn additional children from the original ``rng`` or
     |      the children:
     |
     |      >>> more_child_rngs = rng.spawn(20)
     |      >>> nested_spawn = child_rng1.spawn(20)
     |
     |  standard_cauchy(...)
     |      standard_cauchy(size=None)
     |
     |      Draw samples from a standard Cauchy distribution with mode = 0.
     |
     |      Also known as the Lorentz distribution.
     |
     |      Parameters
     |      ----------
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  Default is None, in which case a
     |          single value is returned.
     |
     |      Returns
     |      -------
     |      samples : ndarray or scalar
     |          The drawn samples.
     |
     |      Notes
     |      -----
     |      The probability density function for the full Cauchy distribution is
     |
     |      .. math:: P(x; x_0, \gamma) = \frac{1}{\pi \gamma \bigl[ 1+
     |                (\frac{x-x_0}{\gamma})^2 \bigr] }
     |
     |      and the Standard Cauchy distribution just sets :math:`x_0=0` and
     |      :math:`\gamma=1`
     |
     |      The Cauchy distribution arises in the solution to the driven harmonic
     |      oscillator problem, and also describes spectral line broadening. It
     |      also describes the distribution of values at which a line tilted at
     |      a random angle will cut the x axis.
     |
     |      When studying hypothesis tests that assume normality, seeing how the
     |      tests perform on data from a Cauchy distribution is a good indicator of
     |      their sensitivity to a heavy-tailed distribution, since the Cauchy looks
     |      very much like a Gaussian distribution, but with heavier tails.
     |
     |      References
     |      ----------
     |      .. [1] NIST/SEMATECH e-Handbook of Statistical Methods, "Cauchy
     |            Distribution",
     |            https://www.itl.nist.gov/div898/handbook/eda/section3/eda3663.htm
     |      .. [2] Weisstein, Eric W. "Cauchy Distribution." From MathWorld--A
     |            Wolfram Web Resource.
     |            http://mathworld.wolfram.com/CauchyDistribution.html
     |      .. [3] Wikipedia, "Cauchy distribution"
     |            https://en.wikipedia.org/wiki/Cauchy_distribution
     |
     |      Examples
     |      --------
     |      Draw samples and plot the distribution:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> s = np.random.default_rng().standard_cauchy(1000000)
     |      >>> s = s[(s>-25) & (s<25)]  # truncate distribution so it plots well
     |      >>> plt.hist(s, bins=100)
     |      >>> plt.show()
     |
     |  standard_exponential(...)
     |      standard_exponential(size=None, dtype=np.float64, method='zig', out=None)
     |
     |      Draw samples from the standard exponential distribution.
     |
     |      `standard_exponential` is identical to the exponential distribution
     |      with a scale parameter of 1.
     |
     |      Parameters
     |      ----------
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  Default is None, in which case a
     |          single value is returned.
     |      dtype : dtype, optional
     |          Desired dtype of the result, only `float64` and `float32` are supported.
     |          Byteorder must be native. The default value is np.float64.
     |      method : str, optional
     |          Either 'inv' or 'zig'. 'inv' uses the default inverse CDF method.
     |          'zig' uses the much faster Ziggurat method of Marsaglia and Tsang.
     |      out : ndarray, optional
     |          Alternative output array in which to place the result. If size is not None,
     |          it must have the same shape as the provided size and must match the type of
     |          the output values.
     |
     |      Returns
     |      -------
     |      out : float or ndarray
     |          Drawn samples.
     |
     |      Examples
     |      --------
     |      Output a 3x8000 array:
     |
     |      >>> n = np.random.default_rng().standard_exponential((3, 8000))
     |
     |  standard_gamma(...)
     |      standard_gamma(shape, size=None, dtype=np.float64, out=None)
     |
     |      Draw samples from a standard Gamma distribution.
     |
     |      Samples are drawn from a Gamma distribution with specified parameters,
     |      shape (sometimes designated "k") and scale=1.
     |
     |      Parameters
     |      ----------
     |      shape : float or array_like of floats
     |          Parameter, must be non-negative.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``shape`` is a scalar.  Otherwise,
     |          ``np.array(shape).size`` samples are drawn.
     |      dtype : dtype, optional
     |          Desired dtype of the result, only `float64` and `float32` are supported.
     |          Byteorder must be native. The default value is np.float64.
     |      out : ndarray, optional
     |          Alternative output array in which to place the result. If size is
     |          not None, it must have the same shape as the provided size and
     |          must match the type of the output values.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized standard gamma distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.gamma : probability density function, distribution or
     |          cumulative density function, etc.
     |
     |      Notes
     |      -----
     |      The probability density for the Gamma distribution is
     |
     |      .. math:: p(x) = x^{k-1}\frac{e^{-x/\theta}}{\theta^k\Gamma(k)},
     |
     |      where :math:`k` is the shape and :math:`\theta` the scale,
     |      and :math:`\Gamma` is the Gamma function.
     |
     |      The Gamma distribution is often used to model the times to failure of
     |      electronic components, and arises naturally in processes for which the
     |      waiting times between Poisson distributed events are relevant.
     |
     |      References
     |      ----------
     |      .. [1] Weisstein, Eric W. "Gamma Distribution." From MathWorld--A
     |             Wolfram Web Resource.
     |             http://mathworld.wolfram.com/GammaDistribution.html
     |      .. [2] Wikipedia, "Gamma distribution",
     |             https://en.wikipedia.org/wiki/Gamma_distribution
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> shape, scale = 2., 1. # mean and width
     |      >>> s = np.random.default_rng().standard_gamma(shape, 1000000)
     |
     |      Display the histogram of the samples, along with
     |      the probability density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> import scipy.special as sps  # doctest: +SKIP
     |      >>> count, bins, ignored = plt.hist(s, 50, density=True)
     |      >>> y = bins**(shape-1) * ((np.exp(-bins/scale))/  # doctest: +SKIP
     |      ...                       (sps.gamma(shape) * scale**shape))
     |      >>> plt.plot(bins, y, linewidth=2, color='r')  # doctest: +SKIP
     |      >>> plt.show()
     |
     |  standard_normal(...)
     |      standard_normal(size=None, dtype=np.float64, out=None)
     |
     |      Draw samples from a standard Normal distribution (mean=0, stdev=1).
     |
     |      Parameters
     |      ----------
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  Default is None, in which case a
     |          single value is returned.
     |      dtype : dtype, optional
     |          Desired dtype of the result, only `float64` and `float32` are supported.
     |          Byteorder must be native. The default value is np.float64.
     |      out : ndarray, optional
     |          Alternative output array in which to place the result. If size is not None,
     |          it must have the same shape as the provided size and must match the type of
     |          the output values.
     |
     |      Returns
     |      -------
     |      out : float or ndarray
     |          A floating-point array of shape ``size`` of drawn samples, or a
     |          single sample if ``size`` was not specified.
     |
     |      See Also
     |      --------
     |      normal :
     |          Equivalent function with additional ``loc`` and ``scale`` arguments
     |          for setting the mean and standard deviation.
     |
     |      Notes
     |      -----
     |      For random samples from the normal distribution with mean ``mu`` and
     |      standard deviation ``sigma``, use one of::
     |
     |          mu + sigma * rng.standard_normal(size=...)
     |          rng.normal(mu, sigma, size=...)
     |
     |      Examples
     |      --------
     |      >>> rng = np.random.default_rng()
     |      >>> rng.standard_normal()
     |      2.1923875335537315 # random
     |
     |      >>> s = rng.standard_normal(8000)
     |      >>> s
     |      array([ 0.6888893 ,  0.78096262, -0.89086505, ...,  0.49876311,  # random
     |             -0.38672696, -0.4685006 ])                                # random
     |      >>> s.shape
     |      (8000,)
     |      >>> s = rng.standard_normal(size=(3, 4, 2))
     |      >>> s.shape
     |      (3, 4, 2)
     |
     |      Two-by-four array of samples from the normal distribution with
     |      mean 3 and standard deviation 2.5:
     |
     |      >>> 3 + 2.5 * rng.standard_normal(size=(2, 4))
     |      array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random
     |             [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random
     |
     |  standard_t(...)
     |      standard_t(df, size=None)
     |
     |      Draw samples from a standard Student's t distribution with `df` degrees
     |      of freedom.
     |
     |      A special case of the hyperbolic distribution.  As `df` gets
     |      large, the result resembles that of the standard normal
     |      distribution (`standard_normal`).
     |
     |      Parameters
     |      ----------
     |      df : float or array_like of floats
     |          Degrees of freedom, must be > 0.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``df`` is a scalar.  Otherwise,
     |          ``np.array(df).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized standard Student's t distribution.
     |
     |      Notes
     |      -----
     |      The probability density function for the t distribution is
     |
     |      .. math:: P(x, df) = \frac{\Gamma(\frac{df+1}{2})}{\sqrt{\pi df}
     |                \Gamma(\frac{df}{2})}\Bigl( 1+\frac{x^2}{df} \Bigr)^{-(df+1)/2}
     |
     |      The t test is based on an assumption that the data come from a
     |      Normal distribution. The t test provides a way to test whether
     |      the sample mean (that is the mean calculated from the data) is
     |      a good estimate of the true mean.
     |
     |      The derivation of the t-distribution was first published in
     |      1908 by William Gosset while working for the Guinness Brewery
     |      in Dublin. Due to proprietary issues, he had to publish under
     |      a pseudonym, and so he used the name Student.
     |
     |      References
     |      ----------
     |      .. [1] Dalgaard, Peter, "Introductory Statistics With R",
     |             Springer, 2002.
     |      .. [2] Wikipedia, "Student's t-distribution"
     |             https://en.wikipedia.org/wiki/Student's_t-distribution
     |
     |      Examples
     |      --------
     |      From Dalgaard page 83 [1]_, suppose the daily energy intake for 11
     |      women in kilojoules (kJ) is:
     |
     |      >>> intake = np.array([5260., 5470, 5640, 6180, 6390, 6515, 6805, 7515, \
     |      ...                    7515, 8230, 8770])
     |
     |      Does their energy intake deviate systematically from the recommended
     |      value of 7725 kJ? Our null hypothesis will be the absence of deviation,
     |      and the alternate hypothesis will be the presence of an effect that could be
     |      either positive or negative, hence making our test 2-tailed.
     |
     |      Because we are estimating the mean and we have N=11 values in our sample,
     |      we have N-1=10 degrees of freedom. We set our significance level to 95% and
     |      compute the t statistic using the empirical mean and empirical standard
     |      deviation of our intake. We use a ddof of 1 to base the computation of our
     |      empirical standard deviation on an unbiased estimate of the variance (note:
     |      the final estimate is not unbiased due to the concave nature of the square
     |      root).
     |
     |      >>> np.mean(intake)
     |      6753.636363636364
     |      >>> intake.std(ddof=1)
     |      1142.1232221373727
     |      >>> t = (np.mean(intake)-7725)/(intake.std(ddof=1)/np.sqrt(len(intake)))
     |      >>> t
     |      -2.8207540608310198
     |
     |      We draw 1000000 samples from Student's t distribution with the adequate
     |      degrees of freedom.
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> s = np.random.default_rng().standard_t(10, size=1000000)
     |      >>> h = plt.hist(s, bins=100, density=True)
     |
     |      Does our t statistic land in one of the two critical regions found at
     |      both tails of the distribution?
     |
     |      >>> np.sum(np.abs(t) < np.abs(s)) / float(len(s))
     |      0.018318  #random < 0.05, statistic is in critical region
     |
     |      The probability value for this 2-tailed test is about 1.83%, which is
     |      lower than the 5% pre-determined significance threshold.
     |
     |      Therefore, the probability of observing values as extreme as our intake
     |      conditionally on the null hypothesis being true is too low, and we reject
     |      the null hypothesis of no deviation.
     |
     |  triangular(...)
     |      triangular(left, mode, right, size=None)
     |
     |      Draw samples from the triangular distribution over the
     |      interval ``[left, right]``.
     |
     |      The triangular distribution is a continuous probability
     |      distribution with lower limit left, peak at mode, and upper
     |      limit right. Unlike the other distributions, these parameters
     |      directly define the shape of the pdf.
     |
     |      Parameters
     |      ----------
     |      left : float or array_like of floats
     |          Lower limit.
     |      mode : float or array_like of floats
     |          The value where the peak of the distribution occurs.
     |          The value must fulfill the condition ``left <= mode <= right``.
     |      right : float or array_like of floats
     |          Upper limit, must be larger than `left`.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``left``, ``mode``, and ``right``
     |          are all scalars.  Otherwise, ``np.broadcast(left, mode, right).size``
     |          samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized triangular distribution.
     |
     |      Notes
     |      -----
     |      The probability density function for the triangular distribution is
     |
     |      .. math:: P(x;l, m, r) = \begin{cases}
     |                \frac{2(x-l)}{(r-l)(m-l)}& \text{for $l \leq x \leq m$},\\
     |                \frac{2(r-x)}{(r-l)(r-m)}& \text{for $m \leq x \leq r$},\\
     |                0& \text{otherwise}.
     |                \end{cases}
     |
     |      The triangular distribution is often used in ill-defined
     |      problems where the underlying distribution is not known, but
     |      some knowledge of the limits and mode exists. Often it is used
     |      in simulations.
     |
     |      References
     |      ----------
     |      .. [1] Wikipedia, "Triangular distribution"
     |             https://en.wikipedia.org/wiki/Triangular_distribution
     |
     |      Examples
     |      --------
     |      Draw values from the distribution and plot the histogram:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> h = plt.hist(np.random.default_rng().triangular(-3, 0, 8, 100000), bins=200,
     |      ...              density=True)
     |      >>> plt.show()
     |
     |  uniform(...)
     |      uniform(low=0.0, high=1.0, size=None)
     |
     |      Draw samples from a uniform distribution.
     |
     |      Samples are uniformly distributed over the half-open interval
     |      ``[low, high)`` (includes low, but excludes high).  In other words,
     |      any value within the given interval is equally likely to be drawn
     |      by `uniform`.
     |
     |      Parameters
     |      ----------
     |      low : float or array_like of floats, optional
     |          Lower boundary of the output interval.  All values generated will be
     |          greater than or equal to low.  The default value is 0.
     |      high : float or array_like of floats
     |          Upper boundary of the output interval.  All values generated will be
     |          less than high.  The high limit may be included in the returned array of
     |          floats due to floating-point rounding in the equation
     |          ``low + (high-low) * random_sample()``.  high - low must be
     |          non-negative.  The default value is 1.0.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``low`` and ``high`` are both scalars.
     |          Otherwise, ``np.broadcast(low, high).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized uniform distribution.
     |
     |      See Also
     |      --------
     |      integers : Discrete uniform distribution, yielding integers.
     |      random : Floats uniformly distributed over ``[0, 1)``.
     |
     |      Notes
     |      -----
     |      The probability density function of the uniform distribution is
     |
     |      .. math:: p(x) = \frac{1}{b - a}
     |
     |      anywhere within the interval ``[a, b)``, and zero elsewhere.
     |
     |      When ``high`` == ``low``, values of ``low`` will be returned.
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> s = np.random.default_rng().uniform(-1,0,1000)
     |
     |      All values are within the given interval:
     |
     |      >>> np.all(s >= -1)
     |      True
     |      >>> np.all(s < 0)
     |      True
     |
     |      Display the histogram of the samples, along with the
     |      probability density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> count, bins, ignored = plt.hist(s, 15, density=True)
     |      >>> plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
     |      >>> plt.show()
     |
     |  vonmises(...)
     |      vonmises(mu, kappa, size=None)
     |
     |      Draw samples from a von Mises distribution.
     |
     |      Samples are drawn from a von Mises distribution with specified mode
     |      (mu) and dispersion (kappa), on the interval [-pi, pi].
     |
     |      The von Mises distribution (also known as the circular normal
     |      distribution) is a continuous probability distribution on the unit
     |      circle.  It may be thought of as the circular analogue of the normal
     |      distribution.
     |
     |      Parameters
     |      ----------
     |      mu : float or array_like of floats
     |          Mode ("center") of the distribution.
     |      kappa : float or array_like of floats
     |          Dispersion of the distribution, has to be >=0.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``mu`` and ``kappa`` are both scalars.
     |          Otherwise, ``np.broadcast(mu, kappa).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized von Mises distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.vonmises : probability density function, distribution, or
     |          cumulative density function, etc.
     |
     |      Notes
     |      -----
     |      The probability density for the von Mises distribution is
     |
     |      .. math:: p(x) = \frac{e^{\kappa cos(x-\mu)}}{2\pi I_0(\kappa)},
     |
     |      where :math:`\mu` is the mode and :math:`\kappa` the dispersion,
     |      and :math:`I_0(\kappa)` is the modified Bessel function of order 0.
     |
     |      The von Mises is named for Richard Edler von Mises, who was born in
     |      Austria-Hungary, in what is now the Ukraine.  He fled to the United
     |      States in 1939 and became a professor at Harvard.  He worked in
     |      probability theory, aerodynamics, fluid mechanics, and philosophy of
     |      science.
     |
     |      References
     |      ----------
     |      .. [1] Abramowitz, M. and Stegun, I. A. (Eds.). "Handbook of
     |             Mathematical Functions with Formulas, Graphs, and Mathematical
     |             Tables, 9th printing," New York: Dover, 1972.
     |      .. [2] von Mises, R., "Mathematical Theory of Probability
     |             and Statistics", New York: Academic Press, 1964.
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> mu, kappa = 0.0, 4.0 # mean and dispersion
     |      >>> s = np.random.default_rng().vonmises(mu, kappa, 1000)
     |
     |      Display the histogram of the samples, along with
     |      the probability density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> from scipy.special import i0  # doctest: +SKIP
     |      >>> plt.hist(s, 50, density=True)
     |      >>> x = np.linspace(-np.pi, np.pi, num=51)
     |      >>> y = np.exp(kappa*np.cos(x-mu))/(2*np.pi*i0(kappa))  # doctest: +SKIP
     |      >>> plt.plot(x, y, linewidth=2, color='r')  # doctest: +SKIP
     |      >>> plt.show()
     |
     |  wald(...)
     |      wald(mean, scale, size=None)
     |
     |      Draw samples from a Wald, or inverse Gaussian, distribution.
     |
     |      As the scale approaches infinity, the distribution becomes more like a
     |      Gaussian. Some references claim that the Wald is an inverse Gaussian
     |      with mean equal to 1, but this is by no means universal.
     |
     |      The inverse Gaussian distribution was first studied in relationship to
     |      Brownian motion. In 1956 M.C.K. Tweedie used the name inverse Gaussian
     |      because there is an inverse relationship between the time to cover a
     |      unit distance and distance covered in unit time.
     |
     |      Parameters
     |      ----------
     |      mean : float or array_like of floats
     |          Distribution mean, must be > 0.
     |      scale : float or array_like of floats
     |          Scale parameter, must be > 0.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``mean`` and ``scale`` are both scalars.
     |          Otherwise, ``np.broadcast(mean, scale).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized Wald distribution.
     |
     |      Notes
     |      -----
     |      The probability density function for the Wald distribution is
     |
     |      .. math:: P(x;mean,scale) = \sqrt{\frac{scale}{2\pi x^3}}e^
     |                                  \frac{-scale(x-mean)^2}{2\cdotp mean^2x}
     |
     |      As noted above the inverse Gaussian distribution first arise
     |      from attempts to model Brownian motion. It is also a
     |      competitor to the Weibull for use in reliability modeling and
     |      modeling stock returns and interest rate processes.
     |
     |      References
     |      ----------
     |      .. [1] Brighton Webs Ltd., Wald Distribution,
     |             https://web.archive.org/web/20090423014010/http://www.brighton-webs.co.uk:80/distributions/wald.asp
     |      .. [2] Chhikara, Raj S., and Folks, J. Leroy, "The Inverse Gaussian
     |             Distribution: Theory : Methodology, and Applications", CRC Press,
     |             1988.
     |      .. [3] Wikipedia, "Inverse Gaussian distribution"
     |             https://en.wikipedia.org/wiki/Inverse_Gaussian_distribution
     |
     |      Examples
     |      --------
     |      Draw values from the distribution and plot the histogram:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> h = plt.hist(np.random.default_rng().wald(3, 2, 100000), bins=200, density=True)
     |      >>> plt.show()
     |
     |  weibull(...)
     |      weibull(a, size=None)
     |
     |      Draw samples from a Weibull distribution.
     |
     |      Draw samples from a 1-parameter Weibull distribution with the given
     |      shape parameter `a`.
     |
     |      .. math:: X = (-ln(U))^{1/a}
     |
     |      Here, U is drawn from the uniform distribution over (0,1].
     |
     |      The more common 2-parameter Weibull, including a scale parameter
     |      :math:`\lambda` is just :math:`X = \lambda(-ln(U))^{1/a}`.
     |
     |      Parameters
     |      ----------
     |      a : float or array_like of floats
     |          Shape parameter of the distribution.  Must be nonnegative.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``a`` is a scalar.  Otherwise,
     |          ``np.array(a).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized Weibull distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.weibull_max
     |      scipy.stats.weibull_min
     |      scipy.stats.genextreme
     |      gumbel
     |
     |      Notes
     |      -----
     |      The Weibull (or Type III asymptotic extreme value distribution
     |      for smallest values, SEV Type III, or Rosin-Rammler
     |      distribution) is one of a class of Generalized Extreme Value
     |      (GEV) distributions used in modeling extreme value problems.
     |      This class includes the Gumbel and Frechet distributions.
     |
     |      The probability density for the Weibull distribution is
     |
     |      .. math:: p(x) = \frac{a}
     |                       {\lambda}(\frac{x}{\lambda})^{a-1}e^{-(x/\lambda)^a},
     |
     |      where :math:`a` is the shape and :math:`\lambda` the scale.
     |
     |      The function has its peak (the mode) at
     |      :math:`\lambda(\frac{a-1}{a})^{1/a}`.
     |
     |      When ``a = 1``, the Weibull distribution reduces to the exponential
     |      distribution.
     |
     |      References
     |      ----------
     |      .. [1] Waloddi Weibull, Royal Technical University, Stockholm,
     |             1939 "A Statistical Theory Of The Strength Of Materials",
     |             Ingeniorsvetenskapsakademiens Handlingar Nr 151, 1939,
     |             Generalstabens Litografiska Anstalts Forlag, Stockholm.
     |      .. [2] Waloddi Weibull, "A Statistical Distribution Function of
     |             Wide Applicability", Journal Of Applied Mechanics ASME Paper
     |             1951.
     |      .. [3] Wikipedia, "Weibull distribution",
     |             https://en.wikipedia.org/wiki/Weibull_distribution
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> rng = np.random.default_rng()
     |      >>> a = 5. # shape
     |      >>> s = rng.weibull(a, 1000)
     |
     |      Display the histogram of the samples, along with
     |      the probability density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> x = np.arange(1,100.)/50.
     |      >>> def weib(x,n,a):
     |      ...     return (a / n) * (x / n)**(a - 1) * np.exp(-(x / n)**a)
     |
     |      >>> count, bins, ignored = plt.hist(rng.weibull(5.,1000))
     |      >>> x = np.arange(1,100.)/50.
     |      >>> scale = count.max()/weib(x, 1., 5.).max()
     |      >>> plt.plot(x, weib(x, 1., 5.)*scale)
     |      >>> plt.show()
     |
     |  zipf(...)
     |      zipf(a, size=None)
     |
     |      Draw samples from a Zipf distribution.
     |
     |      Samples are drawn from a Zipf distribution with specified parameter
     |      `a` > 1.
     |
     |      The Zipf distribution (also known as the zeta distribution) is a
     |      discrete probability distribution that satisfies Zipf's law: the
     |      frequency of an item is inversely proportional to its rank in a
     |      frequency table.
     |
     |      Parameters
     |      ----------
     |      a : float or array_like of floats
     |          Distribution parameter. Must be greater than 1.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``a`` is a scalar. Otherwise,
     |          ``np.array(a).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized Zipf distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.zipf : probability density function, distribution, or
     |          cumulative density function, etc.
     |
     |      Notes
     |      -----
     |      The probability density for the Zipf distribution is
     |
     |      .. math:: p(k) = \frac{k^{-a}}{\zeta(a)},
     |
     |      for integers :math:`k \geq 1`, where :math:`\zeta` is the Riemann Zeta
     |      function.
     |
     |      It is named for the American linguist George Kingsley Zipf, who noted
     |      that the frequency of any word in a sample of a language is inversely
     |      proportional to its rank in the frequency table.
     |
     |      References
     |      ----------
     |      .. [1] Zipf, G. K., "Selected Studies of the Principle of Relative
     |             Frequency in Language," Cambridge, MA: Harvard Univ. Press,
     |             1932.
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> a = 4.0
     |      >>> n = 20000
     |      >>> s = np.random.default_rng().zipf(a, size=n)
     |
     |      Display the histogram of the samples, along with
     |      the expected histogram based on the probability
     |      density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> from scipy.special import zeta  # doctest: +SKIP
     |
     |      `bincount` provides a fast histogram for small integers.
     |
     |      >>> count = np.bincount(s)
     |      >>> k = np.arange(1, s.max() + 1)
     |
     |      >>> plt.bar(k, count[1:], alpha=0.5, label='sample count')
     |      >>> plt.plot(k, n*(k**-a)/zeta(a), 'k.-', alpha=0.5,
     |      ...          label='expected count')   # doctest: +SKIP
     |      >>> plt.semilogy()
     |      >>> plt.grid(alpha=0.4)
     |      >>> plt.legend()
     |      >>> plt.title(f'Zipf sample, a={a}, size={n}')
     |      >>> plt.show()
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
     |  bit_generator
     |      Gets the bit generator instance used by the generator
     |
     |      Returns
     |      -------
     |      bit_generator : BitGenerator
     |          The bit generator instance used by the generator

    class MT19937(numpy.random.bit_generator.BitGenerator)
     |  MT19937(seed=None)
     |
     |  Container for the Mersenne Twister pseudo-random number generator.
     |
     |  Parameters
     |  ----------
     |  seed : {None, int, array_like[ints], SeedSequence}, optional
     |      A seed to initialize the `BitGenerator`. If None, then fresh,
     |      unpredictable entropy will be pulled from the OS. If an ``int`` or
     |      ``array_like[ints]`` is passed, then it will be passed to
     |      `SeedSequence` to derive the initial `BitGenerator` state. One may also
     |      pass in a `SeedSequence` instance.
     |
     |  Attributes
     |  ----------
     |  lock: threading.Lock
     |      Lock instance that is shared so that the same bit git generator can
     |      be used in multiple Generators without corrupting the state. Code that
     |      generates values from a bit generator should hold the bit generator's
     |      lock.
     |
     |  Notes
     |  -----
     |  ``MT19937`` provides a capsule containing function pointers that produce
     |  doubles, and unsigned 32 and 64- bit integers [1]_. These are not
     |  directly consumable in Python and must be consumed by a ``Generator``
     |  or similar object that supports low-level access.
     |
     |  The Python stdlib module "random" also contains a Mersenne Twister
     |  pseudo-random number generator.
     |
     |  **State and Seeding**
     |
     |  The ``MT19937`` state vector consists of a 624-element array of
     |  32-bit unsigned integers plus a single integer value between 0 and 624
     |  that indexes the current position within the main array.
     |
     |  The input seed is processed by `SeedSequence` to fill the whole state. The
     |  first element is reset such that only its most significant bit is set.
     |
     |  **Parallel Features**
     |
     |  The preferred way to use a BitGenerator in parallel applications is to use
     |  the `SeedSequence.spawn` method to obtain entropy values, and to use these
     |  to generate new BitGenerators:
     |
     |  >>> from numpy.random import Generator, MT19937, SeedSequence
     |  >>> sg = SeedSequence(1234)
     |  >>> rg = [Generator(MT19937(s)) for s in sg.spawn(10)]
     |
     |  Another method is to use `MT19937.jumped` which advances the state as-if
     |  :math:`2^{128}` random numbers have been generated ([1]_, [2]_). This
     |  allows the original sequence to be split so that distinct segments can be
     |  used in each worker process. All generators should be chained to ensure
     |  that the segments come from the same sequence.
     |
     |  >>> from numpy.random import Generator, MT19937, SeedSequence
     |  >>> sg = SeedSequence(1234)
     |  >>> bit_generator = MT19937(sg)
     |  >>> rg = []
     |  >>> for _ in range(10):
     |  ...    rg.append(Generator(bit_generator))
     |  ...    # Chain the BitGenerators
     |  ...    bit_generator = bit_generator.jumped()
     |
     |  **Compatibility Guarantee**
     |
     |  ``MT19937`` makes a guarantee that a fixed seed will always produce
     |  the same random integer stream.
     |
     |  References
     |  ----------
     |  .. [1] Hiroshi Haramoto, Makoto Matsumoto, and Pierre L'Ecuyer, "A Fast
     |      Jump Ahead Algorithm for Linear Recurrences in a Polynomial Space",
     |      Sequences and Their Applications - SETA, 290--298, 2008.
     |  .. [2] Hiroshi Haramoto, Makoto Matsumoto, Takuji Nishimura, François
     |      Panneton, Pierre L'Ecuyer, "Efficient Jump Ahead for F2-Linear
     |      Random Number Generators", INFORMS JOURNAL ON COMPUTING, Vol. 20,
     |      No. 3, Summer 2008, pp. 385-390.
     |
     |  Method resolution order:
     |      MT19937
     |      numpy.random.bit_generator.BitGenerator
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce_cython__(...)
     |
     |  __setstate_cython__(...)
     |
     |  jumped(...)
     |      jumped(jumps=1)
     |
     |      Returns a new bit generator with the state jumped
     |
     |      The state of the returned bit generator is jumped as-if
     |      2**(128 * jumps) random numbers have been generated.
     |
     |      Parameters
     |      ----------
     |      jumps : integer, positive
     |          Number of times to jump the state of the bit generator returned
     |
     |      Returns
     |      -------
     |      bit_generator : MT19937
     |          New instance of generator jumped iter times
     |
     |      Notes
     |      -----
     |      The jump step is computed using a modified version of Matsumoto's
     |      implementation of Horner's method. The step polynomial is precomputed
     |      to perform 2**128 steps. The jumped state has been verified to match
     |      the state produced using Matsumoto's original code.
     |
     |      References
     |      ----------
     |      .. [1] Matsumoto, M, Generating multiple disjoint streams of
     |         pseudorandom number sequences.  Accessed on: May 6, 2020.
     |         http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/JUMP/
     |      .. [2] Hiroshi Haramoto, Makoto Matsumoto, Takuji Nishimura, François
     |         Panneton, Pierre L'Ecuyer, "Efficient Jump Ahead for F2-Linear
     |         Random Number Generators", INFORMS JOURNAL ON COMPUTING, Vol. 20,
     |         No. 3, Summer 2008, pp. 385-390.
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
     |  state
     |      Get or set the PRNG state
     |
     |      Returns
     |      -------
     |      state : dict
     |          Dictionary containing the information required to describe the
     |          state of the PRNG
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __pyx_vtable__ = <capsule object NULL>
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from numpy.random.bit_generator.BitGenerator:
     |
     |  __getstate__(...)
     |      Helper for pickle.
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __setstate__(...)
     |
     |  random_raw(...)
     |      random_raw(self, size=None)
     |
     |      Return randoms as generated by the underlying BitGenerator
     |
     |      Parameters
     |      ----------
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  Default is None, in which case a
     |          single value is returned.
     |      output : bool, optional
     |          Output values.  Used for performance testing since the generated
     |          values are not returned.
     |
     |      Returns
     |      -------
     |      out : uint or ndarray
     |          Drawn samples.
     |
     |      Notes
     |      -----
     |      This method directly exposes the raw underlying pseudo-random
     |      number generator. All values are returned as unsigned 64-bit
     |      values irrespective of the number of bits produced by the PRNG.
     |
     |      See the class docstring for the number of bits returned.
     |
     |  spawn(...)
     |      spawn(n_children)
     |
     |      Create new independent child bit generators.
     |
     |      See :ref:`seedsequence-spawn` for additional notes on spawning
     |      children.  Some bit generators also implement ``jumped``
     |      as a different approach for creating independent streams.
     |
     |      .. versionadded:: 1.25.0
     |
     |      Parameters
     |      ----------
     |      n_children : int
     |
     |      Returns
     |      -------
     |      child_bit_generators : list of BitGenerators
     |
     |      Raises
     |      ------
     |      TypeError
     |          When the underlying SeedSequence does not implement spawning.
     |
     |      See Also
     |      --------
     |      random.Generator.spawn, random.SeedSequence.spawn :
     |          Equivalent method on the generator and seed sequence.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from numpy.random.bit_generator.BitGenerator:
     |
     |  capsule
     |
     |  cffi
     |      CFFI interface
     |
     |      Returns
     |      -------
     |      interface : namedtuple
     |          Named tuple containing CFFI wrapper
     |
     |          * state_address - Memory address of the state struct
     |          * state - pointer to the state struct
     |          * next_uint64 - function pointer to produce 64 bit integers
     |          * next_uint32 - function pointer to produce 32 bit integers
     |          * next_double - function pointer to produce doubles
     |          * bitgen - pointer to the bit generator struct
     |
     |  ctypes
     |      ctypes interface
     |
     |      Returns
     |      -------
     |      interface : namedtuple
     |          Named tuple containing ctypes wrapper
     |
     |          * state_address - Memory address of the state struct
     |          * state - pointer to the state struct
     |          * next_uint64 - function pointer to produce 64 bit integers
     |          * next_uint32 - function pointer to produce 32 bit integers
     |          * next_double - function pointer to produce doubles
     |          * bitgen - pointer to the bit generator struct
     |
     |  lock
     |
     |  seed_seq
     |      Get the seed sequence used to initialize the bit generator.
     |
     |      .. versionadded:: 1.25.0
     |
     |      Returns
     |      -------
     |      seed_seq : ISeedSequence
     |          The SeedSequence object used to initialize the BitGenerator.
     |          This is normally a `np.random.SeedSequence` instance.

    class PCG64(numpy.random.bit_generator.BitGenerator)
     |  PCG64(seed=None)
     |
     |  BitGenerator for the PCG-64 pseudo-random number generator.
     |
     |  Parameters
     |  ----------
     |  seed : {None, int, array_like[ints], SeedSequence}, optional
     |      A seed to initialize the `BitGenerator`. If None, then fresh,
     |      unpredictable entropy will be pulled from the OS. If an ``int`` or
     |      ``array_like[ints]`` is passed, then it will be passed to
     |      `SeedSequence` to derive the initial `BitGenerator` state. One may also
     |      pass in a `SeedSequence` instance.
     |
     |  Notes
     |  -----
     |  PCG-64 is a 128-bit implementation of O'Neill's permutation congruential
     |  generator ([1]_, [2]_). PCG-64 has a period of :math:`2^{128}` and supports
     |  advancing an arbitrary number of steps as well as :math:`2^{127}` streams.
     |  The specific member of the PCG family that we use is PCG XSL RR 128/64
     |  as described in the paper ([2]_).
     |
     |  ``PCG64`` provides a capsule containing function pointers that produce
     |  doubles, and unsigned 32 and 64- bit integers. These are not
     |  directly consumable in Python and must be consumed by a ``Generator``
     |  or similar object that supports low-level access.
     |
     |  Supports the method :meth:`advance` to advance the RNG an arbitrary number of
     |  steps. The state of the PCG-64 RNG is represented by 2 128-bit unsigned
     |  integers.
     |
     |  **State and Seeding**
     |
     |  The ``PCG64`` state vector consists of 2 unsigned 128-bit values,
     |  which are represented externally as Python ints. One is the state of the
     |  PRNG, which is advanced by a linear congruential generator (LCG). The
     |  second is a fixed odd increment used in the LCG.
     |
     |  The input seed is processed by `SeedSequence` to generate both values. The
     |  increment is not independently settable.
     |
     |  **Parallel Features**
     |
     |  The preferred way to use a BitGenerator in parallel applications is to use
     |  the `SeedSequence.spawn` method to obtain entropy values, and to use these
     |  to generate new BitGenerators:
     |
     |  >>> from numpy.random import Generator, PCG64, SeedSequence
     |  >>> sg = SeedSequence(1234)
     |  >>> rg = [Generator(PCG64(s)) for s in sg.spawn(10)]
     |
     |  **Compatibility Guarantee**
     |
     |  ``PCG64`` makes a guarantee that a fixed seed will always produce
     |  the same random integer stream.
     |
     |  References
     |  ----------
     |  .. [1] `"PCG, A Family of Better Random Number Generators"
     |         <http://www.pcg-random.org/>`_
     |  .. [2] O'Neill, Melissa E. `"PCG: A Family of Simple Fast Space-Efficient
     |         Statistically Good Algorithms for Random Number Generation"
     |         <https://www.cs.hmc.edu/tr/hmc-cs-2014-0905.pdf>`_
     |
     |  Method resolution order:
     |      PCG64
     |      numpy.random.bit_generator.BitGenerator
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce_cython__(...)
     |
     |  __setstate_cython__(...)
     |
     |  advance(...)
     |      advance(delta)
     |
     |      Advance the underlying RNG as-if delta draws have occurred.
     |
     |      Parameters
     |      ----------
     |      delta : integer, positive
     |          Number of draws to advance the RNG. Must be less than the
     |          size state variable in the underlying RNG.
     |
     |      Returns
     |      -------
     |      self : PCG64
     |          RNG advanced delta steps
     |
     |      Notes
     |      -----
     |      Advancing a RNG updates the underlying RNG state as-if a given
     |      number of calls to the underlying RNG have been made. In general
     |      there is not a one-to-one relationship between the number output
     |      random values from a particular distribution and the number of
     |      draws from the core RNG.  This occurs for two reasons:
     |
     |      * The random values are simulated using a rejection-based method
     |        and so, on average, more than one value from the underlying
     |        RNG is required to generate an single draw.
     |      * The number of bits required to generate a simulated value
     |        differs from the number of bits generated by the underlying
     |        RNG.  For example, two 16-bit integer values can be simulated
     |        from a single draw of a 32-bit RNG.
     |
     |      Advancing the RNG state resets any pre-computed random numbers.
     |      This is required to ensure exact reproducibility.
     |
     |  jumped(...)
     |      jumped(jumps=1)
     |
     |      Returns a new bit generator with the state jumped.
     |
     |      Jumps the state as-if jumps * 210306068529402873165736369884012333109
     |      random numbers have been generated.
     |
     |      Parameters
     |      ----------
     |      jumps : integer, positive
     |          Number of times to jump the state of the bit generator returned
     |
     |      Returns
     |      -------
     |      bit_generator : PCG64
     |          New instance of generator jumped iter times
     |
     |      Notes
     |      -----
     |      The step size is phi-1 when multiplied by 2**128 where phi is the
     |      golden ratio.
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
     |  state
     |      Get or set the PRNG state
     |
     |      Returns
     |      -------
     |      state : dict
     |          Dictionary containing the information required to describe the
     |          state of the PRNG
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __pyx_vtable__ = <capsule object NULL>
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from numpy.random.bit_generator.BitGenerator:
     |
     |  __getstate__(...)
     |      Helper for pickle.
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __setstate__(...)
     |
     |  random_raw(...)
     |      random_raw(self, size=None)
     |
     |      Return randoms as generated by the underlying BitGenerator
     |
     |      Parameters
     |      ----------
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  Default is None, in which case a
     |          single value is returned.
     |      output : bool, optional
     |          Output values.  Used for performance testing since the generated
     |          values are not returned.
     |
     |      Returns
     |      -------
     |      out : uint or ndarray
     |          Drawn samples.
     |
     |      Notes
     |      -----
     |      This method directly exposes the raw underlying pseudo-random
     |      number generator. All values are returned as unsigned 64-bit
     |      values irrespective of the number of bits produced by the PRNG.
     |
     |      See the class docstring for the number of bits returned.
     |
     |  spawn(...)
     |      spawn(n_children)
     |
     |      Create new independent child bit generators.
     |
     |      See :ref:`seedsequence-spawn` for additional notes on spawning
     |      children.  Some bit generators also implement ``jumped``
     |      as a different approach for creating independent streams.
     |
     |      .. versionadded:: 1.25.0
     |
     |      Parameters
     |      ----------
     |      n_children : int
     |
     |      Returns
     |      -------
     |      child_bit_generators : list of BitGenerators
     |
     |      Raises
     |      ------
     |      TypeError
     |          When the underlying SeedSequence does not implement spawning.
     |
     |      See Also
     |      --------
     |      random.Generator.spawn, random.SeedSequence.spawn :
     |          Equivalent method on the generator and seed sequence.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from numpy.random.bit_generator.BitGenerator:
     |
     |  capsule
     |
     |  cffi
     |      CFFI interface
     |
     |      Returns
     |      -------
     |      interface : namedtuple
     |          Named tuple containing CFFI wrapper
     |
     |          * state_address - Memory address of the state struct
     |          * state - pointer to the state struct
     |          * next_uint64 - function pointer to produce 64 bit integers
     |          * next_uint32 - function pointer to produce 32 bit integers
     |          * next_double - function pointer to produce doubles
     |          * bitgen - pointer to the bit generator struct
     |
     |  ctypes
     |      ctypes interface
     |
     |      Returns
     |      -------
     |      interface : namedtuple
     |          Named tuple containing ctypes wrapper
     |
     |          * state_address - Memory address of the state struct
     |          * state - pointer to the state struct
     |          * next_uint64 - function pointer to produce 64 bit integers
     |          * next_uint32 - function pointer to produce 32 bit integers
     |          * next_double - function pointer to produce doubles
     |          * bitgen - pointer to the bit generator struct
     |
     |  lock
     |
     |  seed_seq
     |      Get the seed sequence used to initialize the bit generator.
     |
     |      .. versionadded:: 1.25.0
     |
     |      Returns
     |      -------
     |      seed_seq : ISeedSequence
     |          The SeedSequence object used to initialize the BitGenerator.
     |          This is normally a `np.random.SeedSequence` instance.

    class PCG64DXSM(numpy.random.bit_generator.BitGenerator)
     |  PCG64DXSM(seed=None)
     |
     |  BitGenerator for the PCG-64 DXSM pseudo-random number generator.
     |
     |  Parameters
     |  ----------
     |  seed : {None, int, array_like[ints], SeedSequence}, optional
     |      A seed to initialize the `BitGenerator`. If None, then fresh,
     |      unpredictable entropy will be pulled from the OS. If an ``int`` or
     |      ``array_like[ints]`` is passed, then it will be passed to
     |      `SeedSequence` to derive the initial `BitGenerator` state. One may also
     |      pass in a `SeedSequence` instance.
     |
     |  Notes
     |  -----
     |  PCG-64 DXSM is a 128-bit implementation of O'Neill's permutation congruential
     |  generator ([1]_, [2]_). PCG-64 DXSM has a period of :math:`2^{128}` and supports
     |  advancing an arbitrary number of steps as well as :math:`2^{127}` streams.
     |  The specific member of the PCG family that we use is PCG CM DXSM 128/64. It
     |  differs from ``PCG64`` in that it uses the stronger DXSM output function,
     |  a 64-bit "cheap multiplier" in the LCG, and outputs from the state before
     |  advancing it rather than advance-then-output.
     |
     |  ``PCG64DXSM`` provides a capsule containing function pointers that produce
     |  doubles, and unsigned 32 and 64- bit integers. These are not
     |  directly consumable in Python and must be consumed by a ``Generator``
     |  or similar object that supports low-level access.
     |
     |  Supports the method :meth:`advance` to advance the RNG an arbitrary number of
     |  steps. The state of the PCG-64 DXSM RNG is represented by 2 128-bit unsigned
     |  integers.
     |
     |  **State and Seeding**
     |
     |  The ``PCG64DXSM`` state vector consists of 2 unsigned 128-bit values,
     |  which are represented externally as Python ints. One is the state of the
     |  PRNG, which is advanced by a linear congruential generator (LCG). The
     |  second is a fixed odd increment used in the LCG.
     |
     |  The input seed is processed by `SeedSequence` to generate both values. The
     |  increment is not independently settable.
     |
     |  **Parallel Features**
     |
     |  The preferred way to use a BitGenerator in parallel applications is to use
     |  the `SeedSequence.spawn` method to obtain entropy values, and to use these
     |  to generate new BitGenerators:
     |
     |  >>> from numpy.random import Generator, PCG64DXSM, SeedSequence
     |  >>> sg = SeedSequence(1234)
     |  >>> rg = [Generator(PCG64DXSM(s)) for s in sg.spawn(10)]
     |
     |  **Compatibility Guarantee**
     |
     |  ``PCG64DXSM`` makes a guarantee that a fixed seed will always produce
     |  the same random integer stream.
     |
     |  References
     |  ----------
     |  .. [1] `"PCG, A Family of Better Random Number Generators"
     |         <http://www.pcg-random.org/>`_
     |  .. [2] O'Neill, Melissa E. `"PCG: A Family of Simple Fast Space-Efficient
     |         Statistically Good Algorithms for Random Number Generation"
     |         <https://www.cs.hmc.edu/tr/hmc-cs-2014-0905.pdf>`_
     |
     |  Method resolution order:
     |      PCG64DXSM
     |      numpy.random.bit_generator.BitGenerator
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce_cython__(...)
     |
     |  __setstate_cython__(...)
     |
     |  advance(...)
     |      advance(delta)
     |
     |      Advance the underlying RNG as-if delta draws have occurred.
     |
     |      Parameters
     |      ----------
     |      delta : integer, positive
     |          Number of draws to advance the RNG. Must be less than the
     |          size state variable in the underlying RNG.
     |
     |      Returns
     |      -------
     |      self : PCG64
     |          RNG advanced delta steps
     |
     |      Notes
     |      -----
     |      Advancing a RNG updates the underlying RNG state as-if a given
     |      number of calls to the underlying RNG have been made. In general
     |      there is not a one-to-one relationship between the number output
     |      random values from a particular distribution and the number of
     |      draws from the core RNG.  This occurs for two reasons:
     |
     |      * The random values are simulated using a rejection-based method
     |        and so, on average, more than one value from the underlying
     |        RNG is required to generate an single draw.
     |      * The number of bits required to generate a simulated value
     |        differs from the number of bits generated by the underlying
     |        RNG.  For example, two 16-bit integer values can be simulated
     |        from a single draw of a 32-bit RNG.
     |
     |      Advancing the RNG state resets any pre-computed random numbers.
     |      This is required to ensure exact reproducibility.
     |
     |  jumped(...)
     |      jumped(jumps=1)
     |
     |      Returns a new bit generator with the state jumped.
     |
     |      Jumps the state as-if jumps * 210306068529402873165736369884012333109
     |      random numbers have been generated.
     |
     |      Parameters
     |      ----------
     |      jumps : integer, positive
     |          Number of times to jump the state of the bit generator returned
     |
     |      Returns
     |      -------
     |      bit_generator : PCG64DXSM
     |          New instance of generator jumped iter times
     |
     |      Notes
     |      -----
     |      The step size is phi-1 when multiplied by 2**128 where phi is the
     |      golden ratio.
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
     |  state
     |      Get or set the PRNG state
     |
     |      Returns
     |      -------
     |      state : dict
     |          Dictionary containing the information required to describe the
     |          state of the PRNG
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __pyx_vtable__ = <capsule object NULL>
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from numpy.random.bit_generator.BitGenerator:
     |
     |  __getstate__(...)
     |      Helper for pickle.
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __setstate__(...)
     |
     |  random_raw(...)
     |      random_raw(self, size=None)
     |
     |      Return randoms as generated by the underlying BitGenerator
     |
     |      Parameters
     |      ----------
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  Default is None, in which case a
     |          single value is returned.
     |      output : bool, optional
     |          Output values.  Used for performance testing since the generated
     |          values are not returned.
     |
     |      Returns
     |      -------
     |      out : uint or ndarray
     |          Drawn samples.
     |
     |      Notes
     |      -----
     |      This method directly exposes the raw underlying pseudo-random
     |      number generator. All values are returned as unsigned 64-bit
     |      values irrespective of the number of bits produced by the PRNG.
     |
     |      See the class docstring for the number of bits returned.
     |
     |  spawn(...)
     |      spawn(n_children)
     |
     |      Create new independent child bit generators.
     |
     |      See :ref:`seedsequence-spawn` for additional notes on spawning
     |      children.  Some bit generators also implement ``jumped``
     |      as a different approach for creating independent streams.
     |
     |      .. versionadded:: 1.25.0
     |
     |      Parameters
     |      ----------
     |      n_children : int
     |
     |      Returns
     |      -------
     |      child_bit_generators : list of BitGenerators
     |
     |      Raises
     |      ------
     |      TypeError
     |          When the underlying SeedSequence does not implement spawning.
     |
     |      See Also
     |      --------
     |      random.Generator.spawn, random.SeedSequence.spawn :
     |          Equivalent method on the generator and seed sequence.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from numpy.random.bit_generator.BitGenerator:
     |
     |  capsule
     |
     |  cffi
     |      CFFI interface
     |
     |      Returns
     |      -------
     |      interface : namedtuple
     |          Named tuple containing CFFI wrapper
     |
     |          * state_address - Memory address of the state struct
     |          * state - pointer to the state struct
     |          * next_uint64 - function pointer to produce 64 bit integers
     |          * next_uint32 - function pointer to produce 32 bit integers
     |          * next_double - function pointer to produce doubles
     |          * bitgen - pointer to the bit generator struct
     |
     |  ctypes
     |      ctypes interface
     |
     |      Returns
     |      -------
     |      interface : namedtuple
     |          Named tuple containing ctypes wrapper
     |
     |          * state_address - Memory address of the state struct
     |          * state - pointer to the state struct
     |          * next_uint64 - function pointer to produce 64 bit integers
     |          * next_uint32 - function pointer to produce 32 bit integers
     |          * next_double - function pointer to produce doubles
     |          * bitgen - pointer to the bit generator struct
     |
     |  lock
     |
     |  seed_seq
     |      Get the seed sequence used to initialize the bit generator.
     |
     |      .. versionadded:: 1.25.0
     |
     |      Returns
     |      -------
     |      seed_seq : ISeedSequence
     |          The SeedSequence object used to initialize the BitGenerator.
     |          This is normally a `np.random.SeedSequence` instance.

    class Philox(numpy.random.bit_generator.BitGenerator)
     |  Philox(seed=None, counter=None, key=None)
     |
     |  Container for the Philox (4x64) pseudo-random number generator.
     |
     |  Parameters
     |  ----------
     |  seed : {None, int, array_like[ints], SeedSequence}, optional
     |      A seed to initialize the `BitGenerator`. If None, then fresh,
     |      unpredictable entropy will be pulled from the OS. If an ``int`` or
     |      ``array_like[ints]`` is passed, then it will be passed to
     |      `SeedSequence` to derive the initial `BitGenerator` state. One may also
     |      pass in a `SeedSequence` instance.
     |  counter : {None, int, array_like}, optional
     |      Counter to use in the Philox state. Can be either
     |      a Python int (long in 2.x) in [0, 2**256) or a 4-element uint64 array.
     |      If not provided, the RNG is initialized at 0.
     |  key : {None, int, array_like}, optional
     |      Key to use in the Philox state.  Unlike ``seed``, the value in key is
     |      directly set. Can be either a Python int in [0, 2**128) or a 2-element
     |      uint64 array. `key` and ``seed`` cannot both be used.
     |
     |  Attributes
     |  ----------
     |  lock: threading.Lock
     |      Lock instance that is shared so that the same bit git generator can
     |      be used in multiple Generators without corrupting the state. Code that
     |      generates values from a bit generator should hold the bit generator's
     |      lock.
     |
     |  Notes
     |  -----
     |  Philox is a 64-bit PRNG that uses a counter-based design based on weaker
     |  (and faster) versions of cryptographic functions [1]_. Instances using
     |  different values of the key produce independent sequences.  Philox has a
     |  period of :math:`2^{256} - 1` and supports arbitrary advancing and jumping
     |  the sequence in increments of :math:`2^{128}`. These features allow
     |  multiple non-overlapping sequences to be generated.
     |
     |  ``Philox`` provides a capsule containing function pointers that produce
     |  doubles, and unsigned 32 and 64- bit integers. These are not
     |  directly consumable in Python and must be consumed by a ``Generator``
     |  or similar object that supports low-level access.
     |
     |  **State and Seeding**
     |
     |  The ``Philox`` state vector consists of a 256-bit value encoded as
     |  a 4-element uint64 array and a 128-bit value encoded as a 2-element uint64
     |  array. The former is a counter which is incremented by 1 for every 4 64-bit
     |  randoms produced. The second is a key which determined the sequence
     |  produced. Using different keys produces independent sequences.
     |
     |  The input ``seed`` is processed by `SeedSequence` to generate the key. The
     |  counter is set to 0.
     |
     |  Alternately, one can omit the ``seed`` parameter and set the ``key`` and
     |  ``counter`` directly.
     |
     |  **Parallel Features**
     |
     |  The preferred way to use a BitGenerator in parallel applications is to use
     |  the `SeedSequence.spawn` method to obtain entropy values, and to use these
     |  to generate new BitGenerators:
     |
     |  >>> from numpy.random import Generator, Philox, SeedSequence
     |  >>> sg = SeedSequence(1234)
     |  >>> rg = [Generator(Philox(s)) for s in sg.spawn(10)]
     |
     |  ``Philox`` can be used in parallel applications by calling the ``jumped``
     |  method  to advances the state as-if :math:`2^{128}` random numbers have
     |  been generated. Alternatively, ``advance`` can be used to advance the
     |  counter for any positive step in [0, 2**256). When using ``jumped``, all
     |  generators should be chained to ensure that the segments come from the same
     |  sequence.
     |
     |  >>> from numpy.random import Generator, Philox
     |  >>> bit_generator = Philox(1234)
     |  >>> rg = []
     |  >>> for _ in range(10):
     |  ...    rg.append(Generator(bit_generator))
     |  ...    bit_generator = bit_generator.jumped()
     |
     |  Alternatively, ``Philox`` can be used in parallel applications by using
     |  a sequence of distinct keys where each instance uses different key.
     |
     |  >>> key = 2**96 + 2**33 + 2**17 + 2**9
     |  >>> rg = [Generator(Philox(key=key+i)) for i in range(10)]
     |
     |  **Compatibility Guarantee**
     |
     |  ``Philox`` makes a guarantee that a fixed ``seed`` will always produce
     |  the same random integer stream.
     |
     |  Examples
     |  --------
     |  >>> from numpy.random import Generator, Philox
     |  >>> rg = Generator(Philox(1234))
     |  >>> rg.standard_normal()
     |  0.123  # random
     |
     |  References
     |  ----------
     |  .. [1] John K. Salmon, Mark A. Moraes, Ron O. Dror, and David E. Shaw,
     |         "Parallel Random Numbers: As Easy as 1, 2, 3," Proceedings of
     |         the International Conference for High Performance Computing,
     |         Networking, Storage and Analysis (SC11), New York, NY: ACM, 2011.
     |
     |  Method resolution order:
     |      Philox
     |      numpy.random.bit_generator.BitGenerator
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce_cython__(...)
     |
     |  __setstate_cython__(...)
     |
     |  advance(...)
     |      advance(delta)
     |
     |      Advance the underlying RNG as-if delta draws have occurred.
     |
     |      Parameters
     |      ----------
     |      delta : integer, positive
     |          Number of draws to advance the RNG. Must be less than the
     |          size state variable in the underlying RNG.
     |
     |      Returns
     |      -------
     |      self : Philox
     |          RNG advanced delta steps
     |
     |      Notes
     |      -----
     |      Advancing a RNG updates the underlying RNG state as-if a given
     |      number of calls to the underlying RNG have been made. In general
     |      there is not a one-to-one relationship between the number output
     |      random values from a particular distribution and the number of
     |      draws from the core RNG.  This occurs for two reasons:
     |
     |      * The random values are simulated using a rejection-based method
     |        and so, on average, more than one value from the underlying
     |        RNG is required to generate an single draw.
     |      * The number of bits required to generate a simulated value
     |        differs from the number of bits generated by the underlying
     |        RNG.  For example, two 16-bit integer values can be simulated
     |        from a single draw of a 32-bit RNG.
     |
     |      Advancing the RNG state resets any pre-computed random numbers.
     |      This is required to ensure exact reproducibility.
     |
     |  jumped(...)
     |      jumped(jumps=1)
     |
     |      Returns a new bit generator with the state jumped
     |
     |      The state of the returned bit generator is jumped as-if
     |      (2**128) * jumps random numbers have been generated.
     |
     |      Parameters
     |      ----------
     |      jumps : integer, positive
     |          Number of times to jump the state of the bit generator returned
     |
     |      Returns
     |      -------
     |      bit_generator : Philox
     |          New instance of generator jumped iter times
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
     |  state
     |      Get or set the PRNG state
     |
     |      Returns
     |      -------
     |      state : dict
     |          Dictionary containing the information required to describe the
     |          state of the PRNG
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __pyx_vtable__ = <capsule object NULL>
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from numpy.random.bit_generator.BitGenerator:
     |
     |  __getstate__(...)
     |      Helper for pickle.
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __setstate__(...)
     |
     |  random_raw(...)
     |      random_raw(self, size=None)
     |
     |      Return randoms as generated by the underlying BitGenerator
     |
     |      Parameters
     |      ----------
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  Default is None, in which case a
     |          single value is returned.
     |      output : bool, optional
     |          Output values.  Used for performance testing since the generated
     |          values are not returned.
     |
     |      Returns
     |      -------
     |      out : uint or ndarray
     |          Drawn samples.
     |
     |      Notes
     |      -----
     |      This method directly exposes the raw underlying pseudo-random
     |      number generator. All values are returned as unsigned 64-bit
     |      values irrespective of the number of bits produced by the PRNG.
     |
     |      See the class docstring for the number of bits returned.
     |
     |  spawn(...)
     |      spawn(n_children)
     |
     |      Create new independent child bit generators.
     |
     |      See :ref:`seedsequence-spawn` for additional notes on spawning
     |      children.  Some bit generators also implement ``jumped``
     |      as a different approach for creating independent streams.
     |
     |      .. versionadded:: 1.25.0
     |
     |      Parameters
     |      ----------
     |      n_children : int
     |
     |      Returns
     |      -------
     |      child_bit_generators : list of BitGenerators
     |
     |      Raises
     |      ------
     |      TypeError
     |          When the underlying SeedSequence does not implement spawning.
     |
     |      See Also
     |      --------
     |      random.Generator.spawn, random.SeedSequence.spawn :
     |          Equivalent method on the generator and seed sequence.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from numpy.random.bit_generator.BitGenerator:
     |
     |  capsule
     |
     |  cffi
     |      CFFI interface
     |
     |      Returns
     |      -------
     |      interface : namedtuple
     |          Named tuple containing CFFI wrapper
     |
     |          * state_address - Memory address of the state struct
     |          * state - pointer to the state struct
     |          * next_uint64 - function pointer to produce 64 bit integers
     |          * next_uint32 - function pointer to produce 32 bit integers
     |          * next_double - function pointer to produce doubles
     |          * bitgen - pointer to the bit generator struct
     |
     |  ctypes
     |      ctypes interface
     |
     |      Returns
     |      -------
     |      interface : namedtuple
     |          Named tuple containing ctypes wrapper
     |
     |          * state_address - Memory address of the state struct
     |          * state - pointer to the state struct
     |          * next_uint64 - function pointer to produce 64 bit integers
     |          * next_uint32 - function pointer to produce 32 bit integers
     |          * next_double - function pointer to produce doubles
     |          * bitgen - pointer to the bit generator struct
     |
     |  lock
     |
     |  seed_seq
     |      Get the seed sequence used to initialize the bit generator.
     |
     |      .. versionadded:: 1.25.0
     |
     |      Returns
     |      -------
     |      seed_seq : ISeedSequence
     |          The SeedSequence object used to initialize the BitGenerator.
     |          This is normally a `np.random.SeedSequence` instance.

    class RandomState(builtins.object)
     |  RandomState(seed=None)
     |
     |  Container for the slow Mersenne Twister pseudo-random number generator.
     |  Consider using a different BitGenerator with the Generator container
     |  instead.
     |
     |  `RandomState` and `Generator` expose a number of methods for generating
     |  random numbers drawn from a variety of probability distributions. In
     |  addition to the distribution-specific arguments, each method takes a
     |  keyword argument `size` that defaults to ``None``. If `size` is ``None``,
     |  then a single value is generated and returned. If `size` is an integer,
     |  then a 1-D array filled with generated values is returned. If `size` is a
     |  tuple, then an array with that shape is filled and returned.
     |
     |  **Compatibility Guarantee**
     |
     |  A fixed bit generator using a fixed seed and a fixed series of calls to
     |  'RandomState' methods using the same parameters will always produce the
     |  same results up to roundoff error except when the values were incorrect.
     |  `RandomState` is effectively frozen and will only receive updates that
     |  are required by changes in the internals of Numpy. More substantial
     |  changes, including algorithmic improvements, are reserved for
     |  `Generator`.
     |
     |  Parameters
     |  ----------
     |  seed : {None, int, array_like, BitGenerator}, optional
     |      Random seed used to initialize the pseudo-random number generator or
     |      an instantized BitGenerator.  If an integer or array, used as a seed for
     |      the MT19937 BitGenerator. Values can be any integer between 0 and
     |      2**32 - 1 inclusive, an array (or other sequence) of such integers,
     |      or ``None`` (the default).  If `seed` is ``None``, then the `MT19937`
     |      BitGenerator is initialized by reading data from ``/dev/urandom``
     |      (or the Windows analogue) if available or seed from the clock
     |      otherwise.
     |
     |  Notes
     |  -----
     |  The Python stdlib module "random" also contains a Mersenne Twister
     |  pseudo-random number generator with a number of methods that are similar
     |  to the ones available in `RandomState`. `RandomState`, besides being
     |  NumPy-aware, has the advantage that it provides a much larger number
     |  of probability distributions to choose from.
     |
     |  See Also
     |  --------
     |  Generator
     |  MT19937
     |  numpy.random.BitGenerator
     |
     |  Methods defined here:
     |
     |  __getstate__(...)
     |      Helper for pickle.
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __repr__(...)
     |      Return repr(self).
     |
     |  __setstate__(...)
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  beta(...)
     |      beta(a, b, size=None)
     |
     |      Draw samples from a Beta distribution.
     |
     |      The Beta distribution is a special case of the Dirichlet distribution,
     |      and is related to the Gamma distribution.  It has the probability
     |      distribution function
     |
     |      .. math:: f(x; a,b) = \frac{1}{B(\alpha, \beta)} x^{\alpha - 1}
     |                                                       (1 - x)^{\beta - 1},
     |
     |      where the normalization, B, is the beta function,
     |
     |      .. math:: B(\alpha, \beta) = \int_0^1 t^{\alpha - 1}
     |                                   (1 - t)^{\beta - 1} dt.
     |
     |      It is often seen in Bayesian inference and order statistics.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.beta`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |
     |      Parameters
     |      ----------
     |      a : float or array_like of floats
     |          Alpha, positive (>0).
     |      b : float or array_like of floats
     |          Beta, positive (>0).
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``a`` and ``b`` are both scalars.
     |          Otherwise, ``np.broadcast(a, b).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized beta distribution.
     |
     |      See Also
     |      --------
     |      random.Generator.beta: which should be used for new code.
     |
     |  binomial(...)
     |      binomial(n, p, size=None)
     |
     |      Draw samples from a binomial distribution.
     |
     |      Samples are drawn from a binomial distribution with specified
     |      parameters, n trials and p probability of success where
     |      n an integer >= 0 and p is in the interval [0,1]. (n may be
     |      input as a float, but it is truncated to an integer in use)
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.binomial`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      n : int or array_like of ints
     |          Parameter of the distribution, >= 0. Floats are also accepted,
     |          but they will be truncated to integers.
     |      p : float or array_like of floats
     |          Parameter of the distribution, >= 0 and <=1.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``n`` and ``p`` are both scalars.
     |          Otherwise, ``np.broadcast(n, p).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized binomial distribution, where
     |          each sample is equal to the number of successes over the n trials.
     |
     |      See Also
     |      --------
     |      scipy.stats.binom : probability density function, distribution or
     |          cumulative density function, etc.
     |      random.Generator.binomial: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The probability density for the binomial distribution is
     |
     |      .. math:: P(N) = \binom{n}{N}p^N(1-p)^{n-N},
     |
     |      where :math:`n` is the number of trials, :math:`p` is the probability
     |      of success, and :math:`N` is the number of successes.
     |
     |      When estimating the standard error of a proportion in a population by
     |      using a random sample, the normal distribution works well unless the
     |      product p*n <=5, where p = population proportion estimate, and n =
     |      number of samples, in which case the binomial distribution is used
     |      instead. For example, a sample of 15 people shows 4 who are left
     |      handed, and 11 who are right handed. Then p = 4/15 = 27%. 0.27*15 = 4,
     |      so the binomial distribution should be used in this case.
     |
     |      References
     |      ----------
     |      .. [1] Dalgaard, Peter, "Introductory Statistics with R",
     |             Springer-Verlag, 2002.
     |      .. [2] Glantz, Stanton A. "Primer of Biostatistics.", McGraw-Hill,
     |             Fifth Edition, 2002.
     |      .. [3] Lentner, Marvin, "Elementary Applied Statistics", Bogden
     |             and Quigley, 1972.
     |      .. [4] Weisstein, Eric W. "Binomial Distribution." From MathWorld--A
     |             Wolfram Web Resource.
     |             http://mathworld.wolfram.com/BinomialDistribution.html
     |      .. [5] Wikipedia, "Binomial distribution",
     |             https://en.wikipedia.org/wiki/Binomial_distribution
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> n, p = 10, .5  # number of trials, probability of each trial
     |      >>> s = np.random.binomial(n, p, 1000)
     |      # result of flipping a coin 10 times, tested 1000 times.
     |
     |      A real world example. A company drills 9 wild-cat oil exploration
     |      wells, each with an estimated probability of success of 0.1. All nine
     |      wells fail. What is the probability of that happening?
     |
     |      Let's do 20,000 trials of the model, and count the number that
     |      generate zero positive results.
     |
     |      >>> sum(np.random.binomial(9, 0.1, 20000) == 0)/20000.
     |      # answer = 0.38885, or 38%.
     |
     |  bytes(...)
     |      bytes(length)
     |
     |      Return random bytes.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.bytes`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      length : int
     |          Number of random bytes.
     |
     |      Returns
     |      -------
     |      out : bytes
     |          String of length `length`.
     |
     |      See Also
     |      --------
     |      random.Generator.bytes: which should be used for new code.
     |
     |      Examples
     |      --------
     |      >>> np.random.bytes(10)
     |      b' eh\x85\x022SZ\xbf\xa4' #random
     |
     |  chisquare(...)
     |      chisquare(df, size=None)
     |
     |      Draw samples from a chi-square distribution.
     |
     |      When `df` independent random variables, each with standard normal
     |      distributions (mean 0, variance 1), are squared and summed, the
     |      resulting distribution is chi-square (see Notes).  This distribution
     |      is often used in hypothesis testing.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.chisquare`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      df : float or array_like of floats
     |           Number of degrees of freedom, must be > 0.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``df`` is a scalar.  Otherwise,
     |          ``np.array(df).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized chi-square distribution.
     |
     |      Raises
     |      ------
     |      ValueError
     |          When `df` <= 0 or when an inappropriate `size` (e.g. ``size=-1``)
     |          is given.
     |
     |      See Also
     |      --------
     |      random.Generator.chisquare: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The variable obtained by summing the squares of `df` independent,
     |      standard normally distributed random variables:
     |
     |      .. math:: Q = \sum_{i=0}^{\mathtt{df}} X^2_i
     |
     |      is chi-square distributed, denoted
     |
     |      .. math:: Q \sim \chi^2_k.
     |
     |      The probability density function of the chi-squared distribution is
     |
     |      .. math:: p(x) = \frac{(1/2)^{k/2}}{\Gamma(k/2)}
     |                       x^{k/2 - 1} e^{-x/2},
     |
     |      where :math:`\Gamma` is the gamma function,
     |
     |      .. math:: \Gamma(x) = \int_0^{-\infty} t^{x - 1} e^{-t} dt.
     |
     |      References
     |      ----------
     |      .. [1] NIST "Engineering Statistics Handbook"
     |             https://www.itl.nist.gov/div898/handbook/eda/section3/eda3666.htm
     |
     |      Examples
     |      --------
     |      >>> np.random.chisquare(2,4)
     |      array([ 1.89920014,  9.00867716,  3.13710533,  5.62318272]) # random
     |
     |  choice(...)
     |      choice(a, size=None, replace=True, p=None)
     |
     |      Generates a random sample from a given 1-D array
     |
     |      .. versionadded:: 1.7.0
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.choice`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      a : 1-D array-like or int
     |          If an ndarray, a random sample is generated from its elements.
     |          If an int, the random sample is generated as if it were ``np.arange(a)``
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  Default is None, in which case a
     |          single value is returned.
     |      replace : boolean, optional
     |          Whether the sample is with or without replacement. Default is True,
     |          meaning that a value of ``a`` can be selected multiple times.
     |      p : 1-D array-like, optional
     |          The probabilities associated with each entry in a.
     |          If not given, the sample assumes a uniform distribution over all
     |          entries in ``a``.
     |
     |      Returns
     |      -------
     |      samples : single item or ndarray
     |          The generated random samples
     |
     |      Raises
     |      ------
     |      ValueError
     |          If a is an int and less than zero, if a or p are not 1-dimensional,
     |          if a is an array-like of size 0, if p is not a vector of
     |          probabilities, if a and p have different lengths, or if
     |          replace=False and the sample size is greater than the population
     |          size
     |
     |      See Also
     |      --------
     |      randint, shuffle, permutation
     |      random.Generator.choice: which should be used in new code
     |
     |      Notes
     |      -----
     |      Setting user-specified probabilities through ``p`` uses a more general but less
     |      efficient sampler than the default. The general sampler produces a different sample
     |      than the optimized sampler even if each element of ``p`` is 1 / len(a).
     |
     |      Sampling random rows from a 2-D array is not possible with this function,
     |      but is possible with `Generator.choice` through its ``axis`` keyword.
     |
     |      Examples
     |      --------
     |      Generate a uniform random sample from np.arange(5) of size 3:
     |
     |      >>> np.random.choice(5, 3)
     |      array([0, 3, 4]) # random
     |      >>> #This is equivalent to np.random.randint(0,5,3)
     |
     |      Generate a non-uniform random sample from np.arange(5) of size 3:
     |
     |      >>> np.random.choice(5, 3, p=[0.1, 0, 0.3, 0.6, 0])
     |      array([3, 3, 0]) # random
     |
     |      Generate a uniform random sample from np.arange(5) of size 3 without
     |      replacement:
     |
     |      >>> np.random.choice(5, 3, replace=False)
     |      array([3,1,0]) # random
     |      >>> #This is equivalent to np.random.permutation(np.arange(5))[:3]
     |
     |      Generate a non-uniform random sample from np.arange(5) of size
     |      3 without replacement:
     |
     |      >>> np.random.choice(5, 3, replace=False, p=[0.1, 0, 0.3, 0.6, 0])
     |      array([2, 3, 0]) # random
     |
     |      Any of the above can be repeated with an arbitrary array-like
     |      instead of just integers. For instance:
     |
     |      >>> aa_milne_arr = ['pooh', 'rabbit', 'piglet', 'Christopher']
     |      >>> np.random.choice(aa_milne_arr, 5, p=[0.5, 0.1, 0.1, 0.3])
     |      array(['pooh', 'pooh', 'pooh', 'Christopher', 'piglet'], # random
     |            dtype='<U11')
     |
     |  dirichlet(...)
     |      dirichlet(alpha, size=None)
     |
     |      Draw samples from the Dirichlet distribution.
     |
     |      Draw `size` samples of dimension k from a Dirichlet distribution. A
     |      Dirichlet-distributed random variable can be seen as a multivariate
     |      generalization of a Beta distribution. The Dirichlet distribution
     |      is a conjugate prior of a multinomial distribution in Bayesian
     |      inference.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.dirichlet`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      alpha : sequence of floats, length k
     |          Parameter of the distribution (length ``k`` for sample of
     |          length ``k``).
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n)``, then
     |          ``m * n * k`` samples are drawn.  Default is None, in which case a
     |          vector of length ``k`` is returned.
     |
     |      Returns
     |      -------
     |      samples : ndarray,
     |          The drawn samples, of shape ``(size, k)``.
     |
     |      Raises
     |      ------
     |      ValueError
     |          If any value in ``alpha`` is less than or equal to zero
     |
     |      See Also
     |      --------
     |      random.Generator.dirichlet: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The Dirichlet distribution is a distribution over vectors
     |      :math:`x` that fulfil the conditions :math:`x_i>0` and
     |      :math:`\sum_{i=1}^k x_i = 1`.
     |
     |      The probability density function :math:`p` of a
     |      Dirichlet-distributed random vector :math:`X` is
     |      proportional to
     |
     |      .. math:: p(x) \propto \prod_{i=1}^{k}{x^{\alpha_i-1}_i},
     |
     |      where :math:`\alpha` is a vector containing the positive
     |      concentration parameters.
     |
     |      The method uses the following property for computation: let :math:`Y`
     |      be a random vector which has components that follow a standard gamma
     |      distribution, then :math:`X = \frac{1}{\sum_{i=1}^k{Y_i}} Y`
     |      is Dirichlet-distributed
     |
     |      References
     |      ----------
     |      .. [1] David McKay, "Information Theory, Inference and Learning
     |             Algorithms," chapter 23,
     |             http://www.inference.org.uk/mackay/itila/
     |      .. [2] Wikipedia, "Dirichlet distribution",
     |             https://en.wikipedia.org/wiki/Dirichlet_distribution
     |
     |      Examples
     |      --------
     |      Taking an example cited in Wikipedia, this distribution can be used if
     |      one wanted to cut strings (each of initial length 1.0) into K pieces
     |      with different lengths, where each piece had, on average, a designated
     |      average length, but allowing some variation in the relative sizes of
     |      the pieces.
     |
     |      >>> s = np.random.dirichlet((10, 5, 3), 20).transpose()
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> plt.barh(range(20), s[0])
     |      >>> plt.barh(range(20), s[1], left=s[0], color='g')
     |      >>> plt.barh(range(20), s[2], left=s[0]+s[1], color='r')
     |      >>> plt.title("Lengths of Strings")
     |
     |  exponential(...)
     |      exponential(scale=1.0, size=None)
     |
     |      Draw samples from an exponential distribution.
     |
     |      Its probability density function is
     |
     |      .. math:: f(x; \frac{1}{\beta}) = \frac{1}{\beta} \exp(-\frac{x}{\beta}),
     |
     |      for ``x > 0`` and 0 elsewhere. :math:`\beta` is the scale parameter,
     |      which is the inverse of the rate parameter :math:`\lambda = 1/\beta`.
     |      The rate parameter is an alternative, widely used parameterization
     |      of the exponential distribution [3]_.
     |
     |      The exponential distribution is a continuous analogue of the
     |      geometric distribution.  It describes many common situations, such as
     |      the size of raindrops measured over many rainstorms [1]_, or the time
     |      between page requests to Wikipedia [2]_.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.exponential`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      scale : float or array_like of floats
     |          The scale parameter, :math:`\beta = 1/\lambda`. Must be
     |          non-negative.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``scale`` is a scalar.  Otherwise,
     |          ``np.array(scale).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized exponential distribution.
     |
     |      Examples
     |      --------
     |      A real world example: Assume a company has 10000 customer support
     |      agents and the average time between customer calls is 4 minutes.
     |
     |      >>> n = 10000
     |      >>> time_between_calls = np.random.default_rng().exponential(scale=4, size=n)
     |
     |      What is the probability that a customer will call in the next
     |      4 to 5 minutes?
     |
     |      >>> x = ((time_between_calls < 5).sum())/n
     |      >>> y = ((time_between_calls < 4).sum())/n
     |      >>> x-y
     |      0.08 # may vary
     |
     |      See Also
     |      --------
     |      random.Generator.exponential: which should be used for new code.
     |
     |      References
     |      ----------
     |      .. [1] Peyton Z. Peebles Jr., "Probability, Random Variables and
     |             Random Signal Principles", 4th ed, 2001, p. 57.
     |      .. [2] Wikipedia, "Poisson process",
     |             https://en.wikipedia.org/wiki/Poisson_process
     |      .. [3] Wikipedia, "Exponential distribution",
     |             https://en.wikipedia.org/wiki/Exponential_distribution
     |
     |  f(...)
     |      f(dfnum, dfden, size=None)
     |
     |      Draw samples from an F distribution.
     |
     |      Samples are drawn from an F distribution with specified parameters,
     |      `dfnum` (degrees of freedom in numerator) and `dfden` (degrees of
     |      freedom in denominator), where both parameters must be greater than
     |      zero.
     |
     |      The random variate of the F distribution (also known as the
     |      Fisher distribution) is a continuous probability distribution
     |      that arises in ANOVA tests, and is the ratio of two chi-square
     |      variates.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.f`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      dfnum : float or array_like of floats
     |          Degrees of freedom in numerator, must be > 0.
     |      dfden : float or array_like of float
     |          Degrees of freedom in denominator, must be > 0.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``dfnum`` and ``dfden`` are both scalars.
     |          Otherwise, ``np.broadcast(dfnum, dfden).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized Fisher distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.f : probability density function, distribution or
     |          cumulative density function, etc.
     |      random.Generator.f: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The F statistic is used to compare in-group variances to between-group
     |      variances. Calculating the distribution depends on the sampling, and
     |      so it is a function of the respective degrees of freedom in the
     |      problem.  The variable `dfnum` is the number of samples minus one, the
     |      between-groups degrees of freedom, while `dfden` is the within-groups
     |      degrees of freedom, the sum of the number of samples in each group
     |      minus the number of groups.
     |
     |      References
     |      ----------
     |      .. [1] Glantz, Stanton A. "Primer of Biostatistics.", McGraw-Hill,
     |             Fifth Edition, 2002.
     |      .. [2] Wikipedia, "F-distribution",
     |             https://en.wikipedia.org/wiki/F-distribution
     |
     |      Examples
     |      --------
     |      An example from Glantz[1], pp 47-40:
     |
     |      Two groups, children of diabetics (25 people) and children from people
     |      without diabetes (25 controls). Fasting blood glucose was measured,
     |      case group had a mean value of 86.1, controls had a mean value of
     |      82.2. Standard deviations were 2.09 and 2.49 respectively. Are these
     |      data consistent with the null hypothesis that the parents diabetic
     |      status does not affect their children's blood glucose levels?
     |      Calculating the F statistic from the data gives a value of 36.01.
     |
     |      Draw samples from the distribution:
     |
     |      >>> dfnum = 1. # between group degrees of freedom
     |      >>> dfden = 48. # within groups degrees of freedom
     |      >>> s = np.random.f(dfnum, dfden, 1000)
     |
     |      The lower bound for the top 1% of the samples is :
     |
     |      >>> np.sort(s)[-10]
     |      7.61988120985 # random
     |
     |      So there is about a 1% chance that the F statistic will exceed 7.62,
     |      the measured value is 36, so the null hypothesis is rejected at the 1%
     |      level.
     |
     |  gamma(...)
     |      gamma(shape, scale=1.0, size=None)
     |
     |      Draw samples from a Gamma distribution.
     |
     |      Samples are drawn from a Gamma distribution with specified parameters,
     |      `shape` (sometimes designated "k") and `scale` (sometimes designated
     |      "theta"), where both parameters are > 0.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.gamma`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      shape : float or array_like of floats
     |          The shape of the gamma distribution. Must be non-negative.
     |      scale : float or array_like of floats, optional
     |          The scale of the gamma distribution. Must be non-negative.
     |          Default is equal to 1.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``shape`` and ``scale`` are both scalars.
     |          Otherwise, ``np.broadcast(shape, scale).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized gamma distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.gamma : probability density function, distribution or
     |          cumulative density function, etc.
     |      random.Generator.gamma: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The probability density for the Gamma distribution is
     |
     |      .. math:: p(x) = x^{k-1}\frac{e^{-x/\theta}}{\theta^k\Gamma(k)},
     |
     |      where :math:`k` is the shape and :math:`\theta` the scale,
     |      and :math:`\Gamma` is the Gamma function.
     |
     |      The Gamma distribution is often used to model the times to failure of
     |      electronic components, and arises naturally in processes for which the
     |      waiting times between Poisson distributed events are relevant.
     |
     |      References
     |      ----------
     |      .. [1] Weisstein, Eric W. "Gamma Distribution." From MathWorld--A
     |             Wolfram Web Resource.
     |             http://mathworld.wolfram.com/GammaDistribution.html
     |      .. [2] Wikipedia, "Gamma distribution",
     |             https://en.wikipedia.org/wiki/Gamma_distribution
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> shape, scale = 2., 2.  # mean=4, std=2*sqrt(2)
     |      >>> s = np.random.gamma(shape, scale, 1000)
     |
     |      Display the histogram of the samples, along with
     |      the probability density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> import scipy.special as sps  # doctest: +SKIP
     |      >>> count, bins, ignored = plt.hist(s, 50, density=True)
     |      >>> y = bins**(shape-1)*(np.exp(-bins/scale) /  # doctest: +SKIP
     |      ...                      (sps.gamma(shape)*scale**shape))
     |      >>> plt.plot(bins, y, linewidth=2, color='r')  # doctest: +SKIP
     |      >>> plt.show()
     |
     |  geometric(...)
     |      geometric(p, size=None)
     |
     |      Draw samples from the geometric distribution.
     |
     |      Bernoulli trials are experiments with one of two outcomes:
     |      success or failure (an example of such an experiment is flipping
     |      a coin).  The geometric distribution models the number of trials
     |      that must be run in order to achieve success.  It is therefore
     |      supported on the positive integers, ``k = 1, 2, ...``.
     |
     |      The probability mass function of the geometric distribution is
     |
     |      .. math:: f(k) = (1 - p)^{k - 1} p
     |
     |      where `p` is the probability of success of an individual trial.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.geometric`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      p : float or array_like of floats
     |          The probability of success of an individual trial.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``p`` is a scalar.  Otherwise,
     |          ``np.array(p).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized geometric distribution.
     |
     |      See Also
     |      --------
     |      random.Generator.geometric: which should be used for new code.
     |
     |      Examples
     |      --------
     |      Draw ten thousand values from the geometric distribution,
     |      with the probability of an individual success equal to 0.35:
     |
     |      >>> z = np.random.geometric(p=0.35, size=10000)
     |
     |      How many trials succeeded after a single run?
     |
     |      >>> (z == 1).sum() / 10000.
     |      0.34889999999999999 #random
     |
     |  get_state(...)
     |      get_state(legacy=True)
     |
     |      Return a tuple representing the internal state of the generator.
     |
     |      For more details, see `set_state`.
     |
     |      Parameters
     |      ----------
     |      legacy : bool, optional
     |          Flag indicating to return a legacy tuple state when the BitGenerator
     |          is MT19937, instead of a dict. Raises ValueError if the underlying
     |          bit generator is not an instance of MT19937.
     |
     |      Returns
     |      -------
     |      out : {tuple(str, ndarray of 624 uints, int, int, float), dict}
     |          If legacy is True, the returned tuple has the following items:
     |
     |          1. the string 'MT19937'.
     |          2. a 1-D array of 624 unsigned integer keys.
     |          3. an integer ``pos``.
     |          4. an integer ``has_gauss``.
     |          5. a float ``cached_gaussian``.
     |
     |          If `legacy` is False, or the BitGenerator is not MT19937, then
     |          state is returned as a dictionary.
     |
     |      See Also
     |      --------
     |      set_state
     |
     |      Notes
     |      -----
     |      `set_state` and `get_state` are not needed to work with any of the
     |      random distributions in NumPy. If the internal state is manually altered,
     |      the user should know exactly what he/she is doing.
     |
     |  gumbel(...)
     |      gumbel(loc=0.0, scale=1.0, size=None)
     |
     |      Draw samples from a Gumbel distribution.
     |
     |      Draw samples from a Gumbel distribution with specified location and
     |      scale.  For more information on the Gumbel distribution, see
     |      Notes and References below.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.gumbel`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      loc : float or array_like of floats, optional
     |          The location of the mode of the distribution. Default is 0.
     |      scale : float or array_like of floats, optional
     |          The scale parameter of the distribution. Default is 1. Must be non-
     |          negative.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``loc`` and ``scale`` are both scalars.
     |          Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized Gumbel distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.gumbel_l
     |      scipy.stats.gumbel_r
     |      scipy.stats.genextreme
     |      weibull
     |      random.Generator.gumbel: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The Gumbel (or Smallest Extreme Value (SEV) or the Smallest Extreme
     |      Value Type I) distribution is one of a class of Generalized Extreme
     |      Value (GEV) distributions used in modeling extreme value problems.
     |      The Gumbel is a special case of the Extreme Value Type I distribution
     |      for maximums from distributions with "exponential-like" tails.
     |
     |      The probability density for the Gumbel distribution is
     |
     |      .. math:: p(x) = \frac{e^{-(x - \mu)/ \beta}}{\beta} e^{ -e^{-(x - \mu)/
     |                \beta}},
     |
     |      where :math:`\mu` is the mode, a location parameter, and
     |      :math:`\beta` is the scale parameter.
     |
     |      The Gumbel (named for German mathematician Emil Julius Gumbel) was used
     |      very early in the hydrology literature, for modeling the occurrence of
     |      flood events. It is also used for modeling maximum wind speed and
     |      rainfall rates.  It is a "fat-tailed" distribution - the probability of
     |      an event in the tail of the distribution is larger than if one used a
     |      Gaussian, hence the surprisingly frequent occurrence of 100-year
     |      floods. Floods were initially modeled as a Gaussian process, which
     |      underestimated the frequency of extreme events.
     |
     |      It is one of a class of extreme value distributions, the Generalized
     |      Extreme Value (GEV) distributions, which also includes the Weibull and
     |      Frechet.
     |
     |      The function has a mean of :math:`\mu + 0.57721\beta` and a variance
     |      of :math:`\frac{\pi^2}{6}\beta^2`.
     |
     |      References
     |      ----------
     |      .. [1] Gumbel, E. J., "Statistics of Extremes,"
     |             New York: Columbia University Press, 1958.
     |      .. [2] Reiss, R.-D. and Thomas, M., "Statistical Analysis of Extreme
     |             Values from Insurance, Finance, Hydrology and Other Fields,"
     |             Basel: Birkhauser Verlag, 2001.
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> mu, beta = 0, 0.1 # location and scale
     |      >>> s = np.random.gumbel(mu, beta, 1000)
     |
     |      Display the histogram of the samples, along with
     |      the probability density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> count, bins, ignored = plt.hist(s, 30, density=True)
     |      >>> plt.plot(bins, (1/beta)*np.exp(-(bins - mu)/beta)
     |      ...          * np.exp( -np.exp( -(bins - mu) /beta) ),
     |      ...          linewidth=2, color='r')
     |      >>> plt.show()
     |
     |      Show how an extreme value distribution can arise from a Gaussian process
     |      and compare to a Gaussian:
     |
     |      >>> means = []
     |      >>> maxima = []
     |      >>> for i in range(0,1000) :
     |      ...    a = np.random.normal(mu, beta, 1000)
     |      ...    means.append(a.mean())
     |      ...    maxima.append(a.max())
     |      >>> count, bins, ignored = plt.hist(maxima, 30, density=True)
     |      >>> beta = np.std(maxima) * np.sqrt(6) / np.pi
     |      >>> mu = np.mean(maxima) - 0.57721*beta
     |      >>> plt.plot(bins, (1/beta)*np.exp(-(bins - mu)/beta)
     |      ...          * np.exp(-np.exp(-(bins - mu)/beta)),
     |      ...          linewidth=2, color='r')
     |      >>> plt.plot(bins, 1/(beta * np.sqrt(2 * np.pi))
     |      ...          * np.exp(-(bins - mu)**2 / (2 * beta**2)),
     |      ...          linewidth=2, color='g')
     |      >>> plt.show()
     |
     |  hypergeometric(...)
     |      hypergeometric(ngood, nbad, nsample, size=None)
     |
     |      Draw samples from a Hypergeometric distribution.
     |
     |      Samples are drawn from a hypergeometric distribution with specified
     |      parameters, `ngood` (ways to make a good selection), `nbad` (ways to make
     |      a bad selection), and `nsample` (number of items sampled, which is less
     |      than or equal to the sum ``ngood + nbad``).
     |
     |      .. note::
     |          New code should use the
     |          `~numpy.random.Generator.hypergeometric`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      ngood : int or array_like of ints
     |          Number of ways to make a good selection.  Must be nonnegative.
     |      nbad : int or array_like of ints
     |          Number of ways to make a bad selection.  Must be nonnegative.
     |      nsample : int or array_like of ints
     |          Number of items sampled.  Must be at least 1 and at most
     |          ``ngood + nbad``.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if `ngood`, `nbad`, and `nsample`
     |          are all scalars.  Otherwise, ``np.broadcast(ngood, nbad, nsample).size``
     |          samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized hypergeometric distribution. Each
     |          sample is the number of good items within a randomly selected subset of
     |          size `nsample` taken from a set of `ngood` good items and `nbad` bad items.
     |
     |      See Also
     |      --------
     |      scipy.stats.hypergeom : probability density function, distribution or
     |          cumulative density function, etc.
     |      random.Generator.hypergeometric: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The probability density for the Hypergeometric distribution is
     |
     |      .. math:: P(x) = \frac{\binom{g}{x}\binom{b}{n-x}}{\binom{g+b}{n}},
     |
     |      where :math:`0 \le x \le n` and :math:`n-b \le x \le g`
     |
     |      for P(x) the probability of ``x`` good results in the drawn sample,
     |      g = `ngood`, b = `nbad`, and n = `nsample`.
     |
     |      Consider an urn with black and white marbles in it, `ngood` of them
     |      are black and `nbad` are white. If you draw `nsample` balls without
     |      replacement, then the hypergeometric distribution describes the
     |      distribution of black balls in the drawn sample.
     |
     |      Note that this distribution is very similar to the binomial
     |      distribution, except that in this case, samples are drawn without
     |      replacement, whereas in the Binomial case samples are drawn with
     |      replacement (or the sample space is infinite). As the sample space
     |      becomes large, this distribution approaches the binomial.
     |
     |      References
     |      ----------
     |      .. [1] Lentner, Marvin, "Elementary Applied Statistics", Bogden
     |             and Quigley, 1972.
     |      .. [2] Weisstein, Eric W. "Hypergeometric Distribution." From
     |             MathWorld--A Wolfram Web Resource.
     |             http://mathworld.wolfram.com/HypergeometricDistribution.html
     |      .. [3] Wikipedia, "Hypergeometric distribution",
     |             https://en.wikipedia.org/wiki/Hypergeometric_distribution
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> ngood, nbad, nsamp = 100, 2, 10
     |      # number of good, number of bad, and number of samples
     |      >>> s = np.random.hypergeometric(ngood, nbad, nsamp, 1000)
     |      >>> from matplotlib.pyplot import hist
     |      >>> hist(s)
     |      #   note that it is very unlikely to grab both bad items
     |
     |      Suppose you have an urn with 15 white and 15 black marbles.
     |      If you pull 15 marbles at random, how likely is it that
     |      12 or more of them are one color?
     |
     |      >>> s = np.random.hypergeometric(15, 15, 15, 100000)
     |      >>> sum(s>=12)/100000. + sum(s<=3)/100000.
     |      #   answer = 0.003 ... pretty unlikely!
     |
     |  laplace(...)
     |      laplace(loc=0.0, scale=1.0, size=None)
     |
     |      Draw samples from the Laplace or double exponential distribution with
     |      specified location (or mean) and scale (decay).
     |
     |      The Laplace distribution is similar to the Gaussian/normal distribution,
     |      but is sharper at the peak and has fatter tails. It represents the
     |      difference between two independent, identically distributed exponential
     |      random variables.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.laplace`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      loc : float or array_like of floats, optional
     |          The position, :math:`\mu`, of the distribution peak. Default is 0.
     |      scale : float or array_like of floats, optional
     |          :math:`\lambda`, the exponential decay. Default is 1. Must be non-
     |          negative.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``loc`` and ``scale`` are both scalars.
     |          Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized Laplace distribution.
     |
     |      See Also
     |      --------
     |      random.Generator.laplace: which should be used for new code.
     |
     |      Notes
     |      -----
     |      It has the probability density function
     |
     |      .. math:: f(x; \mu, \lambda) = \frac{1}{2\lambda}
     |                                     \exp\left(-\frac{|x - \mu|}{\lambda}\right).
     |
     |      The first law of Laplace, from 1774, states that the frequency
     |      of an error can be expressed as an exponential function of the
     |      absolute magnitude of the error, which leads to the Laplace
     |      distribution. For many problems in economics and health
     |      sciences, this distribution seems to model the data better
     |      than the standard Gaussian distribution.
     |
     |      References
     |      ----------
     |      .. [1] Abramowitz, M. and Stegun, I. A. (Eds.). "Handbook of
     |             Mathematical Functions with Formulas, Graphs, and Mathematical
     |             Tables, 9th printing," New York: Dover, 1972.
     |      .. [2] Kotz, Samuel, et. al. "The Laplace Distribution and
     |             Generalizations, " Birkhauser, 2001.
     |      .. [3] Weisstein, Eric W. "Laplace Distribution."
     |             From MathWorld--A Wolfram Web Resource.
     |             http://mathworld.wolfram.com/LaplaceDistribution.html
     |      .. [4] Wikipedia, "Laplace distribution",
     |             https://en.wikipedia.org/wiki/Laplace_distribution
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution
     |
     |      >>> loc, scale = 0., 1.
     |      >>> s = np.random.laplace(loc, scale, 1000)
     |
     |      Display the histogram of the samples, along with
     |      the probability density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> count, bins, ignored = plt.hist(s, 30, density=True)
     |      >>> x = np.arange(-8., 8., .01)
     |      >>> pdf = np.exp(-abs(x-loc)/scale)/(2.*scale)
     |      >>> plt.plot(x, pdf)
     |
     |      Plot Gaussian for comparison:
     |
     |      >>> g = (1/(scale * np.sqrt(2 * np.pi)) *
     |      ...      np.exp(-(x - loc)**2 / (2 * scale**2)))
     |      >>> plt.plot(x,g)
     |
     |  logistic(...)
     |      logistic(loc=0.0, scale=1.0, size=None)
     |
     |      Draw samples from a logistic distribution.
     |
     |      Samples are drawn from a logistic distribution with specified
     |      parameters, loc (location or mean, also median), and scale (>0).
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.logistic`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      loc : float or array_like of floats, optional
     |          Parameter of the distribution. Default is 0.
     |      scale : float or array_like of floats, optional
     |          Parameter of the distribution. Must be non-negative.
     |          Default is 1.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``loc`` and ``scale`` are both scalars.
     |          Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized logistic distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.logistic : probability density function, distribution or
     |          cumulative density function, etc.
     |      random.Generator.logistic: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The probability density for the Logistic distribution is
     |
     |      .. math:: P(x) = P(x) = \frac{e^{-(x-\mu)/s}}{s(1+e^{-(x-\mu)/s})^2},
     |
     |      where :math:`\mu` = location and :math:`s` = scale.
     |
     |      The Logistic distribution is used in Extreme Value problems where it
     |      can act as a mixture of Gumbel distributions, in Epidemiology, and by
     |      the World Chess Federation (FIDE) where it is used in the Elo ranking
     |      system, assuming the performance of each player is a logistically
     |      distributed random variable.
     |
     |      References
     |      ----------
     |      .. [1] Reiss, R.-D. and Thomas M. (2001), "Statistical Analysis of
     |             Extreme Values, from Insurance, Finance, Hydrology and Other
     |             Fields," Birkhauser Verlag, Basel, pp 132-133.
     |      .. [2] Weisstein, Eric W. "Logistic Distribution." From
     |             MathWorld--A Wolfram Web Resource.
     |             http://mathworld.wolfram.com/LogisticDistribution.html
     |      .. [3] Wikipedia, "Logistic-distribution",
     |             https://en.wikipedia.org/wiki/Logistic_distribution
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> loc, scale = 10, 1
     |      >>> s = np.random.logistic(loc, scale, 10000)
     |      >>> import matplotlib.pyplot as plt
     |      >>> count, bins, ignored = plt.hist(s, bins=50)
     |
     |      #   plot against distribution
     |
     |      >>> def logist(x, loc, scale):
     |      ...     return np.exp((loc-x)/scale)/(scale*(1+np.exp((loc-x)/scale))**2)
     |      >>> lgst_val = logist(bins, loc, scale)
     |      >>> plt.plot(bins, lgst_val * count.max() / lgst_val.max())
     |      >>> plt.show()
     |
     |  lognormal(...)
     |      lognormal(mean=0.0, sigma=1.0, size=None)
     |
     |      Draw samples from a log-normal distribution.
     |
     |      Draw samples from a log-normal distribution with specified mean,
     |      standard deviation, and array shape.  Note that the mean and standard
     |      deviation are not the values for the distribution itself, but of the
     |      underlying normal distribution it is derived from.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.lognormal`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      mean : float or array_like of floats, optional
     |          Mean value of the underlying normal distribution. Default is 0.
     |      sigma : float or array_like of floats, optional
     |          Standard deviation of the underlying normal distribution. Must be
     |          non-negative. Default is 1.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``mean`` and ``sigma`` are both scalars.
     |          Otherwise, ``np.broadcast(mean, sigma).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized log-normal distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.lognorm : probability density function, distribution,
     |          cumulative density function, etc.
     |      random.Generator.lognormal: which should be used for new code.
     |
     |      Notes
     |      -----
     |      A variable `x` has a log-normal distribution if `log(x)` is normally
     |      distributed.  The probability density function for the log-normal
     |      distribution is:
     |
     |      .. math:: p(x) = \frac{1}{\sigma x \sqrt{2\pi}}
     |                       e^{(-\frac{(ln(x)-\mu)^2}{2\sigma^2})}
     |
     |      where :math:`\mu` is the mean and :math:`\sigma` is the standard
     |      deviation of the normally distributed logarithm of the variable.
     |      A log-normal distribution results if a random variable is the *product*
     |      of a large number of independent, identically-distributed variables in
     |      the same way that a normal distribution results if the variable is the
     |      *sum* of a large number of independent, identically-distributed
     |      variables.
     |
     |      References
     |      ----------
     |      .. [1] Limpert, E., Stahel, W. A., and Abbt, M., "Log-normal
     |             Distributions across the Sciences: Keys and Clues,"
     |             BioScience, Vol. 51, No. 5, May, 2001.
     |             https://stat.ethz.ch/~stahel/lognormal/bioscience.pdf
     |      .. [2] Reiss, R.D. and Thomas, M., "Statistical Analysis of Extreme
     |             Values," Basel: Birkhauser Verlag, 2001, pp. 31-32.
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> mu, sigma = 3., 1. # mean and standard deviation
     |      >>> s = np.random.lognormal(mu, sigma, 1000)
     |
     |      Display the histogram of the samples, along with
     |      the probability density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> count, bins, ignored = plt.hist(s, 100, density=True, align='mid')
     |
     |      >>> x = np.linspace(min(bins), max(bins), 10000)
     |      >>> pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
     |      ...        / (x * sigma * np.sqrt(2 * np.pi)))
     |
     |      >>> plt.plot(x, pdf, linewidth=2, color='r')
     |      >>> plt.axis('tight')
     |      >>> plt.show()
     |
     |      Demonstrate that taking the products of random samples from a uniform
     |      distribution can be fit well by a log-normal probability density
     |      function.
     |
     |      >>> # Generate a thousand samples: each is the product of 100 random
     |      >>> # values, drawn from a normal distribution.
     |      >>> b = []
     |      >>> for i in range(1000):
     |      ...    a = 10. + np.random.standard_normal(100)
     |      ...    b.append(np.prod(a))
     |
     |      >>> b = np.array(b) / np.min(b) # scale values to be positive
     |      >>> count, bins, ignored = plt.hist(b, 100, density=True, align='mid')
     |      >>> sigma = np.std(np.log(b))
     |      >>> mu = np.mean(np.log(b))
     |
     |      >>> x = np.linspace(min(bins), max(bins), 10000)
     |      >>> pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
     |      ...        / (x * sigma * np.sqrt(2 * np.pi)))
     |
     |      >>> plt.plot(x, pdf, color='r', linewidth=2)
     |      >>> plt.show()
     |
     |  logseries(...)
     |      logseries(p, size=None)
     |
     |      Draw samples from a logarithmic series distribution.
     |
     |      Samples are drawn from a log series distribution with specified
     |      shape parameter, 0 <= ``p`` < 1.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.logseries`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      p : float or array_like of floats
     |          Shape parameter for the distribution.  Must be in the range [0, 1).
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``p`` is a scalar.  Otherwise,
     |          ``np.array(p).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized logarithmic series distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.logser : probability density function, distribution or
     |          cumulative density function, etc.
     |      random.Generator.logseries: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The probability density for the Log Series distribution is
     |
     |      .. math:: P(k) = \frac{-p^k}{k \ln(1-p)},
     |
     |      where p = probability.
     |
     |      The log series distribution is frequently used to represent species
     |      richness and occurrence, first proposed by Fisher, Corbet, and
     |      Williams in 1943 [2].  It may also be used to model the numbers of
     |      occupants seen in cars [3].
     |
     |      References
     |      ----------
     |      .. [1] Buzas, Martin A.; Culver, Stephen J.,  Understanding regional
     |             species diversity through the log series distribution of
     |             occurrences: BIODIVERSITY RESEARCH Diversity & Distributions,
     |             Volume 5, Number 5, September 1999 , pp. 187-195(9).
     |      .. [2] Fisher, R.A,, A.S. Corbet, and C.B. Williams. 1943. The
     |             relation between the number of species and the number of
     |             individuals in a random sample of an animal population.
     |             Journal of Animal Ecology, 12:42-58.
     |      .. [3] D. J. Hand, F. Daly, D. Lunn, E. Ostrowski, A Handbook of Small
     |             Data Sets, CRC Press, 1994.
     |      .. [4] Wikipedia, "Logarithmic distribution",
     |             https://en.wikipedia.org/wiki/Logarithmic_distribution
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> a = .6
     |      >>> s = np.random.logseries(a, 10000)
     |      >>> import matplotlib.pyplot as plt
     |      >>> count, bins, ignored = plt.hist(s)
     |
     |      #   plot against distribution
     |
     |      >>> def logseries(k, p):
     |      ...     return -p**k/(k*np.log(1-p))
     |      >>> plt.plot(bins, logseries(bins, a)*count.max()/
     |      ...          logseries(bins, a).max(), 'r')
     |      >>> plt.show()
     |
     |  multinomial(...)
     |      multinomial(n, pvals, size=None)
     |
     |      Draw samples from a multinomial distribution.
     |
     |      The multinomial distribution is a multivariate generalization of the
     |      binomial distribution.  Take an experiment with one of ``p``
     |      possible outcomes.  An example of such an experiment is throwing a dice,
     |      where the outcome can be 1 through 6.  Each sample drawn from the
     |      distribution represents `n` such experiments.  Its values,
     |      ``X_i = [X_0, X_1, ..., X_p]``, represent the number of times the
     |      outcome was ``i``.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.multinomial`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      n : int
     |          Number of experiments.
     |      pvals : sequence of floats, length p
     |          Probabilities of each of the ``p`` different outcomes.  These
     |          must sum to 1 (however, the last element is always assumed to
     |          account for the remaining probability, as long as
     |          ``sum(pvals[:-1]) <= 1)``.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  Default is None, in which case a
     |          single value is returned.
     |
     |      Returns
     |      -------
     |      out : ndarray
     |          The drawn samples, of shape *size*, if that was provided.  If not,
     |          the shape is ``(N,)``.
     |
     |          In other words, each entry ``out[i,j,...,:]`` is an N-dimensional
     |          value drawn from the distribution.
     |
     |      See Also
     |      --------
     |      random.Generator.multinomial: which should be used for new code.
     |
     |      Examples
     |      --------
     |      Throw a dice 20 times:
     |
     |      >>> np.random.multinomial(20, [1/6.]*6, size=1)
     |      array([[4, 1, 7, 5, 2, 1]]) # random
     |
     |      It landed 4 times on 1, once on 2, etc.
     |
     |      Now, throw the dice 20 times, and 20 times again:
     |
     |      >>> np.random.multinomial(20, [1/6.]*6, size=2)
     |      array([[3, 4, 3, 3, 4, 3], # random
     |             [2, 4, 3, 4, 0, 7]])
     |
     |      For the first run, we threw 3 times 1, 4 times 2, etc.  For the second,
     |      we threw 2 times 1, 4 times 2, etc.
     |
     |      A loaded die is more likely to land on number 6:
     |
     |      >>> np.random.multinomial(100, [1/7.]*5 + [2/7.])
     |      array([11, 16, 14, 17, 16, 26]) # random
     |
     |      The probability inputs should be normalized. As an implementation
     |      detail, the value of the last entry is ignored and assumed to take
     |      up any leftover probability mass, but this should not be relied on.
     |      A biased coin which has twice as much weight on one side as on the
     |      other should be sampled like so:
     |
     |      >>> np.random.multinomial(100, [1.0 / 3, 2.0 / 3])  # RIGHT
     |      array([38, 62]) # random
     |
     |      not like:
     |
     |      >>> np.random.multinomial(100, [1.0, 2.0])  # WRONG
     |      Traceback (most recent call last):
     |      ValueError: pvals < 0, pvals > 1 or pvals contains NaNs
     |
     |  multivariate_normal(...)
     |      multivariate_normal(mean, cov, size=None, check_valid='warn', tol=1e-8)
     |
     |      Draw random samples from a multivariate normal distribution.
     |
     |      The multivariate normal, multinormal or Gaussian distribution is a
     |      generalization of the one-dimensional normal distribution to higher
     |      dimensions.  Such a distribution is specified by its mean and
     |      covariance matrix.  These parameters are analogous to the mean
     |      (average or "center") and variance (standard deviation, or "width,"
     |      squared) of the one-dimensional normal distribution.
     |
     |      .. note::
     |          New code should use the
     |          `~numpy.random.Generator.multivariate_normal`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      mean : 1-D array_like, of length N
     |          Mean of the N-dimensional distribution.
     |      cov : 2-D array_like, of shape (N, N)
     |          Covariance matrix of the distribution. It must be symmetric and
     |          positive-semidefinite for proper sampling.
     |      size : int or tuple of ints, optional
     |          Given a shape of, for example, ``(m,n,k)``, ``m*n*k`` samples are
     |          generated, and packed in an `m`-by-`n`-by-`k` arrangement.  Because
     |          each sample is `N`-dimensional, the output shape is ``(m,n,k,N)``.
     |          If no shape is specified, a single (`N`-D) sample is returned.
     |      check_valid : { 'warn', 'raise', 'ignore' }, optional
     |          Behavior when the covariance matrix is not positive semidefinite.
     |      tol : float, optional
     |          Tolerance when checking the singular values in covariance matrix.
     |          cov is cast to double before the check.
     |
     |      Returns
     |      -------
     |      out : ndarray
     |          The drawn samples, of shape *size*, if that was provided.  If not,
     |          the shape is ``(N,)``.
     |
     |          In other words, each entry ``out[i,j,...,:]`` is an N-dimensional
     |          value drawn from the distribution.
     |
     |      See Also
     |      --------
     |      random.Generator.multivariate_normal: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The mean is a coordinate in N-dimensional space, which represents the
     |      location where samples are most likely to be generated.  This is
     |      analogous to the peak of the bell curve for the one-dimensional or
     |      univariate normal distribution.
     |
     |      Covariance indicates the level to which two variables vary together.
     |      From the multivariate normal distribution, we draw N-dimensional
     |      samples, :math:`X = [x_1, x_2, ... x_N]`.  The covariance matrix
     |      element :math:`C_{ij}` is the covariance of :math:`x_i` and :math:`x_j`.
     |      The element :math:`C_{ii}` is the variance of :math:`x_i` (i.e. its
     |      "spread").
     |
     |      Instead of specifying the full covariance matrix, popular
     |      approximations include:
     |
     |        - Spherical covariance (`cov` is a multiple of the identity matrix)
     |        - Diagonal covariance (`cov` has non-negative elements, and only on
     |          the diagonal)
     |
     |      This geometrical property can be seen in two dimensions by plotting
     |      generated data-points:
     |
     |      >>> mean = [0, 0]
     |      >>> cov = [[1, 0], [0, 100]]  # diagonal covariance
     |
     |      Diagonal covariance means that points are oriented along x or y-axis:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> x, y = np.random.multivariate_normal(mean, cov, 5000).T
     |      >>> plt.plot(x, y, 'x')
     |      >>> plt.axis('equal')
     |      >>> plt.show()
     |
     |      Note that the covariance matrix must be positive semidefinite (a.k.a.
     |      nonnegative-definite). Otherwise, the behavior of this method is
     |      undefined and backwards compatibility is not guaranteed.
     |
     |      References
     |      ----------
     |      .. [1] Papoulis, A., "Probability, Random Variables, and Stochastic
     |             Processes," 3rd ed., New York: McGraw-Hill, 1991.
     |      .. [2] Duda, R. O., Hart, P. E., and Stork, D. G., "Pattern
     |             Classification," 2nd ed., New York: Wiley, 2001.
     |
     |      Examples
     |      --------
     |      >>> mean = (1, 2)
     |      >>> cov = [[1, 0], [0, 1]]
     |      >>> x = np.random.multivariate_normal(mean, cov, (3, 3))
     |      >>> x.shape
     |      (3, 3, 2)
     |
     |      Here we generate 800 samples from the bivariate normal distribution
     |      with mean [0, 0] and covariance matrix [[6, -3], [-3, 3.5]].  The
     |      expected variances of the first and second components of the sample
     |      are 6 and 3.5, respectively, and the expected correlation
     |      coefficient is -3/sqrt(6*3.5) ≈ -0.65465.
     |
     |      >>> cov = np.array([[6, -3], [-3, 3.5]])
     |      >>> pts = np.random.multivariate_normal([0, 0], cov, size=800)
     |
     |      Check that the mean, covariance, and correlation coefficient of the
     |      sample are close to the expected values:
     |
     |      >>> pts.mean(axis=0)
     |      array([ 0.0326911 , -0.01280782])  # may vary
     |      >>> np.cov(pts.T)
     |      array([[ 5.96202397, -2.85602287],
     |             [-2.85602287,  3.47613949]])  # may vary
     |      >>> np.corrcoef(pts.T)[0, 1]
     |      -0.6273591314603949  # may vary
     |
     |      We can visualize this data with a scatter plot.  The orientation
     |      of the point cloud illustrates the negative correlation of the
     |      components of this sample.
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> plt.plot(pts[:, 0], pts[:, 1], '.', alpha=0.5)
     |      >>> plt.axis('equal')
     |      >>> plt.grid()
     |      >>> plt.show()
     |
     |  negative_binomial(...)
     |      negative_binomial(n, p, size=None)
     |
     |      Draw samples from a negative binomial distribution.
     |
     |      Samples are drawn from a negative binomial distribution with specified
     |      parameters, `n` successes and `p` probability of success where `n`
     |      is > 0 and `p` is in the interval [0, 1].
     |
     |      .. note::
     |          New code should use the
     |          `~numpy.random.Generator.negative_binomial`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      n : float or array_like of floats
     |          Parameter of the distribution, > 0.
     |      p : float or array_like of floats
     |          Parameter of the distribution, >= 0 and <=1.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``n`` and ``p`` are both scalars.
     |          Otherwise, ``np.broadcast(n, p).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized negative binomial distribution,
     |          where each sample is equal to N, the number of failures that
     |          occurred before a total of n successes was reached.
     |
     |      See Also
     |      --------
     |      random.Generator.negative_binomial: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The probability mass function of the negative binomial distribution is
     |
     |      .. math:: P(N;n,p) = \frac{\Gamma(N+n)}{N!\Gamma(n)}p^{n}(1-p)^{N},
     |
     |      where :math:`n` is the number of successes, :math:`p` is the
     |      probability of success, :math:`N+n` is the number of trials, and
     |      :math:`\Gamma` is the gamma function. When :math:`n` is an integer,
     |      :math:`\frac{\Gamma(N+n)}{N!\Gamma(n)} = \binom{N+n-1}{N}`, which is
     |      the more common form of this term in the pmf. The negative
     |      binomial distribution gives the probability of N failures given n
     |      successes, with a success on the last trial.
     |
     |      If one throws a die repeatedly until the third time a "1" appears,
     |      then the probability distribution of the number of non-"1"s that
     |      appear before the third "1" is a negative binomial distribution.
     |
     |      References
     |      ----------
     |      .. [1] Weisstein, Eric W. "Negative Binomial Distribution." From
     |             MathWorld--A Wolfram Web Resource.
     |             http://mathworld.wolfram.com/NegativeBinomialDistribution.html
     |      .. [2] Wikipedia, "Negative binomial distribution",
     |             https://en.wikipedia.org/wiki/Negative_binomial_distribution
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      A real world example. A company drills wild-cat oil
     |      exploration wells, each with an estimated probability of
     |      success of 0.1.  What is the probability of having one success
     |      for each successive well, that is what is the probability of a
     |      single success after drilling 5 wells, after 6 wells, etc.?
     |
     |      >>> s = np.random.negative_binomial(1, 0.1, 100000)
     |      >>> for i in range(1, 11): # doctest: +SKIP
     |      ...    probability = sum(s<i) / 100000.
     |      ...    print(i, "wells drilled, probability of one success =", probability)
     |
     |  noncentral_chisquare(...)
     |      noncentral_chisquare(df, nonc, size=None)
     |
     |      Draw samples from a noncentral chi-square distribution.
     |
     |      The noncentral :math:`\chi^2` distribution is a generalization of
     |      the :math:`\chi^2` distribution.
     |
     |      .. note::
     |          New code should use the
     |          `~numpy.random.Generator.noncentral_chisquare`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      df : float or array_like of floats
     |          Degrees of freedom, must be > 0.
     |
     |          .. versionchanged:: 1.10.0
     |             Earlier NumPy versions required dfnum > 1.
     |      nonc : float or array_like of floats
     |          Non-centrality, must be non-negative.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``df`` and ``nonc`` are both scalars.
     |          Otherwise, ``np.broadcast(df, nonc).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized noncentral chi-square distribution.
     |
     |      See Also
     |      --------
     |      random.Generator.noncentral_chisquare: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The probability density function for the noncentral Chi-square
     |      distribution is
     |
     |      .. math:: P(x;df,nonc) = \sum^{\infty}_{i=0}
     |                             \frac{e^{-nonc/2}(nonc/2)^{i}}{i!}
     |                             P_{Y_{df+2i}}(x),
     |
     |      where :math:`Y_{q}` is the Chi-square with q degrees of freedom.
     |
     |      References
     |      ----------
     |      .. [1] Wikipedia, "Noncentral chi-squared distribution"
     |             https://en.wikipedia.org/wiki/Noncentral_chi-squared_distribution
     |
     |      Examples
     |      --------
     |      Draw values from the distribution and plot the histogram
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> values = plt.hist(np.random.noncentral_chisquare(3, 20, 100000),
     |      ...                   bins=200, density=True)
     |      >>> plt.show()
     |
     |      Draw values from a noncentral chisquare with very small noncentrality,
     |      and compare to a chisquare.
     |
     |      >>> plt.figure()
     |      >>> values = plt.hist(np.random.noncentral_chisquare(3, .0000001, 100000),
     |      ...                   bins=np.arange(0., 25, .1), density=True)
     |      >>> values2 = plt.hist(np.random.chisquare(3, 100000),
     |      ...                    bins=np.arange(0., 25, .1), density=True)
     |      >>> plt.plot(values[1][0:-1], values[0]-values2[0], 'ob')
     |      >>> plt.show()
     |
     |      Demonstrate how large values of non-centrality lead to a more symmetric
     |      distribution.
     |
     |      >>> plt.figure()
     |      >>> values = plt.hist(np.random.noncentral_chisquare(3, 20, 100000),
     |      ...                   bins=200, density=True)
     |      >>> plt.show()
     |
     |  noncentral_f(...)
     |      noncentral_f(dfnum, dfden, nonc, size=None)
     |
     |      Draw samples from the noncentral F distribution.
     |
     |      Samples are drawn from an F distribution with specified parameters,
     |      `dfnum` (degrees of freedom in numerator) and `dfden` (degrees of
     |      freedom in denominator), where both parameters > 1.
     |      `nonc` is the non-centrality parameter.
     |
     |      .. note::
     |          New code should use the
     |          `~numpy.random.Generator.noncentral_f`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      dfnum : float or array_like of floats
     |          Numerator degrees of freedom, must be > 0.
     |
     |          .. versionchanged:: 1.14.0
     |             Earlier NumPy versions required dfnum > 1.
     |      dfden : float or array_like of floats
     |          Denominator degrees of freedom, must be > 0.
     |      nonc : float or array_like of floats
     |          Non-centrality parameter, the sum of the squares of the numerator
     |          means, must be >= 0.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``dfnum``, ``dfden``, and ``nonc``
     |          are all scalars.  Otherwise, ``np.broadcast(dfnum, dfden, nonc).size``
     |          samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized noncentral Fisher distribution.
     |
     |      See Also
     |      --------
     |      random.Generator.noncentral_f: which should be used for new code.
     |
     |      Notes
     |      -----
     |      When calculating the power of an experiment (power = probability of
     |      rejecting the null hypothesis when a specific alternative is true) the
     |      non-central F statistic becomes important.  When the null hypothesis is
     |      true, the F statistic follows a central F distribution. When the null
     |      hypothesis is not true, then it follows a non-central F statistic.
     |
     |      References
     |      ----------
     |      .. [1] Weisstein, Eric W. "Noncentral F-Distribution."
     |             From MathWorld--A Wolfram Web Resource.
     |             http://mathworld.wolfram.com/NoncentralF-Distribution.html
     |      .. [2] Wikipedia, "Noncentral F-distribution",
     |             https://en.wikipedia.org/wiki/Noncentral_F-distribution
     |
     |      Examples
     |      --------
     |      In a study, testing for a specific alternative to the null hypothesis
     |      requires use of the Noncentral F distribution. We need to calculate the
     |      area in the tail of the distribution that exceeds the value of the F
     |      distribution for the null hypothesis.  We'll plot the two probability
     |      distributions for comparison.
     |
     |      >>> dfnum = 3 # between group deg of freedom
     |      >>> dfden = 20 # within groups degrees of freedom
     |      >>> nonc = 3.0
     |      >>> nc_vals = np.random.noncentral_f(dfnum, dfden, nonc, 1000000)
     |      >>> NF = np.histogram(nc_vals, bins=50, density=True)
     |      >>> c_vals = np.random.f(dfnum, dfden, 1000000)
     |      >>> F = np.histogram(c_vals, bins=50, density=True)
     |      >>> import matplotlib.pyplot as plt
     |      >>> plt.plot(F[1][1:], F[0])
     |      >>> plt.plot(NF[1][1:], NF[0])
     |      >>> plt.show()
     |
     |  normal(...)
     |      normal(loc=0.0, scale=1.0, size=None)
     |
     |      Draw random samples from a normal (Gaussian) distribution.
     |
     |      The probability density function of the normal distribution, first
     |      derived by De Moivre and 200 years later by both Gauss and Laplace
     |      independently [2]_, is often called the bell curve because of
     |      its characteristic shape (see the example below).
     |
     |      The normal distributions occurs often in nature.  For example, it
     |      describes the commonly occurring distribution of samples influenced
     |      by a large number of tiny, random disturbances, each with its own
     |      unique distribution [2]_.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.normal`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      loc : float or array_like of floats
     |          Mean ("centre") of the distribution.
     |      scale : float or array_like of floats
     |          Standard deviation (spread or "width") of the distribution. Must be
     |          non-negative.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``loc`` and ``scale`` are both scalars.
     |          Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized normal distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.norm : probability density function, distribution or
     |          cumulative density function, etc.
     |      random.Generator.normal: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The probability density for the Gaussian distribution is
     |
     |      .. math:: p(x) = \frac{1}{\sqrt{ 2 \pi \sigma^2 }}
     |                       e^{ - \frac{ (x - \mu)^2 } {2 \sigma^2} },
     |
     |      where :math:`\mu` is the mean and :math:`\sigma` the standard
     |      deviation. The square of the standard deviation, :math:`\sigma^2`,
     |      is called the variance.
     |
     |      The function has its peak at the mean, and its "spread" increases with
     |      the standard deviation (the function reaches 0.607 times its maximum at
     |      :math:`x + \sigma` and :math:`x - \sigma` [2]_).  This implies that
     |      normal is more likely to return samples lying close to the mean, rather
     |      than those far away.
     |
     |      References
     |      ----------
     |      .. [1] Wikipedia, "Normal distribution",
     |             https://en.wikipedia.org/wiki/Normal_distribution
     |      .. [2] P. R. Peebles Jr., "Central Limit Theorem" in "Probability,
     |             Random Variables and Random Signal Principles", 4th ed., 2001,
     |             pp. 51, 51, 125.
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> mu, sigma = 0, 0.1 # mean and standard deviation
     |      >>> s = np.random.normal(mu, sigma, 1000)
     |
     |      Verify the mean and the variance:
     |
     |      >>> abs(mu - np.mean(s))
     |      0.0  # may vary
     |
     |      >>> abs(sigma - np.std(s, ddof=1))
     |      0.1  # may vary
     |
     |      Display the histogram of the samples, along with
     |      the probability density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> count, bins, ignored = plt.hist(s, 30, density=True)
     |      >>> plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
     |      ...                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
     |      ...          linewidth=2, color='r')
     |      >>> plt.show()
     |
     |      Two-by-four array of samples from the normal distribution with
     |      mean 3 and standard deviation 2.5:
     |
     |      >>> np.random.normal(3, 2.5, size=(2, 4))
     |      array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random
     |             [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random
     |
     |  pareto(...)
     |      pareto(a, size=None)
     |
     |      Draw samples from a Pareto II or Lomax distribution with
     |      specified shape.
     |
     |      The Lomax or Pareto II distribution is a shifted Pareto
     |      distribution. The classical Pareto distribution can be
     |      obtained from the Lomax distribution by adding 1 and
     |      multiplying by the scale parameter ``m`` (see Notes).  The
     |      smallest value of the Lomax distribution is zero while for the
     |      classical Pareto distribution it is ``mu``, where the standard
     |      Pareto distribution has location ``mu = 1``.  Lomax can also
     |      be considered as a simplified version of the Generalized
     |      Pareto distribution (available in SciPy), with the scale set
     |      to one and the location set to zero.
     |
     |      The Pareto distribution must be greater than zero, and is
     |      unbounded above.  It is also known as the "80-20 rule".  In
     |      this distribution, 80 percent of the weights are in the lowest
     |      20 percent of the range, while the other 20 percent fill the
     |      remaining 80 percent of the range.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.pareto`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      a : float or array_like of floats
     |          Shape of the distribution. Must be positive.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``a`` is a scalar.  Otherwise,
     |          ``np.array(a).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized Pareto distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.lomax : probability density function, distribution or
     |          cumulative density function, etc.
     |      scipy.stats.genpareto : probability density function, distribution or
     |          cumulative density function, etc.
     |      random.Generator.pareto: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The probability density for the Pareto distribution is
     |
     |      .. math:: p(x) = \frac{am^a}{x^{a+1}}
     |
     |      where :math:`a` is the shape and :math:`m` the scale.
     |
     |      The Pareto distribution, named after the Italian economist
     |      Vilfredo Pareto, is a power law probability distribution
     |      useful in many real world problems.  Outside the field of
     |      economics it is generally referred to as the Bradford
     |      distribution. Pareto developed the distribution to describe
     |      the distribution of wealth in an economy.  It has also found
     |      use in insurance, web page access statistics, oil field sizes,
     |      and many other problems, including the download frequency for
     |      projects in Sourceforge [1]_.  It is one of the so-called
     |      "fat-tailed" distributions.
     |
     |      References
     |      ----------
     |      .. [1] Francis Hunt and Paul Johnson, On the Pareto Distribution of
     |             Sourceforge projects.
     |      .. [2] Pareto, V. (1896). Course of Political Economy. Lausanne.
     |      .. [3] Reiss, R.D., Thomas, M.(2001), Statistical Analysis of Extreme
     |             Values, Birkhauser Verlag, Basel, pp 23-30.
     |      .. [4] Wikipedia, "Pareto distribution",
     |             https://en.wikipedia.org/wiki/Pareto_distribution
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> a, m = 3., 2.  # shape and mode
     |      >>> s = (np.random.pareto(a, 1000) + 1) * m
     |
     |      Display the histogram of the samples, along with the probability
     |      density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> count, bins, _ = plt.hist(s, 100, density=True)
     |      >>> fit = a*m**a / bins**(a+1)
     |      >>> plt.plot(bins, max(count)*fit/max(fit), linewidth=2, color='r')
     |      >>> plt.show()
     |
     |  permutation(...)
     |      permutation(x)
     |
     |      Randomly permute a sequence, or return a permuted range.
     |
     |      If `x` is a multi-dimensional array, it is only shuffled along its
     |      first index.
     |
     |      .. note::
     |          New code should use the
     |          `~numpy.random.Generator.permutation`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      x : int or array_like
     |          If `x` is an integer, randomly permute ``np.arange(x)``.
     |          If `x` is an array, make a copy and shuffle the elements
     |          randomly.
     |
     |      Returns
     |      -------
     |      out : ndarray
     |          Permuted sequence or array range.
     |
     |      See Also
     |      --------
     |      random.Generator.permutation: which should be used for new code.
     |
     |      Examples
     |      --------
     |      >>> np.random.permutation(10)
     |      array([1, 7, 4, 3, 0, 9, 2, 5, 8, 6]) # random
     |
     |      >>> np.random.permutation([1, 4, 9, 12, 15])
     |      array([15,  1,  9,  4, 12]) # random
     |
     |      >>> arr = np.arange(9).reshape((3, 3))
     |      >>> np.random.permutation(arr)
     |      array([[6, 7, 8], # random
     |             [0, 1, 2],
     |             [3, 4, 5]])
     |
     |  poisson(...)
     |      poisson(lam=1.0, size=None)
     |
     |      Draw samples from a Poisson distribution.
     |
     |      The Poisson distribution is the limit of the binomial distribution
     |      for large N.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.poisson`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      lam : float or array_like of floats
     |          Expected number of events occurring in a fixed-time interval,
     |          must be >= 0. A sequence must be broadcastable over the requested
     |          size.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``lam`` is a scalar. Otherwise,
     |          ``np.array(lam).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized Poisson distribution.
     |
     |      See Also
     |      --------
     |      random.Generator.poisson: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The Poisson distribution
     |
     |      .. math:: f(k; \lambda)=\frac{\lambda^k e^{-\lambda}}{k!}
     |
     |      For events with an expected separation :math:`\lambda` the Poisson
     |      distribution :math:`f(k; \lambda)` describes the probability of
     |      :math:`k` events occurring within the observed
     |      interval :math:`\lambda`.
     |
     |      Because the output is limited to the range of the C int64 type, a
     |      ValueError is raised when `lam` is within 10 sigma of the maximum
     |      representable value.
     |
     |      References
     |      ----------
     |      .. [1] Weisstein, Eric W. "Poisson Distribution."
     |             From MathWorld--A Wolfram Web Resource.
     |             http://mathworld.wolfram.com/PoissonDistribution.html
     |      .. [2] Wikipedia, "Poisson distribution",
     |             https://en.wikipedia.org/wiki/Poisson_distribution
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> import numpy as np
     |      >>> s = np.random.poisson(5, 10000)
     |
     |      Display histogram of the sample:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> count, bins, ignored = plt.hist(s, 14, density=True)
     |      >>> plt.show()
     |
     |      Draw each 100 values for lambda 100 and 500:
     |
     |      >>> s = np.random.poisson(lam=(100., 500.), size=(100, 2))
     |
     |  power(...)
     |      power(a, size=None)
     |
     |      Draws samples in [0, 1] from a power distribution with positive
     |      exponent a - 1.
     |
     |      Also known as the power function distribution.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.power`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      a : float or array_like of floats
     |          Parameter of the distribution. Must be non-negative.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``a`` is a scalar.  Otherwise,
     |          ``np.array(a).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized power distribution.
     |
     |      Raises
     |      ------
     |      ValueError
     |          If a <= 0.
     |
     |      See Also
     |      --------
     |      random.Generator.power: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The probability density function is
     |
     |      .. math:: P(x; a) = ax^{a-1}, 0 \le x \le 1, a>0.
     |
     |      The power function distribution is just the inverse of the Pareto
     |      distribution. It may also be seen as a special case of the Beta
     |      distribution.
     |
     |      It is used, for example, in modeling the over-reporting of insurance
     |      claims.
     |
     |      References
     |      ----------
     |      .. [1] Christian Kleiber, Samuel Kotz, "Statistical size distributions
     |             in economics and actuarial sciences", Wiley, 2003.
     |      .. [2] Heckert, N. A. and Filliben, James J. "NIST Handbook 148:
     |             Dataplot Reference Manual, Volume 2: Let Subcommands and Library
     |             Functions", National Institute of Standards and Technology
     |             Handbook Series, June 2003.
     |             https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/powpdf.pdf
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> a = 5. # shape
     |      >>> samples = 1000
     |      >>> s = np.random.power(a, samples)
     |
     |      Display the histogram of the samples, along with
     |      the probability density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> count, bins, ignored = plt.hist(s, bins=30)
     |      >>> x = np.linspace(0, 1, 100)
     |      >>> y = a*x**(a-1.)
     |      >>> normed_y = samples*np.diff(bins)[0]*y
     |      >>> plt.plot(x, normed_y)
     |      >>> plt.show()
     |
     |      Compare the power function distribution to the inverse of the Pareto.
     |
     |      >>> from scipy import stats # doctest: +SKIP
     |      >>> rvs = np.random.power(5, 1000000)
     |      >>> rvsp = np.random.pareto(5, 1000000)
     |      >>> xx = np.linspace(0,1,100)
     |      >>> powpdf = stats.powerlaw.pdf(xx,5)  # doctest: +SKIP
     |
     |      >>> plt.figure()
     |      >>> plt.hist(rvs, bins=50, density=True)
     |      >>> plt.plot(xx,powpdf,'r-')  # doctest: +SKIP
     |      >>> plt.title('np.random.power(5)')
     |
     |      >>> plt.figure()
     |      >>> plt.hist(1./(1.+rvsp), bins=50, density=True)
     |      >>> plt.plot(xx,powpdf,'r-')  # doctest: +SKIP
     |      >>> plt.title('inverse of 1 + np.random.pareto(5)')
     |
     |      >>> plt.figure()
     |      >>> plt.hist(1./(1.+rvsp), bins=50, density=True)
     |      >>> plt.plot(xx,powpdf,'r-')  # doctest: +SKIP
     |      >>> plt.title('inverse of stats.pareto(5)')
     |
     |  rand(...)
     |      rand(d0, d1, ..., dn)
     |
     |      Random values in a given shape.
     |
     |      .. note::
     |          This is a convenience function for users porting code from Matlab,
     |          and wraps `random_sample`. That function takes a
     |          tuple to specify the size of the output, which is consistent with
     |          other NumPy functions like `numpy.zeros` and `numpy.ones`.
     |
     |      Create an array of the given shape and populate it with
     |      random samples from a uniform distribution
     |      over ``[0, 1)``.
     |
     |      Parameters
     |      ----------
     |      d0, d1, ..., dn : int, optional
     |          The dimensions of the returned array, must be non-negative.
     |          If no argument is given a single Python float is returned.
     |
     |      Returns
     |      -------
     |      out : ndarray, shape ``(d0, d1, ..., dn)``
     |          Random values.
     |
     |      See Also
     |      --------
     |      random
     |
     |      Examples
     |      --------
     |      >>> np.random.rand(3,2)
     |      array([[ 0.14022471,  0.96360618],  #random
     |             [ 0.37601032,  0.25528411],  #random
     |             [ 0.49313049,  0.94909878]]) #random
     |
     |  randint(...)
     |      randint(low, high=None, size=None, dtype=int)
     |
     |      Return random integers from `low` (inclusive) to `high` (exclusive).
     |
     |      Return random integers from the "discrete uniform" distribution of
     |      the specified dtype in the "half-open" interval [`low`, `high`). If
     |      `high` is None (the default), then results are from [0, `low`).
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.integers`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      low : int or array-like of ints
     |          Lowest (signed) integers to be drawn from the distribution (unless
     |          ``high=None``, in which case this parameter is one above the
     |          *highest* such integer).
     |      high : int or array-like of ints, optional
     |          If provided, one above the largest (signed) integer to be drawn
     |          from the distribution (see above for behavior if ``high=None``).
     |          If array-like, must contain integer values
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  Default is None, in which case a
     |          single value is returned.
     |      dtype : dtype, optional
     |          Desired dtype of the result. Byteorder must be native.
     |          The default value is int.
     |
     |          .. versionadded:: 1.11.0
     |
     |      Returns
     |      -------
     |      out : int or ndarray of ints
     |          `size`-shaped array of random integers from the appropriate
     |          distribution, or a single such random int if `size` not provided.
     |
     |      See Also
     |      --------
     |      random_integers : similar to `randint`, only for the closed
     |          interval [`low`, `high`], and 1 is the lowest value if `high` is
     |          omitted.
     |      random.Generator.integers: which should be used for new code.
     |
     |      Examples
     |      --------
     |      >>> np.random.randint(2, size=10)
     |      array([1, 0, 0, 0, 1, 1, 0, 0, 1, 0]) # random
     |      >>> np.random.randint(1, size=10)
     |      array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
     |
     |      Generate a 2 x 4 array of ints between 0 and 4, inclusive:
     |
     |      >>> np.random.randint(5, size=(2, 4))
     |      array([[4, 0, 2, 1], # random
     |             [3, 2, 2, 0]])
     |
     |      Generate a 1 x 3 array with 3 different upper bounds
     |
     |      >>> np.random.randint(1, [3, 5, 10])
     |      array([2, 2, 9]) # random
     |
     |      Generate a 1 by 3 array with 3 different lower bounds
     |
     |      >>> np.random.randint([1, 5, 7], 10)
     |      array([9, 8, 7]) # random
     |
     |      Generate a 2 by 4 array using broadcasting with dtype of uint8
     |
     |      >>> np.random.randint([1, 3, 5, 7], [[10], [20]], dtype=np.uint8)
     |      array([[ 8,  6,  9,  7], # random
     |             [ 1, 16,  9, 12]], dtype=uint8)
     |
     |  randn(...)
     |      randn(d0, d1, ..., dn)
     |
     |      Return a sample (or samples) from the "standard normal" distribution.
     |
     |      .. note::
     |          This is a convenience function for users porting code from Matlab,
     |          and wraps `standard_normal`. That function takes a
     |          tuple to specify the size of the output, which is consistent with
     |          other NumPy functions like `numpy.zeros` and `numpy.ones`.
     |
     |      .. note::
     |          New code should use the
     |          `~numpy.random.Generator.standard_normal`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      If positive int_like arguments are provided, `randn` generates an array
     |      of shape ``(d0, d1, ..., dn)``, filled
     |      with random floats sampled from a univariate "normal" (Gaussian)
     |      distribution of mean 0 and variance 1. A single float randomly sampled
     |      from the distribution is returned if no argument is provided.
     |
     |      Parameters
     |      ----------
     |      d0, d1, ..., dn : int, optional
     |          The dimensions of the returned array, must be non-negative.
     |          If no argument is given a single Python float is returned.
     |
     |      Returns
     |      -------
     |      Z : ndarray or float
     |          A ``(d0, d1, ..., dn)``-shaped array of floating-point samples from
     |          the standard normal distribution, or a single such float if
     |          no parameters were supplied.
     |
     |      See Also
     |      --------
     |      standard_normal : Similar, but takes a tuple as its argument.
     |      normal : Also accepts mu and sigma arguments.
     |      random.Generator.standard_normal: which should be used for new code.
     |
     |      Notes
     |      -----
     |      For random samples from the normal distribution with mean ``mu`` and
     |      standard deviation ``sigma``, use::
     |
     |          sigma * np.random.randn(...) + mu
     |
     |      Examples
     |      --------
     |      >>> np.random.randn()
     |      2.1923875335537315  # random
     |
     |      Two-by-four array of samples from the normal distribution with
     |      mean 3 and standard deviation 2.5:
     |
     |      >>> 3 + 2.5 * np.random.randn(2, 4)
     |      array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random
     |             [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random
     |
     |  random(...)
     |      random(size=None)
     |
     |      Return random floats in the half-open interval [0.0, 1.0). Alias for
     |      `random_sample` to ease forward-porting to the new random API.
     |
     |  random_integers(...)
     |      random_integers(low, high=None, size=None)
     |
     |      Random integers of type `np.int_` between `low` and `high`, inclusive.
     |
     |      Return random integers of type `np.int_` from the "discrete uniform"
     |      distribution in the closed interval [`low`, `high`].  If `high` is
     |      None (the default), then results are from [1, `low`]. The `np.int_`
     |      type translates to the C long integer type and its precision
     |      is platform dependent.
     |
     |      This function has been deprecated. Use randint instead.
     |
     |      .. deprecated:: 1.11.0
     |
     |      Parameters
     |      ----------
     |      low : int
     |          Lowest (signed) integer to be drawn from the distribution (unless
     |          ``high=None``, in which case this parameter is the *highest* such
     |          integer).
     |      high : int, optional
     |          If provided, the largest (signed) integer to be drawn from the
     |          distribution (see above for behavior if ``high=None``).
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  Default is None, in which case a
     |          single value is returned.
     |
     |      Returns
     |      -------
     |      out : int or ndarray of ints
     |          `size`-shaped array of random integers from the appropriate
     |          distribution, or a single such random int if `size` not provided.
     |
     |      See Also
     |      --------
     |      randint : Similar to `random_integers`, only for the half-open
     |          interval [`low`, `high`), and 0 is the lowest value if `high` is
     |          omitted.
     |
     |      Notes
     |      -----
     |      To sample from N evenly spaced floating-point numbers between a and b,
     |      use::
     |
     |        a + (b - a) * (np.random.random_integers(N) - 1) / (N - 1.)
     |
     |      Examples
     |      --------
     |      >>> np.random.random_integers(5)
     |      4 # random
     |      >>> type(np.random.random_integers(5))
     |      <class 'numpy.int64'>
     |      >>> np.random.random_integers(5, size=(3,2))
     |      array([[5, 4], # random
     |             [3, 3],
     |             [4, 5]])
     |
     |      Choose five random numbers from the set of five evenly-spaced
     |      numbers between 0 and 2.5, inclusive (*i.e.*, from the set
     |      :math:`{0, 5/8, 10/8, 15/8, 20/8}`):
     |
     |      >>> 2.5 * (np.random.random_integers(5, size=(5,)) - 1) / 4.
     |      array([ 0.625,  1.25 ,  0.625,  0.625,  2.5  ]) # random
     |
     |      Roll two six sided dice 1000 times and sum the results:
     |
     |      >>> d1 = np.random.random_integers(1, 6, 1000)
     |      >>> d2 = np.random.random_integers(1, 6, 1000)
     |      >>> dsums = d1 + d2
     |
     |      Display results as a histogram:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> count, bins, ignored = plt.hist(dsums, 11, density=True)
     |      >>> plt.show()
     |
     |  random_sample(...)
     |      random_sample(size=None)
     |
     |      Return random floats in the half-open interval [0.0, 1.0).
     |
     |      Results are from the "continuous uniform" distribution over the
     |      stated interval.  To sample :math:`Unif[a, b), b > a` multiply
     |      the output of `random_sample` by `(b-a)` and add `a`::
     |
     |        (b - a) * random_sample() + a
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.random`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  Default is None, in which case a
     |          single value is returned.
     |
     |      Returns
     |      -------
     |      out : float or ndarray of floats
     |          Array of random floats of shape `size` (unless ``size=None``, in which
     |          case a single float is returned).
     |
     |      See Also
     |      --------
     |      random.Generator.random: which should be used for new code.
     |
     |      Examples
     |      --------
     |      >>> np.random.random_sample()
     |      0.47108547995356098 # random
     |      >>> type(np.random.random_sample())
     |      <class 'float'>
     |      >>> np.random.random_sample((5,))
     |      array([ 0.30220482,  0.86820401,  0.1654503 ,  0.11659149,  0.54323428]) # random
     |
     |      Three-by-two array of random numbers from [-5, 0):
     |
     |      >>> 5 * np.random.random_sample((3, 2)) - 5
     |      array([[-3.99149989, -0.52338984], # random
     |             [-2.99091858, -0.79479508],
     |             [-1.23204345, -1.75224494]])
     |
     |  rayleigh(...)
     |      rayleigh(scale=1.0, size=None)
     |
     |      Draw samples from a Rayleigh distribution.
     |
     |      The :math:`\chi` and Weibull distributions are generalizations of the
     |      Rayleigh.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.rayleigh`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      scale : float or array_like of floats, optional
     |          Scale, also equals the mode. Must be non-negative. Default is 1.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``scale`` is a scalar.  Otherwise,
     |          ``np.array(scale).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized Rayleigh distribution.
     |
     |      See Also
     |      --------
     |      random.Generator.rayleigh: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The probability density function for the Rayleigh distribution is
     |
     |      .. math:: P(x;scale) = \frac{x}{scale^2}e^{\frac{-x^2}{2 \cdotp scale^2}}
     |
     |      The Rayleigh distribution would arise, for example, if the East
     |      and North components of the wind velocity had identical zero-mean
     |      Gaussian distributions.  Then the wind speed would have a Rayleigh
     |      distribution.
     |
     |      References
     |      ----------
     |      .. [1] Brighton Webs Ltd., "Rayleigh Distribution,"
     |             https://web.archive.org/web/20090514091424/http://brighton-webs.co.uk:80/distributions/rayleigh.asp
     |      .. [2] Wikipedia, "Rayleigh distribution"
     |             https://en.wikipedia.org/wiki/Rayleigh_distribution
     |
     |      Examples
     |      --------
     |      Draw values from the distribution and plot the histogram
     |
     |      >>> from matplotlib.pyplot import hist
     |      >>> values = hist(np.random.rayleigh(3, 100000), bins=200, density=True)
     |
     |      Wave heights tend to follow a Rayleigh distribution. If the mean wave
     |      height is 1 meter, what fraction of waves are likely to be larger than 3
     |      meters?
     |
     |      >>> meanvalue = 1
     |      >>> modevalue = np.sqrt(2 / np.pi) * meanvalue
     |      >>> s = np.random.rayleigh(modevalue, 1000000)
     |
     |      The percentage of waves larger than 3 meters is:
     |
     |      >>> 100.*sum(s>3)/1000000.
     |      0.087300000000000003 # random
     |
     |  seed(...)
     |      seed(seed=None)
     |
     |      Reseed a legacy MT19937 BitGenerator
     |
     |      Notes
     |      -----
     |      This is a convenience, legacy function.
     |
     |      The best practice is to **not** reseed a BitGenerator, rather to
     |      recreate a new one. This method is here for legacy reasons.
     |      This example demonstrates best practice.
     |
     |      >>> from numpy.random import MT19937
     |      >>> from numpy.random import RandomState, SeedSequence
     |      >>> rs = RandomState(MT19937(SeedSequence(123456789)))
     |      # Later, you want to restart the stream
     |      >>> rs = RandomState(MT19937(SeedSequence(987654321)))
     |
     |  set_state(...)
     |      set_state(state)
     |
     |      Set the internal state of the generator from a tuple.
     |
     |      For use if one has reason to manually (re-)set the internal state of
     |      the bit generator used by the RandomState instance. By default,
     |      RandomState uses the "Mersenne Twister"[1]_ pseudo-random number
     |      generating algorithm.
     |
     |      Parameters
     |      ----------
     |      state : {tuple(str, ndarray of 624 uints, int, int, float), dict}
     |          The `state` tuple has the following items:
     |
     |          1. the string 'MT19937', specifying the Mersenne Twister algorithm.
     |          2. a 1-D array of 624 unsigned integers ``keys``.
     |          3. an integer ``pos``.
     |          4. an integer ``has_gauss``.
     |          5. a float ``cached_gaussian``.
     |
     |          If state is a dictionary, it is directly set using the BitGenerators
     |          `state` property.
     |
     |      Returns
     |      -------
     |      out : None
     |          Returns 'None' on success.
     |
     |      See Also
     |      --------
     |      get_state
     |
     |      Notes
     |      -----
     |      `set_state` and `get_state` are not needed to work with any of the
     |      random distributions in NumPy. If the internal state is manually altered,
     |      the user should know exactly what he/she is doing.
     |
     |      For backwards compatibility, the form (str, array of 624 uints, int) is
     |      also accepted although it is missing some information about the cached
     |      Gaussian value: ``state = ('MT19937', keys, pos)``.
     |
     |      References
     |      ----------
     |      .. [1] M. Matsumoto and T. Nishimura, "Mersenne Twister: A
     |         623-dimensionally equidistributed uniform pseudorandom number
     |         generator," *ACM Trans. on Modeling and Computer Simulation*,
     |         Vol. 8, No. 1, pp. 3-30, Jan. 1998.
     |
     |  shuffle(...)
     |      shuffle(x)
     |
     |      Modify a sequence in-place by shuffling its contents.
     |
     |      This function only shuffles the array along the first axis of a
     |      multi-dimensional array. The order of sub-arrays is changed but
     |      their contents remains the same.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.shuffle`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      x : ndarray or MutableSequence
     |          The array, list or mutable sequence to be shuffled.
     |
     |      Returns
     |      -------
     |      None
     |
     |      See Also
     |      --------
     |      random.Generator.shuffle: which should be used for new code.
     |
     |      Examples
     |      --------
     |      >>> arr = np.arange(10)
     |      >>> np.random.shuffle(arr)
     |      >>> arr
     |      [1 7 5 2 9 4 3 6 0 8] # random
     |
     |      Multi-dimensional arrays are only shuffled along the first axis:
     |
     |      >>> arr = np.arange(9).reshape((3, 3))
     |      >>> np.random.shuffle(arr)
     |      >>> arr
     |      array([[3, 4, 5], # random
     |             [6, 7, 8],
     |             [0, 1, 2]])
     |
     |  standard_cauchy(...)
     |      standard_cauchy(size=None)
     |
     |      Draw samples from a standard Cauchy distribution with mode = 0.
     |
     |      Also known as the Lorentz distribution.
     |
     |      .. note::
     |          New code should use the
     |          `~numpy.random.Generator.standard_cauchy`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  Default is None, in which case a
     |          single value is returned.
     |
     |      Returns
     |      -------
     |      samples : ndarray or scalar
     |          The drawn samples.
     |
     |      See Also
     |      --------
     |      random.Generator.standard_cauchy: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The probability density function for the full Cauchy distribution is
     |
     |      .. math:: P(x; x_0, \gamma) = \frac{1}{\pi \gamma \bigl[ 1+
     |                (\frac{x-x_0}{\gamma})^2 \bigr] }
     |
     |      and the Standard Cauchy distribution just sets :math:`x_0=0` and
     |      :math:`\gamma=1`
     |
     |      The Cauchy distribution arises in the solution to the driven harmonic
     |      oscillator problem, and also describes spectral line broadening. It
     |      also describes the distribution of values at which a line tilted at
     |      a random angle will cut the x axis.
     |
     |      When studying hypothesis tests that assume normality, seeing how the
     |      tests perform on data from a Cauchy distribution is a good indicator of
     |      their sensitivity to a heavy-tailed distribution, since the Cauchy looks
     |      very much like a Gaussian distribution, but with heavier tails.
     |
     |      References
     |      ----------
     |      .. [1] NIST/SEMATECH e-Handbook of Statistical Methods, "Cauchy
     |            Distribution",
     |            https://www.itl.nist.gov/div898/handbook/eda/section3/eda3663.htm
     |      .. [2] Weisstein, Eric W. "Cauchy Distribution." From MathWorld--A
     |            Wolfram Web Resource.
     |            http://mathworld.wolfram.com/CauchyDistribution.html
     |      .. [3] Wikipedia, "Cauchy distribution"
     |            https://en.wikipedia.org/wiki/Cauchy_distribution
     |
     |      Examples
     |      --------
     |      Draw samples and plot the distribution:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> s = np.random.standard_cauchy(1000000)
     |      >>> s = s[(s>-25) & (s<25)]  # truncate distribution so it plots well
     |      >>> plt.hist(s, bins=100)
     |      >>> plt.show()
     |
     |  standard_exponential(...)
     |      standard_exponential(size=None)
     |
     |      Draw samples from the standard exponential distribution.
     |
     |      `standard_exponential` is identical to the exponential distribution
     |      with a scale parameter of 1.
     |
     |      .. note::
     |          New code should use the
     |          `~numpy.random.Generator.standard_exponential`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  Default is None, in which case a
     |          single value is returned.
     |
     |      Returns
     |      -------
     |      out : float or ndarray
     |          Drawn samples.
     |
     |      See Also
     |      --------
     |      random.Generator.standard_exponential: which should be used for new code.
     |
     |      Examples
     |      --------
     |      Output a 3x8000 array:
     |
     |      >>> n = np.random.standard_exponential((3, 8000))
     |
     |  standard_gamma(...)
     |      standard_gamma(shape, size=None)
     |
     |      Draw samples from a standard Gamma distribution.
     |
     |      Samples are drawn from a Gamma distribution with specified parameters,
     |      shape (sometimes designated "k") and scale=1.
     |
     |      .. note::
     |          New code should use the
     |          `~numpy.random.Generator.standard_gamma`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      shape : float or array_like of floats
     |          Parameter, must be non-negative.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``shape`` is a scalar.  Otherwise,
     |          ``np.array(shape).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized standard gamma distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.gamma : probability density function, distribution or
     |          cumulative density function, etc.
     |      random.Generator.standard_gamma: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The probability density for the Gamma distribution is
     |
     |      .. math:: p(x) = x^{k-1}\frac{e^{-x/\theta}}{\theta^k\Gamma(k)},
     |
     |      where :math:`k` is the shape and :math:`\theta` the scale,
     |      and :math:`\Gamma` is the Gamma function.
     |
     |      The Gamma distribution is often used to model the times to failure of
     |      electronic components, and arises naturally in processes for which the
     |      waiting times between Poisson distributed events are relevant.
     |
     |      References
     |      ----------
     |      .. [1] Weisstein, Eric W. "Gamma Distribution." From MathWorld--A
     |             Wolfram Web Resource.
     |             http://mathworld.wolfram.com/GammaDistribution.html
     |      .. [2] Wikipedia, "Gamma distribution",
     |             https://en.wikipedia.org/wiki/Gamma_distribution
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> shape, scale = 2., 1. # mean and width
     |      >>> s = np.random.standard_gamma(shape, 1000000)
     |
     |      Display the histogram of the samples, along with
     |      the probability density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> import scipy.special as sps  # doctest: +SKIP
     |      >>> count, bins, ignored = plt.hist(s, 50, density=True)
     |      >>> y = bins**(shape-1) * ((np.exp(-bins/scale))/  # doctest: +SKIP
     |      ...                       (sps.gamma(shape) * scale**shape))
     |      >>> plt.plot(bins, y, linewidth=2, color='r')  # doctest: +SKIP
     |      >>> plt.show()
     |
     |  standard_normal(...)
     |      standard_normal(size=None)
     |
     |      Draw samples from a standard Normal distribution (mean=0, stdev=1).
     |
     |      .. note::
     |          New code should use the
     |          `~numpy.random.Generator.standard_normal`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  Default is None, in which case a
     |          single value is returned.
     |
     |      Returns
     |      -------
     |      out : float or ndarray
     |          A floating-point array of shape ``size`` of drawn samples, or a
     |          single sample if ``size`` was not specified.
     |
     |      See Also
     |      --------
     |      normal :
     |          Equivalent function with additional ``loc`` and ``scale`` arguments
     |          for setting the mean and standard deviation.
     |      random.Generator.standard_normal: which should be used for new code.
     |
     |      Notes
     |      -----
     |      For random samples from the normal distribution with mean ``mu`` and
     |      standard deviation ``sigma``, use one of::
     |
     |          mu + sigma * np.random.standard_normal(size=...)
     |          np.random.normal(mu, sigma, size=...)
     |
     |      Examples
     |      --------
     |      >>> np.random.standard_normal()
     |      2.1923875335537315 #random
     |
     |      >>> s = np.random.standard_normal(8000)
     |      >>> s
     |      array([ 0.6888893 ,  0.78096262, -0.89086505, ...,  0.49876311,  # random
     |             -0.38672696, -0.4685006 ])                                # random
     |      >>> s.shape
     |      (8000,)
     |      >>> s = np.random.standard_normal(size=(3, 4, 2))
     |      >>> s.shape
     |      (3, 4, 2)
     |
     |      Two-by-four array of samples from the normal distribution with
     |      mean 3 and standard deviation 2.5:
     |
     |      >>> 3 + 2.5 * np.random.standard_normal(size=(2, 4))
     |      array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random
     |             [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random
     |
     |  standard_t(...)
     |      standard_t(df, size=None)
     |
     |      Draw samples from a standard Student's t distribution with `df` degrees
     |      of freedom.
     |
     |      A special case of the hyperbolic distribution.  As `df` gets
     |      large, the result resembles that of the standard normal
     |      distribution (`standard_normal`).
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.standard_t`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      df : float or array_like of floats
     |          Degrees of freedom, must be > 0.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``df`` is a scalar.  Otherwise,
     |          ``np.array(df).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized standard Student's t distribution.
     |
     |      See Also
     |      --------
     |      random.Generator.standard_t: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The probability density function for the t distribution is
     |
     |      .. math:: P(x, df) = \frac{\Gamma(\frac{df+1}{2})}{\sqrt{\pi df}
     |                \Gamma(\frac{df}{2})}\Bigl( 1+\frac{x^2}{df} \Bigr)^{-(df+1)/2}
     |
     |      The t test is based on an assumption that the data come from a
     |      Normal distribution. The t test provides a way to test whether
     |      the sample mean (that is the mean calculated from the data) is
     |      a good estimate of the true mean.
     |
     |      The derivation of the t-distribution was first published in
     |      1908 by William Gosset while working for the Guinness Brewery
     |      in Dublin. Due to proprietary issues, he had to publish under
     |      a pseudonym, and so he used the name Student.
     |
     |      References
     |      ----------
     |      .. [1] Dalgaard, Peter, "Introductory Statistics With R",
     |             Springer, 2002.
     |      .. [2] Wikipedia, "Student's t-distribution"
     |             https://en.wikipedia.org/wiki/Student's_t-distribution
     |
     |      Examples
     |      --------
     |      From Dalgaard page 83 [1]_, suppose the daily energy intake for 11
     |      women in kilojoules (kJ) is:
     |
     |      >>> intake = np.array([5260., 5470, 5640, 6180, 6390, 6515, 6805, 7515, \
     |      ...                    7515, 8230, 8770])
     |
     |      Does their energy intake deviate systematically from the recommended
     |      value of 7725 kJ? Our null hypothesis will be the absence of deviation,
     |      and the alternate hypothesis will be the presence of an effect that could be
     |      either positive or negative, hence making our test 2-tailed.
     |
     |      Because we are estimating the mean and we have N=11 values in our sample,
     |      we have N-1=10 degrees of freedom. We set our significance level to 95% and
     |      compute the t statistic using the empirical mean and empirical standard
     |      deviation of our intake. We use a ddof of 1 to base the computation of our
     |      empirical standard deviation on an unbiased estimate of the variance (note:
     |      the final estimate is not unbiased due to the concave nature of the square
     |      root).
     |
     |      >>> np.mean(intake)
     |      6753.636363636364
     |      >>> intake.std(ddof=1)
     |      1142.1232221373727
     |      >>> t = (np.mean(intake)-7725)/(intake.std(ddof=1)/np.sqrt(len(intake)))
     |      >>> t
     |      -2.8207540608310198
     |
     |      We draw 1000000 samples from Student's t distribution with the adequate
     |      degrees of freedom.
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> s = np.random.standard_t(10, size=1000000)
     |      >>> h = plt.hist(s, bins=100, density=True)
     |
     |      Does our t statistic land in one of the two critical regions found at
     |      both tails of the distribution?
     |
     |      >>> np.sum(np.abs(t) < np.abs(s)) / float(len(s))
     |      0.018318  #random < 0.05, statistic is in critical region
     |
     |      The probability value for this 2-tailed test is about 1.83%, which is
     |      lower than the 5% pre-determined significance threshold.
     |
     |      Therefore, the probability of observing values as extreme as our intake
     |      conditionally on the null hypothesis being true is too low, and we reject
     |      the null hypothesis of no deviation.
     |
     |  tomaxint(...)
     |      tomaxint(size=None)
     |
     |      Return a sample of uniformly distributed random integers in the interval
     |      [0, ``np.iinfo(np.int_).max``]. The `np.int_` type translates to the C long
     |      integer type and its precision is platform dependent.
     |
     |      Parameters
     |      ----------
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  Default is None, in which case a
     |          single value is returned.
     |
     |      Returns
     |      -------
     |      out : ndarray
     |          Drawn samples, with shape `size`.
     |
     |      See Also
     |      --------
     |      randint : Uniform sampling over a given half-open interval of integers.
     |      random_integers : Uniform sampling over a given closed interval of
     |          integers.
     |
     |      Examples
     |      --------
     |      >>> rs = np.random.RandomState() # need a RandomState object
     |      >>> rs.tomaxint((2,2,2))
     |      array([[[1170048599, 1600360186], # random
     |              [ 739731006, 1947757578]],
     |             [[1871712945,  752307660],
     |              [1601631370, 1479324245]]])
     |      >>> rs.tomaxint((2,2,2)) < np.iinfo(np.int_).max
     |      array([[[ True,  True],
     |              [ True,  True]],
     |             [[ True,  True],
     |              [ True,  True]]])
     |
     |  triangular(...)
     |      triangular(left, mode, right, size=None)
     |
     |      Draw samples from the triangular distribution over the
     |      interval ``[left, right]``.
     |
     |      The triangular distribution is a continuous probability
     |      distribution with lower limit left, peak at mode, and upper
     |      limit right. Unlike the other distributions, these parameters
     |      directly define the shape of the pdf.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.triangular`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      left : float or array_like of floats
     |          Lower limit.
     |      mode : float or array_like of floats
     |          The value where the peak of the distribution occurs.
     |          The value must fulfill the condition ``left <= mode <= right``.
     |      right : float or array_like of floats
     |          Upper limit, must be larger than `left`.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``left``, ``mode``, and ``right``
     |          are all scalars.  Otherwise, ``np.broadcast(left, mode, right).size``
     |          samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized triangular distribution.
     |
     |      See Also
     |      --------
     |      random.Generator.triangular: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The probability density function for the triangular distribution is
     |
     |      .. math:: P(x;l, m, r) = \begin{cases}
     |                \frac{2(x-l)}{(r-l)(m-l)}& \text{for $l \leq x \leq m$},\\
     |                \frac{2(r-x)}{(r-l)(r-m)}& \text{for $m \leq x \leq r$},\\
     |                0& \text{otherwise}.
     |                \end{cases}
     |
     |      The triangular distribution is often used in ill-defined
     |      problems where the underlying distribution is not known, but
     |      some knowledge of the limits and mode exists. Often it is used
     |      in simulations.
     |
     |      References
     |      ----------
     |      .. [1] Wikipedia, "Triangular distribution"
     |             https://en.wikipedia.org/wiki/Triangular_distribution
     |
     |      Examples
     |      --------
     |      Draw values from the distribution and plot the histogram:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> h = plt.hist(np.random.triangular(-3, 0, 8, 100000), bins=200,
     |      ...              density=True)
     |      >>> plt.show()
     |
     |  uniform(...)
     |      uniform(low=0.0, high=1.0, size=None)
     |
     |      Draw samples from a uniform distribution.
     |
     |      Samples are uniformly distributed over the half-open interval
     |      ``[low, high)`` (includes low, but excludes high).  In other words,
     |      any value within the given interval is equally likely to be drawn
     |      by `uniform`.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.uniform`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      low : float or array_like of floats, optional
     |          Lower boundary of the output interval.  All values generated will be
     |          greater than or equal to low.  The default value is 0.
     |      high : float or array_like of floats
     |          Upper boundary of the output interval.  All values generated will be
     |          less than or equal to high.  The high limit may be included in the
     |          returned array of floats due to floating-point rounding in the
     |          equation ``low + (high-low) * random_sample()``.  The default value
     |          is 1.0.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``low`` and ``high`` are both scalars.
     |          Otherwise, ``np.broadcast(low, high).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized uniform distribution.
     |
     |      See Also
     |      --------
     |      randint : Discrete uniform distribution, yielding integers.
     |      random_integers : Discrete uniform distribution over the closed
     |                        interval ``[low, high]``.
     |      random_sample : Floats uniformly distributed over ``[0, 1)``.
     |      random : Alias for `random_sample`.
     |      rand : Convenience function that accepts dimensions as input, e.g.,
     |             ``rand(2,2)`` would generate a 2-by-2 array of floats,
     |             uniformly distributed over ``[0, 1)``.
     |      random.Generator.uniform: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The probability density function of the uniform distribution is
     |
     |      .. math:: p(x) = \frac{1}{b - a}
     |
     |      anywhere within the interval ``[a, b)``, and zero elsewhere.
     |
     |      When ``high`` == ``low``, values of ``low`` will be returned.
     |      If ``high`` < ``low``, the results are officially undefined
     |      and may eventually raise an error, i.e. do not rely on this
     |      function to behave when passed arguments satisfying that
     |      inequality condition. The ``high`` limit may be included in the
     |      returned array of floats due to floating-point rounding in the
     |      equation ``low + (high-low) * random_sample()``. For example:
     |
     |      >>> x = np.float32(5*0.99999999)
     |      >>> x
     |      5.0
     |
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> s = np.random.uniform(-1,0,1000)
     |
     |      All values are within the given interval:
     |
     |      >>> np.all(s >= -1)
     |      True
     |      >>> np.all(s < 0)
     |      True
     |
     |      Display the histogram of the samples, along with the
     |      probability density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> count, bins, ignored = plt.hist(s, 15, density=True)
     |      >>> plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
     |      >>> plt.show()
     |
     |  vonmises(...)
     |      vonmises(mu, kappa, size=None)
     |
     |      Draw samples from a von Mises distribution.
     |
     |      Samples are drawn from a von Mises distribution with specified mode
     |      (mu) and dispersion (kappa), on the interval [-pi, pi].
     |
     |      The von Mises distribution (also known as the circular normal
     |      distribution) is a continuous probability distribution on the unit
     |      circle.  It may be thought of as the circular analogue of the normal
     |      distribution.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.vonmises`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      mu : float or array_like of floats
     |          Mode ("center") of the distribution.
     |      kappa : float or array_like of floats
     |          Dispersion of the distribution, has to be >=0.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``mu`` and ``kappa`` are both scalars.
     |          Otherwise, ``np.broadcast(mu, kappa).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized von Mises distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.vonmises : probability density function, distribution, or
     |          cumulative density function, etc.
     |      random.Generator.vonmises: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The probability density for the von Mises distribution is
     |
     |      .. math:: p(x) = \frac{e^{\kappa cos(x-\mu)}}{2\pi I_0(\kappa)},
     |
     |      where :math:`\mu` is the mode and :math:`\kappa` the dispersion,
     |      and :math:`I_0(\kappa)` is the modified Bessel function of order 0.
     |
     |      The von Mises is named for Richard Edler von Mises, who was born in
     |      Austria-Hungary, in what is now the Ukraine.  He fled to the United
     |      States in 1939 and became a professor at Harvard.  He worked in
     |      probability theory, aerodynamics, fluid mechanics, and philosophy of
     |      science.
     |
     |      References
     |      ----------
     |      .. [1] Abramowitz, M. and Stegun, I. A. (Eds.). "Handbook of
     |             Mathematical Functions with Formulas, Graphs, and Mathematical
     |             Tables, 9th printing," New York: Dover, 1972.
     |      .. [2] von Mises, R., "Mathematical Theory of Probability
     |             and Statistics", New York: Academic Press, 1964.
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> mu, kappa = 0.0, 4.0 # mean and dispersion
     |      >>> s = np.random.vonmises(mu, kappa, 1000)
     |
     |      Display the histogram of the samples, along with
     |      the probability density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> from scipy.special import i0  # doctest: +SKIP
     |      >>> plt.hist(s, 50, density=True)
     |      >>> x = np.linspace(-np.pi, np.pi, num=51)
     |      >>> y = np.exp(kappa*np.cos(x-mu))/(2*np.pi*i0(kappa))  # doctest: +SKIP
     |      >>> plt.plot(x, y, linewidth=2, color='r')  # doctest: +SKIP
     |      >>> plt.show()
     |
     |  wald(...)
     |      wald(mean, scale, size=None)
     |
     |      Draw samples from a Wald, or inverse Gaussian, distribution.
     |
     |      As the scale approaches infinity, the distribution becomes more like a
     |      Gaussian. Some references claim that the Wald is an inverse Gaussian
     |      with mean equal to 1, but this is by no means universal.
     |
     |      The inverse Gaussian distribution was first studied in relationship to
     |      Brownian motion. In 1956 M.C.K. Tweedie used the name inverse Gaussian
     |      because there is an inverse relationship between the time to cover a
     |      unit distance and distance covered in unit time.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.wald`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      mean : float or array_like of floats
     |          Distribution mean, must be > 0.
     |      scale : float or array_like of floats
     |          Scale parameter, must be > 0.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``mean`` and ``scale`` are both scalars.
     |          Otherwise, ``np.broadcast(mean, scale).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized Wald distribution.
     |
     |      See Also
     |      --------
     |      random.Generator.wald: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The probability density function for the Wald distribution is
     |
     |      .. math:: P(x;mean,scale) = \sqrt{\frac{scale}{2\pi x^3}}e^
     |                                  \frac{-scale(x-mean)^2}{2\cdotp mean^2x}
     |
     |      As noted above the inverse Gaussian distribution first arise
     |      from attempts to model Brownian motion. It is also a
     |      competitor to the Weibull for use in reliability modeling and
     |      modeling stock returns and interest rate processes.
     |
     |      References
     |      ----------
     |      .. [1] Brighton Webs Ltd., Wald Distribution,
     |             https://web.archive.org/web/20090423014010/http://www.brighton-webs.co.uk:80/distributions/wald.asp
     |      .. [2] Chhikara, Raj S., and Folks, J. Leroy, "The Inverse Gaussian
     |             Distribution: Theory : Methodology, and Applications", CRC Press,
     |             1988.
     |      .. [3] Wikipedia, "Inverse Gaussian distribution"
     |             https://en.wikipedia.org/wiki/Inverse_Gaussian_distribution
     |
     |      Examples
     |      --------
     |      Draw values from the distribution and plot the histogram:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> h = plt.hist(np.random.wald(3, 2, 100000), bins=200, density=True)
     |      >>> plt.show()
     |
     |  weibull(...)
     |      weibull(a, size=None)
     |
     |      Draw samples from a Weibull distribution.
     |
     |      Draw samples from a 1-parameter Weibull distribution with the given
     |      shape parameter `a`.
     |
     |      .. math:: X = (-ln(U))^{1/a}
     |
     |      Here, U is drawn from the uniform distribution over (0,1].
     |
     |      The more common 2-parameter Weibull, including a scale parameter
     |      :math:`\lambda` is just :math:`X = \lambda(-ln(U))^{1/a}`.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.weibull`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      a : float or array_like of floats
     |          Shape parameter of the distribution.  Must be nonnegative.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``a`` is a scalar.  Otherwise,
     |          ``np.array(a).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized Weibull distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.weibull_max
     |      scipy.stats.weibull_min
     |      scipy.stats.genextreme
     |      gumbel
     |      random.Generator.weibull: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The Weibull (or Type III asymptotic extreme value distribution
     |      for smallest values, SEV Type III, or Rosin-Rammler
     |      distribution) is one of a class of Generalized Extreme Value
     |      (GEV) distributions used in modeling extreme value problems.
     |      This class includes the Gumbel and Frechet distributions.
     |
     |      The probability density for the Weibull distribution is
     |
     |      .. math:: p(x) = \frac{a}
     |                       {\lambda}(\frac{x}{\lambda})^{a-1}e^{-(x/\lambda)^a},
     |
     |      where :math:`a` is the shape and :math:`\lambda` the scale.
     |
     |      The function has its peak (the mode) at
     |      :math:`\lambda(\frac{a-1}{a})^{1/a}`.
     |
     |      When ``a = 1``, the Weibull distribution reduces to the exponential
     |      distribution.
     |
     |      References
     |      ----------
     |      .. [1] Waloddi Weibull, Royal Technical University, Stockholm,
     |             1939 "A Statistical Theory Of The Strength Of Materials",
     |             Ingeniorsvetenskapsakademiens Handlingar Nr 151, 1939,
     |             Generalstabens Litografiska Anstalts Forlag, Stockholm.
     |      .. [2] Waloddi Weibull, "A Statistical Distribution Function of
     |             Wide Applicability", Journal Of Applied Mechanics ASME Paper
     |             1951.
     |      .. [3] Wikipedia, "Weibull distribution",
     |             https://en.wikipedia.org/wiki/Weibull_distribution
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> a = 5. # shape
     |      >>> s = np.random.weibull(a, 1000)
     |
     |      Display the histogram of the samples, along with
     |      the probability density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> x = np.arange(1,100.)/50.
     |      >>> def weib(x,n,a):
     |      ...     return (a / n) * (x / n)**(a - 1) * np.exp(-(x / n)**a)
     |
     |      >>> count, bins, ignored = plt.hist(np.random.weibull(5.,1000))
     |      >>> x = np.arange(1,100.)/50.
     |      >>> scale = count.max()/weib(x, 1., 5.).max()
     |      >>> plt.plot(x, weib(x, 1., 5.)*scale)
     |      >>> plt.show()
     |
     |  zipf(...)
     |      zipf(a, size=None)
     |
     |      Draw samples from a Zipf distribution.
     |
     |      Samples are drawn from a Zipf distribution with specified parameter
     |      `a` > 1.
     |
     |      The Zipf distribution (also known as the zeta distribution) is a
     |      discrete probability distribution that satisfies Zipf's law: the
     |      frequency of an item is inversely proportional to its rank in a
     |      frequency table.
     |
     |      .. note::
     |          New code should use the `~numpy.random.Generator.zipf`
     |          method of a `~numpy.random.Generator` instance instead;
     |          please see the :ref:`random-quick-start`.
     |
     |      Parameters
     |      ----------
     |      a : float or array_like of floats
     |          Distribution parameter. Must be greater than 1.
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  If size is ``None`` (default),
     |          a single value is returned if ``a`` is a scalar. Otherwise,
     |          ``np.array(a).size`` samples are drawn.
     |
     |      Returns
     |      -------
     |      out : ndarray or scalar
     |          Drawn samples from the parameterized Zipf distribution.
     |
     |      See Also
     |      --------
     |      scipy.stats.zipf : probability density function, distribution, or
     |          cumulative density function, etc.
     |      random.Generator.zipf: which should be used for new code.
     |
     |      Notes
     |      -----
     |      The probability density for the Zipf distribution is
     |
     |      .. math:: p(k) = \frac{k^{-a}}{\zeta(a)},
     |
     |      for integers :math:`k \geq 1`, where :math:`\zeta` is the Riemann Zeta
     |      function.
     |
     |      It is named for the American linguist George Kingsley Zipf, who noted
     |      that the frequency of any word in a sample of a language is inversely
     |      proportional to its rank in the frequency table.
     |
     |      References
     |      ----------
     |      .. [1] Zipf, G. K., "Selected Studies of the Principle of Relative
     |             Frequency in Language," Cambridge, MA: Harvard Univ. Press,
     |             1932.
     |
     |      Examples
     |      --------
     |      Draw samples from the distribution:
     |
     |      >>> a = 4.0
     |      >>> n = 20000
     |      >>> s = np.random.zipf(a, n)
     |
     |      Display the histogram of the samples, along with
     |      the expected histogram based on the probability
     |      density function:
     |
     |      >>> import matplotlib.pyplot as plt
     |      >>> from scipy.special import zeta  # doctest: +SKIP
     |
     |      `bincount` provides a fast histogram for small integers.
     |
     |      >>> count = np.bincount(s)
     |      >>> k = np.arange(1, s.max() + 1)
     |
     |      >>> plt.bar(k, count[1:], alpha=0.5, label='sample count')
     |      >>> plt.plot(k, n*(k**-a)/zeta(a), 'k.-', alpha=0.5,
     |      ...          label='expected count')   # doctest: +SKIP
     |      >>> plt.semilogy()
     |      >>> plt.grid(alpha=0.4)
     |      >>> plt.legend()
     |      >>> plt.title(f'Zipf sample, a={a}, size={n}')
     |      >>> plt.show()
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __pyx_vtable__ = <capsule object NULL>

    class SFC64(numpy.random.bit_generator.BitGenerator)
     |  SFC64(seed=None)
     |
     |  BitGenerator for Chris Doty-Humphrey's Small Fast Chaotic PRNG.
     |
     |  Parameters
     |  ----------
     |  seed : {None, int, array_like[ints], SeedSequence}, optional
     |      A seed to initialize the `BitGenerator`. If None, then fresh,
     |      unpredictable entropy will be pulled from the OS. If an ``int`` or
     |      ``array_like[ints]`` is passed, then it will be passed to
     |      `SeedSequence` to derive the initial `BitGenerator` state. One may also
     |      pass in a `SeedSequence` instance.
     |
     |  Notes
     |  -----
     |  ``SFC64`` is a 256-bit implementation of Chris Doty-Humphrey's Small Fast
     |  Chaotic PRNG ([1]_). ``SFC64`` has a few different cycles that one might be
     |  on, depending on the seed; the expected period will be about
     |  :math:`2^{255}` ([2]_). ``SFC64`` incorporates a 64-bit counter which means
     |  that the absolute minimum cycle length is :math:`2^{64}` and that distinct
     |  seeds will not run into each other for at least :math:`2^{64}` iterations.
     |
     |  ``SFC64`` provides a capsule containing function pointers that produce
     |  doubles, and unsigned 32 and 64- bit integers. These are not
     |  directly consumable in Python and must be consumed by a ``Generator``
     |  or similar object that supports low-level access.
     |
     |  **State and Seeding**
     |
     |  The ``SFC64`` state vector consists of 4 unsigned 64-bit values. The last
     |  is a 64-bit counter that increments by 1 each iteration.
     |
     |  The input seed is processed by `SeedSequence` to generate the first
     |  3 values, then the ``SFC64`` algorithm is iterated a small number of times
     |  to mix.
     |
     |  **Compatibility Guarantee**
     |
     |  ``SFC64`` makes a guarantee that a fixed seed will always produce the same
     |  random integer stream.
     |
     |  References
     |  ----------
     |  .. [1] `"PractRand"
     |          <http://pracrand.sourceforge.net/RNG_engines.txt>`_
     |  .. [2] `"Random Invertible Mapping Statistics"
     |          <http://www.pcg-random.org/posts/random-invertible-mapping-statistics.html>`_
     |
     |  Method resolution order:
     |      SFC64
     |      numpy.random.bit_generator.BitGenerator
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce_cython__(...)
     |
     |  __setstate_cython__(...)
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
     |  state
     |      Get or set the PRNG state
     |
     |      Returns
     |      -------
     |      state : dict
     |          Dictionary containing the information required to describe the
     |          state of the PRNG
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __pyx_vtable__ = <capsule object NULL>
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from numpy.random.bit_generator.BitGenerator:
     |
     |  __getstate__(...)
     |      Helper for pickle.
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __setstate__(...)
     |
     |  random_raw(...)
     |      random_raw(self, size=None)
     |
     |      Return randoms as generated by the underlying BitGenerator
     |
     |      Parameters
     |      ----------
     |      size : int or tuple of ints, optional
     |          Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
     |          ``m * n * k`` samples are drawn.  Default is None, in which case a
     |          single value is returned.
     |      output : bool, optional
     |          Output values.  Used for performance testing since the generated
     |          values are not returned.
     |
     |      Returns
     |      -------
     |      out : uint or ndarray
     |          Drawn samples.
     |
     |      Notes
     |      -----
     |      This method directly exposes the raw underlying pseudo-random
     |      number generator. All values are returned as unsigned 64-bit
     |      values irrespective of the number of bits produced by the PRNG.
     |
     |      See the class docstring for the number of bits returned.
     |
     |  spawn(...)
     |      spawn(n_children)
     |
     |      Create new independent child bit generators.
     |
     |      See :ref:`seedsequence-spawn` for additional notes on spawning
     |      children.  Some bit generators also implement ``jumped``
     |      as a different approach for creating independent streams.
     |
     |      .. versionadded:: 1.25.0
     |
     |      Parameters
     |      ----------
     |      n_children : int
     |
     |      Returns
     |      -------
     |      child_bit_generators : list of BitGenerators
     |
     |      Raises
     |      ------
     |      TypeError
     |          When the underlying SeedSequence does not implement spawning.
     |
     |      See Also
     |      --------
     |      random.Generator.spawn, random.SeedSequence.spawn :
     |          Equivalent method on the generator and seed sequence.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from numpy.random.bit_generator.BitGenerator:
     |
     |  capsule
     |
     |  cffi
     |      CFFI interface
     |
     |      Returns
     |      -------
     |      interface : namedtuple
     |          Named tuple containing CFFI wrapper
     |
     |          * state_address - Memory address of the state struct
     |          * state - pointer to the state struct
     |          * next_uint64 - function pointer to produce 64 bit integers
     |          * next_uint32 - function pointer to produce 32 bit integers
     |          * next_double - function pointer to produce doubles
     |          * bitgen - pointer to the bit generator struct
     |
     |  ctypes
     |      ctypes interface
     |
     |      Returns
     |      -------
     |      interface : namedtuple
     |          Named tuple containing ctypes wrapper
     |
     |          * state_address - Memory address of the state struct
     |          * state - pointer to the state struct
     |          * next_uint64 - function pointer to produce 64 bit integers
     |          * next_uint32 - function pointer to produce 32 bit integers
     |          * next_double - function pointer to produce doubles
     |          * bitgen - pointer to the bit generator struct
     |
     |  lock
     |
     |  seed_seq
     |      Get the seed sequence used to initialize the bit generator.
     |
     |      .. versionadded:: 1.25.0
     |
     |      Returns
     |      -------
     |      seed_seq : ISeedSequence
     |          The SeedSequence object used to initialize the BitGenerator.
     |          This is normally a `np.random.SeedSequence` instance.

    class SeedSequence(builtins.object)
     |  SeedSequence(entropy=None, *, spawn_key=(), pool_size=4)
     |
     |  SeedSequence mixes sources of entropy in a reproducible way to set the
     |  initial state for independent and very probably non-overlapping
     |  BitGenerators.
     |
     |  Once the SeedSequence is instantiated, you can call the `generate_state`
     |  method to get an appropriately sized seed. Calling `spawn(n) <spawn>` will
     |  create ``n`` SeedSequences that can be used to seed independent
     |  BitGenerators, i.e. for different threads.
     |
     |  Parameters
     |  ----------
     |  entropy : {None, int, sequence[int]}, optional
     |      The entropy for creating a `SeedSequence`.
     |      All integer values must be non-negative.
     |  spawn_key : {(), sequence[int]}, optional
     |      An additional source of entropy based on the position of this
     |      `SeedSequence` in the tree of such objects created with the
     |      `SeedSequence.spawn` method. Typically, only `SeedSequence.spawn` will
     |      set this, and users will not.
     |  pool_size : {int}, optional
     |      Size of the pooled entropy to store. Default is 4 to give a 128-bit
     |      entropy pool. 8 (for 256 bits) is another reasonable choice if working
     |      with larger PRNGs, but there is very little to be gained by selecting
     |      another value.
     |  n_children_spawned : {int}, optional
     |      The number of children already spawned. Only pass this if
     |      reconstructing a `SeedSequence` from a serialized form.
     |
     |  Notes
     |  -----
     |
     |  Best practice for achieving reproducible bit streams is to use
     |  the default ``None`` for the initial entropy, and then use
     |  `SeedSequence.entropy` to log/pickle the `entropy` for reproducibility:
     |
     |  >>> sq1 = np.random.SeedSequence()
     |  >>> sq1.entropy
     |  243799254704924441050048792905230269161  # random
     |  >>> sq2 = np.random.SeedSequence(sq1.entropy)
     |  >>> np.all(sq1.generate_state(10) == sq2.generate_state(10))
     |  True
     |
     |  Methods defined here:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce__ = __reduce_cython__(...)
     |
     |  __repr__(...)
     |      Return repr(self).
     |
     |  __setstate__ = __setstate_cython__(...)
     |
     |  generate_state(...)
     |      generate_state(n_words, dtype=np.uint32)
     |
     |      Return the requested number of words for PRNG seeding.
     |
     |      A BitGenerator should call this method in its constructor with
     |      an appropriate `n_words` parameter to properly seed itself.
     |
     |      Parameters
     |      ----------
     |      n_words : int
     |      dtype : np.uint32 or np.uint64, optional
     |          The size of each word. This should only be either `uint32` or
     |          `uint64`. Strings (`'uint32'`, `'uint64'`) are fine. Note that
     |          requesting `uint64` will draw twice as many bits as `uint32` for
     |          the same `n_words`. This is a convenience for `BitGenerator`s that
     |          express their states as `uint64` arrays.
     |
     |      Returns
     |      -------
     |      state : uint32 or uint64 array, shape=(n_words,)
     |
     |  spawn(...)
     |      spawn(n_children)
     |
     |      Spawn a number of child `SeedSequence` s by extending the
     |      `spawn_key`.
     |
     |      See :ref:`seedsequence-spawn` for additional notes on spawning
     |      children.
     |
     |      Parameters
     |      ----------
     |      n_children : int
     |
     |      Returns
     |      -------
     |      seqs : list of `SeedSequence` s
     |
     |      See Also
     |      --------
     |      random.Generator.spawn, random.BitGenerator.spawn :
     |          Equivalent method on the generator and bit generator.
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
     |  entropy
     |
     |  n_children_spawned
     |
     |  pool
     |
     |  pool_size
     |
     |  spawn_key
     |
     |  state
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __pyx_vtable__ = <capsule object NULL>

FUNCTIONS
    beta(...) method of numpy.random.mtrand.RandomState instance
        beta(a, b, size=None)

        Draw samples from a Beta distribution.

        The Beta distribution is a special case of the Dirichlet distribution,
        and is related to the Gamma distribution.  It has the probability
        distribution function

        .. math:: f(x; a,b) = \frac{1}{B(\alpha, \beta)} x^{\alpha - 1}
                                                         (1 - x)^{\beta - 1},

        where the normalization, B, is the beta function,

        .. math:: B(\alpha, \beta) = \int_0^1 t^{\alpha - 1}
                                     (1 - t)^{\beta - 1} dt.

        It is often seen in Bayesian inference and order statistics.

        .. note::
            New code should use the `~numpy.random.Generator.beta`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.


        Parameters
        ----------
        a : float or array_like of floats
            Alpha, positive (>0).
        b : float or array_like of floats
            Beta, positive (>0).
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``a`` and ``b`` are both scalars.
            Otherwise, ``np.broadcast(a, b).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized beta distribution.

        See Also
        --------
        random.Generator.beta: which should be used for new code.

    binomial(...) method of numpy.random.mtrand.RandomState instance
        binomial(n, p, size=None)

        Draw samples from a binomial distribution.

        Samples are drawn from a binomial distribution with specified
        parameters, n trials and p probability of success where
        n an integer >= 0 and p is in the interval [0,1]. (n may be
        input as a float, but it is truncated to an integer in use)

        .. note::
            New code should use the `~numpy.random.Generator.binomial`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        n : int or array_like of ints
            Parameter of the distribution, >= 0. Floats are also accepted,
            but they will be truncated to integers.
        p : float or array_like of floats
            Parameter of the distribution, >= 0 and <=1.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``n`` and ``p`` are both scalars.
            Otherwise, ``np.broadcast(n, p).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized binomial distribution, where
            each sample is equal to the number of successes over the n trials.

        See Also
        --------
        scipy.stats.binom : probability density function, distribution or
            cumulative density function, etc.
        random.Generator.binomial: which should be used for new code.

        Notes
        -----
        The probability density for the binomial distribution is

        .. math:: P(N) = \binom{n}{N}p^N(1-p)^{n-N},

        where :math:`n` is the number of trials, :math:`p` is the probability
        of success, and :math:`N` is the number of successes.

        When estimating the standard error of a proportion in a population by
        using a random sample, the normal distribution works well unless the
        product p*n <=5, where p = population proportion estimate, and n =
        number of samples, in which case the binomial distribution is used
        instead. For example, a sample of 15 people shows 4 who are left
        handed, and 11 who are right handed. Then p = 4/15 = 27%. 0.27*15 = 4,
        so the binomial distribution should be used in this case.

        References
        ----------
        .. [1] Dalgaard, Peter, "Introductory Statistics with R",
               Springer-Verlag, 2002.
        .. [2] Glantz, Stanton A. "Primer of Biostatistics.", McGraw-Hill,
               Fifth Edition, 2002.
        .. [3] Lentner, Marvin, "Elementary Applied Statistics", Bogden
               and Quigley, 1972.
        .. [4] Weisstein, Eric W. "Binomial Distribution." From MathWorld--A
               Wolfram Web Resource.
               http://mathworld.wolfram.com/BinomialDistribution.html
        .. [5] Wikipedia, "Binomial distribution",
               https://en.wikipedia.org/wiki/Binomial_distribution

        Examples
        --------
        Draw samples from the distribution:

        >>> n, p = 10, .5  # number of trials, probability of each trial
        >>> s = np.random.binomial(n, p, 1000)
        # result of flipping a coin 10 times, tested 1000 times.

        A real world example. A company drills 9 wild-cat oil exploration
        wells, each with an estimated probability of success of 0.1. All nine
        wells fail. What is the probability of that happening?

        Let's do 20,000 trials of the model, and count the number that
        generate zero positive results.

        >>> sum(np.random.binomial(9, 0.1, 20000) == 0)/20000.
        # answer = 0.38885, or 38%.

    bytes(...) method of numpy.random.mtrand.RandomState instance
        bytes(length)

        Return random bytes.

        .. note::
            New code should use the `~numpy.random.Generator.bytes`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        length : int
            Number of random bytes.

        Returns
        -------
        out : bytes
            String of length `length`.

        See Also
        --------
        random.Generator.bytes: which should be used for new code.

        Examples
        --------
        >>> np.random.bytes(10)
        b' eh\x85\x022SZ\xbf\xa4' #random

    chisquare(...) method of numpy.random.mtrand.RandomState instance
        chisquare(df, size=None)

        Draw samples from a chi-square distribution.

        When `df` independent random variables, each with standard normal
        distributions (mean 0, variance 1), are squared and summed, the
        resulting distribution is chi-square (see Notes).  This distribution
        is often used in hypothesis testing.

        .. note::
            New code should use the `~numpy.random.Generator.chisquare`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        df : float or array_like of floats
             Number of degrees of freedom, must be > 0.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``df`` is a scalar.  Otherwise,
            ``np.array(df).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized chi-square distribution.

        Raises
        ------
        ValueError
            When `df` <= 0 or when an inappropriate `size` (e.g. ``size=-1``)
            is given.

        See Also
        --------
        random.Generator.chisquare: which should be used for new code.

        Notes
        -----
        The variable obtained by summing the squares of `df` independent,
        standard normally distributed random variables:

        .. math:: Q = \sum_{i=0}^{\mathtt{df}} X^2_i

        is chi-square distributed, denoted

        .. math:: Q \sim \chi^2_k.

        The probability density function of the chi-squared distribution is

        .. math:: p(x) = \frac{(1/2)^{k/2}}{\Gamma(k/2)}
                         x^{k/2 - 1} e^{-x/2},

        where :math:`\Gamma` is the gamma function,

        .. math:: \Gamma(x) = \int_0^{-\infty} t^{x - 1} e^{-t} dt.

        References
        ----------
        .. [1] NIST "Engineering Statistics Handbook"
               https://www.itl.nist.gov/div898/handbook/eda/section3/eda3666.htm

        Examples
        --------
        >>> np.random.chisquare(2,4)
        array([ 1.89920014,  9.00867716,  3.13710533,  5.62318272]) # random

    choice(...) method of numpy.random.mtrand.RandomState instance
        choice(a, size=None, replace=True, p=None)

        Generates a random sample from a given 1-D array

        .. versionadded:: 1.7.0

        .. note::
            New code should use the `~numpy.random.Generator.choice`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        a : 1-D array-like or int
            If an ndarray, a random sample is generated from its elements.
            If an int, the random sample is generated as if it were ``np.arange(a)``
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  Default is None, in which case a
            single value is returned.
        replace : boolean, optional
            Whether the sample is with or without replacement. Default is True,
            meaning that a value of ``a`` can be selected multiple times.
        p : 1-D array-like, optional
            The probabilities associated with each entry in a.
            If not given, the sample assumes a uniform distribution over all
            entries in ``a``.

        Returns
        -------
        samples : single item or ndarray
            The generated random samples

        Raises
        ------
        ValueError
            If a is an int and less than zero, if a or p are not 1-dimensional,
            if a is an array-like of size 0, if p is not a vector of
            probabilities, if a and p have different lengths, or if
            replace=False and the sample size is greater than the population
            size

        See Also
        --------
        randint, shuffle, permutation
        random.Generator.choice: which should be used in new code

        Notes
        -----
        Setting user-specified probabilities through ``p`` uses a more general but less
        efficient sampler than the default. The general sampler produces a different sample
        than the optimized sampler even if each element of ``p`` is 1 / len(a).

        Sampling random rows from a 2-D array is not possible with this function,
        but is possible with `Generator.choice` through its ``axis`` keyword.

        Examples
        --------
        Generate a uniform random sample from np.arange(5) of size 3:

        >>> np.random.choice(5, 3)
        array([0, 3, 4]) # random
        >>> #This is equivalent to np.random.randint(0,5,3)

        Generate a non-uniform random sample from np.arange(5) of size 3:

        >>> np.random.choice(5, 3, p=[0.1, 0, 0.3, 0.6, 0])
        array([3, 3, 0]) # random

        Generate a uniform random sample from np.arange(5) of size 3 without
        replacement:

        >>> np.random.choice(5, 3, replace=False)
        array([3,1,0]) # random
        >>> #This is equivalent to np.random.permutation(np.arange(5))[:3]

        Generate a non-uniform random sample from np.arange(5) of size
        3 without replacement:

        >>> np.random.choice(5, 3, replace=False, p=[0.1, 0, 0.3, 0.6, 0])
        array([2, 3, 0]) # random

        Any of the above can be repeated with an arbitrary array-like
        instead of just integers. For instance:

        >>> aa_milne_arr = ['pooh', 'rabbit', 'piglet', 'Christopher']
        >>> np.random.choice(aa_milne_arr, 5, p=[0.5, 0.1, 0.1, 0.3])
        array(['pooh', 'pooh', 'pooh', 'Christopher', 'piglet'], # random
              dtype='<U11')

    default_rng(...)
        default_rng(seed=None)
        Construct a new Generator with the default BitGenerator (PCG64).

            Parameters
            ----------
            seed : {None, int, array_like[ints], SeedSequence, BitGenerator, Generator}, optional
                A seed to initialize the `BitGenerator`. If None, then fresh,
                unpredictable entropy will be pulled from the OS. If an ``int`` or
                ``array_like[ints]`` is passed, then it will be passed to
                `SeedSequence` to derive the initial `BitGenerator` state. One may also
                pass in a `SeedSequence` instance.
                Additionally, when passed a `BitGenerator`, it will be wrapped by
                `Generator`. If passed a `Generator`, it will be returned unaltered.

            Returns
            -------
            Generator
                The initialized generator object.

            Notes
            -----
            If ``seed`` is not a `BitGenerator` or a `Generator`, a new `BitGenerator`
            is instantiated. This function does not manage a default global instance.

            See :ref:`seeding_and_entropy` for more information about seeding.

            Examples
            --------
            ``default_rng`` is the recommended constructor for the random number class
            ``Generator``. Here are several ways we can construct a random
            number generator using ``default_rng`` and the ``Generator`` class.

            Here we use ``default_rng`` to generate a random float:

            >>> import numpy as np
            >>> rng = np.random.default_rng(12345)
            >>> print(rng)
            Generator(PCG64)
            >>> rfloat = rng.random()
            >>> rfloat
            0.22733602246716966
            >>> type(rfloat)
            <class 'float'>

            Here we use ``default_rng`` to generate 3 random integers between 0
            (inclusive) and 10 (exclusive):

            >>> import numpy as np
            >>> rng = np.random.default_rng(12345)
            >>> rints = rng.integers(low=0, high=10, size=3)
            >>> rints
            array([6, 2, 7])
            >>> type(rints[0])
            <class 'numpy.int64'>

            Here we specify a seed so that we have reproducible results:

            >>> import numpy as np
            >>> rng = np.random.default_rng(seed=42)
            >>> print(rng)
            Generator(PCG64)
            >>> arr1 = rng.random((3, 3))
            >>> arr1
            array([[0.77395605, 0.43887844, 0.85859792],
                   [0.69736803, 0.09417735, 0.97562235],
                   [0.7611397 , 0.78606431, 0.12811363]])

            If we exit and restart our Python interpreter, we'll see that we
            generate the same random numbers again:

            >>> import numpy as np
            >>> rng = np.random.default_rng(seed=42)
            >>> arr2 = rng.random((3, 3))
            >>> arr2
            array([[0.77395605, 0.43887844, 0.85859792],
                   [0.69736803, 0.09417735, 0.97562235],
                   [0.7611397 , 0.78606431, 0.12811363]])

    dirichlet(...) method of numpy.random.mtrand.RandomState instance
        dirichlet(alpha, size=None)

        Draw samples from the Dirichlet distribution.

        Draw `size` samples of dimension k from a Dirichlet distribution. A
        Dirichlet-distributed random variable can be seen as a multivariate
        generalization of a Beta distribution. The Dirichlet distribution
        is a conjugate prior of a multinomial distribution in Bayesian
        inference.

        .. note::
            New code should use the `~numpy.random.Generator.dirichlet`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        alpha : sequence of floats, length k
            Parameter of the distribution (length ``k`` for sample of
            length ``k``).
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n)``, then
            ``m * n * k`` samples are drawn.  Default is None, in which case a
            vector of length ``k`` is returned.

        Returns
        -------
        samples : ndarray,
            The drawn samples, of shape ``(size, k)``.

        Raises
        ------
        ValueError
            If any value in ``alpha`` is less than or equal to zero

        See Also
        --------
        random.Generator.dirichlet: which should be used for new code.

        Notes
        -----
        The Dirichlet distribution is a distribution over vectors
        :math:`x` that fulfil the conditions :math:`x_i>0` and
        :math:`\sum_{i=1}^k x_i = 1`.

        The probability density function :math:`p` of a
        Dirichlet-distributed random vector :math:`X` is
        proportional to

        .. math:: p(x) \propto \prod_{i=1}^{k}{x^{\alpha_i-1}_i},

        where :math:`\alpha` is a vector containing the positive
        concentration parameters.

        The method uses the following property for computation: let :math:`Y`
        be a random vector which has components that follow a standard gamma
        distribution, then :math:`X = \frac{1}{\sum_{i=1}^k{Y_i}} Y`
        is Dirichlet-distributed

        References
        ----------
        .. [1] David McKay, "Information Theory, Inference and Learning
               Algorithms," chapter 23,
               http://www.inference.org.uk/mackay/itila/
        .. [2] Wikipedia, "Dirichlet distribution",
               https://en.wikipedia.org/wiki/Dirichlet_distribution

        Examples
        --------
        Taking an example cited in Wikipedia, this distribution can be used if
        one wanted to cut strings (each of initial length 1.0) into K pieces
        with different lengths, where each piece had, on average, a designated
        average length, but allowing some variation in the relative sizes of
        the pieces.

        >>> s = np.random.dirichlet((10, 5, 3), 20).transpose()

        >>> import matplotlib.pyplot as plt
        >>> plt.barh(range(20), s[0])
        >>> plt.barh(range(20), s[1], left=s[0], color='g')
        >>> plt.barh(range(20), s[2], left=s[0]+s[1], color='r')
        >>> plt.title("Lengths of Strings")

    exponential(...) method of numpy.random.mtrand.RandomState instance
        exponential(scale=1.0, size=None)

        Draw samples from an exponential distribution.

        Its probability density function is

        .. math:: f(x; \frac{1}{\beta}) = \frac{1}{\beta} \exp(-\frac{x}{\beta}),

        for ``x > 0`` and 0 elsewhere. :math:`\beta` is the scale parameter,
        which is the inverse of the rate parameter :math:`\lambda = 1/\beta`.
        The rate parameter is an alternative, widely used parameterization
        of the exponential distribution [3]_.

        The exponential distribution is a continuous analogue of the
        geometric distribution.  It describes many common situations, such as
        the size of raindrops measured over many rainstorms [1]_, or the time
        between page requests to Wikipedia [2]_.

        .. note::
            New code should use the `~numpy.random.Generator.exponential`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        scale : float or array_like of floats
            The scale parameter, :math:`\beta = 1/\lambda`. Must be
            non-negative.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``scale`` is a scalar.  Otherwise,
            ``np.array(scale).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized exponential distribution.

        Examples
        --------
        A real world example: Assume a company has 10000 customer support
        agents and the average time between customer calls is 4 minutes.

        >>> n = 10000
        >>> time_between_calls = np.random.default_rng().exponential(scale=4, size=n)

        What is the probability that a customer will call in the next
        4 to 5 minutes?

        >>> x = ((time_between_calls < 5).sum())/n
        >>> y = ((time_between_calls < 4).sum())/n
        >>> x-y
        0.08 # may vary

        See Also
        --------
        random.Generator.exponential: which should be used for new code.

        References
        ----------
        .. [1] Peyton Z. Peebles Jr., "Probability, Random Variables and
               Random Signal Principles", 4th ed, 2001, p. 57.
        .. [2] Wikipedia, "Poisson process",
               https://en.wikipedia.org/wiki/Poisson_process
        .. [3] Wikipedia, "Exponential distribution",
               https://en.wikipedia.org/wiki/Exponential_distribution

    f(...) method of numpy.random.mtrand.RandomState instance
        f(dfnum, dfden, size=None)

        Draw samples from an F distribution.

        Samples are drawn from an F distribution with specified parameters,
        `dfnum` (degrees of freedom in numerator) and `dfden` (degrees of
        freedom in denominator), where both parameters must be greater than
        zero.

        The random variate of the F distribution (also known as the
        Fisher distribution) is a continuous probability distribution
        that arises in ANOVA tests, and is the ratio of two chi-square
        variates.

        .. note::
            New code should use the `~numpy.random.Generator.f`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        dfnum : float or array_like of floats
            Degrees of freedom in numerator, must be > 0.
        dfden : float or array_like of float
            Degrees of freedom in denominator, must be > 0.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``dfnum`` and ``dfden`` are both scalars.
            Otherwise, ``np.broadcast(dfnum, dfden).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized Fisher distribution.

        See Also
        --------
        scipy.stats.f : probability density function, distribution or
            cumulative density function, etc.
        random.Generator.f: which should be used for new code.

        Notes
        -----
        The F statistic is used to compare in-group variances to between-group
        variances. Calculating the distribution depends on the sampling, and
        so it is a function of the respective degrees of freedom in the
        problem.  The variable `dfnum` is the number of samples minus one, the
        between-groups degrees of freedom, while `dfden` is the within-groups
        degrees of freedom, the sum of the number of samples in each group
        minus the number of groups.

        References
        ----------
        .. [1] Glantz, Stanton A. "Primer of Biostatistics.", McGraw-Hill,
               Fifth Edition, 2002.
        .. [2] Wikipedia, "F-distribution",
               https://en.wikipedia.org/wiki/F-distribution

        Examples
        --------
        An example from Glantz[1], pp 47-40:

        Two groups, children of diabetics (25 people) and children from people
        without diabetes (25 controls). Fasting blood glucose was measured,
        case group had a mean value of 86.1, controls had a mean value of
        82.2. Standard deviations were 2.09 and 2.49 respectively. Are these
        data consistent with the null hypothesis that the parents diabetic
        status does not affect their children's blood glucose levels?
        Calculating the F statistic from the data gives a value of 36.01.

        Draw samples from the distribution:

        >>> dfnum = 1. # between group degrees of freedom
        >>> dfden = 48. # within groups degrees of freedom
        >>> s = np.random.f(dfnum, dfden, 1000)

        The lower bound for the top 1% of the samples is :

        >>> np.sort(s)[-10]
        7.61988120985 # random

        So there is about a 1% chance that the F statistic will exceed 7.62,
        the measured value is 36, so the null hypothesis is rejected at the 1%
        level.

    gamma(...) method of numpy.random.mtrand.RandomState instance
        gamma(shape, scale=1.0, size=None)

        Draw samples from a Gamma distribution.

        Samples are drawn from a Gamma distribution with specified parameters,
        `shape` (sometimes designated "k") and `scale` (sometimes designated
        "theta"), where both parameters are > 0.

        .. note::
            New code should use the `~numpy.random.Generator.gamma`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        shape : float or array_like of floats
            The shape of the gamma distribution. Must be non-negative.
        scale : float or array_like of floats, optional
            The scale of the gamma distribution. Must be non-negative.
            Default is equal to 1.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``shape`` and ``scale`` are both scalars.
            Otherwise, ``np.broadcast(shape, scale).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized gamma distribution.

        See Also
        --------
        scipy.stats.gamma : probability density function, distribution or
            cumulative density function, etc.
        random.Generator.gamma: which should be used for new code.

        Notes
        -----
        The probability density for the Gamma distribution is

        .. math:: p(x) = x^{k-1}\frac{e^{-x/\theta}}{\theta^k\Gamma(k)},

        where :math:`k` is the shape and :math:`\theta` the scale,
        and :math:`\Gamma` is the Gamma function.

        The Gamma distribution is often used to model the times to failure of
        electronic components, and arises naturally in processes for which the
        waiting times between Poisson distributed events are relevant.

        References
        ----------
        .. [1] Weisstein, Eric W. "Gamma Distribution." From MathWorld--A
               Wolfram Web Resource.
               http://mathworld.wolfram.com/GammaDistribution.html
        .. [2] Wikipedia, "Gamma distribution",
               https://en.wikipedia.org/wiki/Gamma_distribution

        Examples
        --------
        Draw samples from the distribution:

        >>> shape, scale = 2., 2.  # mean=4, std=2*sqrt(2)
        >>> s = np.random.gamma(shape, scale, 1000)

        Display the histogram of the samples, along with
        the probability density function:

        >>> import matplotlib.pyplot as plt
        >>> import scipy.special as sps  # doctest: +SKIP
        >>> count, bins, ignored = plt.hist(s, 50, density=True)
        >>> y = bins**(shape-1)*(np.exp(-bins/scale) /  # doctest: +SKIP
        ...                      (sps.gamma(shape)*scale**shape))
        >>> plt.plot(bins, y, linewidth=2, color='r')  # doctest: +SKIP
        >>> plt.show()

    geometric(...) method of numpy.random.mtrand.RandomState instance
        geometric(p, size=None)

        Draw samples from the geometric distribution.

        Bernoulli trials are experiments with one of two outcomes:
        success or failure (an example of such an experiment is flipping
        a coin).  The geometric distribution models the number of trials
        that must be run in order to achieve success.  It is therefore
        supported on the positive integers, ``k = 1, 2, ...``.

        The probability mass function of the geometric distribution is

        .. math:: f(k) = (1 - p)^{k - 1} p

        where `p` is the probability of success of an individual trial.

        .. note::
            New code should use the `~numpy.random.Generator.geometric`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        p : float or array_like of floats
            The probability of success of an individual trial.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``p`` is a scalar.  Otherwise,
            ``np.array(p).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized geometric distribution.

        See Also
        --------
        random.Generator.geometric: which should be used for new code.

        Examples
        --------
        Draw ten thousand values from the geometric distribution,
        with the probability of an individual success equal to 0.35:

        >>> z = np.random.geometric(p=0.35, size=10000)

        How many trials succeeded after a single run?

        >>> (z == 1).sum() / 10000.
        0.34889999999999999 #random

    get_state(...) method of numpy.random.mtrand.RandomState instance
        get_state(legacy=True)

        Return a tuple representing the internal state of the generator.

        For more details, see `set_state`.

        Parameters
        ----------
        legacy : bool, optional
            Flag indicating to return a legacy tuple state when the BitGenerator
            is MT19937, instead of a dict. Raises ValueError if the underlying
            bit generator is not an instance of MT19937.

        Returns
        -------
        out : {tuple(str, ndarray of 624 uints, int, int, float), dict}
            If legacy is True, the returned tuple has the following items:

            1. the string 'MT19937'.
            2. a 1-D array of 624 unsigned integer keys.
            3. an integer ``pos``.
            4. an integer ``has_gauss``.
            5. a float ``cached_gaussian``.

            If `legacy` is False, or the BitGenerator is not MT19937, then
            state is returned as a dictionary.

        See Also
        --------
        set_state

        Notes
        -----
        `set_state` and `get_state` are not needed to work with any of the
        random distributions in NumPy. If the internal state is manually altered,
        the user should know exactly what he/she is doing.

    gumbel(...) method of numpy.random.mtrand.RandomState instance
        gumbel(loc=0.0, scale=1.0, size=None)

        Draw samples from a Gumbel distribution.

        Draw samples from a Gumbel distribution with specified location and
        scale.  For more information on the Gumbel distribution, see
        Notes and References below.

        .. note::
            New code should use the `~numpy.random.Generator.gumbel`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        loc : float or array_like of floats, optional
            The location of the mode of the distribution. Default is 0.
        scale : float or array_like of floats, optional
            The scale parameter of the distribution. Default is 1. Must be non-
            negative.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``loc`` and ``scale`` are both scalars.
            Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized Gumbel distribution.

        See Also
        --------
        scipy.stats.gumbel_l
        scipy.stats.gumbel_r
        scipy.stats.genextreme
        weibull
        random.Generator.gumbel: which should be used for new code.

        Notes
        -----
        The Gumbel (or Smallest Extreme Value (SEV) or the Smallest Extreme
        Value Type I) distribution is one of a class of Generalized Extreme
        Value (GEV) distributions used in modeling extreme value problems.
        The Gumbel is a special case of the Extreme Value Type I distribution
        for maximums from distributions with "exponential-like" tails.

        The probability density for the Gumbel distribution is

        .. math:: p(x) = \frac{e^{-(x - \mu)/ \beta}}{\beta} e^{ -e^{-(x - \mu)/
                  \beta}},

        where :math:`\mu` is the mode, a location parameter, and
        :math:`\beta` is the scale parameter.

        The Gumbel (named for German mathematician Emil Julius Gumbel) was used
        very early in the hydrology literature, for modeling the occurrence of
        flood events. It is also used for modeling maximum wind speed and
        rainfall rates.  It is a "fat-tailed" distribution - the probability of
        an event in the tail of the distribution is larger than if one used a
        Gaussian, hence the surprisingly frequent occurrence of 100-year
        floods. Floods were initially modeled as a Gaussian process, which
        underestimated the frequency of extreme events.

        It is one of a class of extreme value distributions, the Generalized
        Extreme Value (GEV) distributions, which also includes the Weibull and
        Frechet.

        The function has a mean of :math:`\mu + 0.57721\beta` and a variance
        of :math:`\frac{\pi^2}{6}\beta^2`.

        References
        ----------
        .. [1] Gumbel, E. J., "Statistics of Extremes,"
               New York: Columbia University Press, 1958.
        .. [2] Reiss, R.-D. and Thomas, M., "Statistical Analysis of Extreme
               Values from Insurance, Finance, Hydrology and Other Fields,"
               Basel: Birkhauser Verlag, 2001.

        Examples
        --------
        Draw samples from the distribution:

        >>> mu, beta = 0, 0.1 # location and scale
        >>> s = np.random.gumbel(mu, beta, 1000)

        Display the histogram of the samples, along with
        the probability density function:

        >>> import matplotlib.pyplot as plt
        >>> count, bins, ignored = plt.hist(s, 30, density=True)
        >>> plt.plot(bins, (1/beta)*np.exp(-(bins - mu)/beta)
        ...          * np.exp( -np.exp( -(bins - mu) /beta) ),
        ...          linewidth=2, color='r')
        >>> plt.show()

        Show how an extreme value distribution can arise from a Gaussian process
        and compare to a Gaussian:

        >>> means = []
        >>> maxima = []
        >>> for i in range(0,1000) :
        ...    a = np.random.normal(mu, beta, 1000)
        ...    means.append(a.mean())
        ...    maxima.append(a.max())
        >>> count, bins, ignored = plt.hist(maxima, 30, density=True)
        >>> beta = np.std(maxima) * np.sqrt(6) / np.pi
        >>> mu = np.mean(maxima) - 0.57721*beta
        >>> plt.plot(bins, (1/beta)*np.exp(-(bins - mu)/beta)
        ...          * np.exp(-np.exp(-(bins - mu)/beta)),
        ...          linewidth=2, color='r')
        >>> plt.plot(bins, 1/(beta * np.sqrt(2 * np.pi))
        ...          * np.exp(-(bins - mu)**2 / (2 * beta**2)),
        ...          linewidth=2, color='g')
        >>> plt.show()

    hypergeometric(...) method of numpy.random.mtrand.RandomState instance
        hypergeometric(ngood, nbad, nsample, size=None)

        Draw samples from a Hypergeometric distribution.

        Samples are drawn from a hypergeometric distribution with specified
        parameters, `ngood` (ways to make a good selection), `nbad` (ways to make
        a bad selection), and `nsample` (number of items sampled, which is less
        than or equal to the sum ``ngood + nbad``).

        .. note::
            New code should use the
            `~numpy.random.Generator.hypergeometric`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        ngood : int or array_like of ints
            Number of ways to make a good selection.  Must be nonnegative.
        nbad : int or array_like of ints
            Number of ways to make a bad selection.  Must be nonnegative.
        nsample : int or array_like of ints
            Number of items sampled.  Must be at least 1 and at most
            ``ngood + nbad``.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if `ngood`, `nbad`, and `nsample`
            are all scalars.  Otherwise, ``np.broadcast(ngood, nbad, nsample).size``
            samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized hypergeometric distribution. Each
            sample is the number of good items within a randomly selected subset of
            size `nsample` taken from a set of `ngood` good items and `nbad` bad items.

        See Also
        --------
        scipy.stats.hypergeom : probability density function, distribution or
            cumulative density function, etc.
        random.Generator.hypergeometric: which should be used for new code.

        Notes
        -----
        The probability density for the Hypergeometric distribution is

        .. math:: P(x) = \frac{\binom{g}{x}\binom{b}{n-x}}{\binom{g+b}{n}},

        where :math:`0 \le x \le n` and :math:`n-b \le x \le g`

        for P(x) the probability of ``x`` good results in the drawn sample,
        g = `ngood`, b = `nbad`, and n = `nsample`.

        Consider an urn with black and white marbles in it, `ngood` of them
        are black and `nbad` are white. If you draw `nsample` balls without
        replacement, then the hypergeometric distribution describes the
        distribution of black balls in the drawn sample.

        Note that this distribution is very similar to the binomial
        distribution, except that in this case, samples are drawn without
        replacement, whereas in the Binomial case samples are drawn with
        replacement (or the sample space is infinite). As the sample space
        becomes large, this distribution approaches the binomial.

        References
        ----------
        .. [1] Lentner, Marvin, "Elementary Applied Statistics", Bogden
               and Quigley, 1972.
        .. [2] Weisstein, Eric W. "Hypergeometric Distribution." From
               MathWorld--A Wolfram Web Resource.
               http://mathworld.wolfram.com/HypergeometricDistribution.html
        .. [3] Wikipedia, "Hypergeometric distribution",
               https://en.wikipedia.org/wiki/Hypergeometric_distribution

        Examples
        --------
        Draw samples from the distribution:

        >>> ngood, nbad, nsamp = 100, 2, 10
        # number of good, number of bad, and number of samples
        >>> s = np.random.hypergeometric(ngood, nbad, nsamp, 1000)
        >>> from matplotlib.pyplot import hist
        >>> hist(s)
        #   note that it is very unlikely to grab both bad items

        Suppose you have an urn with 15 white and 15 black marbles.
        If you pull 15 marbles at random, how likely is it that
        12 or more of them are one color?

        >>> s = np.random.hypergeometric(15, 15, 15, 100000)
        >>> sum(s>=12)/100000. + sum(s<=3)/100000.
        #   answer = 0.003 ... pretty unlikely!

    laplace(...) method of numpy.random.mtrand.RandomState instance
        laplace(loc=0.0, scale=1.0, size=None)

        Draw samples from the Laplace or double exponential distribution with
        specified location (or mean) and scale (decay).

        The Laplace distribution is similar to the Gaussian/normal distribution,
        but is sharper at the peak and has fatter tails. It represents the
        difference between two independent, identically distributed exponential
        random variables.

        .. note::
            New code should use the `~numpy.random.Generator.laplace`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        loc : float or array_like of floats, optional
            The position, :math:`\mu`, of the distribution peak. Default is 0.
        scale : float or array_like of floats, optional
            :math:`\lambda`, the exponential decay. Default is 1. Must be non-
            negative.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``loc`` and ``scale`` are both scalars.
            Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized Laplace distribution.

        See Also
        --------
        random.Generator.laplace: which should be used for new code.

        Notes
        -----
        It has the probability density function

        .. math:: f(x; \mu, \lambda) = \frac{1}{2\lambda}
                                       \exp\left(-\frac{|x - \mu|}{\lambda}\right).

        The first law of Laplace, from 1774, states that the frequency
        of an error can be expressed as an exponential function of the
        absolute magnitude of the error, which leads to the Laplace
        distribution. For many problems in economics and health
        sciences, this distribution seems to model the data better
        than the standard Gaussian distribution.

        References
        ----------
        .. [1] Abramowitz, M. and Stegun, I. A. (Eds.). "Handbook of
               Mathematical Functions with Formulas, Graphs, and Mathematical
               Tables, 9th printing," New York: Dover, 1972.
        .. [2] Kotz, Samuel, et. al. "The Laplace Distribution and
               Generalizations, " Birkhauser, 2001.
        .. [3] Weisstein, Eric W. "Laplace Distribution."
               From MathWorld--A Wolfram Web Resource.
               http://mathworld.wolfram.com/LaplaceDistribution.html
        .. [4] Wikipedia, "Laplace distribution",
               https://en.wikipedia.org/wiki/Laplace_distribution

        Examples
        --------
        Draw samples from the distribution

        >>> loc, scale = 0., 1.
        >>> s = np.random.laplace(loc, scale, 1000)

        Display the histogram of the samples, along with
        the probability density function:

        >>> import matplotlib.pyplot as plt
        >>> count, bins, ignored = plt.hist(s, 30, density=True)
        >>> x = np.arange(-8., 8., .01)
        >>> pdf = np.exp(-abs(x-loc)/scale)/(2.*scale)
        >>> plt.plot(x, pdf)

        Plot Gaussian for comparison:

        >>> g = (1/(scale * np.sqrt(2 * np.pi)) *
        ...      np.exp(-(x - loc)**2 / (2 * scale**2)))
        >>> plt.plot(x,g)

    logistic(...) method of numpy.random.mtrand.RandomState instance
        logistic(loc=0.0, scale=1.0, size=None)

        Draw samples from a logistic distribution.

        Samples are drawn from a logistic distribution with specified
        parameters, loc (location or mean, also median), and scale (>0).

        .. note::
            New code should use the `~numpy.random.Generator.logistic`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        loc : float or array_like of floats, optional
            Parameter of the distribution. Default is 0.
        scale : float or array_like of floats, optional
            Parameter of the distribution. Must be non-negative.
            Default is 1.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``loc`` and ``scale`` are both scalars.
            Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized logistic distribution.

        See Also
        --------
        scipy.stats.logistic : probability density function, distribution or
            cumulative density function, etc.
        random.Generator.logistic: which should be used for new code.

        Notes
        -----
        The probability density for the Logistic distribution is

        .. math:: P(x) = P(x) = \frac{e^{-(x-\mu)/s}}{s(1+e^{-(x-\mu)/s})^2},

        where :math:`\mu` = location and :math:`s` = scale.

        The Logistic distribution is used in Extreme Value problems where it
        can act as a mixture of Gumbel distributions, in Epidemiology, and by
        the World Chess Federation (FIDE) where it is used in the Elo ranking
        system, assuming the performance of each player is a logistically
        distributed random variable.

        References
        ----------
        .. [1] Reiss, R.-D. and Thomas M. (2001), "Statistical Analysis of
               Extreme Values, from Insurance, Finance, Hydrology and Other
               Fields," Birkhauser Verlag, Basel, pp 132-133.
        .. [2] Weisstein, Eric W. "Logistic Distribution." From
               MathWorld--A Wolfram Web Resource.
               http://mathworld.wolfram.com/LogisticDistribution.html
        .. [3] Wikipedia, "Logistic-distribution",
               https://en.wikipedia.org/wiki/Logistic_distribution

        Examples
        --------
        Draw samples from the distribution:

        >>> loc, scale = 10, 1
        >>> s = np.random.logistic(loc, scale, 10000)
        >>> import matplotlib.pyplot as plt
        >>> count, bins, ignored = plt.hist(s, bins=50)

        #   plot against distribution

        >>> def logist(x, loc, scale):
        ...     return np.exp((loc-x)/scale)/(scale*(1+np.exp((loc-x)/scale))**2)
        >>> lgst_val = logist(bins, loc, scale)
        >>> plt.plot(bins, lgst_val * count.max() / lgst_val.max())
        >>> plt.show()

    lognormal(...) method of numpy.random.mtrand.RandomState instance
        lognormal(mean=0.0, sigma=1.0, size=None)

        Draw samples from a log-normal distribution.

        Draw samples from a log-normal distribution with specified mean,
        standard deviation, and array shape.  Note that the mean and standard
        deviation are not the values for the distribution itself, but of the
        underlying normal distribution it is derived from.

        .. note::
            New code should use the `~numpy.random.Generator.lognormal`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        mean : float or array_like of floats, optional
            Mean value of the underlying normal distribution. Default is 0.
        sigma : float or array_like of floats, optional
            Standard deviation of the underlying normal distribution. Must be
            non-negative. Default is 1.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``mean`` and ``sigma`` are both scalars.
            Otherwise, ``np.broadcast(mean, sigma).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized log-normal distribution.

        See Also
        --------
        scipy.stats.lognorm : probability density function, distribution,
            cumulative density function, etc.
        random.Generator.lognormal: which should be used for new code.

        Notes
        -----
        A variable `x` has a log-normal distribution if `log(x)` is normally
        distributed.  The probability density function for the log-normal
        distribution is:

        .. math:: p(x) = \frac{1}{\sigma x \sqrt{2\pi}}
                         e^{(-\frac{(ln(x)-\mu)^2}{2\sigma^2})}

        where :math:`\mu` is the mean and :math:`\sigma` is the standard
        deviation of the normally distributed logarithm of the variable.
        A log-normal distribution results if a random variable is the *product*
        of a large number of independent, identically-distributed variables in
        the same way that a normal distribution results if the variable is the
        *sum* of a large number of independent, identically-distributed
        variables.

        References
        ----------
        .. [1] Limpert, E., Stahel, W. A., and Abbt, M., "Log-normal
               Distributions across the Sciences: Keys and Clues,"
               BioScience, Vol. 51, No. 5, May, 2001.
               https://stat.ethz.ch/~stahel/lognormal/bioscience.pdf
        .. [2] Reiss, R.D. and Thomas, M., "Statistical Analysis of Extreme
               Values," Basel: Birkhauser Verlag, 2001, pp. 31-32.

        Examples
        --------
        Draw samples from the distribution:

        >>> mu, sigma = 3., 1. # mean and standard deviation
        >>> s = np.random.lognormal(mu, sigma, 1000)

        Display the histogram of the samples, along with
        the probability density function:

        >>> import matplotlib.pyplot as plt
        >>> count, bins, ignored = plt.hist(s, 100, density=True, align='mid')

        >>> x = np.linspace(min(bins), max(bins), 10000)
        >>> pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
        ...        / (x * sigma * np.sqrt(2 * np.pi)))

        >>> plt.plot(x, pdf, linewidth=2, color='r')
        >>> plt.axis('tight')
        >>> plt.show()

        Demonstrate that taking the products of random samples from a uniform
        distribution can be fit well by a log-normal probability density
        function.

        >>> # Generate a thousand samples: each is the product of 100 random
        >>> # values, drawn from a normal distribution.
        >>> b = []
        >>> for i in range(1000):
        ...    a = 10. + np.random.standard_normal(100)
        ...    b.append(np.prod(a))

        >>> b = np.array(b) / np.min(b) # scale values to be positive
        >>> count, bins, ignored = plt.hist(b, 100, density=True, align='mid')
        >>> sigma = np.std(np.log(b))
        >>> mu = np.mean(np.log(b))

        >>> x = np.linspace(min(bins), max(bins), 10000)
        >>> pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
        ...        / (x * sigma * np.sqrt(2 * np.pi)))

        >>> plt.plot(x, pdf, color='r', linewidth=2)
        >>> plt.show()

    logseries(...) method of numpy.random.mtrand.RandomState instance
        logseries(p, size=None)

        Draw samples from a logarithmic series distribution.

        Samples are drawn from a log series distribution with specified
        shape parameter, 0 <= ``p`` < 1.

        .. note::
            New code should use the `~numpy.random.Generator.logseries`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        p : float or array_like of floats
            Shape parameter for the distribution.  Must be in the range [0, 1).
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``p`` is a scalar.  Otherwise,
            ``np.array(p).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized logarithmic series distribution.

        See Also
        --------
        scipy.stats.logser : probability density function, distribution or
            cumulative density function, etc.
        random.Generator.logseries: which should be used for new code.

        Notes
        -----
        The probability density for the Log Series distribution is

        .. math:: P(k) = \frac{-p^k}{k \ln(1-p)},

        where p = probability.

        The log series distribution is frequently used to represent species
        richness and occurrence, first proposed by Fisher, Corbet, and
        Williams in 1943 [2].  It may also be used to model the numbers of
        occupants seen in cars [3].

        References
        ----------
        .. [1] Buzas, Martin A.; Culver, Stephen J.,  Understanding regional
               species diversity through the log series distribution of
               occurrences: BIODIVERSITY RESEARCH Diversity & Distributions,
               Volume 5, Number 5, September 1999 , pp. 187-195(9).
        .. [2] Fisher, R.A,, A.S. Corbet, and C.B. Williams. 1943. The
               relation between the number of species and the number of
               individuals in a random sample of an animal population.
               Journal of Animal Ecology, 12:42-58.
        .. [3] D. J. Hand, F. Daly, D. Lunn, E. Ostrowski, A Handbook of Small
               Data Sets, CRC Press, 1994.
        .. [4] Wikipedia, "Logarithmic distribution",
               https://en.wikipedia.org/wiki/Logarithmic_distribution

        Examples
        --------
        Draw samples from the distribution:

        >>> a = .6
        >>> s = np.random.logseries(a, 10000)
        >>> import matplotlib.pyplot as plt
        >>> count, bins, ignored = plt.hist(s)

        #   plot against distribution

        >>> def logseries(k, p):
        ...     return -p**k/(k*np.log(1-p))
        >>> plt.plot(bins, logseries(bins, a)*count.max()/
        ...          logseries(bins, a).max(), 'r')
        >>> plt.show()

    multinomial(...) method of numpy.random.mtrand.RandomState instance
        multinomial(n, pvals, size=None)

        Draw samples from a multinomial distribution.

        The multinomial distribution is a multivariate generalization of the
        binomial distribution.  Take an experiment with one of ``p``
        possible outcomes.  An example of such an experiment is throwing a dice,
        where the outcome can be 1 through 6.  Each sample drawn from the
        distribution represents `n` such experiments.  Its values,
        ``X_i = [X_0, X_1, ..., X_p]``, represent the number of times the
        outcome was ``i``.

        .. note::
            New code should use the `~numpy.random.Generator.multinomial`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        n : int
            Number of experiments.
        pvals : sequence of floats, length p
            Probabilities of each of the ``p`` different outcomes.  These
            must sum to 1 (however, the last element is always assumed to
            account for the remaining probability, as long as
            ``sum(pvals[:-1]) <= 1)``.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  Default is None, in which case a
            single value is returned.

        Returns
        -------
        out : ndarray
            The drawn samples, of shape *size*, if that was provided.  If not,
            the shape is ``(N,)``.

            In other words, each entry ``out[i,j,...,:]`` is an N-dimensional
            value drawn from the distribution.

        See Also
        --------
        random.Generator.multinomial: which should be used for new code.

        Examples
        --------
        Throw a dice 20 times:

        >>> np.random.multinomial(20, [1/6.]*6, size=1)
        array([[4, 1, 7, 5, 2, 1]]) # random

        It landed 4 times on 1, once on 2, etc.

        Now, throw the dice 20 times, and 20 times again:

        >>> np.random.multinomial(20, [1/6.]*6, size=2)
        array([[3, 4, 3, 3, 4, 3], # random
               [2, 4, 3, 4, 0, 7]])

        For the first run, we threw 3 times 1, 4 times 2, etc.  For the second,
        we threw 2 times 1, 4 times 2, etc.

        A loaded die is more likely to land on number 6:

        >>> np.random.multinomial(100, [1/7.]*5 + [2/7.])
        array([11, 16, 14, 17, 16, 26]) # random

        The probability inputs should be normalized. As an implementation
        detail, the value of the last entry is ignored and assumed to take
        up any leftover probability mass, but this should not be relied on.
        A biased coin which has twice as much weight on one side as on the
        other should be sampled like so:

        >>> np.random.multinomial(100, [1.0 / 3, 2.0 / 3])  # RIGHT
        array([38, 62]) # random

        not like:

        >>> np.random.multinomial(100, [1.0, 2.0])  # WRONG
        Traceback (most recent call last):
        ValueError: pvals < 0, pvals > 1 or pvals contains NaNs

    multivariate_normal(...) method of numpy.random.mtrand.RandomState instance
        multivariate_normal(mean, cov, size=None, check_valid='warn', tol=1e-8)

        Draw random samples from a multivariate normal distribution.

        The multivariate normal, multinormal or Gaussian distribution is a
        generalization of the one-dimensional normal distribution to higher
        dimensions.  Such a distribution is specified by its mean and
        covariance matrix.  These parameters are analogous to the mean
        (average or "center") and variance (standard deviation, or "width,"
        squared) of the one-dimensional normal distribution.

        .. note::
            New code should use the
            `~numpy.random.Generator.multivariate_normal`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        mean : 1-D array_like, of length N
            Mean of the N-dimensional distribution.
        cov : 2-D array_like, of shape (N, N)
            Covariance matrix of the distribution. It must be symmetric and
            positive-semidefinite for proper sampling.
        size : int or tuple of ints, optional
            Given a shape of, for example, ``(m,n,k)``, ``m*n*k`` samples are
            generated, and packed in an `m`-by-`n`-by-`k` arrangement.  Because
            each sample is `N`-dimensional, the output shape is ``(m,n,k,N)``.
            If no shape is specified, a single (`N`-D) sample is returned.
        check_valid : { 'warn', 'raise', 'ignore' }, optional
            Behavior when the covariance matrix is not positive semidefinite.
        tol : float, optional
            Tolerance when checking the singular values in covariance matrix.
            cov is cast to double before the check.

        Returns
        -------
        out : ndarray
            The drawn samples, of shape *size*, if that was provided.  If not,
            the shape is ``(N,)``.

            In other words, each entry ``out[i,j,...,:]`` is an N-dimensional
            value drawn from the distribution.

        See Also
        --------
        random.Generator.multivariate_normal: which should be used for new code.

        Notes
        -----
        The mean is a coordinate in N-dimensional space, which represents the
        location where samples are most likely to be generated.  This is
        analogous to the peak of the bell curve for the one-dimensional or
        univariate normal distribution.

        Covariance indicates the level to which two variables vary together.
        From the multivariate normal distribution, we draw N-dimensional
        samples, :math:`X = [x_1, x_2, ... x_N]`.  The covariance matrix
        element :math:`C_{ij}` is the covariance of :math:`x_i` and :math:`x_j`.
        The element :math:`C_{ii}` is the variance of :math:`x_i` (i.e. its
        "spread").

        Instead of specifying the full covariance matrix, popular
        approximations include:

          - Spherical covariance (`cov` is a multiple of the identity matrix)
          - Diagonal covariance (`cov` has non-negative elements, and only on
            the diagonal)

        This geometrical property can be seen in two dimensions by plotting
        generated data-points:

        >>> mean = [0, 0]
        >>> cov = [[1, 0], [0, 100]]  # diagonal covariance

        Diagonal covariance means that points are oriented along x or y-axis:

        >>> import matplotlib.pyplot as plt
        >>> x, y = np.random.multivariate_normal(mean, cov, 5000).T
        >>> plt.plot(x, y, 'x')
        >>> plt.axis('equal')
        >>> plt.show()

        Note that the covariance matrix must be positive semidefinite (a.k.a.
        nonnegative-definite). Otherwise, the behavior of this method is
        undefined and backwards compatibility is not guaranteed.

        References
        ----------
        .. [1] Papoulis, A., "Probability, Random Variables, and Stochastic
               Processes," 3rd ed., New York: McGraw-Hill, 1991.
        .. [2] Duda, R. O., Hart, P. E., and Stork, D. G., "Pattern
               Classification," 2nd ed., New York: Wiley, 2001.

        Examples
        --------
        >>> mean = (1, 2)
        >>> cov = [[1, 0], [0, 1]]
        >>> x = np.random.multivariate_normal(mean, cov, (3, 3))
        >>> x.shape
        (3, 3, 2)

        Here we generate 800 samples from the bivariate normal distribution
        with mean [0, 0] and covariance matrix [[6, -3], [-3, 3.5]].  The
        expected variances of the first and second components of the sample
        are 6 and 3.5, respectively, and the expected correlation
        coefficient is -3/sqrt(6*3.5) ≈ -0.65465.

        >>> cov = np.array([[6, -3], [-3, 3.5]])
        >>> pts = np.random.multivariate_normal([0, 0], cov, size=800)

        Check that the mean, covariance, and correlation coefficient of the
        sample are close to the expected values:

        >>> pts.mean(axis=0)
        array([ 0.0326911 , -0.01280782])  # may vary
        >>> np.cov(pts.T)
        array([[ 5.96202397, -2.85602287],
               [-2.85602287,  3.47613949]])  # may vary
        >>> np.corrcoef(pts.T)[0, 1]
        -0.6273591314603949  # may vary

        We can visualize this data with a scatter plot.  The orientation
        of the point cloud illustrates the negative correlation of the
        components of this sample.

        >>> import matplotlib.pyplot as plt
        >>> plt.plot(pts[:, 0], pts[:, 1], '.', alpha=0.5)
        >>> plt.axis('equal')
        >>> plt.grid()
        >>> plt.show()

    negative_binomial(...) method of numpy.random.mtrand.RandomState instance
        negative_binomial(n, p, size=None)

        Draw samples from a negative binomial distribution.

        Samples are drawn from a negative binomial distribution with specified
        parameters, `n` successes and `p` probability of success where `n`
        is > 0 and `p` is in the interval [0, 1].

        .. note::
            New code should use the
            `~numpy.random.Generator.negative_binomial`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        n : float or array_like of floats
            Parameter of the distribution, > 0.
        p : float or array_like of floats
            Parameter of the distribution, >= 0 and <=1.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``n`` and ``p`` are both scalars.
            Otherwise, ``np.broadcast(n, p).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized negative binomial distribution,
            where each sample is equal to N, the number of failures that
            occurred before a total of n successes was reached.

        See Also
        --------
        random.Generator.negative_binomial: which should be used for new code.

        Notes
        -----
        The probability mass function of the negative binomial distribution is

        .. math:: P(N;n,p) = \frac{\Gamma(N+n)}{N!\Gamma(n)}p^{n}(1-p)^{N},

        where :math:`n` is the number of successes, :math:`p` is the
        probability of success, :math:`N+n` is the number of trials, and
        :math:`\Gamma` is the gamma function. When :math:`n` is an integer,
        :math:`\frac{\Gamma(N+n)}{N!\Gamma(n)} = \binom{N+n-1}{N}`, which is
        the more common form of this term in the pmf. The negative
        binomial distribution gives the probability of N failures given n
        successes, with a success on the last trial.

        If one throws a die repeatedly until the third time a "1" appears,
        then the probability distribution of the number of non-"1"s that
        appear before the third "1" is a negative binomial distribution.

        References
        ----------
        .. [1] Weisstein, Eric W. "Negative Binomial Distribution." From
               MathWorld--A Wolfram Web Resource.
               http://mathworld.wolfram.com/NegativeBinomialDistribution.html
        .. [2] Wikipedia, "Negative binomial distribution",
               https://en.wikipedia.org/wiki/Negative_binomial_distribution

        Examples
        --------
        Draw samples from the distribution:

        A real world example. A company drills wild-cat oil
        exploration wells, each with an estimated probability of
        success of 0.1.  What is the probability of having one success
        for each successive well, that is what is the probability of a
        single success after drilling 5 wells, after 6 wells, etc.?

        >>> s = np.random.negative_binomial(1, 0.1, 100000)
        >>> for i in range(1, 11): # doctest: +SKIP
        ...    probability = sum(s<i) / 100000.
        ...    print(i, "wells drilled, probability of one success =", probability)

    noncentral_chisquare(...) method of numpy.random.mtrand.RandomState instance
        noncentral_chisquare(df, nonc, size=None)

        Draw samples from a noncentral chi-square distribution.

        The noncentral :math:`\chi^2` distribution is a generalization of
        the :math:`\chi^2` distribution.

        .. note::
            New code should use the
            `~numpy.random.Generator.noncentral_chisquare`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        df : float or array_like of floats
            Degrees of freedom, must be > 0.

            .. versionchanged:: 1.10.0
               Earlier NumPy versions required dfnum > 1.
        nonc : float or array_like of floats
            Non-centrality, must be non-negative.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``df`` and ``nonc`` are both scalars.
            Otherwise, ``np.broadcast(df, nonc).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized noncentral chi-square distribution.

        See Also
        --------
        random.Generator.noncentral_chisquare: which should be used for new code.

        Notes
        -----
        The probability density function for the noncentral Chi-square
        distribution is

        .. math:: P(x;df,nonc) = \sum^{\infty}_{i=0}
                               \frac{e^{-nonc/2}(nonc/2)^{i}}{i!}
                               P_{Y_{df+2i}}(x),

        where :math:`Y_{q}` is the Chi-square with q degrees of freedom.

        References
        ----------
        .. [1] Wikipedia, "Noncentral chi-squared distribution"
               https://en.wikipedia.org/wiki/Noncentral_chi-squared_distribution

        Examples
        --------
        Draw values from the distribution and plot the histogram

        >>> import matplotlib.pyplot as plt
        >>> values = plt.hist(np.random.noncentral_chisquare(3, 20, 100000),
        ...                   bins=200, density=True)
        >>> plt.show()

        Draw values from a noncentral chisquare with very small noncentrality,
        and compare to a chisquare.

        >>> plt.figure()
        >>> values = plt.hist(np.random.noncentral_chisquare(3, .0000001, 100000),
        ...                   bins=np.arange(0., 25, .1), density=True)
        >>> values2 = plt.hist(np.random.chisquare(3, 100000),
        ...                    bins=np.arange(0., 25, .1), density=True)
        >>> plt.plot(values[1][0:-1], values[0]-values2[0], 'ob')
        >>> plt.show()

        Demonstrate how large values of non-centrality lead to a more symmetric
        distribution.

        >>> plt.figure()
        >>> values = plt.hist(np.random.noncentral_chisquare(3, 20, 100000),
        ...                   bins=200, density=True)
        >>> plt.show()

    noncentral_f(...) method of numpy.random.mtrand.RandomState instance
        noncentral_f(dfnum, dfden, nonc, size=None)

        Draw samples from the noncentral F distribution.

        Samples are drawn from an F distribution with specified parameters,
        `dfnum` (degrees of freedom in numerator) and `dfden` (degrees of
        freedom in denominator), where both parameters > 1.
        `nonc` is the non-centrality parameter.

        .. note::
            New code should use the
            `~numpy.random.Generator.noncentral_f`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        dfnum : float or array_like of floats
            Numerator degrees of freedom, must be > 0.

            .. versionchanged:: 1.14.0
               Earlier NumPy versions required dfnum > 1.
        dfden : float or array_like of floats
            Denominator degrees of freedom, must be > 0.
        nonc : float or array_like of floats
            Non-centrality parameter, the sum of the squares of the numerator
            means, must be >= 0.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``dfnum``, ``dfden``, and ``nonc``
            are all scalars.  Otherwise, ``np.broadcast(dfnum, dfden, nonc).size``
            samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized noncentral Fisher distribution.

        See Also
        --------
        random.Generator.noncentral_f: which should be used for new code.

        Notes
        -----
        When calculating the power of an experiment (power = probability of
        rejecting the null hypothesis when a specific alternative is true) the
        non-central F statistic becomes important.  When the null hypothesis is
        true, the F statistic follows a central F distribution. When the null
        hypothesis is not true, then it follows a non-central F statistic.

        References
        ----------
        .. [1] Weisstein, Eric W. "Noncentral F-Distribution."
               From MathWorld--A Wolfram Web Resource.
               http://mathworld.wolfram.com/NoncentralF-Distribution.html
        .. [2] Wikipedia, "Noncentral F-distribution",
               https://en.wikipedia.org/wiki/Noncentral_F-distribution

        Examples
        --------
        In a study, testing for a specific alternative to the null hypothesis
        requires use of the Noncentral F distribution. We need to calculate the
        area in the tail of the distribution that exceeds the value of the F
        distribution for the null hypothesis.  We'll plot the two probability
        distributions for comparison.

        >>> dfnum = 3 # between group deg of freedom
        >>> dfden = 20 # within groups degrees of freedom
        >>> nonc = 3.0
        >>> nc_vals = np.random.noncentral_f(dfnum, dfden, nonc, 1000000)
        >>> NF = np.histogram(nc_vals, bins=50, density=True)
        >>> c_vals = np.random.f(dfnum, dfden, 1000000)
        >>> F = np.histogram(c_vals, bins=50, density=True)
        >>> import matplotlib.pyplot as plt
        >>> plt.plot(F[1][1:], F[0])
        >>> plt.plot(NF[1][1:], NF[0])
        >>> plt.show()

    normal(...) method of numpy.random.mtrand.RandomState instance
        normal(loc=0.0, scale=1.0, size=None)

        Draw random samples from a normal (Gaussian) distribution.

        The probability density function of the normal distribution, first
        derived by De Moivre and 200 years later by both Gauss and Laplace
        independently [2]_, is often called the bell curve because of
        its characteristic shape (see the example below).

        The normal distributions occurs often in nature.  For example, it
        describes the commonly occurring distribution of samples influenced
        by a large number of tiny, random disturbances, each with its own
        unique distribution [2]_.

        .. note::
            New code should use the `~numpy.random.Generator.normal`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        loc : float or array_like of floats
            Mean ("centre") of the distribution.
        scale : float or array_like of floats
            Standard deviation (spread or "width") of the distribution. Must be
            non-negative.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``loc`` and ``scale`` are both scalars.
            Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized normal distribution.

        See Also
        --------
        scipy.stats.norm : probability density function, distribution or
            cumulative density function, etc.
        random.Generator.normal: which should be used for new code.

        Notes
        -----
        The probability density for the Gaussian distribution is

        .. math:: p(x) = \frac{1}{\sqrt{ 2 \pi \sigma^2 }}
                         e^{ - \frac{ (x - \mu)^2 } {2 \sigma^2} },

        where :math:`\mu` is the mean and :math:`\sigma` the standard
        deviation. The square of the standard deviation, :math:`\sigma^2`,
        is called the variance.

        The function has its peak at the mean, and its "spread" increases with
        the standard deviation (the function reaches 0.607 times its maximum at
        :math:`x + \sigma` and :math:`x - \sigma` [2]_).  This implies that
        normal is more likely to return samples lying close to the mean, rather
        than those far away.

        References
        ----------
        .. [1] Wikipedia, "Normal distribution",
               https://en.wikipedia.org/wiki/Normal_distribution
        .. [2] P. R. Peebles Jr., "Central Limit Theorem" in "Probability,
               Random Variables and Random Signal Principles", 4th ed., 2001,
               pp. 51, 51, 125.

        Examples
        --------
        Draw samples from the distribution:

        >>> mu, sigma = 0, 0.1 # mean and standard deviation
        >>> s = np.random.normal(mu, sigma, 1000)

        Verify the mean and the variance:

        >>> abs(mu - np.mean(s))
        0.0  # may vary

        >>> abs(sigma - np.std(s, ddof=1))
        0.1  # may vary

        Display the histogram of the samples, along with
        the probability density function:

        >>> import matplotlib.pyplot as plt
        >>> count, bins, ignored = plt.hist(s, 30, density=True)
        >>> plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
        ...                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
        ...          linewidth=2, color='r')
        >>> plt.show()

        Two-by-four array of samples from the normal distribution with
        mean 3 and standard deviation 2.5:

        >>> np.random.normal(3, 2.5, size=(2, 4))
        array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random
               [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random

    pareto(...) method of numpy.random.mtrand.RandomState instance
        pareto(a, size=None)

        Draw samples from a Pareto II or Lomax distribution with
        specified shape.

        The Lomax or Pareto II distribution is a shifted Pareto
        distribution. The classical Pareto distribution can be
        obtained from the Lomax distribution by adding 1 and
        multiplying by the scale parameter ``m`` (see Notes).  The
        smallest value of the Lomax distribution is zero while for the
        classical Pareto distribution it is ``mu``, where the standard
        Pareto distribution has location ``mu = 1``.  Lomax can also
        be considered as a simplified version of the Generalized
        Pareto distribution (available in SciPy), with the scale set
        to one and the location set to zero.

        The Pareto distribution must be greater than zero, and is
        unbounded above.  It is also known as the "80-20 rule".  In
        this distribution, 80 percent of the weights are in the lowest
        20 percent of the range, while the other 20 percent fill the
        remaining 80 percent of the range.

        .. note::
            New code should use the `~numpy.random.Generator.pareto`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        a : float or array_like of floats
            Shape of the distribution. Must be positive.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``a`` is a scalar.  Otherwise,
            ``np.array(a).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized Pareto distribution.

        See Also
        --------
        scipy.stats.lomax : probability density function, distribution or
            cumulative density function, etc.
        scipy.stats.genpareto : probability density function, distribution or
            cumulative density function, etc.
        random.Generator.pareto: which should be used for new code.

        Notes
        -----
        The probability density for the Pareto distribution is

        .. math:: p(x) = \frac{am^a}{x^{a+1}}

        where :math:`a` is the shape and :math:`m` the scale.

        The Pareto distribution, named after the Italian economist
        Vilfredo Pareto, is a power law probability distribution
        useful in many real world problems.  Outside the field of
        economics it is generally referred to as the Bradford
        distribution. Pareto developed the distribution to describe
        the distribution of wealth in an economy.  It has also found
        use in insurance, web page access statistics, oil field sizes,
        and many other problems, including the download frequency for
        projects in Sourceforge [1]_.  It is one of the so-called
        "fat-tailed" distributions.

        References
        ----------
        .. [1] Francis Hunt and Paul Johnson, On the Pareto Distribution of
               Sourceforge projects.
        .. [2] Pareto, V. (1896). Course of Political Economy. Lausanne.
        .. [3] Reiss, R.D., Thomas, M.(2001), Statistical Analysis of Extreme
               Values, Birkhauser Verlag, Basel, pp 23-30.
        .. [4] Wikipedia, "Pareto distribution",
               https://en.wikipedia.org/wiki/Pareto_distribution

        Examples
        --------
        Draw samples from the distribution:

        >>> a, m = 3., 2.  # shape and mode
        >>> s = (np.random.pareto(a, 1000) + 1) * m

        Display the histogram of the samples, along with the probability
        density function:

        >>> import matplotlib.pyplot as plt
        >>> count, bins, _ = plt.hist(s, 100, density=True)
        >>> fit = a*m**a / bins**(a+1)
        >>> plt.plot(bins, max(count)*fit/max(fit), linewidth=2, color='r')
        >>> plt.show()

    permutation(...) method of numpy.random.mtrand.RandomState instance
        permutation(x)

        Randomly permute a sequence, or return a permuted range.

        If `x` is a multi-dimensional array, it is only shuffled along its
        first index.

        .. note::
            New code should use the
            `~numpy.random.Generator.permutation`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        x : int or array_like
            If `x` is an integer, randomly permute ``np.arange(x)``.
            If `x` is an array, make a copy and shuffle the elements
            randomly.

        Returns
        -------
        out : ndarray
            Permuted sequence or array range.

        See Also
        --------
        random.Generator.permutation: which should be used for new code.

        Examples
        --------
        >>> np.random.permutation(10)
        array([1, 7, 4, 3, 0, 9, 2, 5, 8, 6]) # random

        >>> np.random.permutation([1, 4, 9, 12, 15])
        array([15,  1,  9,  4, 12]) # random

        >>> arr = np.arange(9).reshape((3, 3))
        >>> np.random.permutation(arr)
        array([[6, 7, 8], # random
               [0, 1, 2],
               [3, 4, 5]])

    poisson(...) method of numpy.random.mtrand.RandomState instance
        poisson(lam=1.0, size=None)

        Draw samples from a Poisson distribution.

        The Poisson distribution is the limit of the binomial distribution
        for large N.

        .. note::
            New code should use the `~numpy.random.Generator.poisson`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        lam : float or array_like of floats
            Expected number of events occurring in a fixed-time interval,
            must be >= 0. A sequence must be broadcastable over the requested
            size.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``lam`` is a scalar. Otherwise,
            ``np.array(lam).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized Poisson distribution.

        See Also
        --------
        random.Generator.poisson: which should be used for new code.

        Notes
        -----
        The Poisson distribution

        .. math:: f(k; \lambda)=\frac{\lambda^k e^{-\lambda}}{k!}

        For events with an expected separation :math:`\lambda` the Poisson
        distribution :math:`f(k; \lambda)` describes the probability of
        :math:`k` events occurring within the observed
        interval :math:`\lambda`.

        Because the output is limited to the range of the C int64 type, a
        ValueError is raised when `lam` is within 10 sigma of the maximum
        representable value.

        References
        ----------
        .. [1] Weisstein, Eric W. "Poisson Distribution."
               From MathWorld--A Wolfram Web Resource.
               http://mathworld.wolfram.com/PoissonDistribution.html
        .. [2] Wikipedia, "Poisson distribution",
               https://en.wikipedia.org/wiki/Poisson_distribution

        Examples
        --------
        Draw samples from the distribution:

        >>> import numpy as np
        >>> s = np.random.poisson(5, 10000)

        Display histogram of the sample:

        >>> import matplotlib.pyplot as plt
        >>> count, bins, ignored = plt.hist(s, 14, density=True)
        >>> plt.show()

        Draw each 100 values for lambda 100 and 500:

        >>> s = np.random.poisson(lam=(100., 500.), size=(100, 2))

    power(...) method of numpy.random.mtrand.RandomState instance
        power(a, size=None)

        Draws samples in [0, 1] from a power distribution with positive
        exponent a - 1.

        Also known as the power function distribution.

        .. note::
            New code should use the `~numpy.random.Generator.power`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        a : float or array_like of floats
            Parameter of the distribution. Must be non-negative.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``a`` is a scalar.  Otherwise,
            ``np.array(a).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized power distribution.

        Raises
        ------
        ValueError
            If a <= 0.

        See Also
        --------
        random.Generator.power: which should be used for new code.

        Notes
        -----
        The probability density function is

        .. math:: P(x; a) = ax^{a-1}, 0 \le x \le 1, a>0.

        The power function distribution is just the inverse of the Pareto
        distribution. It may also be seen as a special case of the Beta
        distribution.

        It is used, for example, in modeling the over-reporting of insurance
        claims.

        References
        ----------
        .. [1] Christian Kleiber, Samuel Kotz, "Statistical size distributions
               in economics and actuarial sciences", Wiley, 2003.
        .. [2] Heckert, N. A. and Filliben, James J. "NIST Handbook 148:
               Dataplot Reference Manual, Volume 2: Let Subcommands and Library
               Functions", National Institute of Standards and Technology
               Handbook Series, June 2003.
               https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/powpdf.pdf

        Examples
        --------
        Draw samples from the distribution:

        >>> a = 5. # shape
        >>> samples = 1000
        >>> s = np.random.power(a, samples)

        Display the histogram of the samples, along with
        the probability density function:

        >>> import matplotlib.pyplot as plt
        >>> count, bins, ignored = plt.hist(s, bins=30)
        >>> x = np.linspace(0, 1, 100)
        >>> y = a*x**(a-1.)
        >>> normed_y = samples*np.diff(bins)[0]*y
        >>> plt.plot(x, normed_y)
        >>> plt.show()

        Compare the power function distribution to the inverse of the Pareto.

        >>> from scipy import stats # doctest: +SKIP
        >>> rvs = np.random.power(5, 1000000)
        >>> rvsp = np.random.pareto(5, 1000000)
        >>> xx = np.linspace(0,1,100)
        >>> powpdf = stats.powerlaw.pdf(xx,5)  # doctest: +SKIP

        >>> plt.figure()
        >>> plt.hist(rvs, bins=50, density=True)
        >>> plt.plot(xx,powpdf,'r-')  # doctest: +SKIP
        >>> plt.title('np.random.power(5)')

        >>> plt.figure()
        >>> plt.hist(1./(1.+rvsp), bins=50, density=True)
        >>> plt.plot(xx,powpdf,'r-')  # doctest: +SKIP
        >>> plt.title('inverse of 1 + np.random.pareto(5)')

        >>> plt.figure()
        >>> plt.hist(1./(1.+rvsp), bins=50, density=True)
        >>> plt.plot(xx,powpdf,'r-')  # doctest: +SKIP
        >>> plt.title('inverse of stats.pareto(5)')

    rand(...) method of numpy.random.mtrand.RandomState instance
        rand(d0, d1, ..., dn)

        Random values in a given shape.

        .. note::
            This is a convenience function for users porting code from Matlab,
            and wraps `random_sample`. That function takes a
            tuple to specify the size of the output, which is consistent with
            other NumPy functions like `numpy.zeros` and `numpy.ones`.

        Create an array of the given shape and populate it with
        random samples from a uniform distribution
        over ``[0, 1)``.

        Parameters
        ----------
        d0, d1, ..., dn : int, optional
            The dimensions of the returned array, must be non-negative.
            If no argument is given a single Python float is returned.

        Returns
        -------
        out : ndarray, shape ``(d0, d1, ..., dn)``
            Random values.

        See Also
        --------
        random

        Examples
        --------
        >>> np.random.rand(3,2)
        array([[ 0.14022471,  0.96360618],  #random
               [ 0.37601032,  0.25528411],  #random
               [ 0.49313049,  0.94909878]]) #random

    randint(...) method of numpy.random.mtrand.RandomState instance
        randint(low, high=None, size=None, dtype=int)

        Return random integers from `low` (inclusive) to `high` (exclusive).

        Return random integers from the "discrete uniform" distribution of
        the specified dtype in the "half-open" interval [`low`, `high`). If
        `high` is None (the default), then results are from [0, `low`).

        .. note::
            New code should use the `~numpy.random.Generator.integers`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        low : int or array-like of ints
            Lowest (signed) integers to be drawn from the distribution (unless
            ``high=None``, in which case this parameter is one above the
            *highest* such integer).
        high : int or array-like of ints, optional
            If provided, one above the largest (signed) integer to be drawn
            from the distribution (see above for behavior if ``high=None``).
            If array-like, must contain integer values
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  Default is None, in which case a
            single value is returned.
        dtype : dtype, optional
            Desired dtype of the result. Byteorder must be native.
            The default value is int.

            .. versionadded:: 1.11.0

        Returns
        -------
        out : int or ndarray of ints
            `size`-shaped array of random integers from the appropriate
            distribution, or a single such random int if `size` not provided.

        See Also
        --------
        random_integers : similar to `randint`, only for the closed
            interval [`low`, `high`], and 1 is the lowest value if `high` is
            omitted.
        random.Generator.integers: which should be used for new code.

        Examples
        --------
        >>> np.random.randint(2, size=10)
        array([1, 0, 0, 0, 1, 1, 0, 0, 1, 0]) # random
        >>> np.random.randint(1, size=10)
        array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        Generate a 2 x 4 array of ints between 0 and 4, inclusive:

        >>> np.random.randint(5, size=(2, 4))
        array([[4, 0, 2, 1], # random
               [3, 2, 2, 0]])

        Generate a 1 x 3 array with 3 different upper bounds

        >>> np.random.randint(1, [3, 5, 10])
        array([2, 2, 9]) # random

        Generate a 1 by 3 array with 3 different lower bounds

        >>> np.random.randint([1, 5, 7], 10)
        array([9, 8, 7]) # random

        Generate a 2 by 4 array using broadcasting with dtype of uint8

        >>> np.random.randint([1, 3, 5, 7], [[10], [20]], dtype=np.uint8)
        array([[ 8,  6,  9,  7], # random
               [ 1, 16,  9, 12]], dtype=uint8)

    randn(...) method of numpy.random.mtrand.RandomState instance
        randn(d0, d1, ..., dn)

        Return a sample (or samples) from the "standard normal" distribution.

        .. note::
            This is a convenience function for users porting code from Matlab,
            and wraps `standard_normal`. That function takes a
            tuple to specify the size of the output, which is consistent with
            other NumPy functions like `numpy.zeros` and `numpy.ones`.

        .. note::
            New code should use the
            `~numpy.random.Generator.standard_normal`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        If positive int_like arguments are provided, `randn` generates an array
        of shape ``(d0, d1, ..., dn)``, filled
        with random floats sampled from a univariate "normal" (Gaussian)
        distribution of mean 0 and variance 1. A single float randomly sampled
        from the distribution is returned if no argument is provided.

        Parameters
        ----------
        d0, d1, ..., dn : int, optional
            The dimensions of the returned array, must be non-negative.
            If no argument is given a single Python float is returned.

        Returns
        -------
        Z : ndarray or float
            A ``(d0, d1, ..., dn)``-shaped array of floating-point samples from
            the standard normal distribution, or a single such float if
            no parameters were supplied.

        See Also
        --------
        standard_normal : Similar, but takes a tuple as its argument.
        normal : Also accepts mu and sigma arguments.
        random.Generator.standard_normal: which should be used for new code.

        Notes
        -----
        For random samples from the normal distribution with mean ``mu`` and
        standard deviation ``sigma``, use::

            sigma * np.random.randn(...) + mu

        Examples
        --------
        >>> np.random.randn()
        2.1923875335537315  # random

        Two-by-four array of samples from the normal distribution with
        mean 3 and standard deviation 2.5:

        >>> 3 + 2.5 * np.random.randn(2, 4)
        array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random
               [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random

    random(...) method of numpy.random.mtrand.RandomState instance
        random(size=None)

        Return random floats in the half-open interval [0.0, 1.0). Alias for
        `random_sample` to ease forward-porting to the new random API.

    random_integers(...) method of numpy.random.mtrand.RandomState instance
        random_integers(low, high=None, size=None)

        Random integers of type `np.int_` between `low` and `high`, inclusive.

        Return random integers of type `np.int_` from the "discrete uniform"
        distribution in the closed interval [`low`, `high`].  If `high` is
        None (the default), then results are from [1, `low`]. The `np.int_`
        type translates to the C long integer type and its precision
        is platform dependent.

        This function has been deprecated. Use randint instead.

        .. deprecated:: 1.11.0

        Parameters
        ----------
        low : int
            Lowest (signed) integer to be drawn from the distribution (unless
            ``high=None``, in which case this parameter is the *highest* such
            integer).
        high : int, optional
            If provided, the largest (signed) integer to be drawn from the
            distribution (see above for behavior if ``high=None``).
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  Default is None, in which case a
            single value is returned.

        Returns
        -------
        out : int or ndarray of ints
            `size`-shaped array of random integers from the appropriate
            distribution, or a single such random int if `size` not provided.

        See Also
        --------
        randint : Similar to `random_integers`, only for the half-open
            interval [`low`, `high`), and 0 is the lowest value if `high` is
            omitted.

        Notes
        -----
        To sample from N evenly spaced floating-point numbers between a and b,
        use::

          a + (b - a) * (np.random.random_integers(N) - 1) / (N - 1.)

        Examples
        --------
        >>> np.random.random_integers(5)
        4 # random
        >>> type(np.random.random_integers(5))
        <class 'numpy.int64'>
        >>> np.random.random_integers(5, size=(3,2))
        array([[5, 4], # random
               [3, 3],
               [4, 5]])

        Choose five random numbers from the set of five evenly-spaced
        numbers between 0 and 2.5, inclusive (*i.e.*, from the set
        :math:`{0, 5/8, 10/8, 15/8, 20/8}`):

        >>> 2.5 * (np.random.random_integers(5, size=(5,)) - 1) / 4.
        array([ 0.625,  1.25 ,  0.625,  0.625,  2.5  ]) # random

        Roll two six sided dice 1000 times and sum the results:

        >>> d1 = np.random.random_integers(1, 6, 1000)
        >>> d2 = np.random.random_integers(1, 6, 1000)
        >>> dsums = d1 + d2

        Display results as a histogram:

        >>> import matplotlib.pyplot as plt
        >>> count, bins, ignored = plt.hist(dsums, 11, density=True)
        >>> plt.show()

    random_sample(...) method of numpy.random.mtrand.RandomState instance
        random_sample(size=None)

        Return random floats in the half-open interval [0.0, 1.0).

        Results are from the "continuous uniform" distribution over the
        stated interval.  To sample :math:`Unif[a, b), b > a` multiply
        the output of `random_sample` by `(b-a)` and add `a`::

          (b - a) * random_sample() + a

        .. note::
            New code should use the `~numpy.random.Generator.random`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  Default is None, in which case a
            single value is returned.

        Returns
        -------
        out : float or ndarray of floats
            Array of random floats of shape `size` (unless ``size=None``, in which
            case a single float is returned).

        See Also
        --------
        random.Generator.random: which should be used for new code.

        Examples
        --------
        >>> np.random.random_sample()
        0.47108547995356098 # random
        >>> type(np.random.random_sample())
        <class 'float'>
        >>> np.random.random_sample((5,))
        array([ 0.30220482,  0.86820401,  0.1654503 ,  0.11659149,  0.54323428]) # random

        Three-by-two array of random numbers from [-5, 0):

        >>> 5 * np.random.random_sample((3, 2)) - 5
        array([[-3.99149989, -0.52338984], # random
               [-2.99091858, -0.79479508],
               [-1.23204345, -1.75224494]])

    ranf(...)
        This is an alias of `random_sample`. See `random_sample`  for the complete
        documentation.

    rayleigh(...) method of numpy.random.mtrand.RandomState instance
        rayleigh(scale=1.0, size=None)

        Draw samples from a Rayleigh distribution.

        The :math:`\chi` and Weibull distributions are generalizations of the
        Rayleigh.

        .. note::
            New code should use the `~numpy.random.Generator.rayleigh`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        scale : float or array_like of floats, optional
            Scale, also equals the mode. Must be non-negative. Default is 1.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``scale`` is a scalar.  Otherwise,
            ``np.array(scale).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized Rayleigh distribution.

        See Also
        --------
        random.Generator.rayleigh: which should be used for new code.

        Notes
        -----
        The probability density function for the Rayleigh distribution is

        .. math:: P(x;scale) = \frac{x}{scale^2}e^{\frac{-x^2}{2 \cdotp scale^2}}

        The Rayleigh distribution would arise, for example, if the East
        and North components of the wind velocity had identical zero-mean
        Gaussian distributions.  Then the wind speed would have a Rayleigh
        distribution.

        References
        ----------
        .. [1] Brighton Webs Ltd., "Rayleigh Distribution,"
               https://web.archive.org/web/20090514091424/http://brighton-webs.co.uk:80/distributions/rayleigh.asp
        .. [2] Wikipedia, "Rayleigh distribution"
               https://en.wikipedia.org/wiki/Rayleigh_distribution

        Examples
        --------
        Draw values from the distribution and plot the histogram

        >>> from matplotlib.pyplot import hist
        >>> values = hist(np.random.rayleigh(3, 100000), bins=200, density=True)

        Wave heights tend to follow a Rayleigh distribution. If the mean wave
        height is 1 meter, what fraction of waves are likely to be larger than 3
        meters?

        >>> meanvalue = 1
        >>> modevalue = np.sqrt(2 / np.pi) * meanvalue
        >>> s = np.random.rayleigh(modevalue, 1000000)

        The percentage of waves larger than 3 meters is:

        >>> 100.*sum(s>3)/1000000.
        0.087300000000000003 # random

    sample(...)
        This is an alias of `random_sample`. See `random_sample`  for the complete
        documentation.

    seed(...)
        seed(seed=None)

        Reseed the singleton RandomState instance.

        Notes
        -----
        This is a convenience, legacy function that exists to support
        older code that uses the singleton RandomState. Best practice
        is to use a dedicated ``Generator`` instance rather than
        the random variate generation methods exposed directly in
        the random module.

        See Also
        --------
        numpy.random.Generator

    set_state(...) method of numpy.random.mtrand.RandomState instance
        set_state(state)

        Set the internal state of the generator from a tuple.

        For use if one has reason to manually (re-)set the internal state of
        the bit generator used by the RandomState instance. By default,
        RandomState uses the "Mersenne Twister"[1]_ pseudo-random number
        generating algorithm.

        Parameters
        ----------
        state : {tuple(str, ndarray of 624 uints, int, int, float), dict}
            The `state` tuple has the following items:

            1. the string 'MT19937', specifying the Mersenne Twister algorithm.
            2. a 1-D array of 624 unsigned integers ``keys``.
            3. an integer ``pos``.
            4. an integer ``has_gauss``.
            5. a float ``cached_gaussian``.

            If state is a dictionary, it is directly set using the BitGenerators
            `state` property.

        Returns
        -------
        out : None
            Returns 'None' on success.

        See Also
        --------
        get_state

        Notes
        -----
        `set_state` and `get_state` are not needed to work with any of the
        random distributions in NumPy. If the internal state is manually altered,
        the user should know exactly what he/she is doing.

        For backwards compatibility, the form (str, array of 624 uints, int) is
        also accepted although it is missing some information about the cached
        Gaussian value: ``state = ('MT19937', keys, pos)``.

        References
        ----------
        .. [1] M. Matsumoto and T. Nishimura, "Mersenne Twister: A
           623-dimensionally equidistributed uniform pseudorandom number
           generator," *ACM Trans. on Modeling and Computer Simulation*,
           Vol. 8, No. 1, pp. 3-30, Jan. 1998.

    shuffle(...) method of numpy.random.mtrand.RandomState instance
        shuffle(x)

        Modify a sequence in-place by shuffling its contents.

        This function only shuffles the array along the first axis of a
        multi-dimensional array. The order of sub-arrays is changed but
        their contents remains the same.

        .. note::
            New code should use the `~numpy.random.Generator.shuffle`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        x : ndarray or MutableSequence
            The array, list or mutable sequence to be shuffled.

        Returns
        -------
        None

        See Also
        --------
        random.Generator.shuffle: which should be used for new code.

        Examples
        --------
        >>> arr = np.arange(10)
        >>> np.random.shuffle(arr)
        >>> arr
        [1 7 5 2 9 4 3 6 0 8] # random

        Multi-dimensional arrays are only shuffled along the first axis:

        >>> arr = np.arange(9).reshape((3, 3))
        >>> np.random.shuffle(arr)
        >>> arr
        array([[3, 4, 5], # random
               [6, 7, 8],
               [0, 1, 2]])

    standard_cauchy(...) method of numpy.random.mtrand.RandomState instance
        standard_cauchy(size=None)

        Draw samples from a standard Cauchy distribution with mode = 0.

        Also known as the Lorentz distribution.

        .. note::
            New code should use the
            `~numpy.random.Generator.standard_cauchy`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  Default is None, in which case a
            single value is returned.

        Returns
        -------
        samples : ndarray or scalar
            The drawn samples.

        See Also
        --------
        random.Generator.standard_cauchy: which should be used for new code.

        Notes
        -----
        The probability density function for the full Cauchy distribution is

        .. math:: P(x; x_0, \gamma) = \frac{1}{\pi \gamma \bigl[ 1+
                  (\frac{x-x_0}{\gamma})^2 \bigr] }

        and the Standard Cauchy distribution just sets :math:`x_0=0` and
        :math:`\gamma=1`

        The Cauchy distribution arises in the solution to the driven harmonic
        oscillator problem, and also describes spectral line broadening. It
        also describes the distribution of values at which a line tilted at
        a random angle will cut the x axis.

        When studying hypothesis tests that assume normality, seeing how the
        tests perform on data from a Cauchy distribution is a good indicator of
        their sensitivity to a heavy-tailed distribution, since the Cauchy looks
        very much like a Gaussian distribution, but with heavier tails.

        References
        ----------
        .. [1] NIST/SEMATECH e-Handbook of Statistical Methods, "Cauchy
              Distribution",
              https://www.itl.nist.gov/div898/handbook/eda/section3/eda3663.htm
        .. [2] Weisstein, Eric W. "Cauchy Distribution." From MathWorld--A
              Wolfram Web Resource.
              http://mathworld.wolfram.com/CauchyDistribution.html
        .. [3] Wikipedia, "Cauchy distribution"
              https://en.wikipedia.org/wiki/Cauchy_distribution

        Examples
        --------
        Draw samples and plot the distribution:

        >>> import matplotlib.pyplot as plt
        >>> s = np.random.standard_cauchy(1000000)
        >>> s = s[(s>-25) & (s<25)]  # truncate distribution so it plots well
        >>> plt.hist(s, bins=100)
        >>> plt.show()

    standard_exponential(...) method of numpy.random.mtrand.RandomState instance
        standard_exponential(size=None)

        Draw samples from the standard exponential distribution.

        `standard_exponential` is identical to the exponential distribution
        with a scale parameter of 1.

        .. note::
            New code should use the
            `~numpy.random.Generator.standard_exponential`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  Default is None, in which case a
            single value is returned.

        Returns
        -------
        out : float or ndarray
            Drawn samples.

        See Also
        --------
        random.Generator.standard_exponential: which should be used for new code.

        Examples
        --------
        Output a 3x8000 array:

        >>> n = np.random.standard_exponential((3, 8000))

    standard_gamma(...) method of numpy.random.mtrand.RandomState instance
        standard_gamma(shape, size=None)

        Draw samples from a standard Gamma distribution.

        Samples are drawn from a Gamma distribution with specified parameters,
        shape (sometimes designated "k") and scale=1.

        .. note::
            New code should use the
            `~numpy.random.Generator.standard_gamma`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        shape : float or array_like of floats
            Parameter, must be non-negative.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``shape`` is a scalar.  Otherwise,
            ``np.array(shape).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized standard gamma distribution.

        See Also
        --------
        scipy.stats.gamma : probability density function, distribution or
            cumulative density function, etc.
        random.Generator.standard_gamma: which should be used for new code.

        Notes
        -----
        The probability density for the Gamma distribution is

        .. math:: p(x) = x^{k-1}\frac{e^{-x/\theta}}{\theta^k\Gamma(k)},

        where :math:`k` is the shape and :math:`\theta` the scale,
        and :math:`\Gamma` is the Gamma function.

        The Gamma distribution is often used to model the times to failure of
        electronic components, and arises naturally in processes for which the
        waiting times between Poisson distributed events are relevant.

        References
        ----------
        .. [1] Weisstein, Eric W. "Gamma Distribution." From MathWorld--A
               Wolfram Web Resource.
               http://mathworld.wolfram.com/GammaDistribution.html
        .. [2] Wikipedia, "Gamma distribution",
               https://en.wikipedia.org/wiki/Gamma_distribution

        Examples
        --------
        Draw samples from the distribution:

        >>> shape, scale = 2., 1. # mean and width
        >>> s = np.random.standard_gamma(shape, 1000000)

        Display the histogram of the samples, along with
        the probability density function:

        >>> import matplotlib.pyplot as plt
        >>> import scipy.special as sps  # doctest: +SKIP
        >>> count, bins, ignored = plt.hist(s, 50, density=True)
        >>> y = bins**(shape-1) * ((np.exp(-bins/scale))/  # doctest: +SKIP
        ...                       (sps.gamma(shape) * scale**shape))
        >>> plt.plot(bins, y, linewidth=2, color='r')  # doctest: +SKIP
        >>> plt.show()

    standard_normal(...) method of numpy.random.mtrand.RandomState instance
        standard_normal(size=None)

        Draw samples from a standard Normal distribution (mean=0, stdev=1).

        .. note::
            New code should use the
            `~numpy.random.Generator.standard_normal`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  Default is None, in which case a
            single value is returned.

        Returns
        -------
        out : float or ndarray
            A floating-point array of shape ``size`` of drawn samples, or a
            single sample if ``size`` was not specified.

        See Also
        --------
        normal :
            Equivalent function with additional ``loc`` and ``scale`` arguments
            for setting the mean and standard deviation.
        random.Generator.standard_normal: which should be used for new code.

        Notes
        -----
        For random samples from the normal distribution with mean ``mu`` and
        standard deviation ``sigma``, use one of::

            mu + sigma * np.random.standard_normal(size=...)
            np.random.normal(mu, sigma, size=...)

        Examples
        --------
        >>> np.random.standard_normal()
        2.1923875335537315 #random

        >>> s = np.random.standard_normal(8000)
        >>> s
        array([ 0.6888893 ,  0.78096262, -0.89086505, ...,  0.49876311,  # random
               -0.38672696, -0.4685006 ])                                # random
        >>> s.shape
        (8000,)
        >>> s = np.random.standard_normal(size=(3, 4, 2))
        >>> s.shape
        (3, 4, 2)

        Two-by-four array of samples from the normal distribution with
        mean 3 and standard deviation 2.5:

        >>> 3 + 2.5 * np.random.standard_normal(size=(2, 4))
        array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random
               [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random

    standard_t(...) method of numpy.random.mtrand.RandomState instance
        standard_t(df, size=None)

        Draw samples from a standard Student's t distribution with `df` degrees
        of freedom.

        A special case of the hyperbolic distribution.  As `df` gets
        large, the result resembles that of the standard normal
        distribution (`standard_normal`).

        .. note::
            New code should use the `~numpy.random.Generator.standard_t`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        df : float or array_like of floats
            Degrees of freedom, must be > 0.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``df`` is a scalar.  Otherwise,
            ``np.array(df).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized standard Student's t distribution.

        See Also
        --------
        random.Generator.standard_t: which should be used for new code.

        Notes
        -----
        The probability density function for the t distribution is

        .. math:: P(x, df) = \frac{\Gamma(\frac{df+1}{2})}{\sqrt{\pi df}
                  \Gamma(\frac{df}{2})}\Bigl( 1+\frac{x^2}{df} \Bigr)^{-(df+1)/2}

        The t test is based on an assumption that the data come from a
        Normal distribution. The t test provides a way to test whether
        the sample mean (that is the mean calculated from the data) is
        a good estimate of the true mean.

        The derivation of the t-distribution was first published in
        1908 by William Gosset while working for the Guinness Brewery
        in Dublin. Due to proprietary issues, he had to publish under
        a pseudonym, and so he used the name Student.

        References
        ----------
        .. [1] Dalgaard, Peter, "Introductory Statistics With R",
               Springer, 2002.
        .. [2] Wikipedia, "Student's t-distribution"
               https://en.wikipedia.org/wiki/Student's_t-distribution

        Examples
        --------
        From Dalgaard page 83 [1]_, suppose the daily energy intake for 11
        women in kilojoules (kJ) is:

        >>> intake = np.array([5260., 5470, 5640, 6180, 6390, 6515, 6805, 7515, \
        ...                    7515, 8230, 8770])

        Does their energy intake deviate systematically from the recommended
        value of 7725 kJ? Our null hypothesis will be the absence of deviation,
        and the alternate hypothesis will be the presence of an effect that could be
        either positive or negative, hence making our test 2-tailed.

        Because we are estimating the mean and we have N=11 values in our sample,
        we have N-1=10 degrees of freedom. We set our significance level to 95% and
        compute the t statistic using the empirical mean and empirical standard
        deviation of our intake. We use a ddof of 1 to base the computation of our
        empirical standard deviation on an unbiased estimate of the variance (note:
        the final estimate is not unbiased due to the concave nature of the square
        root).

        >>> np.mean(intake)
        6753.636363636364
        >>> intake.std(ddof=1)
        1142.1232221373727
        >>> t = (np.mean(intake)-7725)/(intake.std(ddof=1)/np.sqrt(len(intake)))
        >>> t
        -2.8207540608310198

        We draw 1000000 samples from Student's t distribution with the adequate
        degrees of freedom.

        >>> import matplotlib.pyplot as plt
        >>> s = np.random.standard_t(10, size=1000000)
        >>> h = plt.hist(s, bins=100, density=True)

        Does our t statistic land in one of the two critical regions found at
        both tails of the distribution?

        >>> np.sum(np.abs(t) < np.abs(s)) / float(len(s))
        0.018318  #random < 0.05, statistic is in critical region

        The probability value for this 2-tailed test is about 1.83%, which is
        lower than the 5% pre-determined significance threshold.

        Therefore, the probability of observing values as extreme as our intake
        conditionally on the null hypothesis being true is too low, and we reject
        the null hypothesis of no deviation.

    triangular(...) method of numpy.random.mtrand.RandomState instance
        triangular(left, mode, right, size=None)

        Draw samples from the triangular distribution over the
        interval ``[left, right]``.

        The triangular distribution is a continuous probability
        distribution with lower limit left, peak at mode, and upper
        limit right. Unlike the other distributions, these parameters
        directly define the shape of the pdf.

        .. note::
            New code should use the `~numpy.random.Generator.triangular`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        left : float or array_like of floats
            Lower limit.
        mode : float or array_like of floats
            The value where the peak of the distribution occurs.
            The value must fulfill the condition ``left <= mode <= right``.
        right : float or array_like of floats
            Upper limit, must be larger than `left`.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``left``, ``mode``, and ``right``
            are all scalars.  Otherwise, ``np.broadcast(left, mode, right).size``
            samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized triangular distribution.

        See Also
        --------
        random.Generator.triangular: which should be used for new code.

        Notes
        -----
        The probability density function for the triangular distribution is

        .. math:: P(x;l, m, r) = \begin{cases}
                  \frac{2(x-l)}{(r-l)(m-l)}& \text{for $l \leq x \leq m$},\\
                  \frac{2(r-x)}{(r-l)(r-m)}& \text{for $m \leq x \leq r$},\\
                  0& \text{otherwise}.
                  \end{cases}

        The triangular distribution is often used in ill-defined
        problems where the underlying distribution is not known, but
        some knowledge of the limits and mode exists. Often it is used
        in simulations.

        References
        ----------
        .. [1] Wikipedia, "Triangular distribution"
               https://en.wikipedia.org/wiki/Triangular_distribution

        Examples
        --------
        Draw values from the distribution and plot the histogram:

        >>> import matplotlib.pyplot as plt
        >>> h = plt.hist(np.random.triangular(-3, 0, 8, 100000), bins=200,
        ...              density=True)
        >>> plt.show()

    uniform(...) method of numpy.random.mtrand.RandomState instance
        uniform(low=0.0, high=1.0, size=None)

        Draw samples from a uniform distribution.

        Samples are uniformly distributed over the half-open interval
        ``[low, high)`` (includes low, but excludes high).  In other words,
        any value within the given interval is equally likely to be drawn
        by `uniform`.

        .. note::
            New code should use the `~numpy.random.Generator.uniform`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        low : float or array_like of floats, optional
            Lower boundary of the output interval.  All values generated will be
            greater than or equal to low.  The default value is 0.
        high : float or array_like of floats
            Upper boundary of the output interval.  All values generated will be
            less than or equal to high.  The high limit may be included in the
            returned array of floats due to floating-point rounding in the
            equation ``low + (high-low) * random_sample()``.  The default value
            is 1.0.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``low`` and ``high`` are both scalars.
            Otherwise, ``np.broadcast(low, high).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized uniform distribution.

        See Also
        --------
        randint : Discrete uniform distribution, yielding integers.
        random_integers : Discrete uniform distribution over the closed
                          interval ``[low, high]``.
        random_sample : Floats uniformly distributed over ``[0, 1)``.
        random : Alias for `random_sample`.
        rand : Convenience function that accepts dimensions as input, e.g.,
               ``rand(2,2)`` would generate a 2-by-2 array of floats,
               uniformly distributed over ``[0, 1)``.
        random.Generator.uniform: which should be used for new code.

        Notes
        -----
        The probability density function of the uniform distribution is

        .. math:: p(x) = \frac{1}{b - a}

        anywhere within the interval ``[a, b)``, and zero elsewhere.

        When ``high`` == ``low``, values of ``low`` will be returned.
        If ``high`` < ``low``, the results are officially undefined
        and may eventually raise an error, i.e. do not rely on this
        function to behave when passed arguments satisfying that
        inequality condition. The ``high`` limit may be included in the
        returned array of floats due to floating-point rounding in the
        equation ``low + (high-low) * random_sample()``. For example:

        >>> x = np.float32(5*0.99999999)
        >>> x
        5.0


        Examples
        --------
        Draw samples from the distribution:

        >>> s = np.random.uniform(-1,0,1000)

        All values are within the given interval:

        >>> np.all(s >= -1)
        True
        >>> np.all(s < 0)
        True

        Display the histogram of the samples, along with the
        probability density function:

        >>> import matplotlib.pyplot as plt
        >>> count, bins, ignored = plt.hist(s, 15, density=True)
        >>> plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
        >>> plt.show()

    vonmises(...) method of numpy.random.mtrand.RandomState instance
        vonmises(mu, kappa, size=None)

        Draw samples from a von Mises distribution.

        Samples are drawn from a von Mises distribution with specified mode
        (mu) and dispersion (kappa), on the interval [-pi, pi].

        The von Mises distribution (also known as the circular normal
        distribution) is a continuous probability distribution on the unit
        circle.  It may be thought of as the circular analogue of the normal
        distribution.

        .. note::
            New code should use the `~numpy.random.Generator.vonmises`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        mu : float or array_like of floats
            Mode ("center") of the distribution.
        kappa : float or array_like of floats
            Dispersion of the distribution, has to be >=0.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``mu`` and ``kappa`` are both scalars.
            Otherwise, ``np.broadcast(mu, kappa).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized von Mises distribution.

        See Also
        --------
        scipy.stats.vonmises : probability density function, distribution, or
            cumulative density function, etc.
        random.Generator.vonmises: which should be used for new code.

        Notes
        -----
        The probability density for the von Mises distribution is

        .. math:: p(x) = \frac{e^{\kappa cos(x-\mu)}}{2\pi I_0(\kappa)},

        where :math:`\mu` is the mode and :math:`\kappa` the dispersion,
        and :math:`I_0(\kappa)` is the modified Bessel function of order 0.

        The von Mises is named for Richard Edler von Mises, who was born in
        Austria-Hungary, in what is now the Ukraine.  He fled to the United
        States in 1939 and became a professor at Harvard.  He worked in
        probability theory, aerodynamics, fluid mechanics, and philosophy of
        science.

        References
        ----------
        .. [1] Abramowitz, M. and Stegun, I. A. (Eds.). "Handbook of
               Mathematical Functions with Formulas, Graphs, and Mathematical
               Tables, 9th printing," New York: Dover, 1972.
        .. [2] von Mises, R., "Mathematical Theory of Probability
               and Statistics", New York: Academic Press, 1964.

        Examples
        --------
        Draw samples from the distribution:

        >>> mu, kappa = 0.0, 4.0 # mean and dispersion
        >>> s = np.random.vonmises(mu, kappa, 1000)

        Display the histogram of the samples, along with
        the probability density function:

        >>> import matplotlib.pyplot as plt
        >>> from scipy.special import i0  # doctest: +SKIP
        >>> plt.hist(s, 50, density=True)
        >>> x = np.linspace(-np.pi, np.pi, num=51)
        >>> y = np.exp(kappa*np.cos(x-mu))/(2*np.pi*i0(kappa))  # doctest: +SKIP
        >>> plt.plot(x, y, linewidth=2, color='r')  # doctest: +SKIP
        >>> plt.show()

    wald(...) method of numpy.random.mtrand.RandomState instance
        wald(mean, scale, size=None)

        Draw samples from a Wald, or inverse Gaussian, distribution.

        As the scale approaches infinity, the distribution becomes more like a
        Gaussian. Some references claim that the Wald is an inverse Gaussian
        with mean equal to 1, but this is by no means universal.

        The inverse Gaussian distribution was first studied in relationship to
        Brownian motion. In 1956 M.C.K. Tweedie used the name inverse Gaussian
        because there is an inverse relationship between the time to cover a
        unit distance and distance covered in unit time.

        .. note::
            New code should use the `~numpy.random.Generator.wald`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        mean : float or array_like of floats
            Distribution mean, must be > 0.
        scale : float or array_like of floats
            Scale parameter, must be > 0.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``mean`` and ``scale`` are both scalars.
            Otherwise, ``np.broadcast(mean, scale).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized Wald distribution.

        See Also
        --------
        random.Generator.wald: which should be used for new code.

        Notes
        -----
        The probability density function for the Wald distribution is

        .. math:: P(x;mean,scale) = \sqrt{\frac{scale}{2\pi x^3}}e^
                                    \frac{-scale(x-mean)^2}{2\cdotp mean^2x}

        As noted above the inverse Gaussian distribution first arise
        from attempts to model Brownian motion. It is also a
        competitor to the Weibull for use in reliability modeling and
        modeling stock returns and interest rate processes.

        References
        ----------
        .. [1] Brighton Webs Ltd., Wald Distribution,
               https://web.archive.org/web/20090423014010/http://www.brighton-webs.co.uk:80/distributions/wald.asp
        .. [2] Chhikara, Raj S., and Folks, J. Leroy, "The Inverse Gaussian
               Distribution: Theory : Methodology, and Applications", CRC Press,
               1988.
        .. [3] Wikipedia, "Inverse Gaussian distribution"
               https://en.wikipedia.org/wiki/Inverse_Gaussian_distribution

        Examples
        --------
        Draw values from the distribution and plot the histogram:

        >>> import matplotlib.pyplot as plt
        >>> h = plt.hist(np.random.wald(3, 2, 100000), bins=200, density=True)
        >>> plt.show()

    weibull(...) method of numpy.random.mtrand.RandomState instance
        weibull(a, size=None)

        Draw samples from a Weibull distribution.

        Draw samples from a 1-parameter Weibull distribution with the given
        shape parameter `a`.

        .. math:: X = (-ln(U))^{1/a}

        Here, U is drawn from the uniform distribution over (0,1].

        The more common 2-parameter Weibull, including a scale parameter
        :math:`\lambda` is just :math:`X = \lambda(-ln(U))^{1/a}`.

        .. note::
            New code should use the `~numpy.random.Generator.weibull`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        a : float or array_like of floats
            Shape parameter of the distribution.  Must be nonnegative.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``a`` is a scalar.  Otherwise,
            ``np.array(a).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized Weibull distribution.

        See Also
        --------
        scipy.stats.weibull_max
        scipy.stats.weibull_min
        scipy.stats.genextreme
        gumbel
        random.Generator.weibull: which should be used for new code.

        Notes
        -----
        The Weibull (or Type III asymptotic extreme value distribution
        for smallest values, SEV Type III, or Rosin-Rammler
        distribution) is one of a class of Generalized Extreme Value
        (GEV) distributions used in modeling extreme value problems.
        This class includes the Gumbel and Frechet distributions.

        The probability density for the Weibull distribution is

        .. math:: p(x) = \frac{a}
                         {\lambda}(\frac{x}{\lambda})^{a-1}e^{-(x/\lambda)^a},

        where :math:`a` is the shape and :math:`\lambda` the scale.

        The function has its peak (the mode) at
        :math:`\lambda(\frac{a-1}{a})^{1/a}`.

        When ``a = 1``, the Weibull distribution reduces to the exponential
        distribution.

        References
        ----------
        .. [1] Waloddi Weibull, Royal Technical University, Stockholm,
               1939 "A Statistical Theory Of The Strength Of Materials",
               Ingeniorsvetenskapsakademiens Handlingar Nr 151, 1939,
               Generalstabens Litografiska Anstalts Forlag, Stockholm.
        .. [2] Waloddi Weibull, "A Statistical Distribution Function of
               Wide Applicability", Journal Of Applied Mechanics ASME Paper
               1951.
        .. [3] Wikipedia, "Weibull distribution",
               https://en.wikipedia.org/wiki/Weibull_distribution

        Examples
        --------
        Draw samples from the distribution:

        >>> a = 5. # shape
        >>> s = np.random.weibull(a, 1000)

        Display the histogram of the samples, along with
        the probability density function:

        >>> import matplotlib.pyplot as plt
        >>> x = np.arange(1,100.)/50.
        >>> def weib(x,n,a):
        ...     return (a / n) * (x / n)**(a - 1) * np.exp(-(x / n)**a)

        >>> count, bins, ignored = plt.hist(np.random.weibull(5.,1000))
        >>> x = np.arange(1,100.)/50.
        >>> scale = count.max()/weib(x, 1., 5.).max()
        >>> plt.plot(x, weib(x, 1., 5.)*scale)
        >>> plt.show()

    zipf(...) method of numpy.random.mtrand.RandomState instance
        zipf(a, size=None)

        Draw samples from a Zipf distribution.

        Samples are drawn from a Zipf distribution with specified parameter
        `a` > 1.

        The Zipf distribution (also known as the zeta distribution) is a
        discrete probability distribution that satisfies Zipf's law: the
        frequency of an item is inversely proportional to its rank in a
        frequency table.

        .. note::
            New code should use the `~numpy.random.Generator.zipf`
            method of a `~numpy.random.Generator` instance instead;
            please see the :ref:`random-quick-start`.

        Parameters
        ----------
        a : float or array_like of floats
            Distribution parameter. Must be greater than 1.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  If size is ``None`` (default),
            a single value is returned if ``a`` is a scalar. Otherwise,
            ``np.array(a).size`` samples are drawn.

        Returns
        -------
        out : ndarray or scalar
            Drawn samples from the parameterized Zipf distribution.

        See Also
        --------
        scipy.stats.zipf : probability density function, distribution, or
            cumulative density function, etc.
        random.Generator.zipf: which should be used for new code.

        Notes
        -----
        The probability density for the Zipf distribution is

        .. math:: p(k) = \frac{k^{-a}}{\zeta(a)},

        for integers :math:`k \geq 1`, where :math:`\zeta` is the Riemann Zeta
        function.

        It is named for the American linguist George Kingsley Zipf, who noted
        that the frequency of any word in a sample of a language is inversely
        proportional to its rank in the frequency table.

        References
        ----------
        .. [1] Zipf, G. K., "Selected Studies of the Principle of Relative
               Frequency in Language," Cambridge, MA: Harvard Univ. Press,
               1932.

        Examples
        --------
        Draw samples from the distribution:

        >>> a = 4.0
        >>> n = 20000
        >>> s = np.random.zipf(a, n)

        Display the histogram of the samples, along with
        the expected histogram based on the probability
        density function:

        >>> import matplotlib.pyplot as plt
        >>> from scipy.special import zeta  # doctest: +SKIP

        `bincount` provides a fast histogram for small integers.

        >>> count = np.bincount(s)
        >>> k = np.arange(1, s.max() + 1)

        >>> plt.bar(k, count[1:], alpha=0.5, label='sample count')
        >>> plt.plot(k, n*(k**-a)/zeta(a), 'k.-', alpha=0.5,
        ...          label='expected count')   # doctest: +SKIP
        >>> plt.semilogy()
        >>> plt.grid(alpha=0.4)
        >>> plt.legend()
        >>> plt.title(f'Zipf sample, a={a}, size={n}')
        >>> plt.show()

DATA
    __all__ = ['beta', 'binomial', 'bytes', 'chisquare', 'choice', 'dirich...

FILE
    /Users/leopoldogonzalez/miniconda3/lib/python3.12/site-packages/numpy/random/__init__.py


None
&&&&&&&&&&&&&&&&&&&&&& remainder &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on ufunc:

remainder = <ufunc 'remainder'>
    remainder(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])

    Returns the element-wise remainder of division.

    Computes the remainder complementary to the `floor_divide` function.  It is
    equivalent to the Python modulus operator``x1 % x2`` and has the same sign
    as the divisor `x2`. The MATLAB function equivalent to ``np.remainder``
    is ``mod``.

    .. warning::

        This should not be confused with:

        * Python 3.7's `math.remainder` and C's ``remainder``, which
          computes the IEEE remainder, which are the complement to
          ``round(x1 / x2)``.
        * The MATLAB ``rem`` function and or the C ``%`` operator which is the
          complement to ``int(x1 / x2)``.

    Parameters
    ----------
    x1 : array_like
        Dividend array.
    x2 : array_like
        Divisor array.
        If ``x1.shape != x2.shape``, they must be broadcastable to a common
        shape (which becomes the shape of the output).
    out : ndarray, None, or tuple of ndarray and None, optional
        A location into which the result is stored. If provided, it must have
        a shape that the inputs broadcast to. If not provided or None,
        a freshly-allocated array is returned. A tuple (possible only as a
        keyword argument) must have length equal to the number of outputs.
    where : array_like, optional
        This condition is broadcast over the input. At locations where the
        condition is True, the `out` array will be set to the ufunc result.
        Elsewhere, the `out` array will retain its original value.
        Note that if an uninitialized `out` array is created via the default
        ``out=None``, locations within it where the condition is False will
        remain uninitialized.
    **kwargs
        For other keyword-only arguments, see the
        :ref:`ufunc docs <ufuncs.kwargs>`.

    Returns
    -------
    y : ndarray
        The element-wise remainder of the quotient ``floor_divide(x1, x2)``.
        This is a scalar if both `x1` and `x2` are scalars.

    See Also
    --------
    floor_divide : Equivalent of Python ``//`` operator.
    divmod : Simultaneous floor division and remainder.
    fmod : Equivalent of the MATLAB ``rem`` function.
    divide, floor

    Notes
    -----
    Returns 0 when `x2` is 0 and both `x1` and `x2` are (arrays of)
    integers.
    ``mod`` is an alias of ``remainder``.

    Examples
    --------
    >>> np.remainder([4, 7], [2, 3])
    array([0, 1])
    >>> np.remainder(np.arange(7), 5)
    array([0, 1, 2, 3, 4, 0, 1])

    The ``%`` operator can be used as a shorthand for ``np.remainder`` on
    ndarrays.

    >>> x1 = np.arange(7)
    >>> x1 % 5
    array([0, 1, 2, 3, 4, 0, 1])

None
&&&&&&&&&&&&&&&&&&&&&& reshape &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

reshape(a, newshape, order='C')
    Gives a new shape to an array without changing its data.

    Parameters
    ----------
    a : array_like
        Array to be reshaped.
    newshape : int or tuple of ints
        The new shape should be compatible with the original shape. If
        an integer, then the result will be a 1-D array of that length.
        One shape dimension can be -1. In this case, the value is
        inferred from the length of the array and remaining dimensions.
    order : {'C', 'F', 'A'}, optional
        Read the elements of `a` using this index order, and place the
        elements into the reshaped array using this index order.  'C'
        means to read / write the elements using C-like index order,
        with the last axis index changing fastest, back to the first
        axis index changing slowest. 'F' means to read / write the
        elements using Fortran-like index order, with the first index
        changing fastest, and the last index changing slowest. Note that
        the 'C' and 'F' options take no account of the memory layout of
        the underlying array, and only refer to the order of indexing.
        'A' means to read / write the elements in Fortran-like index
        order if `a` is Fortran *contiguous* in memory, C-like order
        otherwise.

    Returns
    -------
    reshaped_array : ndarray
        This will be a new view object if possible; otherwise, it will
        be a copy.  Note there is no guarantee of the *memory layout* (C- or
        Fortran- contiguous) of the returned array.

    See Also
    --------
    ndarray.reshape : Equivalent method.

    Notes
    -----
    It is not always possible to change the shape of an array without copying
    the data.

    The `order` keyword gives the index ordering both for *fetching* the values
    from `a`, and then *placing* the values into the output array.
    For example, let's say you have an array:

    >>> a = np.arange(6).reshape((3, 2))
    >>> a
    array([[0, 1],
           [2, 3],
           [4, 5]])

    You can think of reshaping as first raveling the array (using the given
    index order), then inserting the elements from the raveled array into the
    new array using the same kind of index ordering as was used for the
    raveling.

    >>> np.reshape(a, (2, 3)) # C-like index ordering
    array([[0, 1, 2],
           [3, 4, 5]])
    >>> np.reshape(np.ravel(a), (2, 3)) # equivalent to C ravel then C reshape
    array([[0, 1, 2],
           [3, 4, 5]])
    >>> np.reshape(a, (2, 3), order='F') # Fortran-like index ordering
    array([[0, 4, 3],
           [2, 1, 5]])
    >>> np.reshape(np.ravel(a, order='F'), (2, 3), order='F')
    array([[0, 4, 3],
           [2, 1, 5]])

    Examples
    --------
    >>> a = np.array([[1,2,3], [4,5,6]])
    >>> np.reshape(a, 6)
    array([1, 2, 3, 4, 5, 6])
    >>> np.reshape(a, 6, order='F')
    array([1, 4, 2, 5, 3, 6])

    >>> np.reshape(a, (3,-1))       # the unspecified value is inferred to be 2
    array([[1, 2],
           [3, 4],
           [5, 6]])

None
&&&&&&&&&&&&&&&&&&&&&& round &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

round(a, decimals=0, out=None)
    Evenly round to the given number of decimals.

    Parameters
    ----------
    a : array_like
        Input data.
    decimals : int, optional
        Number of decimal places to round to (default: 0).  If
        decimals is negative, it specifies the number of positions to
        the left of the decimal point.
    out : ndarray, optional
        Alternative output array in which to place the result. It must have
        the same shape as the expected output, but the type of the output
        values will be cast if necessary. See :ref:`ufuncs-output-type` for more
        details.

    Returns
    -------
    rounded_array : ndarray
        An array of the same type as `a`, containing the rounded values.
        Unless `out` was specified, a new array is created.  A reference to
        the result is returned.

        The real and imaginary parts of complex numbers are rounded
        separately.  The result of rounding a float is a float.

    See Also
    --------
    ndarray.round : equivalent method
    around : an alias for this function
    ceil, fix, floor, rint, trunc


    Notes
    -----
    For values exactly halfway between rounded decimal values, NumPy
    rounds to the nearest even value. Thus 1.5 and 2.5 round to 2.0,
    -0.5 and 0.5 round to 0.0, etc.

    ``np.round`` uses a fast but sometimes inexact algorithm to round
    floating-point datatypes. For positive `decimals` it is equivalent to
    ``np.true_divide(np.rint(a * 10**decimals), 10**decimals)``, which has
    error due to the inexact representation of decimal fractions in the IEEE
    floating point standard [1]_ and errors introduced when scaling by powers
    of ten. For instance, note the extra "1" in the following:

        >>> np.round(56294995342131.5, 3)
        56294995342131.51

    If your goal is to print such values with a fixed number of decimals, it is
    preferable to use numpy's float printing routines to limit the number of
    printed decimals:

        >>> np.format_float_positional(56294995342131.5, precision=3)
        '56294995342131.5'

    The float printing routines use an accurate but much more computationally
    demanding algorithm to compute the number of digits after the decimal
    point.

    Alternatively, Python's builtin `round` function uses a more accurate
    but slower algorithm for 64-bit floating point values:

        >>> round(56294995342131.5, 3)
        56294995342131.5
        >>> np.round(16.055, 2), round(16.055, 2)  # equals 16.0549999999999997
        (16.06, 16.05)


    References
    ----------
    .. [1] "Lecture Notes on the Status of IEEE 754", William Kahan,
           https://people.eecs.berkeley.edu/~wkahan/ieee754status/IEEE754.PDF

    Examples
    --------
    >>> np.round([0.37, 1.64])
    array([0., 2.])
    >>> np.round([0.37, 1.64], decimals=1)
    array([0.4, 1.6])
    >>> np.round([.5, 1.5, 2.5, 3.5, 4.5]) # rounds to nearest even value
    array([0., 2., 2., 4., 4.])
    >>> np.round([1,2,3,11], decimals=1) # ndarray of ints is returned
    array([ 1,  2,  3, 11])
    >>> np.round([1,2,3,11], decimals=-1)
    array([ 0,  0,  0, 10])

None
&&&&&&&&&&&&&&&&&&&&&& save &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

save(file, arr, allow_pickle=True, fix_imports=True)
    Save an array to a binary file in NumPy ``.npy`` format.

    Parameters
    ----------
    file : file, str, or pathlib.Path
        File or filename to which the data is saved.  If file is a file-object,
        then the filename is unchanged.  If file is a string or Path, a ``.npy``
        extension will be appended to the filename if it does not already
        have one.
    arr : array_like
        Array data to be saved.
    allow_pickle : bool, optional
        Allow saving object arrays using Python pickles. Reasons for disallowing
        pickles include security (loading pickled data can execute arbitrary
        code) and portability (pickled objects may not be loadable on different
        Python installations, for example if the stored objects require libraries
        that are not available, and not all pickled data is compatible between
        Python 2 and Python 3).
        Default: True
    fix_imports : bool, optional
        Only useful in forcing objects in object arrays on Python 3 to be
        pickled in a Python 2 compatible way. If `fix_imports` is True, pickle
        will try to map the new Python 3 names to the old module names used in
        Python 2, so that the pickle data stream is readable with Python 2.

    See Also
    --------
    savez : Save several arrays into a ``.npz`` archive
    savetxt, load

    Notes
    -----
    For a description of the ``.npy`` format, see :py:mod:`numpy.lib.format`.

    Any data saved to the file is appended to the end of the file.

    Examples
    --------
    >>> from tempfile import TemporaryFile
    >>> outfile = TemporaryFile()

    >>> x = np.arange(10)
    >>> np.save(outfile, x)

    >>> _ = outfile.seek(0) # Only needed here to simulate closing & reopening file
    >>> np.load(outfile)
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


    >>> with open('test.npy', 'wb') as f:
    ...     np.save(f, np.array([1, 2]))
    ...     np.save(f, np.array([1, 3]))
    >>> with open('test.npy', 'rb') as f:
    ...     a = np.load(f)
    ...     b = np.load(f)
    >>> print(a, b)
    # [1 2] [1 3]

None
&&&&&&&&&&&&&&&&&&&&&& savetxt &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=None)
    Save an array to a text file.

    Parameters
    ----------
    fname : filename or file handle
        If the filename ends in ``.gz``, the file is automatically saved in
        compressed gzip format.  `loadtxt` understands gzipped files
        transparently.
    X : 1D or 2D array_like
        Data to be saved to a text file.
    fmt : str or sequence of strs, optional
        A single format (%10.5f), a sequence of formats, or a
        multi-format string, e.g. 'Iteration %d -- %10.5f', in which
        case `delimiter` is ignored. For complex `X`, the legal options
        for `fmt` are:

        * a single specifier, `fmt='%.4e'`, resulting in numbers formatted
          like `' (%s+%sj)' % (fmt, fmt)`
        * a full string specifying every real and imaginary part, e.g.
          `' %.4e %+.4ej %.4e %+.4ej %.4e %+.4ej'` for 3 columns
        * a list of specifiers, one per column - in this case, the real
          and imaginary part must have separate specifiers,
          e.g. `['%.3e + %.3ej', '(%.15e%+.15ej)']` for 2 columns
    delimiter : str, optional
        String or character separating columns.
    newline : str, optional
        String or character separating lines.

        .. versionadded:: 1.5.0
    header : str, optional
        String that will be written at the beginning of the file.

        .. versionadded:: 1.7.0
    footer : str, optional
        String that will be written at the end of the file.

        .. versionadded:: 1.7.0
    comments : str, optional
        String that will be prepended to the ``header`` and ``footer`` strings,
        to mark them as comments. Default: '# ',  as expected by e.g.
        ``numpy.loadtxt``.

        .. versionadded:: 1.7.0
    encoding : {None, str}, optional
        Encoding used to encode the outputfile. Does not apply to output
        streams. If the encoding is something other than 'bytes' or 'latin1'
        you will not be able to load the file in NumPy versions < 1.14. Default
        is 'latin1'.

        .. versionadded:: 1.14.0


    See Also
    --------
    save : Save an array to a binary file in NumPy ``.npy`` format
    savez : Save several arrays into an uncompressed ``.npz`` archive
    savez_compressed : Save several arrays into a compressed ``.npz`` archive

    Notes
    -----
    Further explanation of the `fmt` parameter
    (``%[flag]width[.precision]specifier``):

    flags:
        ``-`` : left justify

        ``+`` : Forces to precede result with + or -.

        ``0`` : Left pad the number with zeros instead of space (see width).

    width:
        Minimum number of characters to be printed. The value is not truncated
        if it has more characters.

    precision:
        - For integer specifiers (eg. ``d,i,o,x``), the minimum number of
          digits.
        - For ``e, E`` and ``f`` specifiers, the number of digits to print
          after the decimal point.
        - For ``g`` and ``G``, the maximum number of significant digits.
        - For ``s``, the maximum number of characters.

    specifiers:
        ``c`` : character

        ``d`` or ``i`` : signed decimal integer

        ``e`` or ``E`` : scientific notation with ``e`` or ``E``.

        ``f`` : decimal floating point

        ``g,G`` : use the shorter of ``e,E`` or ``f``

        ``o`` : signed octal

        ``s`` : string of characters

        ``u`` : unsigned decimal integer

        ``x,X`` : unsigned hexadecimal integer

    This explanation of ``fmt`` is not complete, for an exhaustive
    specification see [1]_.

    References
    ----------
    .. [1] `Format Specification Mini-Language
           <https://docs.python.org/library/string.html#format-specification-mini-language>`_,
           Python Documentation.

    Examples
    --------
    >>> x = y = z = np.arange(0.0,5.0,1.0)
    >>> np.savetxt('test.out', x, delimiter=',')   # X is an array
    >>> np.savetxt('test.out', (x,y,z))   # x,y,z equal sized 1D arrays
    >>> np.savetxt('test.out', x, fmt='%1.4e')   # use exponential notation

None
&&&&&&&&&&&&&&&&&&&&&& shape &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

shape(a)
    Return the shape of an array.

    Parameters
    ----------
    a : array_like
        Input array.

    Returns
    -------
    shape : tuple of ints
        The elements of the shape tuple give the lengths of the
        corresponding array dimensions.

    See Also
    --------
    len : ``len(a)`` is equivalent to ``np.shape(a)[0]`` for N-D arrays with
          ``N>=1``.
    ndarray.shape : Equivalent array method.

    Examples
    --------
    >>> np.shape(np.eye(3))
    (3, 3)
    >>> np.shape([[1, 3]])
    (1, 2)
    >>> np.shape([0])
    (1,)
    >>> np.shape(0)
    ()

    >>> a = np.array([(1, 2), (3, 4), (5, 6)],
    ...              dtype=[('x', 'i4'), ('y', 'i4')])
    >>> np.shape(a)
    (3,)
    >>> a.shape
    (3,)

None
&&&&&&&&&&&&&&&&&&&&&& sin &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on ufunc:

sin = <ufunc 'sin'>
    sin(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])

    Trigonometric sine, element-wise.

    Parameters
    ----------
    x : array_like
        Angle, in radians (:math:`2 \pi` rad equals 360 degrees).
    out : ndarray, None, or tuple of ndarray and None, optional
        A location into which the result is stored. If provided, it must have
        a shape that the inputs broadcast to. If not provided or None,
        a freshly-allocated array is returned. A tuple (possible only as a
        keyword argument) must have length equal to the number of outputs.
    where : array_like, optional
        This condition is broadcast over the input. At locations where the
        condition is True, the `out` array will be set to the ufunc result.
        Elsewhere, the `out` array will retain its original value.
        Note that if an uninitialized `out` array is created via the default
        ``out=None``, locations within it where the condition is False will
        remain uninitialized.
    **kwargs
        For other keyword-only arguments, see the
        :ref:`ufunc docs <ufuncs.kwargs>`.

    Returns
    -------
    y : array_like
        The sine of each element of x.
        This is a scalar if `x` is a scalar.

    See Also
    --------
    arcsin, sinh, cos

    Notes
    -----
    The sine is one of the fundamental functions of trigonometry (the
    mathematical study of triangles).  Consider a circle of radius 1
    centered on the origin.  A ray comes in from the :math:`+x` axis, makes
    an angle at the origin (measured counter-clockwise from that axis), and
    departs from the origin.  The :math:`y` coordinate of the outgoing
    ray's intersection with the unit circle is the sine of that angle.  It
    ranges from -1 for :math:`x=3\pi / 2` to +1 for :math:`\pi / 2.`  The
    function has zeroes where the angle is a multiple of :math:`\pi`.
    Sines of angles between :math:`\pi` and :math:`2\pi` are negative.
    The numerous properties of the sine and related functions are included
    in any standard trigonometry text.

    Examples
    --------
    Print sine of one angle:

    >>> np.sin(np.pi/2.)
    1.0

    Print sines of an array of angles given in degrees:

    >>> np.sin(np.array((0., 30., 45., 60., 90.)) * np.pi / 180. )
    array([ 0.        ,  0.5       ,  0.70710678,  0.8660254 ,  1.        ])

    Plot the sine function:

    >>> import matplotlib.pylab as plt
    >>> x = np.linspace(-np.pi, np.pi, 201)
    >>> plt.plot(x, np.sin(x))
    >>> plt.xlabel('Angle [rad]')
    >>> plt.ylabel('sin(x)')
    >>> plt.axis('tight')
    >>> plt.show()

None
&&&&&&&&&&&&&&&&&&&&&& size &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

size(a, axis=None)
    Return the number of elements along a given axis.

    Parameters
    ----------
    a : array_like
        Input data.
    axis : int, optional
        Axis along which the elements are counted.  By default, give
        the total number of elements.

    Returns
    -------
    element_count : int
        Number of elements along the specified axis.

    See Also
    --------
    shape : dimensions of array
    ndarray.shape : dimensions of array
    ndarray.size : number of elements in array

    Examples
    --------
    >>> a = np.array([[1,2,3],[4,5,6]])
    >>> np.size(a)
    6
    >>> np.size(a,1)
    3
    >>> np.size(a,0)
    2

None
&&&&&&&&&&&&&&&&&&&&&& sort &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

sort(a, axis=-1, kind=None, order=None)
    Return a sorted copy of an array.

    Parameters
    ----------
    a : array_like
        Array to be sorted.
    axis : int or None, optional
        Axis along which to sort. If None, the array is flattened before
        sorting. The default is -1, which sorts along the last axis.
    kind : {'quicksort', 'mergesort', 'heapsort', 'stable'}, optional
        Sorting algorithm. The default is 'quicksort'. Note that both 'stable'
        and 'mergesort' use timsort or radix sort under the covers and, in general,
        the actual implementation will vary with data type. The 'mergesort' option
        is retained for backwards compatibility.

        .. versionchanged:: 1.15.0.
           The 'stable' option was added.

    order : str or list of str, optional
        When `a` is an array with fields defined, this argument specifies
        which fields to compare first, second, etc.  A single field can
        be specified as a string, and not all fields need be specified,
        but unspecified fields will still be used, in the order in which
        they come up in the dtype, to break ties.

    Returns
    -------
    sorted_array : ndarray
        Array of the same type and shape as `a`.

    See Also
    --------
    ndarray.sort : Method to sort an array in-place.
    argsort : Indirect sort.
    lexsort : Indirect stable sort on multiple keys.
    searchsorted : Find elements in a sorted array.
    partition : Partial sort.

    Notes
    -----
    The various sorting algorithms are characterized by their average speed,
    worst case performance, work space size, and whether they are stable. A
    stable sort keeps items with the same key in the same relative
    order. The four algorithms implemented in NumPy have the following
    properties:

    =========== ======= ============= ============ ========
       kind      speed   worst case    work space   stable
    =========== ======= ============= ============ ========
    'quicksort'    1     O(n^2)            0          no
    'heapsort'     3     O(n*log(n))       0          no
    'mergesort'    2     O(n*log(n))      ~n/2        yes
    'timsort'      2     O(n*log(n))      ~n/2        yes
    =========== ======= ============= ============ ========

    .. note:: The datatype determines which of 'mergesort' or 'timsort'
       is actually used, even if 'mergesort' is specified. User selection
       at a finer scale is not currently available.

    All the sort algorithms make temporary copies of the data when
    sorting along any but the last axis.  Consequently, sorting along
    the last axis is faster and uses less space than sorting along
    any other axis.

    The sort order for complex numbers is lexicographic. If both the real
    and imaginary parts are non-nan then the order is determined by the
    real parts except when they are equal, in which case the order is
    determined by the imaginary parts.

    Previous to numpy 1.4.0 sorting real and complex arrays containing nan
    values led to undefined behaviour. In numpy versions >= 1.4.0 nan
    values are sorted to the end. The extended sort order is:

      * Real: [R, nan]
      * Complex: [R + Rj, R + nanj, nan + Rj, nan + nanj]

    where R is a non-nan real value. Complex values with the same nan
    placements are sorted according to the non-nan part if it exists.
    Non-nan values are sorted as before.

    .. versionadded:: 1.12.0

    quicksort has been changed to `introsort <https://en.wikipedia.org/wiki/Introsort>`_.
    When sorting does not make enough progress it switches to
    `heapsort <https://en.wikipedia.org/wiki/Heapsort>`_.
    This implementation makes quicksort O(n*log(n)) in the worst case.

    'stable' automatically chooses the best stable sorting algorithm
    for the data type being sorted.
    It, along with 'mergesort' is currently mapped to
    `timsort <https://en.wikipedia.org/wiki/Timsort>`_
    or `radix sort <https://en.wikipedia.org/wiki/Radix_sort>`_
    depending on the data type.
    API forward compatibility currently limits the
    ability to select the implementation and it is hardwired for the different
    data types.

    .. versionadded:: 1.17.0

    Timsort is added for better performance on already or nearly
    sorted data. On random data timsort is almost identical to
    mergesort. It is now used for stable sort while quicksort is still the
    default sort if none is chosen. For timsort details, refer to
    `CPython listsort.txt <https://github.com/python/cpython/blob/3.7/Objects/listsort.txt>`_.
    'mergesort' and 'stable' are mapped to radix sort for integer data types. Radix sort is an
    O(n) sort instead of O(n log n).

    .. versionchanged:: 1.18.0

    NaT now sorts to the end of arrays for consistency with NaN.

    Examples
    --------
    >>> a = np.array([[1,4],[3,1]])
    >>> np.sort(a)                # sort along the last axis
    array([[1, 4],
           [1, 3]])
    >>> np.sort(a, axis=None)     # sort the flattened array
    array([1, 1, 3, 4])
    >>> np.sort(a, axis=0)        # sort along the first axis
    array([[1, 1],
           [3, 4]])

    Use the `order` keyword to specify a field to use when sorting a
    structured array:

    >>> dtype = [('name', 'S10'), ('height', float), ('age', int)]
    >>> values = [('Arthur', 1.8, 41), ('Lancelot', 1.9, 38),
    ...           ('Galahad', 1.7, 38)]
    >>> a = np.array(values, dtype=dtype)       # create a structured array
    >>> np.sort(a, order='height')                        # doctest: +SKIP
    array([('Galahad', 1.7, 38), ('Arthur', 1.8, 41),
           ('Lancelot', 1.8999999999999999, 38)],
          dtype=[('name', '|S10'), ('height', '<f8'), ('age', '<i4')])

    Sort by age, then height if ages are equal:

    >>> np.sort(a, order=['age', 'height'])               # doctest: +SKIP
    array([('Galahad', 1.7, 38), ('Lancelot', 1.8999999999999999, 38),
           ('Arthur', 1.8, 41)],
          dtype=[('name', '|S10'), ('height', '<f8'), ('age', '<i4')])

None
&&&&&&&&&&&&&&&&&&&&&& sqrt &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on ufunc:

sqrt = <ufunc 'sqrt'>
    sqrt(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])

    Return the non-negative square-root of an array, element-wise.

    Parameters
    ----------
    x : array_like
        The values whose square-roots are required.
    out : ndarray, None, or tuple of ndarray and None, optional
        A location into which the result is stored. If provided, it must have
        a shape that the inputs broadcast to. If not provided or None,
        a freshly-allocated array is returned. A tuple (possible only as a
        keyword argument) must have length equal to the number of outputs.
    where : array_like, optional
        This condition is broadcast over the input. At locations where the
        condition is True, the `out` array will be set to the ufunc result.
        Elsewhere, the `out` array will retain its original value.
        Note that if an uninitialized `out` array is created via the default
        ``out=None``, locations within it where the condition is False will
        remain uninitialized.
    **kwargs
        For other keyword-only arguments, see the
        :ref:`ufunc docs <ufuncs.kwargs>`.

    Returns
    -------
    y : ndarray
        An array of the same shape as `x`, containing the positive
        square-root of each element in `x`.  If any element in `x` is
        complex, a complex array is returned (and the square-roots of
        negative reals are calculated).  If all of the elements in `x`
        are real, so is `y`, with negative elements returning ``nan``.
        If `out` was provided, `y` is a reference to it.
        This is a scalar if `x` is a scalar.

    See Also
    --------
    emath.sqrt
        A version which returns complex numbers when given negative reals.
        Note that 0.0 and -0.0 are handled differently for complex inputs.

    Notes
    -----
    *sqrt* has--consistent with common convention--as its branch cut the
    real "interval" [`-inf`, 0), and is continuous from above on it.
    A branch cut is a curve in the complex plane across which a given
    complex function fails to be continuous.

    Examples
    --------
    >>> np.sqrt([1,4,9])
    array([ 1.,  2.,  3.])

    >>> np.sqrt([4, -1, -3+4J])
    array([ 2.+0.j,  0.+1.j,  1.+2.j])

    >>> np.sqrt([4, -1, np.inf])
    array([ 2., nan, inf])

None
&&&&&&&&&&&&&&&&&&&&&& std &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

std(a, axis=None, dtype=None, out=None, ddof=0, keepdims=<no value>, *, where=<no value>)
    Compute the standard deviation along the specified axis.

    Returns the standard deviation, a measure of the spread of a distribution,
    of the array elements. The standard deviation is computed for the
    flattened array by default, otherwise over the specified axis.

    Parameters
    ----------
    a : array_like
        Calculate the standard deviation of these values.
    axis : None or int or tuple of ints, optional
        Axis or axes along which the standard deviation is computed. The
        default is to compute the standard deviation of the flattened array.

        .. versionadded:: 1.7.0

        If this is a tuple of ints, a standard deviation is performed over
        multiple axes, instead of a single axis or all the axes as before.
    dtype : dtype, optional
        Type to use in computing the standard deviation. For arrays of
        integer type the default is float64, for arrays of float types it is
        the same as the array type.
    out : ndarray, optional
        Alternative output array in which to place the result. It must have
        the same shape as the expected output but the type (of the calculated
        values) will be cast if necessary.
    ddof : int, optional
        Means Delta Degrees of Freedom.  The divisor used in calculations
        is ``N - ddof``, where ``N`` represents the number of elements.
        By default `ddof` is zero.
    keepdims : bool, optional
        If this is set to True, the axes which are reduced are left
        in the result as dimensions with size one. With this option,
        the result will broadcast correctly against the input array.

        If the default value is passed, then `keepdims` will not be
        passed through to the `std` method of sub-classes of
        `ndarray`, however any non-default value will be.  If the
        sub-class' method does not implement `keepdims` any
        exceptions will be raised.

    where : array_like of bool, optional
        Elements to include in the standard deviation.
        See `~numpy.ufunc.reduce` for details.

        .. versionadded:: 1.20.0

    Returns
    -------
    standard_deviation : ndarray, see dtype parameter above.
        If `out` is None, return a new array containing the standard deviation,
        otherwise return a reference to the output array.

    See Also
    --------
    var, mean, nanmean, nanstd, nanvar
    :ref:`ufuncs-output-type`

    Notes
    -----
    The standard deviation is the square root of the average of the squared
    deviations from the mean, i.e., ``std = sqrt(mean(x))``, where
    ``x = abs(a - a.mean())**2``.

    The average squared deviation is typically calculated as ``x.sum() / N``,
    where ``N = len(x)``. If, however, `ddof` is specified, the divisor
    ``N - ddof`` is used instead. In standard statistical practice, ``ddof=1``
    provides an unbiased estimator of the variance of the infinite population.
    ``ddof=0`` provides a maximum likelihood estimate of the variance for
    normally distributed variables. The standard deviation computed in this
    function is the square root of the estimated variance, so even with
    ``ddof=1``, it will not be an unbiased estimate of the standard deviation
    per se.

    Note that, for complex numbers, `std` takes the absolute
    value before squaring, so that the result is always real and nonnegative.

    For floating-point input, the *std* is computed using the same
    precision the input has. Depending on the input data, this can cause
    the results to be inaccurate, especially for float32 (see example below).
    Specifying a higher-accuracy accumulator using the `dtype` keyword can
    alleviate this issue.

    Examples
    --------
    >>> a = np.array([[1, 2], [3, 4]])
    >>> np.std(a)
    1.1180339887498949 # may vary
    >>> np.std(a, axis=0)
    array([1.,  1.])
    >>> np.std(a, axis=1)
    array([0.5,  0.5])

    In single precision, std() can be inaccurate:

    >>> a = np.zeros((2, 512*512), dtype=np.float32)
    >>> a[0, :] = 1.0
    >>> a[1, :] = 0.1
    >>> np.std(a)
    0.45000005

    Computing the standard deviation in float64 is more accurate:

    >>> np.std(a, dtype=np.float64)
    0.44999999925494177 # may vary

    Specifying a where argument:

    >>> a = np.array([[14, 8, 11, 10], [7, 9, 10, 11], [10, 15, 5, 10]])
    >>> np.std(a)
    2.614064523559687 # may vary
    >>> np.std(a, where=[[True], [True], [False]])
    2.0

None
&&&&&&&&&&&&&&&&&&&&&& sum &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

sum(a, axis=None, dtype=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)
    Sum of array elements over a given axis.

    Parameters
    ----------
    a : array_like
        Elements to sum.
    axis : None or int or tuple of ints, optional
        Axis or axes along which a sum is performed.  The default,
        axis=None, will sum all of the elements of the input array.  If
        axis is negative it counts from the last to the first axis.

        .. versionadded:: 1.7.0

        If axis is a tuple of ints, a sum is performed on all of the axes
        specified in the tuple instead of a single axis or all the axes as
        before.
    dtype : dtype, optional
        The type of the returned array and of the accumulator in which the
        elements are summed.  The dtype of `a` is used by default unless `a`
        has an integer dtype of less precision than the default platform
        integer.  In that case, if `a` is signed then the platform integer
        is used while if `a` is unsigned then an unsigned integer of the
        same precision as the platform integer is used.
    out : ndarray, optional
        Alternative output array in which to place the result. It must have
        the same shape as the expected output, but the type of the output
        values will be cast if necessary.
    keepdims : bool, optional
        If this is set to True, the axes which are reduced are left
        in the result as dimensions with size one. With this option,
        the result will broadcast correctly against the input array.

        If the default value is passed, then `keepdims` will not be
        passed through to the `sum` method of sub-classes of
        `ndarray`, however any non-default value will be.  If the
        sub-class' method does not implement `keepdims` any
        exceptions will be raised.
    initial : scalar, optional
        Starting value for the sum. See `~numpy.ufunc.reduce` for details.

        .. versionadded:: 1.15.0

    where : array_like of bool, optional
        Elements to include in the sum. See `~numpy.ufunc.reduce` for details.

        .. versionadded:: 1.17.0

    Returns
    -------
    sum_along_axis : ndarray
        An array with the same shape as `a`, with the specified
        axis removed.   If `a` is a 0-d array, or if `axis` is None, a scalar
        is returned.  If an output array is specified, a reference to
        `out` is returned.

    See Also
    --------
    ndarray.sum : Equivalent method.

    add.reduce : Equivalent functionality of `add`.

    cumsum : Cumulative sum of array elements.

    trapz : Integration of array values using the composite trapezoidal rule.

    mean, average

    Notes
    -----
    Arithmetic is modular when using integer types, and no error is
    raised on overflow.

    The sum of an empty array is the neutral element 0:

    >>> np.sum([])
    0.0

    For floating point numbers the numerical precision of sum (and
    ``np.add.reduce``) is in general limited by directly adding each number
    individually to the result causing rounding errors in every step.
    However, often numpy will use a  numerically better approach (partial
    pairwise summation) leading to improved precision in many use-cases.
    This improved precision is always provided when no ``axis`` is given.
    When ``axis`` is given, it will depend on which axis is summed.
    Technically, to provide the best speed possible, the improved precision
    is only used when the summation is along the fast axis in memory.
    Note that the exact precision may vary depending on other parameters.
    In contrast to NumPy, Python's ``math.fsum`` function uses a slower but
    more precise approach to summation.
    Especially when summing a large number of lower precision floating point
    numbers, such as ``float32``, numerical errors can become significant.
    In such cases it can be advisable to use `dtype="float64"` to use a higher
    precision for the output.

    Examples
    --------
    >>> np.sum([0.5, 1.5])
    2.0
    >>> np.sum([0.5, 0.7, 0.2, 1.5], dtype=np.int32)
    1
    >>> np.sum([[0, 1], [0, 5]])
    6
    >>> np.sum([[0, 1], [0, 5]], axis=0)
    array([0, 6])
    >>> np.sum([[0, 1], [0, 5]], axis=1)
    array([1, 5])
    >>> np.sum([[0, 1], [np.nan, 5]], where=[False, True], axis=1)
    array([1., 5.])

    If the accumulator is too small, overflow occurs:

    >>> np.ones(128, dtype=np.int8).sum(dtype=np.int8)
    -128

    You can also start the sum with a value other than zero:

    >>> np.sum([10], initial=5)
    15

None
&&&&&&&&&&&&&&&&&&&&&& tan &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on ufunc:

tan = <ufunc 'tan'>
    tan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])

    Compute tangent element-wise.

    Equivalent to ``np.sin(x)/np.cos(x)`` element-wise.

    Parameters
    ----------
    x : array_like
        Input array.
    out : ndarray, None, or tuple of ndarray and None, optional
        A location into which the result is stored. If provided, it must have
        a shape that the inputs broadcast to. If not provided or None,
        a freshly-allocated array is returned. A tuple (possible only as a
        keyword argument) must have length equal to the number of outputs.
    where : array_like, optional
        This condition is broadcast over the input. At locations where the
        condition is True, the `out` array will be set to the ufunc result.
        Elsewhere, the `out` array will retain its original value.
        Note that if an uninitialized `out` array is created via the default
        ``out=None``, locations within it where the condition is False will
        remain uninitialized.
    **kwargs
        For other keyword-only arguments, see the
        :ref:`ufunc docs <ufuncs.kwargs>`.

    Returns
    -------
    y : ndarray
        The corresponding tangent values.
        This is a scalar if `x` is a scalar.

    Notes
    -----
    If `out` is provided, the function writes the result into it,
    and returns a reference to `out`.  (See Examples)

    References
    ----------
    M. Abramowitz and I. A. Stegun, Handbook of Mathematical Functions.
    New York, NY: Dover, 1972.

    Examples
    --------
    >>> from math import pi
    >>> np.tan(np.array([-pi,pi/2,pi]))
    array([  1.22460635e-16,   1.63317787e+16,  -1.22460635e-16])
    >>>
    >>> # Example of providing the optional output parameter illustrating
    >>> # that what is returned is a reference to said parameter
    >>> out1 = np.array([0], dtype='d')
    >>> out2 = np.cos([0.1], out1)
    >>> out2 is out1
    True
    >>>
    >>> # Example of ValueError due to provision of shape mis-matched `out`
    >>> np.cos(np.zeros((3,3)),np.zeros((2,2)))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: operands could not be broadcast together with shapes (3,3) (2,2)

None
&&&&&&&&&&&&&&&&&&&&&& transpose &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

transpose(a, axes=None)
    Returns an array with axes transposed.

    For a 1-D array, this returns an unchanged view of the original array, as a
    transposed vector is simply the same vector.
    To convert a 1-D array into a 2-D column vector, an additional dimension
    must be added, e.g., ``np.atleast2d(a).T`` achieves this, as does
    ``a[:, np.newaxis]``.
    For a 2-D array, this is the standard matrix transpose.
    For an n-D array, if axes are given, their order indicates how the
    axes are permuted (see Examples). If axes are not provided, then
    ``transpose(a).shape == a.shape[::-1]``.

    Parameters
    ----------
    a : array_like
        Input array.
    axes : tuple or list of ints, optional
        If specified, it must be a tuple or list which contains a permutation
        of [0,1,...,N-1] where N is the number of axes of `a`. The `i`'th axis
        of the returned array will correspond to the axis numbered ``axes[i]``
        of the input. If not specified, defaults to ``range(a.ndim)[::-1]``,
        which reverses the order of the axes.

    Returns
    -------
    p : ndarray
        `a` with its axes permuted. A view is returned whenever possible.

    See Also
    --------
    ndarray.transpose : Equivalent method.
    moveaxis : Move axes of an array to new positions.
    argsort : Return the indices that would sort an array.

    Notes
    -----
    Use ``transpose(a, argsort(axes))`` to invert the transposition of tensors
    when using the `axes` keyword argument.

    Examples
    --------
    >>> a = np.array([[1, 2], [3, 4]])
    >>> a
    array([[1, 2],
           [3, 4]])
    >>> np.transpose(a)
    array([[1, 3],
           [2, 4]])

    >>> a = np.array([1, 2, 3, 4])
    >>> a
    array([1, 2, 3, 4])
    >>> np.transpose(a)
    array([1, 2, 3, 4])

    >>> a = np.ones((1, 2, 3))
    >>> np.transpose(a, (1, 0, 2)).shape
    (2, 1, 3)

    >>> a = np.ones((2, 3, 4, 5))
    >>> np.transpose(a).shape
    (5, 4, 3, 2)

None
&&&&&&&&&&&&&&&&&&&&&& unique &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

unique(ar, return_index=False, return_inverse=False, return_counts=False, axis=None, *, equal_nan=True)
    Find the unique elements of an array.

    Returns the sorted unique elements of an array. There are three optional
    outputs in addition to the unique elements:

    * the indices of the input array that give the unique values
    * the indices of the unique array that reconstruct the input array
    * the number of times each unique value comes up in the input array

    Parameters
    ----------
    ar : array_like
        Input array. Unless `axis` is specified, this will be flattened if it
        is not already 1-D.
    return_index : bool, optional
        If True, also return the indices of `ar` (along the specified axis,
        if provided, or in the flattened array) that result in the unique array.
    return_inverse : bool, optional
        If True, also return the indices of the unique array (for the specified
        axis, if provided) that can be used to reconstruct `ar`.
    return_counts : bool, optional
        If True, also return the number of times each unique item appears
        in `ar`.
    axis : int or None, optional
        The axis to operate on. If None, `ar` will be flattened. If an integer,
        the subarrays indexed by the given axis will be flattened and treated
        as the elements of a 1-D array with the dimension of the given axis,
        see the notes for more details.  Object arrays or structured arrays
        that contain objects are not supported if the `axis` kwarg is used. The
        default is None.

        .. versionadded:: 1.13.0

    equal_nan : bool, optional
        If True, collapses multiple NaN values in the return array into one.

        .. versionadded:: 1.24

    Returns
    -------
    unique : ndarray
        The sorted unique values.
    unique_indices : ndarray, optional
        The indices of the first occurrences of the unique values in the
        original array. Only provided if `return_index` is True.
    unique_inverse : ndarray, optional
        The indices to reconstruct the original array from the
        unique array. Only provided if `return_inverse` is True.
    unique_counts : ndarray, optional
        The number of times each of the unique values comes up in the
        original array. Only provided if `return_counts` is True.

        .. versionadded:: 1.9.0

    See Also
    --------
    numpy.lib.arraysetops : Module with a number of other functions for
                            performing set operations on arrays.
    repeat : Repeat elements of an array.

    Notes
    -----
    When an axis is specified the subarrays indexed by the axis are sorted.
    This is done by making the specified axis the first dimension of the array
    (move the axis to the first dimension to keep the order of the other axes)
    and then flattening the subarrays in C order. The flattened subarrays are
    then viewed as a structured type with each element given a label, with the
    effect that we end up with a 1-D array of structured types that can be
    treated in the same way as any other 1-D array. The result is that the
    flattened subarrays are sorted in lexicographic order starting with the
    first element.

    .. versionchanged: NumPy 1.21
        If nan values are in the input array, a single nan is put
        to the end of the sorted unique values.

        Also for complex arrays all NaN values are considered equivalent
        (no matter whether the NaN is in the real or imaginary part).
        As the representant for the returned array the smallest one in the
        lexicographical order is chosen - see np.sort for how the lexicographical
        order is defined for complex arrays.

    Examples
    --------
    >>> np.unique([1, 1, 2, 2, 3, 3])
    array([1, 2, 3])
    >>> a = np.array([[1, 1], [2, 3]])
    >>> np.unique(a)
    array([1, 2, 3])

    Return the unique rows of a 2D array

    >>> a = np.array([[1, 0, 0], [1, 0, 0], [2, 3, 4]])
    >>> np.unique(a, axis=0)
    array([[1, 0, 0], [2, 3, 4]])

    Return the indices of the original array that give the unique values:

    >>> a = np.array(['a', 'b', 'b', 'c', 'a'])
    >>> u, indices = np.unique(a, return_index=True)
    >>> u
    array(['a', 'b', 'c'], dtype='<U1')
    >>> indices
    array([0, 1, 3])
    >>> a[indices]
    array(['a', 'b', 'c'], dtype='<U1')

    Reconstruct the input array from the unique values and inverse:

    >>> a = np.array([1, 2, 6, 4, 2, 3, 2])
    >>> u, indices = np.unique(a, return_inverse=True)
    >>> u
    array([1, 2, 3, 4, 6])
    >>> indices
    array([0, 1, 4, 3, 1, 2, 1])
    >>> u[indices]
    array([1, 2, 6, 4, 2, 3, 2])

    Reconstruct the input values from the unique values and counts:

    >>> a = np.array([1, 2, 6, 4, 2, 3, 2])
    >>> values, counts = np.unique(a, return_counts=True)
    >>> values
    array([1, 2, 3, 4, 6])
    >>> counts
    array([1, 3, 1, 1, 1])
    >>> np.repeat(values, counts)
    array([1, 2, 2, 2, 3, 4, 6])    # original order not preserved

None
&&&&&&&&&&&&&&&&&&&&&& var &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

var(a, axis=None, dtype=None, out=None, ddof=0, keepdims=<no value>, *, where=<no value>)
    Compute the variance along the specified axis.

    Returns the variance of the array elements, a measure of the spread of a
    distribution.  The variance is computed for the flattened array by
    default, otherwise over the specified axis.

    Parameters
    ----------
    a : array_like
        Array containing numbers whose variance is desired.  If `a` is not an
        array, a conversion is attempted.
    axis : None or int or tuple of ints, optional
        Axis or axes along which the variance is computed.  The default is to
        compute the variance of the flattened array.

        .. versionadded:: 1.7.0

        If this is a tuple of ints, a variance is performed over multiple axes,
        instead of a single axis or all the axes as before.
    dtype : data-type, optional
        Type to use in computing the variance.  For arrays of integer type
        the default is `float64`; for arrays of float types it is the same as
        the array type.
    out : ndarray, optional
        Alternate output array in which to place the result.  It must have
        the same shape as the expected output, but the type is cast if
        necessary.
    ddof : int, optional
        "Delta Degrees of Freedom": the divisor used in the calculation is
        ``N - ddof``, where ``N`` represents the number of elements. By
        default `ddof` is zero.
    keepdims : bool, optional
        If this is set to True, the axes which are reduced are left
        in the result as dimensions with size one. With this option,
        the result will broadcast correctly against the input array.

        If the default value is passed, then `keepdims` will not be
        passed through to the `var` method of sub-classes of
        `ndarray`, however any non-default value will be.  If the
        sub-class' method does not implement `keepdims` any
        exceptions will be raised.

    where : array_like of bool, optional
        Elements to include in the variance. See `~numpy.ufunc.reduce` for
        details.

        .. versionadded:: 1.20.0

    Returns
    -------
    variance : ndarray, see dtype parameter above
        If ``out=None``, returns a new array containing the variance;
        otherwise, a reference to the output array is returned.

    See Also
    --------
    std, mean, nanmean, nanstd, nanvar
    :ref:`ufuncs-output-type`

    Notes
    -----
    The variance is the average of the squared deviations from the mean,
    i.e.,  ``var = mean(x)``, where ``x = abs(a - a.mean())**2``.

    The mean is typically calculated as ``x.sum() / N``, where ``N = len(x)``.
    If, however, `ddof` is specified, the divisor ``N - ddof`` is used
    instead.  In standard statistical practice, ``ddof=1`` provides an
    unbiased estimator of the variance of a hypothetical infinite population.
    ``ddof=0`` provides a maximum likelihood estimate of the variance for
    normally distributed variables.

    Note that for complex numbers, the absolute value is taken before
    squaring, so that the result is always real and nonnegative.

    For floating-point input, the variance is computed using the same
    precision the input has.  Depending on the input data, this can cause
    the results to be inaccurate, especially for `float32` (see example
    below).  Specifying a higher-accuracy accumulator using the ``dtype``
    keyword can alleviate this issue.

    Examples
    --------
    >>> a = np.array([[1, 2], [3, 4]])
    >>> np.var(a)
    1.25
    >>> np.var(a, axis=0)
    array([1.,  1.])
    >>> np.var(a, axis=1)
    array([0.25,  0.25])

    In single precision, var() can be inaccurate:

    >>> a = np.zeros((2, 512*512), dtype=np.float32)
    >>> a[0, :] = 1.0
    >>> a[1, :] = 0.1
    >>> np.var(a)
    0.20250003

    Computing the variance in float64 is more accurate:

    >>> np.var(a, dtype=np.float64)
    0.20249999932944759 # may vary
    >>> ((1-0.55)**2 + (0.1-0.55)**2)/2
    0.2025

    Specifying a where argument:

    >>> a = np.array([[14, 8, 11, 10], [7, 9, 10, 11], [10, 15, 5, 10]])
    >>> np.var(a)
    6.833333333333333 # may vary
    >>> np.var(a, where=[[True], [True], [False]])
    4.0

None
&&&&&&&&&&&&&&&&&&&&&& zeros &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on built-in function zeros in module numpy:

zeros(...)
    zeros(shape, dtype=float, order='C', *, like=None)

    Return a new array of given shape and type, filled with zeros.

    Parameters
    ----------
    shape : int or tuple of ints
        Shape of the new array, e.g., ``(2, 3)`` or ``2``.
    dtype : data-type, optional
        The desired data-type for the array, e.g., `numpy.int8`.  Default is
        `numpy.float64`.
    order : {'C', 'F'}, optional, default: 'C'
        Whether to store multi-dimensional data in row-major
        (C-style) or column-major (Fortran-style) order in
        memory.
    like : array_like, optional
        Reference object to allow the creation of arrays which are not
        NumPy arrays. If an array-like passed in as ``like`` supports
        the ``__array_function__`` protocol, the result will be defined
        by it. In this case, it ensures the creation of an array object
        compatible with that passed in via this argument.

        .. versionadded:: 1.20.0

    Returns
    -------
    out : ndarray
        Array of zeros with the given shape, dtype, and order.

    See Also
    --------
    zeros_like : Return an array of zeros with shape and type of input.
    empty : Return a new uninitialized array.
    ones : Return a new array setting values to one.
    full : Return a new array of given shape filled with value.

    Examples
    --------
    >>> np.zeros(5)
    array([ 0.,  0.,  0.,  0.,  0.])

    >>> np.zeros((5,), dtype=int)
    array([0, 0, 0, 0, 0])

    >>> np.zeros((2, 1))
    array([[ 0.],
           [ 0.]])

    >>> s = (2,2)
    >>> np.zeros(s)
    array([[ 0.,  0.],
           [ 0.,  0.]])

    >>> np.zeros((2,), dtype=[('x', 'i4'), ('y', 'i4')]) # custom dtype
    array([(0, 0), (0, 0)],
          dtype=[('x', '<i4'), ('y', '<i4')])

None
