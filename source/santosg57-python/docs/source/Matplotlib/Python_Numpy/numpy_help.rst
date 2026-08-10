numpy_help
==========

........................... False_ ...........................
Help on bool object:

class bool(generic)
 |  Boolean type (True or False), stored as a byte.
 |
 |  .. warning::
 |
 |     The :class:`bool` type is not a subclass of the :class:`int_` type
 |     (the :class:`bool` is not even a number type). This is different
 |     than Python's default implementation of :class:`bool` as a
........................... ScalarType ...........................
Help on tuple object:

class tuple(object)
 |  tuple(iterable=(), /)
 |
 |  Built-in immutable sequence.
 |
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |
........................... True_ ...........................
Help on bool object:

class bool(generic)
 |  Boolean type (True or False), stored as a byte.
 |
 |  .. warning::
 |
 |     The :class:`bool` type is not a subclass of the :class:`int_` type
 |     (the :class:`bool` is not even a number type). This is different
 |     than Python's default implementation of :class:`bool` as a
........................... abs ...........................
Help on ufunc in module numpy:

absolute = <ufunc 'absolute'>
    absolute(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Calculate the absolute value element-wise.

    ``np.abs`` is a shorthand for this function.

    Parameters
........................... absolute ...........................
Help on ufunc in module numpy:

absolute = <ufunc 'absolute'>
    absolute(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Calculate the absolute value element-wise.

    ``np.abs`` is a shorthand for this function.

    Parameters
........................... acos ...........................
Help on ufunc in module numpy:

arccos = <ufunc 'arccos'>
    arccos(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Trigonometric inverse cosine, element-wise.

    The inverse of `cos` so that, if ``y = cos(x)``, then ``x = arccos(y)``.

    Parameters
........................... acosh ...........................
Help on ufunc in module numpy:

arccosh = <ufunc 'arccosh'>
    arccosh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Inverse hyperbolic cosine, element-wise.

    Parameters
    ----------
    x : array_like
........................... add ...........................
Help on ufunc in module numpy:

add = <ufunc 'add'>
    add(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Add arguments element-wise.

    Parameters
    ----------
    x1, x2 : array_like
........................... all ...........................
Help on _ArrayFunctionDispatcher in module numpy:

all(a, axis=None, out=None, keepdims=<no value>, *, where=<no value>)
    Test whether all array elements along a given axis evaluate to True.

    Parameters
    ----------
    a : array_like
        Input array or object that can be converted to an array.
    axis : None or int or tuple of ints, optional
........................... allclose ...........................
Help on _ArrayFunctionDispatcher in module numpy:

allclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False)
    Returns True if two arrays are element-wise equal within a tolerance.

    The tolerance values are positive, typically very small numbers.  The
    relative difference (`rtol` * abs(`b`)) and the absolute difference
    `atol` are added together to compare against the absolute difference
    between `a` and `b`.

........................... amax ...........................
Help on _ArrayFunctionDispatcher in module numpy:

amax(
    a,
    axis=None,
    out=None,
    keepdims=<no value>,
    initial=<no value>,
    where=<no value>
)
........................... amin ...........................
Help on _ArrayFunctionDispatcher in module numpy:

amin(
    a,
    axis=None,
    out=None,
    keepdims=<no value>,
    initial=<no value>,
    where=<no value>
)
........................... angle ...........................
Help on _ArrayFunctionDispatcher in module numpy:

angle(z, deg=False)
    Return the angle of the complex argument.

    Parameters
    ----------
    z : array_like
        A complex number or sequence of complex numbers.
    deg : bool, optional
........................... any ...........................
Help on _ArrayFunctionDispatcher in module numpy:

any(a, axis=None, out=None, keepdims=<no value>, *, where=<no value>)
    Test whether any array element along a given axis evaluates to True.

    Returns single boolean if `axis` is ``None``

    Parameters
    ----------
    a : array_like
........................... append ...........................
Help on _ArrayFunctionDispatcher in module numpy:

append(arr, values, axis=None)
    Append values to the end of an array.

    Parameters
    ----------
    arr : array_like
        Values are appended to a copy of this array.
    values : array_like
........................... apply_along_axis ...........................
Help on _ArrayFunctionDispatcher in module numpy:

apply_along_axis(func1d, axis, arr, *args, **kwargs)
    Apply a function to 1-D slices along the given axis.

    Execute `func1d(a, *args, **kwargs)` where `func1d` operates on 1-D arrays
    and `a` is a 1-D slice of `arr` along `axis`.

    This is equivalent to (but faster than) the following use of `ndindex` and
    `s_`, which sets each of ``ii``, ``jj``, and ``kk`` to a tuple of indices::
........................... apply_over_axes ...........................
Help on _ArrayFunctionDispatcher in module numpy:

apply_over_axes(func, a, axes)
    Apply a function repeatedly over multiple axes.

    `func` is called as `res = func(a, axis)`, where `axis` is the first
    element of `axes`.  The result `res` of the function call must have
    either the same dimensions as `a` or one less dimension.  If `res`
    has one less dimension than `a`, a dimension is inserted before
    `axis`.  The call to `func` is then repeated for each axis in `axes`,
........................... arange ...........................
Help on built-in function arange in module numpy:

arange(...)
    arange([start,] stop[, step,], dtype=None, *, device=None, like=None)

    Return evenly spaced values within a given interval.

    ``arange`` can be called with a varying number of positional arguments:

    * ``arange(stop)``: Values are generated within the half-open interval
........................... arccos ...........................
Help on ufunc in module numpy:

arccos = <ufunc 'arccos'>
    arccos(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Trigonometric inverse cosine, element-wise.

    The inverse of `cos` so that, if ``y = cos(x)``, then ``x = arccos(y)``.

    Parameters
........................... arccosh ...........................
Help on ufunc in module numpy:

arccosh = <ufunc 'arccosh'>
    arccosh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Inverse hyperbolic cosine, element-wise.

    Parameters
    ----------
    x : array_like
........................... arcsin ...........................
Help on ufunc in module numpy:

arcsin = <ufunc 'arcsin'>
    arcsin(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Inverse sine, element-wise.

    Parameters
    ----------
    x : array_like
........................... arcsinh ...........................
Help on ufunc in module numpy:

arcsinh = <ufunc 'arcsinh'>
    arcsinh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Inverse hyperbolic sine element-wise.

    Parameters
    ----------
    x : array_like
........................... arctan ...........................
Help on ufunc in module numpy:

arctan = <ufunc 'arctan'>
    arctan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Trigonometric inverse tangent, element-wise.

    The inverse of tan, so that if ``y = tan(x)`` then ``x = arctan(y)``.

    Parameters
........................... arctan2 ...........................
Help on ufunc in module numpy:

arctan2 = <ufunc 'arctan2'>
    arctan2(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Element-wise arc tangent of ``x1/x2`` choosing the quadrant correctly.

    The quadrant (i.e., branch) is chosen so that ``arctan2(x1, x2)`` is
    the signed angle in radians between the ray ending at the origin and
    passing through the point (1,0), and the ray ending at the origin and
    ...... ...... ................
    `x1`   `x2`   `arctan2(x1,x2)`
    ====== ====== ================
    +/- 0  +0     +/- 0
    +/- 0  -0     +/- pi
     > 0   +/-inf +0 / +pi
     < 0   +/-inf -0 / -pi
    +/-inf +inf   +/- (pi/4)
    +/-inf -inf   +/- (3*pi/4)
    ====== ====== ================

........................... arctanh ...........................
Help on ufunc in module numpy:

arctanh = <ufunc 'arctanh'>
    arctanh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Inverse hyperbolic tangent element-wise.

    Parameters
    ----------
    x : array_like
........................... argmax ...........................
Help on _ArrayFunctionDispatcher in module numpy:

argmax(a, axis=None, out=None, *, keepdims=<no value>)
    Returns the indices of the maximum values along an axis.

    Parameters
    ----------
    a : array_like
        Input array.
    axis : int, optional
........................... argmin ...........................
Help on _ArrayFunctionDispatcher in module numpy:

argmin(a, axis=None, out=None, *, keepdims=<no value>)
    Returns the indices of the minimum values along an axis.

    Parameters
    ----------
    a : array_like
        Input array.
    axis : int, optional
........................... argpartition ...........................
Help on _ArrayFunctionDispatcher in module numpy:

argpartition(a, kth, axis=-1, kind='introselect', order=None)
    Perform an indirect partition along the given axis using the
    algorithm specified by the `kind` keyword. It returns an array of
    indices of the same shape as `a` that index data along the given
    axis in partitioned order.

    Parameters
    ----------
........................... argsort ...........................
Help on _ArrayFunctionDispatcher in module numpy:

argsort(a, axis=-1, kind=None, order=None, *, stable=None)
    Returns the indices that would sort an array.

    Perform an indirect sort along the given axis using the algorithm specified
    by the `kind` keyword. It returns an array of indices of the same shape as
    `a` that index data along the given axis in sorted order.

    Parameters
........................... argwhere ...........................
Help on _ArrayFunctionDispatcher in module numpy:

argwhere(a)
    Find the indices of array elements that are non-zero, grouped by element.

    Parameters
    ----------
    a : array_like
        Input data.

........................... around ...........................
Help on _ArrayFunctionDispatcher in module numpy:

around(a, decimals=0, out=None)
    Round an array to the given number of decimals.

    `around` is an alias of `~numpy.round`.

    See Also
    --------
    ndarray.round : equivalent method
........................... array ...........................
Help on built-in function array in module numpy:

array(...)
    array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0,
          like=None)

    Create an array.

    Parameters
    ----------
        ..... ......... ...................................................
        order  no copy                     copy=True
        ===== ========= ===================================================
        'K'   unchanged F & C order preserved, otherwise most similar order
        'A'   unchanged F order if input is F and not C, otherwise C order
        'C'   C order   C order
        'F'   F order   F order
        ===== ========= ===================================================

        When ``copy=None`` and a copy is made for other reasons, the result is
        the same as if ``copy=True``, with some exceptions for 'A', see the
........................... array2string ...........................
Help on _ArrayFunctionDispatcher in module numpy:

array2string(
    a,
    max_line_width=None,
    precision=None,
    suppress_small=None,
    separator=' ',
    prefix='',
    style=<no value>,
........................... array_equal ...........................
Help on _ArrayFunctionDispatcher in module numpy:

array_equal(a1, a2, equal_nan=False)
    True if two arrays have the same shape and elements, False otherwise.

    Parameters
    ----------
    a1, a2 : array_like
        Input arrays.
    equal_nan : bool
........................... array_equiv ...........................
Help on _ArrayFunctionDispatcher in module numpy:

array_equiv(a1, a2)
    Returns True if input arrays are shape consistent and all elements equal.

    Shape consistent means they are either the same shape, or one input array
    can be broadcasted to create the same shape as the other one.

    Parameters
    ----------
........................... array_repr ...........................
Help on _ArrayFunctionDispatcher in module numpy:

array_repr(arr, max_line_width=None, precision=None, suppress_small=None)
    Return the string representation of an array.

    Parameters
    ----------
    arr : ndarray
        Input array.
    max_line_width : int, optional
........................... array_split ...........................
Help on _ArrayFunctionDispatcher in module numpy:

array_split(ary, indices_or_sections, axis=0)
    Split an array into multiple sub-arrays.

    Please refer to the ``split`` documentation.  The only difference
    between these functions is that ``array_split`` allows
    `indices_or_sections` to be an integer that does *not* equally
    divide the axis. For an array of length l that should be split
    into n sections, it returns l % n sub-arrays of size l//n + 1
........................... array_str ...........................
Help on _ArrayFunctionDispatcher in module numpy:

array_str(a, max_line_width=None, precision=None, suppress_small=None)
    Return a string representation of the data in an array.

    The data in the array is returned as a single string.  This function is
    similar to `array_repr`, the difference being that `array_repr` also
    returns information on the kind of array and its data type.

    Parameters
........................... asanyarray ...........................
Help on built-in function asanyarray in module numpy:

asanyarray(...)
    asanyarray(a, dtype=None, order=None, *, device=None, copy=None, like=None)

    Convert the input to an ndarray, but pass ndarray subclasses through.

    Parameters
    ----------
    a : array_like
........................... asarray ...........................
Help on built-in function asarray in module numpy:

asarray(...)
    asarray(a, dtype=None, order=None, *, device=None, copy=None, like=None)

    Convert the input to an array.

    Parameters
    ----------
    a : array_like
........................... asarray_chkfinite ...........................
Help on function asarray_chkfinite in module numpy:

asarray_chkfinite(a, dtype=None, order=None)
    Convert the input to an array, checking for NaNs or Infs.

    Parameters
    ----------
    a : array_like
        Input data, in any form that can be converted to an array.  This
        includes lists, lists of tuples, tuples, tuples of tuples, tuples
........................... ascontiguousarray ...........................
Help on built-in function ascontiguousarray in module numpy:

ascontiguousarray(...)
    ascontiguousarray(a, dtype=None, *, like=None)

    Return a contiguous array (ndim >= 1) in memory (C order).

    Parameters
    ----------
    a : array_like
........................... asfortranarray ...........................
Help on built-in function asfortranarray in module numpy:

asfortranarray(...)
    asfortranarray(a, dtype=None, *, like=None)

    Return an array (ndim >= 1) laid out in Fortran order in memory.

    Parameters
    ----------
    a : array_like
........................... asin ...........................
Help on ufunc in module numpy:

arcsin = <ufunc 'arcsin'>
    arcsin(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Inverse sine, element-wise.

    Parameters
    ----------
    x : array_like
........................... asinh ...........................
Help on ufunc in module numpy:

arcsinh = <ufunc 'arcsinh'>
    arcsinh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Inverse hyperbolic sine element-wise.

    Parameters
    ----------
    x : array_like
........................... asmatrix ...........................
Help on function asmatrix in module numpy:

asmatrix(data, dtype=None)
    Interpret the input as a matrix.

    Unlike `matrix`, `asmatrix` does not make a copy if the input is already
    a matrix or an ndarray.  Equivalent to ``matrix(data, copy=False)``.

    Parameters
    ----------
........................... astype ...........................
Help on _ArrayFunctionDispatcher in module numpy:

astype(x, dtype, /, *, copy=True, device=None)
    Copies an array to a specified data type.

    This function is an Array API compatible alternative to
    `numpy.ndarray.astype`.

    Parameters
    ----------
........................... atan ...........................
Help on ufunc in module numpy:

arctan = <ufunc 'arctan'>
    arctan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Trigonometric inverse tangent, element-wise.

    The inverse of tan, so that if ``y = tan(x)`` then ``x = arctan(y)``.

    Parameters
........................... atan2 ...........................
Help on ufunc in module numpy:

arctan2 = <ufunc 'arctan2'>
    arctan2(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Element-wise arc tangent of ``x1/x2`` choosing the quadrant correctly.

    The quadrant (i.e., branch) is chosen so that ``arctan2(x1, x2)`` is
    the signed angle in radians between the ray ending at the origin and
    passing through the point (1,0), and the ray ending at the origin and
    ...... ...... ................
    `x1`   `x2`   `arctan2(x1,x2)`
    ====== ====== ================
    +/- 0  +0     +/- 0
    +/- 0  -0     +/- pi
     > 0   +/-inf +0 / +pi
     < 0   +/-inf -0 / -pi
    +/-inf +inf   +/- (pi/4)
    +/-inf -inf   +/- (3*pi/4)
    ====== ====== ================

........................... atanh ...........................
Help on ufunc in module numpy:

arctanh = <ufunc 'arctanh'>
    arctanh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Inverse hyperbolic tangent element-wise.

    Parameters
    ----------
    x : array_like
........................... atleast_1d ...........................
Help on _ArrayFunctionDispatcher in module numpy:

atleast_1d(*arys)
    Convert inputs to arrays with at least one dimension.

    Scalar inputs are converted to 1-dimensional arrays, whilst
    higher-dimensional inputs are preserved.

    Parameters
    ----------
........................... atleast_2d ...........................
Help on _ArrayFunctionDispatcher in module numpy:

atleast_2d(*arys)
    View inputs as arrays with at least two dimensions.

    Parameters
    ----------
    arys1, arys2, ... : array_like
        One or more array-like sequences.  Non-array inputs are converted
        to arrays.  Arrays that already have two or more dimensions are
........................... atleast_3d ...........................
Help on _ArrayFunctionDispatcher in module numpy:

atleast_3d(*arys)
    View inputs as arrays with at least three dimensions.

    Parameters
    ----------
    arys1, arys2, ... : array_like
        One or more array-like sequences.  Non-array inputs are converted to
        arrays.  Arrays that already have three or more dimensions are
........................... average ...........................
Help on _ArrayFunctionDispatcher in module numpy:

average(a, axis=None, weights=None, returned=False, *, keepdims=<no value>)
    Compute the weighted average along the specified axis.

    Parameters
    ----------
    a : array_like
        Array containing data to be averaged. If `a` is not an array, a
        conversion is attempted.
........................... bartlett ...........................
Help on function bartlett in module numpy:

bartlett(M)
    Return the Bartlett window.

    The Bartlett window is very similar to a triangular window, except
    that the end points are at zero.  It is often used in signal
    processing for tapering a signal, without generating too much
    ripple in the frequency domain.

........................... base_repr ...........................
Help on function base_repr in module numpy:

base_repr(number, base=2, padding=0)
    Return a string representation of a number in the given base system.

    Parameters
    ----------
    number : int
        The value to convert. Positive and negative values are handled.
    base : int, optional
........................... binary_repr ...........................
Help on function binary_repr in module numpy:

binary_repr(num, width=None)
    Return the binary representation of the input number as a string.

    For negative numbers, if width is not given, a minus sign is added to the
    front. If width is given, the two's complement of the number is
    returned, with respect to that width.

    In a two's-complement system negative numbers are represented by the two's
........................... bincount ...........................
Help on _ArrayFunctionDispatcher in module numpy:

bincount(...)
    bincount(x, /, weights=None, minlength=0)

    Count number of occurrences of each value in array of non-negative ints.

    The number of bins (of size 1) is one larger than the largest value in
    `x`. If `minlength` is specified, there will be at least this number
    of bins in the output array (though it will be longer if necessary,
........................... bitwise_and ...........................
Help on ufunc in module numpy:

bitwise_and = <ufunc 'bitwise_and'>
    bitwise_and(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Compute the bit-wise AND of two arrays element-wise.

    Computes the bit-wise AND of the underlying binary representation of
    the integers in the input arrays. This ufunc implements the C/Python
    operator ``&``.
........................... bitwise_count ...........................
Help on ufunc in module numpy:

bitwise_count = <ufunc 'bitwise_count'>
    bitwise_count(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Computes the number of 1-bits in the absolute value of ``x``.
    Analogous to the builtin `int.bit_count` or ``popcount`` in C++.

    Parameters
    ----------
........................... bitwise_invert ...........................
Help on ufunc in module numpy:

invert = <ufunc 'invert'>
    invert(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Compute bit-wise inversion, or bit-wise NOT, element-wise.

    Computes the bit-wise NOT of the underlying binary representation of
    the integers in the input arrays. This ufunc implements the C/Python
    operator ``~``.
........................... bitwise_left_shift ...........................
Help on ufunc in module numpy:

left_shift = <ufunc 'left_shift'>
    left_shift(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Shift the bits of an integer to the left.

    Bits are shifted to the left by appending `x2` 0s at the right of `x1`.
    Since the internal representation of numbers is in binary format, this
    operation is equivalent to multiplying `x1` by ``2**x2``.
........................... bitwise_not ...........................
Help on ufunc in module numpy:

invert = <ufunc 'invert'>
    invert(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Compute bit-wise inversion, or bit-wise NOT, element-wise.

    Computes the bit-wise NOT of the underlying binary representation of
    the integers in the input arrays. This ufunc implements the C/Python
    operator ``~``.
........................... bitwise_or ...........................
Help on ufunc in module numpy:

bitwise_or = <ufunc 'bitwise_or'>
    bitwise_or(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Compute the bit-wise OR of two arrays element-wise.

    Computes the bit-wise OR of the underlying binary representation of
    the integers in the input arrays. This ufunc implements the C/Python
    operator ``|``.
........................... bitwise_right_shift ...........................
Help on ufunc in module numpy:

right_shift = <ufunc 'right_shift'>
    right_shift(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Shift the bits of an integer to the right.

    Bits are shifted to the right `x2`.  Because the internal
    representation of numbers is in binary format, this operation is
    equivalent to dividing `x1` by ``2**x2``.
........................... bitwise_xor ...........................
Help on ufunc in module numpy:

bitwise_xor = <ufunc 'bitwise_xor'>
    bitwise_xor(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Compute the bit-wise XOR of two arrays element-wise.

    Computes the bit-wise XOR of the underlying binary representation of
    the integers in the input arrays. This ufunc implements the C/Python
    operator ``^``.
........................... blackman ...........................
Help on function blackman in module numpy:

blackman(M)
    Return the Blackman window.

    The Blackman window is a taper formed by using the first three
    terms of a summation of cosines. It was designed to have close to the
    minimal leakage possible.  It is close to optimal, only slightly worse
    than a Kaiser window.

........................... block ...........................
Help on _ArrayFunctionDispatcher in module numpy:

block(arrays)
    Assemble an nd-array from nested lists of blocks.

    Blocks in the innermost lists are concatenated (see `concatenate`) along
    the last dimension (-1), then these are concatenated along the
    second-last dimension (-2), and so on until the outermost list is reached.

    Blocks can be of any dimension, but will not be broadcasted using
........................... bmat ...........................
Help on function bmat in module numpy:

bmat(obj, ldict=None, gdict=None)
    Build a matrix object from a string, nested sequence, or array.

    Parameters
    ----------
    obj : str or array_like
        Input data. If a string, variables in the current scope may be
        referenced by name.
........................... bool ...........................
Help on class bool in module numpy:

class bool(generic)
 |  Boolean type (True or False), stored as a byte.
 |
 |  .. warning::
 |
 |     The :class:`bool` type is not a subclass of the :class:`int_` type
 |     (the :class:`bool` is not even a number type). This is different
 |     than Python's default implementation of :class:`bool` as a
........................... bool_ ...........................
Help on class bool in module numpy:

class bool(generic)
 |  Boolean type (True or False), stored as a byte.
 |
 |  .. warning::
 |
 |     The :class:`bool` type is not a subclass of the :class:`int_` type
 |     (the :class:`bool` is not even a number type). This is different
 |     than Python's default implementation of :class:`bool` as a
........................... broadcast ...........................
Help on class broadcast in module numpy:

class broadcast(builtins.object)
 |  Produce an object that mimics broadcasting.
 |
 |  Parameters
 |  ----------
 |  in1, in2, ... : array_like
 |      Input parameters.
 |
........................... broadcast_arrays ...........................
Help on _ArrayFunctionDispatcher in module numpy:

broadcast_arrays(*args, subok=False)
    Broadcast any number of arrays against each other.

    Parameters
    ----------
    *args : array_likes
        The arrays to broadcast.

........................... broadcast_shapes ...........................
Help on function broadcast_shapes in module numpy:

broadcast_shapes(*args)
    Broadcast the input shapes into a single shape.

    :ref:`Learn more about broadcasting here <basics.broadcasting>`.

    .. versionadded:: 1.20.0

    Parameters
........................... broadcast_to ...........................
Help on _ArrayFunctionDispatcher in module numpy:

broadcast_to(array, shape, subok=False)
    Broadcast an array to a new shape.

    Parameters
    ----------
    array : array_like
        The array to broadcast.
    shape : tuple or int
........................... busday_count ...........................
Help on _ArrayFunctionDispatcher in module numpy:

busday_count(...)
    busday_count(
        begindates,
        enddates,
        weekmask='1111100',
        holidays=[],
        busdaycal=None,
        out=None
........................... busday_offset ...........................
Help on _ArrayFunctionDispatcher in module numpy:

busday_offset(...)
    busday_offset(
        dates,
        offsets,
        roll='raise',
        weekmask='1111100',
        holidays=None,
        busdaycal=None,
........................... busdaycalendar ...........................
Help on class busdaycalendar in module numpy:

class busdaycalendar(builtins.object)
 |  busdaycalendar(weekmask='1111100', holidays=None)
 |
 |  A business day calendar object that efficiently stores information
 |  defining valid days for the busday family of functions.
 |
 |  The default valid days are Monday through Friday ("business days").
 |  A busdaycalendar object can be specified with any set of weekly
........................... byte ...........................
Help on class int8 in module numpy:

class int8(signedinteger)
 |  Signed integer type, compatible with C ``char``.
 |
 |  :Character code: ``'b'``
 |  :Canonical name: `numpy.byte`
 |  :Alias on this platform (Linux x86_64): `numpy.int8`: 8-bit signed integer (``-128`` to ``127``).
 |
 |  Method resolution order:
........................... bytes_ ...........................
Help on class bytes_ in module numpy:

class bytes_(builtins.bytes, character)
 |  A byte string.
 |
 |  When used in arrays, this type strips trailing null bytes.
 |
 |  :Character code: ``'S'``
 |
 |  Method resolution order:
........................... c_ ...........................
Help on CClass in module numpy.lib._index_tricks_impl object:

class CClass(AxisConcatenator)
 |  Translates slice objects to concatenation along the second axis.
 |
 |  This is short-hand for ``np.r_['-1,2,0', index expression]``, which is
 |  useful because of its common occurrence. In particular, arrays will be
 |  stacked along their last axis after being upgraded to at least 2-D with
 |  1's post-pended to the shape (column vectors made out of 1-D arrays).
 |
........................... can_cast ...........................
Help on _ArrayFunctionDispatcher in module numpy:

can_cast(...)
    can_cast(from_, to, casting='safe')

    Returns True if cast between data types can occur according to the
    casting rule.

    Parameters
    ----------
........................... cbrt ...........................
Help on ufunc in module numpy:

cbrt = <ufunc 'cbrt'>
    cbrt(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Return the cube-root of an array, element-wise.

    Parameters
    ----------
    x : array_like
........................... cdouble ...........................
Help on class complex128 in module numpy:

class complex128(complexfloating, builtins.complex)
 |  complex128(real=0, imag=0)
 |
 |  Complex number type composed of two double-precision floating-point
 |  numbers, compatible with Python :class:`complex`.
 |
 |  :Character code: ``'D'``
 |  :Canonical name: `numpy.cdouble`
........................... ceil ...........................
Help on ufunc in module numpy:

ceil = <ufunc 'ceil'>
    ceil(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Return the ceiling of the input, element-wise.

    The ceil of the scalar `x` is the smallest integer `i`, such that
    ``i >= x``.  It is often denoted as :math:`\lceil x \rceil`.

........................... char ...........................
Help on package numpy.char in numpy:

NAME
    numpy.char

DESCRIPTION
    This module contains a set of functions for vectorized string
    operations and methods.

    .. note::
........................... character ...........................
Help on class character in module numpy:

class character(flexible)
 |  Abstract base class of all character string scalar types.
 |
 |  Method resolution order:
 |      character
 |      flexible
 |      generic
 |      builtins.object
........................... choose ...........................
Help on _ArrayFunctionDispatcher in module numpy:

choose(a, choices, out=None, mode='raise')
    Construct an array from an index array and a list of arrays to choose from.

    First of all, if confused or uncertain, definitely look at the Examples -
    in its full generality, this function is less simple than it might
    seem from the following code description::

        np.choose(a,c) == np.array([c[a[I]][I] for I in np.ndindex(a.shape)])
........................... clip ...........................
Help on _ArrayFunctionDispatcher in module numpy:

clip(
    a,
    a_min=<no value>,
    a_max=<no value>,
    out=None,
    *,
    min=<no value>,
    max=<no value>,
........................... clongdouble ...........................
Help on class clongdouble in module numpy:

class clongdouble(complexfloating)
 |  Complex number type composed of two extended-precision floating-point
 |  numbers.
 |
 |  :Character code: ``'G'``
 |  :Alias on this platform (Linux x86_64): `numpy.complex256`: Complex number type composed of 2 128-bit extended-precision floating-point numbers.
 |
 |  Method resolution order:
........................... column_stack ...........................
Help on _ArrayFunctionDispatcher in module numpy:

column_stack(tup)
    Stack 1-D arrays as columns into a 2-D array.

    Take a sequence of 1-D arrays and stack them as columns
    to make a single 2-D array. 2-D arrays are stacked as-is,
    just like with `hstack`.  1-D arrays are turned into 2-D columns
    first.

........................... common_type ...........................
Help on _ArrayFunctionDispatcher in module numpy:

common_type(*arrays)
    Return a scalar type which is common to the input arrays.

    The return type will always be an inexact (i.e. floating point) scalar
    type, even if all the arrays are integer arrays. If one of the inputs is
    an integer array, the minimum precision type that is returned is a
    64-bit floating point dtype.

........................... complex128 ...........................
Help on class complex128 in module numpy:

class complex128(complexfloating, builtins.complex)
 |  complex128(real=0, imag=0)
 |
 |  Complex number type composed of two double-precision floating-point
 |  numbers, compatible with Python :class:`complex`.
 |
 |  :Character code: ``'D'``
 |  :Canonical name: `numpy.cdouble`
........................... complex256 ...........................
Help on class clongdouble in module numpy:

class clongdouble(complexfloating)
 |  Complex number type composed of two extended-precision floating-point
 |  numbers.
 |
 |  :Character code: ``'G'``
 |  :Alias on this platform (Linux x86_64): `numpy.complex256`: Complex number type composed of 2 128-bit extended-precision floating-point numbers.
 |
 |  Method resolution order:
........................... complex64 ...........................
Help on class complex64 in module numpy:

class complex64(complexfloating)
 |  Complex number type composed of two single-precision floating-point
 |  numbers.
 |
 |  :Character code: ``'F'``
 |  :Canonical name: `numpy.csingle`
 |  :Alias on this platform (Linux x86_64): `numpy.complex64`: Complex number type composed of 2 32-bit-precision floating-point numbers.
 |
........................... complexfloating ...........................
Help on class complexfloating in module numpy:

class complexfloating(inexact)
 |  Abstract base class of all complex number scalar types that are made up of
 |  floating-point numbers.
 |
 |  Method resolution order:
 |      complexfloating
 |      inexact
 |      number
........................... compress ...........................
Help on _ArrayFunctionDispatcher in module numpy:

compress(condition, a, axis=None, out=None)
    Return selected slices of an array along given axis.

    When working along a given axis, a slice along that axis is returned in
    `output` for each index where `condition` evaluates to True. When
    working on a 1-D array, `compress` is equivalent to `extract`.

    Parameters
........................... concat ...........................
Help on _ArrayFunctionDispatcher in module numpy:

concatenate(...)
    concatenate(
        (a1, a2, ...),
        axis=0,
        out=None,
        dtype=None,
        casting="same_kind"
    )
........................... concatenate ...........................
Help on _ArrayFunctionDispatcher in module numpy:

concatenate(...)
    concatenate(
        (a1, a2, ...),
        axis=0,
        out=None,
        dtype=None,
        casting="same_kind"
    )
........................... conj ...........................
Help on ufunc in module numpy:

conjugate = <ufunc 'conjugate'>
    conjugate(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Return the complex conjugate, element-wise.

    The complex conjugate of a complex number is obtained by changing the
    sign of its imaginary part.

........................... conjugate ...........................
Help on ufunc in module numpy:

conjugate = <ufunc 'conjugate'>
    conjugate(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Return the complex conjugate, element-wise.

    The complex conjugate of a complex number is obtained by changing the
    sign of its imaginary part.

........................... convolve ...........................
Help on _ArrayFunctionDispatcher in module numpy:

convolve(a, v, mode='full')
    Returns the discrete, linear convolution of two one-dimensional sequences.

    The convolution operator is often seen in signal processing, where it
    models the effect of a linear time-invariant system on a signal [1]_.  In
    probability theory, the sum of two independent random variables is
    distributed according to the convolution of their individual
    distributions.
........................... copy ...........................
Help on _ArrayFunctionDispatcher in module numpy:

copy(a, order='K', subok=False)
    Return an array copy of the given object.

    Parameters
    ----------
    a : array_like
        Input data.
    order : {'C', 'F', 'A', 'K'}, optional
........................... copysign ...........................
Help on ufunc in module numpy:

copysign = <ufunc 'copysign'>
    copysign(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Change the sign of x1 to that of x2, element-wise.

    If `x2` is a scalar, its sign will be copied to all elements of `x1`.

    Parameters
........................... copyto ...........................
Help on _ArrayFunctionDispatcher in module numpy:

copyto(...)
    copyto(dst, src, casting='same_kind', where=True)

    Copies values from one array to another, broadcasting as necessary.

    Raises a TypeError if the `casting` rule is violated, and if
    `where` is provided, it selects which elements to copy.

........................... core ...........................
Help on package numpy.core in numpy:

NAME
    numpy.core

DESCRIPTION
    The `numpy.core` submodule exists solely for backward compatibility
    purposes. The original `core` was renamed to `_core` and made private.
    `numpy.core` will be removed in the future.

........................... corrcoef ...........................
Help on _ArrayFunctionDispatcher in module numpy:

corrcoef(
    x,
    y=None,
    rowvar=True,
    bias=<no value>,
    ddof=<no value>,
    *,
    dtype=None
........................... correlate ...........................
Help on _ArrayFunctionDispatcher in module numpy:

correlate(a, v, mode='valid')
    Cross-correlation of two 1-dimensional sequences.

    This function computes the correlation as generally defined in signal
    processing texts [1]_:

    .. math:: c_k = \sum_n a_{n+k} \cdot \overline{v}_n

........................... cos ...........................
Help on ufunc in module numpy:

cos = <ufunc 'cos'>
    cos(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Cosine element-wise.

    Parameters
    ----------
    x : array_like
........................... cosh ...........................
Help on ufunc in module numpy:

cosh = <ufunc 'cosh'>
    cosh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Hyperbolic cosine, element-wise.

    Equivalent to ``1/2 * (np.exp(x) + np.exp(-x))`` and ``np.cos(1j*x)``.

    Parameters
........................... count_nonzero ...........................
Help on _ArrayFunctionDispatcher in module numpy:

count_nonzero(a, axis=None, *, keepdims=False)
    Counts the number of non-zero values in the array ``a``.

    The word "non-zero" is in reference to the Python 2.x
    built-in method ``__nonzero__()`` (renamed ``__bool__()``
    in Python 3.x) of Python objects that tests an object's
    "truthfulness". For example, any number is considered
    truthful if it is nonzero, whereas any string is considered
........................... cov ...........................
Help on _ArrayFunctionDispatcher in module numpy:

cov(
    m,
    y=None,
    rowvar=True,
    bias=False,
    ddof=None,
    fweights=None,
    aweights=None,
........................... cross ...........................
Help on _ArrayFunctionDispatcher in module numpy:

cross(a, b, axisa=-1, axisb=-1, axisc=-1, axis=None)
    Return the cross product of two (arrays of) vectors.

    The cross product of `a` and `b` in :math:`R^3` is a vector perpendicular
    to both `a` and `b`.  If `a` and `b` are arrays of vectors, the vectors
    are defined by the last axis of `a` and `b` by default, and these axes
    can have dimensions 2 or 3.  Where the dimension of either `a` or `b` is
    2, the third component of the input vector is assumed to be zero and the
........................... csingle ...........................
Help on class complex64 in module numpy:

class complex64(complexfloating)
 |  Complex number type composed of two single-precision floating-point
 |  numbers.
 |
 |  :Character code: ``'F'``
 |  :Canonical name: `numpy.csingle`
 |  :Alias on this platform (Linux x86_64): `numpy.complex64`: Complex number type composed of 2 32-bit-precision floating-point numbers.
 |
........................... ctypeslib ...........................
Help on module numpy.ctypeslib in numpy:

NAME
    numpy.ctypeslib

DESCRIPTION
    ============================
    ``ctypes`` Utility Functions
    ============================

........................... cumprod ...........................
Help on _ArrayFunctionDispatcher in module numpy:

cumprod(a, axis=None, dtype=None, out=None)
    Return the cumulative product of elements along a given axis.

    Parameters
    ----------
    a : array_like
        Input array.
    axis : int, optional
........................... cumsum ...........................
Help on _ArrayFunctionDispatcher in module numpy:

cumsum(a, axis=None, dtype=None, out=None)
    Return the cumulative sum of the elements along a given axis.

    Parameters
    ----------
    a : array_like
        Input array.
    axis : int, optional
........................... cumulative_prod ...........................
Help on _ArrayFunctionDispatcher in module numpy:

cumulative_prod(x, /, *, axis=None, dtype=None, out=None, include_initial=False)
    Return the cumulative product of elements along a given axis.

    This function is an Array API compatible alternative to `numpy.cumprod`.

    Parameters
    ----------
    x : array_like
........................... cumulative_sum ...........................
Help on _ArrayFunctionDispatcher in module numpy:

cumulative_sum(x, /, *, axis=None, dtype=None, out=None, include_initial=False)
    Return the cumulative sum of the elements along a given axis.

    This function is an Array API compatible alternative to `numpy.cumsum`.

    Parameters
    ----------
    x : array_like
........................... datetime64 ...........................
Help on class datetime64 in module numpy:

class datetime64(generic)
 |  If created from a 64-bit integer, it represents an offset from
 |  ``1970-01-01T00:00:00``.
 |  If created from string, the string can be in ISO 8601 date
 |  or datetime format.
 |
 |  When parsing a string to create a datetime object, if the string contains
 |  a trailing timezone (A 'Z' or a timezone offset), the timezone will be
........................... datetime_as_string ...........................
Help on _ArrayFunctionDispatcher in module numpy:

datetime_as_string(...)
    datetime_as_string(arr, unit=None, timezone='naive', casting='same_kind')

    Convert an array of datetimes into an array of strings.

    Parameters
    ----------
    arr : array_like of datetime64
........................... datetime_data ...........................
Help on built-in function datetime_data in module numpy:

datetime_data(...)
    datetime_data(dtype, /)

    Get information about the step size of a date or time type.

    The returned tuple can be passed as the second argument of `numpy.datetime64` and
    `numpy.timedelta64`.

........................... deg2rad ...........................
Help on ufunc in module numpy:

deg2rad = <ufunc 'deg2rad'>
    deg2rad(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Convert angles from degrees to radians.

    Parameters
    ----------
    x : array_like
........................... degrees ...........................
Help on ufunc in module numpy:

degrees = <ufunc 'degrees'>
    degrees(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Convert angles from radians to degrees.

    Parameters
    ----------
    x : array_like
........................... delete ...........................
Help on _ArrayFunctionDispatcher in module numpy:

delete(arr, obj, axis=None)
    Return a new array with sub-arrays along an axis deleted. For a one
    dimensional array, this returns those entries not returned by
    `arr[obj]`.

    Parameters
    ----------
    arr : array_like
........................... diag ...........................
Help on _ArrayFunctionDispatcher in module numpy:

diag(v, k=0)
    Extract a diagonal or construct a diagonal array.

    See the more detailed documentation for ``numpy.diagonal`` if you use this
    function to extract a diagonal and wish to write to the resulting array;
    whether it returns a copy or a view depends on what version of numpy you
    are using.

........................... diag_indices ...........................
Help on function diag_indices in module numpy:

diag_indices(n, ndim=2)
    Return the indices to access the main diagonal of an array.

    This returns a tuple of indices that can be used to access the main
    diagonal of an array `a` with ``a.ndim >= 2`` dimensions and shape
    (n, n, ..., n). For ``a.ndim = 2`` this is the usual diagonal, for
    ``a.ndim > 2`` this is the set of indices to access ``a[i, i, ..., i]``
    for ``i = [0..n-1]``.
........................... diag_indices_from ...........................
Help on _ArrayFunctionDispatcher in module numpy:

diag_indices_from(arr)
    Return the indices to access the main diagonal of an n-dimensional array.

    See `diag_indices` for full details.

    Parameters
    ----------
    arr : array, at least 2-D
........................... diagflat ...........................
Help on _ArrayFunctionDispatcher in module numpy:

diagflat(v, k=0)
    Create a two-dimensional array with the flattened input as a diagonal.

    Parameters
    ----------
    v : array_like
        Input data, which is flattened and set as the `k`-th
        diagonal of the output.
........................... diagonal ...........................
Help on _ArrayFunctionDispatcher in module numpy:

diagonal(a, offset=0, axis1=0, axis2=1)
    Return specified diagonals.

    If `a` is 2-D, returns the diagonal of `a` with the given offset,
    i.e., the collection of elements of the form ``a[i, i+offset]``.  If
    `a` has more than two dimensions, then the axes specified by `axis1`
    and `axis2` are used to determine the 2-D sub-array whose diagonal is
    returned.  The shape of the resulting array can be determined by
........................... diff ...........................
Help on _ArrayFunctionDispatcher in module numpy:

diff(a, n=1, axis=-1, prepend=<no value>, append=<no value>)
    Calculate the n-th discrete difference along the given axis.

    The first difference is given by ``out[i] = a[i+1] - a[i]`` along
    the given axis, higher differences are calculated by using `diff`
    recursively.

    Parameters
........................... digitize ...........................
Help on _ArrayFunctionDispatcher in module numpy:

digitize(x, bins, right=False)
    Return the indices of the bins to which each value in input array belongs.

    =========  =============  ============================
    `right`    order of bins  returned index `i` satisfies
    =========  =============  ============================
    ``False``  increasing     ``bins[i-1] <= x < bins[i]``
    ``True``   increasing     ``bins[i-1] < x <= bins[i]``
    .........  .............  ............................

    If values in `x` are beyond the bounds of `bins`, 0 or ``len(bins)`` is
    returned as appropriate.

    Parameters
    ----------
    x : array_like
        Input array to be binned. Prior to NumPy 1.10.0, this array had to
        be 1-dimensional, but can now have any shape.
    bins : array_like
........................... divide ...........................
Help on ufunc in module numpy:

divide = <ufunc 'divide'>
    divide(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Divide arguments element-wise.

    Parameters
    ----------
    x1 : array_like
........................... divmod ...........................
Help on ufunc in module numpy:

divmod = <ufunc 'divmod'>
    divmod(x1, x2[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Return element-wise quotient and remainder simultaneously.

    ``np.divmod(x, y)`` is equivalent to ``(x // y, x % y)``, but faster
    because it avoids redundant work. It is used to implement the Python
    built-in function ``divmod`` on NumPy arrays.
........................... dot ...........................
Help on _ArrayFunctionDispatcher in module numpy:

dot(...)
    dot(a, b, out=None)

    Dot product of two arrays. Specifically,

    - If both `a` and `b` are 1-D arrays, it is inner product of vectors
      (without complex conjugation).

........................... double ...........................
Help on class float64 in module numpy:

class float64(floating, builtins.float)
 |  float64(x=0, /)
 |
 |  Double-precision floating-point number type, compatible with Python
 |  :class:`float` and C ``double``.
 |
 |  :Character code: ``'d'``
 |  :Canonical name: `numpy.double`
........................... dsplit ...........................
Help on _ArrayFunctionDispatcher in module numpy:

dsplit(ary, indices_or_sections)
    Split array into multiple sub-arrays along the 3rd axis (depth).

    Please refer to the `split` documentation.  `dsplit` is equivalent
    to `split` with ``axis=2``, the array is always split along the third
    axis provided the array dimension is greater than or equal to 3.

    See Also
........................... dstack ...........................
Help on _ArrayFunctionDispatcher in module numpy:

dstack(tup)
    Stack arrays in sequence depth wise (along third axis).

    This is equivalent to concatenation along the third axis after 2-D arrays
    of shape `(M,N)` have been reshaped to `(M,N,1)` and 1-D arrays of shape
    `(N,)` have been reshaped to `(1,N,1)`. Rebuilds arrays divided by
    `dsplit`.

........................... dtype ...........................
Help on class dtype in module numpy:

class dtype(builtins.object)
 |  dtype(dtype, align=False, copy=False, [metadata])
 |
 |  Create a data type object.
 |
 |  A numpy array is homogeneous, and contains elements described by a
 |  dtype object. A dtype object can be constructed from different
 |  combinations of fundamental numeric types.
 |      .  ........................................................................
 |      0  if this is a structured array type, with fields
 |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
 |      2  if the dtype is for a user-defined numpy type
 |         A user-defined type uses the numpy C-API machinery to extend
 |         numpy to handle a new array type. See
 |         :ref:`user.user-defined-data-types` in the NumPy manual.
 |      =  ========================================================================
 |
 |      Examples
 |      --------
 |      .  ......................
 |      b  boolean
 |      i  signed integer
 |      u  unsigned integer
 |      f  floating-point
 |      c  complex floating-point
 |      m  timedelta
 |      M  datetime
 |      O  object
 |      S  (byte-)string
 |      U  Unicode
 |      .  ......................
 |
 |      Examples
 |      --------
 |
 |      >>> import numpy as np
 |      >>> dt = np.dtype('i4')
 |      >>> dt.kind
 |      'i'
 |      >>> dt = np.dtype('f8')
 |      >>> dt.kind
........................... dtypes ...........................
Help on module numpy.dtypes in numpy:

NAME
    numpy.dtypes

DESCRIPTION
    This module is home to specific dtypes related functionality and their classes.
    For more general information about dtypes, also see `numpy.dtype` and
    :ref:`arrays.dtypes`.

     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
     |      .  ........................................................................
     |      0  if this is a structured array type, with fields
     |      1  if this is a dtype compiled into numpy (such as ints, floats etc)
     |      2  if the dtype is for a user-defined numpy type
     |         A user-defined type uses the numpy C-API machinery to extend
     |         numpy to handle a new array type. See
     |         :ref:`user.user-defined-data-types` in the NumPy manual.
     |      =  ========================================================================
     |
     |      Examples
     |      --------
     |      .  ......................
     |      b  boolean
     |      i  signed integer
     |      u  unsigned integer
     |      f  floating-point
     |      c  complex floating-point
     |      m  timedelta
     |      M  datetime
     |      O  object
     |      S  (byte-)string
     |      U  Unicode
     |      .  ......................
     |
     |      Examples
     |      --------
     |
     |      >>> import numpy as np
     |      >>> dt = np.dtype('i4')
     |      >>> dt.kind
     |      'i'
     |      >>> dt = np.dtype('f8')
     |      >>> dt.kind
........................... e ...........................
Help on float object:

class float(object)
 |  float(x=0, /)
 |
 |  Convert a string or number to a floating-point number, if possible.
 |
 |  Methods defined here:
 |
 |  __abs__(self, /)
........................... ediff1d ...........................
Help on _ArrayFunctionDispatcher in module numpy:

ediff1d(ary, to_end=None, to_begin=None)
    The differences between consecutive elements of an array.

    Parameters
    ----------
    ary : array_like
        If necessary, will be flattened before the differences are taken.
    to_end : array_like, optional
........................... einsum ...........................
Help on _ArrayFunctionDispatcher in module numpy:

einsum(*operands, out=None, optimize=False, **kwargs)
    einsum(subscripts, *operands, out=None, dtype=None, order='K',
           casting='safe', optimize=False)

    Evaluates the Einstein summation convention on the operands.

    Using the Einstein summation convention, many common multi-dimensional,
    linear algebraic array operations can be represented in a simple fashion.
........................... einsum_path ...........................
Help on _ArrayFunctionDispatcher in module numpy:

einsum_path(*operands, optimize='greedy', einsum_call=False)
    einsum_path(subscripts, *operands, optimize='greedy')

    Evaluates the lowest cost contraction order for an einsum expression by
    considering the creation of intermediate arrays.

    Parameters
    ----------
........................... emath ...........................
Help on module numpy.lib.scimath in numpy.lib:

NAME
    numpy.lib.scimath

DESCRIPTION
    Wrapper functions to more user-friendly calling of certain math functions
    whose output data-type is different than the input data-type in certain
    domains of the input.

........................... empty ...........................
Help on built-in function empty in module numpy:

empty(...)
    empty(shape, dtype=float, order='C', *, device=None, like=None)

    Return a new array of given shape and type, without initializing entries.

    Parameters
    ----------
    shape : int or tuple of int
........................... empty_like ...........................
Help on _ArrayFunctionDispatcher in module numpy:

empty_like(...)
    empty_like(prototype, dtype=None, order='K', subok=True, shape=None, *,
               device=None)

    Return a new array with the same shape and type as a given array.

    Parameters
    ----------
........................... equal ...........................
Help on ufunc in module numpy:

equal = <ufunc 'equal'>
    equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Return (x1 == x2) element-wise.

    Parameters
    ----------
    x1, x2 : array_like
........................... errstate ...........................
Help on class errstate in module numpy:

class errstate(builtins.object)
 |  errstate(
 |      *,
 |      call=<numpy._core._ufunc_config._unspecified object at 0x73733c208590>,
 |      all=None,
 |      divide=None,
 |      over=None,
 |      under=None,
........................... euler_gamma ...........................
Help on float object:

class float(object)
 |  float(x=0, /)
 |
 |  Convert a string or number to a floating-point number, if possible.
 |
 |  Methods defined here:
 |
 |  __abs__(self, /)
........................... exceptions ...........................
Help on module numpy.exceptions in numpy:

NAME
    numpy.exceptions

DESCRIPTION
    Exceptions and Warnings (:mod:`numpy.exceptions`)
    =================================================

    General exceptions used by NumPy.  Note that some exceptions may be module
........................... exp ...........................
Help on ufunc in module numpy:

exp = <ufunc 'exp'>
    exp(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Calculate the exponential of all elements in the input array.

    Parameters
    ----------
    x : array_like
........................... exp2 ...........................
Help on ufunc in module numpy:

exp2 = <ufunc 'exp2'>
    exp2(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Calculate `2**p` for all `p` in the input array.

    Parameters
    ----------
    x : array_like
........................... expand_dims ...........................
Help on _ArrayFunctionDispatcher in module numpy:

expand_dims(a, axis)
    Expand the shape of an array.

    Insert a new axis that will appear at the `axis` position in the expanded
    array shape.

    Parameters
    ----------
........................... expm1 ...........................
Help on ufunc in module numpy:

expm1 = <ufunc 'expm1'>
    expm1(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Calculate ``exp(x) - 1`` for all elements in the array.

    Parameters
    ----------
    x : array_like
........................... extract ...........................
Help on _ArrayFunctionDispatcher in module numpy:

extract(condition, arr)
    Return the elements of an array that satisfy some condition.

    This is equivalent to ``np.compress(ravel(condition), ravel(arr))``.  If
    `condition` is boolean ``np.extract`` is equivalent to ``arr[condition]``.

    Note that `place` does the exact opposite of `extract`.

........................... eye ...........................
Help on function eye in module numpy:

eye(N, M=None, k=0, dtype=<class 'float'>, order='C', *, device=None, like=None)
    Return a 2-D array with ones on the diagonal and zeros elsewhere.

    Parameters
    ----------
    N : int
      Number of rows in the output.
    M : int, optional
........................... f2py ...........................
Help on package numpy.f2py in numpy:

NAME
    numpy.f2py - Fortran to Python Interface Generator.

DESCRIPTION
    Copyright 1999 -- 2011 Pearu Peterson all rights reserved.
    Copyright 2011 -- present NumPy Developers.
    Permission to use, modify, and distribute this software is given under the terms
    of the NumPy License.
........................... fabs ...........................
Help on ufunc in module numpy:

fabs = <ufunc 'fabs'>
    fabs(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Compute the absolute values element-wise.

    This function returns the absolute values (positive magnitude) of the
    data in `x`. Complex values are not handled, use `absolute` to find the
    absolute values of complex data.
........................... fft ...........................
Help on package numpy.fft in numpy:

NAME
    numpy.fft

DESCRIPTION
    Discrete Fourier Transform (:mod:`numpy.fft`)
    =============================================

    .. currentmodule:: numpy.fft
........................... fill_diagonal ...........................
Help on _ArrayFunctionDispatcher in module numpy:

fill_diagonal(a, val, wrap=False)
    Fill the main diagonal of the given array of any dimensionality.

    For an array `a` with ``a.ndim >= 2``, the diagonal is the list of
    values ``a[i, ..., i]`` with indices ``i`` all identical.  This function
    modifies the input array in-place without returning a value.

    Parameters
........................... finfo ...........................
Help on class finfo in module numpy:

class finfo(builtins.object)
 |  finfo(dtype)
 |
 |  finfo(dtype)
 |
 |  Machine limits for floating point types.
 |
 |  Attributes
........................... fix ...........................
Help on _ArrayFunctionDispatcher in module numpy:

fix(x, out=None)
    Round to nearest integer towards zero.

    Round an array of floats element-wise to nearest integer towards zero.
    The rounded values have the same data-type as the input.

    Parameters
    ----------
........................... flatiter ...........................
Help on class flatiter in module numpy:

class flatiter(builtins.object)
 |  Flat iterator object to iterate over arrays.
 |
 |  A `flatiter` iterator is returned by ``x.flat`` for any array `x`.
 |  It allows iterating over the array as if it were a 1-D array,
 |  either in a for-loop or by calling its `next` method.
 |
 |  Iteration is done in row-major, C-style order (the last
........................... flatnonzero ...........................
Help on _ArrayFunctionDispatcher in module numpy:

flatnonzero(a)
    Return indices that are non-zero in the flattened version of a.

    This is equivalent to ``np.nonzero(np.ravel(a))[0]``.

    Parameters
    ----------
    a : array_like
........................... flexible ...........................
Help on class flexible in module numpy:

class flexible(generic)
 |  Abstract base class of all scalar types without predefined length.
 |  The actual size of these types depends on the specific `numpy.dtype`
 |  instantiation.
 |
 |  Method resolution order:
 |      flexible
 |      generic
........................... flip ...........................
Help on _ArrayFunctionDispatcher in module numpy:

flip(m, axis=None)
    Reverse the order of elements in an array along the given axis.

    The shape of the array is preserved, but the elements are reordered.

    Parameters
    ----------
    m : array_like
........................... fliplr ...........................
Help on _ArrayFunctionDispatcher in module numpy:

fliplr(m)
    Reverse the order of elements along axis 1 (left/right).

    For a 2-D array, this flips the entries in each row in the left/right
    direction. Columns are preserved, but appear in a different order than
    before.

    Parameters
........................... flipud ...........................
Help on _ArrayFunctionDispatcher in module numpy:

flipud(m)
    Reverse the order of elements along axis 0 (up/down).

    For a 2-D array, this flips the entries in each column in the up/down
    direction. Rows are preserved, but appear in a different order than before.

    Parameters
    ----------
........................... float128 ...........................
Help on class longdouble in module numpy:

class longdouble(floating)
 |  Extended-precision floating-point number type, compatible with C
 |  ``long double`` but not necessarily with IEEE 754 quadruple-precision.
 |
 |  :Character code: ``'g'``
 |  :Alias on this platform (Linux x86_64): `numpy.float128`: 128-bit extended-precision floating-point number type.
 |
 |  Method resolution order:
........................... float16 ...........................
Help on class float16 in module numpy:

class float16(floating)
 |  Half-precision floating-point number type.
 |
 |  :Character code: ``'e'``
 |  :Canonical name: `numpy.half`
 |  :Alias on this platform (Linux x86_64): `numpy.float16`: 16-bit-precision floating-point number type: sign bit, 5 bits exponent, 10 bits mantissa.
 |
 |  Method resolution order:
........................... float32 ...........................
Help on class float32 in module numpy:

class float32(floating)
 |  Single-precision floating-point number type, compatible with C ``float``.
 |
 |  :Character code: ``'f'``
 |  :Canonical name: `numpy.single`
 |  :Alias on this platform (Linux x86_64): `numpy.float32`: 32-bit-precision floating-point number type: sign bit, 8 bits exponent, 23 bits mantissa.
 |
 |  Method resolution order:
........................... float64 ...........................
Help on class float64 in module numpy:

class float64(floating, builtins.float)
 |  float64(x=0, /)
 |
 |  Double-precision floating-point number type, compatible with Python
 |  :class:`float` and C ``double``.
 |
 |  :Character code: ``'d'``
 |  :Canonical name: `numpy.double`
........................... float_power ...........................
Help on ufunc in module numpy:

float_power = <ufunc 'float_power'>
    float_power(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    First array elements raised to powers from second array, element-wise.

    Raise each base in `x1` to the positionally-corresponding power in `x2`.
    `x1` and `x2` must be broadcastable to the same shape. This differs from
    the power function in that integers, float16, and float32  are promoted to
........................... floating ...........................
Help on class floating in module numpy:

class floating(inexact)
 |  Abstract base class of all floating-point scalar types.
 |
 |  Method resolution order:
 |      floating
 |      inexact
 |      number
 |      generic
........................... floor ...........................
Help on ufunc in module numpy:

floor = <ufunc 'floor'>
    floor(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Return the floor of the input, element-wise.

    The floor of the scalar `x` is the largest integer `i`, such that
    `i <= x`.  It is often denoted as :math:`\lfloor x \rfloor`.

........................... floor_divide ...........................
Help on ufunc in module numpy:

floor_divide = <ufunc 'floor_divide'>
    floor_divide(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Return the largest integer smaller or equal to the division of the inputs.
    It is equivalent to the Python ``//`` operator and pairs with the
    Python ``%`` (`remainder`), function so that ``a = a % b + b * (a // b)``
    up to roundoff.

........................... fmax ...........................
Help on ufunc in module numpy:

fmax = <ufunc 'fmax'>
    fmax(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Element-wise maximum of array elements.

    Compare two arrays and return a new array containing the element-wise
    maxima. If one of the elements being compared is a NaN, then the
    non-nan element is returned. If both elements are NaNs then the first
........................... fmin ...........................
Help on ufunc in module numpy:

fmin = <ufunc 'fmin'>
    fmin(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Element-wise minimum of array elements.

    Compare two arrays and return a new array containing the element-wise
    minima. If one of the elements being compared is a NaN, then the
    non-nan element is returned. If both elements are NaNs then the first
........................... fmod ...........................
Help on ufunc in module numpy:

fmod = <ufunc 'fmod'>
    fmod(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Returns the element-wise remainder of division.

    This is the NumPy implementation of the C library function fmod, the
    remainder has the same sign as the dividend `x1`. It is equivalent to
    the Matlab(TM) ``rem`` function and should not be confused with the
........................... format_float_positional ...........................
Help on function format_float_positional in module numpy:

format_float_positional(
    x,
    precision=None,
    unique=True,
    fractional=True,
    trim='k',
    sign=False,
    pad_left=None,
........................... format_float_scientific ...........................
Help on function format_float_scientific in module numpy:

format_float_scientific(
    x,
    precision=None,
    unique=True,
    trim='k',
    sign=False,
    pad_left=None,
    exp_digits=None,
........................... frexp ...........................
Help on ufunc in module numpy:

frexp = <ufunc 'frexp'>
    frexp(x[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Decompose the elements of x into mantissa and twos exponent.

    Returns (`mantissa`, `exponent`), where ``x = mantissa * 2**exponent``.
    The mantissa lies in the open interval(-1, 1), while the twos
    exponent is a signed integer.
........................... from_dlpack ...........................
Help on built-in function from_dlpack in module numpy:

from_dlpack(...)
    from_dlpack(x, /, *, device=None, copy=None)

    Create a NumPy array from an object implementing the ``__dlpack__``
    protocol. Generally, the returned NumPy array is a view of the input
    object. See [1]_ and [2]_ for more details.

    Parameters
........................... frombuffer ...........................
Help on built-in function frombuffer in module numpy:

frombuffer(...)
    frombuffer(buffer, dtype=float, count=-1, offset=0, *, like=None)

    Interpret a buffer as a 1-dimensional array.

    Parameters
    ----------
    buffer : buffer_like
........................... fromfile ...........................
Help on built-in function fromfile in module numpy:

fromfile(...)
    fromfile(file, dtype=float, count=-1, sep='', offset=0, *, like=None)

    Construct an array from data in a text or binary file.

    A highly efficient way of reading binary data with a known data-type,
    as well as parsing simply formatted text files.  Data written using the
    `tofile` method can be read using this function.
........................... fromfunction ...........................
Help on function fromfunction in module numpy:

fromfunction(function, shape, *, dtype=<class 'float'>, like=None, **kwargs)
    Construct an array by executing a function over each coordinate.

    The resulting array therefore has a value ``fn(x, y, z)`` at
    coordinate ``(x, y, z)``.

    Parameters
    ----------
........................... fromiter ...........................
Help on built-in function fromiter in module numpy:

fromiter(...)
    fromiter(iter, dtype, count=-1, *, like=None)

    Create a new 1-dimensional array from an iterable object.

    Parameters
    ----------
    iter : iterable object
........................... frompyfunc ...........................
Help on built-in function frompyfunc in module numpy:

frompyfunc(...)
    frompyfunc(func, /, nin, nout, *[, identity])

    Takes an arbitrary Python function and returns a NumPy ufunc.

    Can be used, for example, to add broadcasting to a built-in Python
    function (see Examples section).

........................... fromregex ...........................
Help on function fromregex in module numpy:

fromregex(file, regexp, dtype, encoding=None)
    Construct an array from a text file, using regular expression parsing.

    The returned array is always a structured array, and is constructed from
    all matches of the regular expression in the file. Groups in the regular
    expression are converted to fields of the structured array.

    Parameters
........................... fromstring ...........................
Help on built-in function fromstring in module numpy:

fromstring(...)
    fromstring(string, dtype=float, count=-1, *, sep, like=None)

    A new 1-D array initialized from text data in a string.

    Parameters
    ----------
    string : str
........................... full ...........................
Help on function full in module numpy:

full(shape, fill_value, dtype=None, order='C', *, device=None, like=None)
    Return a new array of given shape and type, filled with `fill_value`.

    Parameters
    ----------
    shape : int or sequence of ints
        Shape of the new array, e.g., ``(2, 3)`` or ``2``.
    fill_value : scalar or array_like
........................... full_like ...........................
Help on _ArrayFunctionDispatcher in module numpy:

full_like(
    a,
    fill_value,
    dtype=None,
    order='K',
    subok=True,
    shape=None,
    *,
........................... gcd ...........................
Help on ufunc in module numpy:

gcd = <ufunc 'gcd'>
    gcd(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Returns the greatest common divisor of ``|x1|`` and ``|x2|``

    Parameters
    ----------
    x1, x2 : array_like, int
........................... generic ...........................
Help on class generic in module numpy:

class generic(builtins.object)
 |  Base class for numpy scalar types.
 |
 |  Class from which most (all?) numpy scalar types are derived.  For
 |  consistency, exposes the same API as `ndarray`, despite many
 |  consequent attributes being either "get-only," or completely irrelevant.
 |  This is the class from which it is strongly suggested users should derive
 |  custom scalar types.
........................... genfromtxt ...........................
Help on function genfromtxt in module numpy:

genfromtxt(
    fname,
    dtype=<class 'float'>,
    comments='#',
    delimiter=None,
    skip_header=0,
    skip_footer=0,
    converters=None,
........................... geomspace ...........................
Help on _ArrayFunctionDispatcher in module numpy:

geomspace(start, stop, num=50, endpoint=True, dtype=None, axis=0)
    Return numbers spaced evenly on a log scale (a geometric progression).

    This is similar to `logspace`, but with endpoints specified directly.
    Each output sample is a constant multiple of the previous.

    Parameters
    ----------
........................... get_include ...........................
Help on function get_include in module numpy:

get_include()
    Return the directory that contains the NumPy \*.h header files.

    Extension modules that need to compile against NumPy may need to use this
    function to locate the appropriate include directory.

    Notes
    -----
........................... get_printoptions ...........................
Help on function get_printoptions in module numpy:

get_printoptions()
    Return the current print options.

    Returns
    -------
    print_opts : dict
        Dictionary of current print options with keys

........................... getbufsize ...........................
Help on function getbufsize in module numpy:

getbufsize()
    Return the size of the buffer used in ufuncs.

    Returns
    -------
    getbufsize : int
        Size of ufunc buffer in bytes.

........................... geterr ...........................
Help on function geterr in module numpy:

geterr()
    Get the current way of handling floating-point errors.

    Returns
    -------
    res : dict
        A dictionary with keys "divide", "over", "under", and "invalid",
        whose values are from the strings "ignore", "print", "log", "warn",
........................... geterrcall ...........................
Help on function geterrcall in module numpy:

geterrcall()
    Return the current callback function used on floating-point errors.

    When the error handling for a floating-point error (one of "divide",
    "over", "under", or "invalid") is set to 'call' or 'log', the function
    that is called or the log instance that is written to is returned by
    `geterrcall`. This function or log instance has been set with
    `seterrcall`.
........................... gradient ...........................
Help on _ArrayFunctionDispatcher in module numpy:

gradient(f, *varargs, axis=None, edge_order=1)
    Return the gradient of an N-dimensional array.

    The gradient is computed using second order accurate central differences
    in the interior points and either first or second order accurate one-sides
    (forward or backwards) differences at the boundaries.
    The returned gradient hence has the same shape as the input array.

........................... greater ...........................
Help on ufunc in module numpy:

greater = <ufunc 'greater'>
    greater(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Return the truth value of (x1 > x2) element-wise.

    Parameters
    ----------
    x1, x2 : array_like
........................... greater_equal ...........................
Help on ufunc in module numpy:

greater_equal = <ufunc 'greater_equal'>
    greater_equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Return the truth value of (x1 >= x2) element-wise.

    Parameters
    ----------
    x1, x2 : array_like
........................... half ...........................
Help on class float16 in module numpy:

class float16(floating)
 |  Half-precision floating-point number type.
 |
 |  :Character code: ``'e'``
 |  :Canonical name: `numpy.half`
 |  :Alias on this platform (Linux x86_64): `numpy.float16`: 16-bit-precision floating-point number type: sign bit, 5 bits exponent, 10 bits mantissa.
 |
 |  Method resolution order:
........................... hamming ...........................
Help on function hamming in module numpy:

hamming(M)
    Return the Hamming window.

    The Hamming window is a taper formed by using a weighted cosine.

    Parameters
    ----------
    M : int
........................... hanning ...........................
Help on function hanning in module numpy:

hanning(M)
    Return the Hanning window.

    The Hanning window is a taper formed by using a weighted cosine.

    Parameters
    ----------
    M : int
........................... heaviside ...........................
Help on ufunc in module numpy:

heaviside = <ufunc 'heaviside'>
    heaviside(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Compute the Heaviside step function.

    The Heaviside step function [1]_ is defined as::

                              0   if x1 < 0
........................... histogram ...........................
Help on _ArrayFunctionDispatcher in module numpy:

histogram(a, bins=10, range=None, density=None, weights=None)
    Compute the histogram of a dataset.

    Parameters
    ----------
    a : array_like
        Input data. The histogram is computed over the flattened array.
    bins : int or sequence of scalars or str, optional
........................... histogram2d ...........................
Help on _ArrayFunctionDispatcher in module numpy:

histogram2d(x, y, bins=10, range=None, density=None, weights=None)
    Compute the bi-dimensional histogram of two data samples.

    Parameters
    ----------
    x : array_like, shape (N,)
        An array containing the x coordinates of the points to be
        histogrammed.
........................... histogram_bin_edges ...........................
Help on _ArrayFunctionDispatcher in module numpy:

histogram_bin_edges(a, bins=10, range=None, weights=None)
    Function to calculate only the edges of the bins used by the `histogram`
    function.

    Parameters
    ----------
    a : array_like
        Input data. The histogram is computed over the flattened array.
........................... histogramdd ...........................
Help on _ArrayFunctionDispatcher in module numpy:

histogramdd(sample, bins=10, range=None, density=None, weights=None)
    Compute the multidimensional histogram of some data.

    Parameters
    ----------
    sample : (N, D) array, or (N, D) array_like
        The data to be histogrammed.

........................... hsplit ...........................
Help on _ArrayFunctionDispatcher in module numpy:

hsplit(ary, indices_or_sections)
    Split an array into multiple sub-arrays horizontally (column-wise).

    Please refer to the `split` documentation.  `hsplit` is equivalent
    to `split` with ``axis=1``, the array is always split along the second
    axis except for 1-D arrays, where it is split at ``axis=0``.

    See Also
........................... hstack ...........................
Help on _ArrayFunctionDispatcher in module numpy:

hstack(tup, *, dtype=None, casting='same_kind')
    Stack arrays in sequence horizontally (column wise).

    This is equivalent to concatenation along the second axis, except for 1-D
    arrays where it concatenates along the first axis. Rebuilds arrays divided
    by `hsplit`.

    This function makes most sense for arrays with up to 3 dimensions. For
........................... hypot ...........................
Help on ufunc in module numpy:

hypot = <ufunc 'hypot'>
    hypot(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Given the "legs" of a right triangle, return its hypotenuse.

    Equivalent to ``sqrt(x1**2 + x2**2)``, element-wise.  If `x1` or
    `x2` is scalar_like (i.e., unambiguously cast-able to a scalar type),
    it is broadcast for use with each element of the other argument.
........................... i0 ...........................
Help on _ArrayFunctionDispatcher in module numpy:

i0(x)
    Modified Bessel function of the first kind, order 0.

    Usually denoted :math:`I_0`.

    Parameters
    ----------
    x : array_like of float
........................... identity ...........................
Help on function identity in module numpy:

identity(n, dtype=None, *, like=None)
    Return the identity array.

    The identity array is a square array with ones on
    the main diagonal.

    Parameters
    ----------
........................... iinfo ...........................
Help on class iinfo in module numpy:

class iinfo(builtins.object)
 |  iinfo(int_type)
 |
 |  iinfo(type)
 |
 |  Machine limits for integer types.
 |
 |  Attributes
........................... imag ...........................
Help on _ArrayFunctionDispatcher in module numpy:

imag(val)
    Return the imaginary part of the complex argument.

    Parameters
    ----------
    val : array_like
        Input array.

........................... in1d ...........................
Help on _ArrayFunctionDispatcher in module numpy:

in1d(ar1, ar2, assume_unique=False, invert=False, *, kind=None)
    Test whether each element of a 1-D array is also present in a second array.

    .. deprecated:: 2.0
        Use :func:`isin` instead of `in1d` for new code.

    Returns a boolean array the same length as `ar1` that is True
    where an element of `ar1` is in `ar2` and False otherwise.
........................... index_exp ...........................
Help on IndexExpression in module numpy.lib._index_tricks_impl object:

class IndexExpression(builtins.object)
 |  IndexExpression(maketuple)
 |
 |  A nicer way to build up index tuples for arrays.
 |
 |  .. note::
 |     Use one of the two predefined instances ``index_exp`` or `s_`
 |     rather than directly using `IndexExpression`.
........................... indices ...........................
Help on function indices in module numpy:

indices(dimensions, dtype=<class 'int'>, sparse=False)
    Return an array representing the indices of a grid.

    Compute an array where the subarrays contain index values 0, 1, ...
    varying only along the corresponding axis.

    Parameters
    ----------
........................... inexact ...........................
Help on class inexact in module numpy:

class inexact(number)
 |  Abstract base class of all numeric scalar types with a (potentially)
 |  inexact representation of the values in its range, such as
 |  floating-point numbers.
 |
 |  Method resolution order:
 |      inexact
 |      number
........................... inf ...........................
Help on float object:

class float(object)
 |  float(x=0, /)
 |
 |  Convert a string or number to a floating-point number, if possible.
 |
 |  Methods defined here:
 |
 |  __abs__(self, /)
........................... info ...........................
Help on function info in module numpy:

info(object=None, maxwidth=76, output=None, toplevel='numpy')
    Get help information for an array, function, class, or module.

    Parameters
    ----------
    object : object or str, optional
        Input object or name to get information about. If `object` is
        an `ndarray` instance, information about the array is printed.
........................... inner ...........................
Help on _ArrayFunctionDispatcher in module numpy:

inner(...)
    inner(a, b, /)

    Inner product of two arrays.

    Ordinary inner product of vectors for 1-D arrays (without complex
    conjugation), in higher dimensions a sum product over the last axes.

........................... insert ...........................
Help on _ArrayFunctionDispatcher in module numpy:

insert(arr, obj, values, axis=None)
    Insert values along the given axis before the given indices.

    Parameters
    ----------
    arr : array_like
        Input array.
    obj : slice, int, array-like of ints or bools
........................... int16 ...........................
Help on class int16 in module numpy:

class int16(signedinteger)
 |  Signed integer type, compatible with C ``short``.
 |
 |  :Character code: ``'h'``
 |  :Canonical name: `numpy.short`
 |  :Alias on this platform (Linux x86_64): `numpy.int16`: 16-bit signed integer (``-32_768`` to ``32_767``).
 |
 |  Method resolution order:
........................... int32 ...........................
Help on class int32 in module numpy:

class int32(signedinteger)
 |  Signed integer type, compatible with C ``int``.
 |
 |  :Character code: ``'i'``
 |  :Canonical name: `numpy.intc`
 |  :Alias on this platform (Linux x86_64): `numpy.int32`: 32-bit signed integer (``-2_147_483_648`` to ``2_147_483_647``).
 |
 |  Method resolution order:
........................... int64 ...........................
Help on class int64 in module numpy:

class int64(signedinteger)
 |  Default signed integer type, 64bit on 64bit systems and 32bit on 32bit
 |  systems.
 |
 |  :Character code: ``'l'``
 |  :Canonical name: `numpy.int_`
 |  :Alias on this platform (Linux x86_64): `numpy.int64`: 64-bit signed integer (``-9_223_372_036_854_775_808`` to ``9_223_372_036_854_775_807``).
 |  :Alias on this platform (Linux x86_64): `numpy.intp`: Signed integer large enough to fit pointer, compatible with C ``intptr_t``.
........................... int8 ...........................
Help on class int8 in module numpy:

class int8(signedinteger)
 |  Signed integer type, compatible with C ``char``.
 |
 |  :Character code: ``'b'``
 |  :Canonical name: `numpy.byte`
 |  :Alias on this platform (Linux x86_64): `numpy.int8`: 8-bit signed integer (``-128`` to ``127``).
 |
 |  Method resolution order:
........................... int_ ...........................
Help on class int64 in module numpy:

class int64(signedinteger)
 |  Default signed integer type, 64bit on 64bit systems and 32bit on 32bit
 |  systems.
 |
 |  :Character code: ``'l'``
 |  :Canonical name: `numpy.int_`
 |  :Alias on this platform (Linux x86_64): `numpy.int64`: 64-bit signed integer (``-9_223_372_036_854_775_808`` to ``9_223_372_036_854_775_807``).
 |  :Alias on this platform (Linux x86_64): `numpy.intp`: Signed integer large enough to fit pointer, compatible with C ``intptr_t``.
........................... intc ...........................
Help on class int32 in module numpy:

class int32(signedinteger)
 |  Signed integer type, compatible with C ``int``.
 |
 |  :Character code: ``'i'``
 |  :Canonical name: `numpy.intc`
 |  :Alias on this platform (Linux x86_64): `numpy.int32`: 32-bit signed integer (``-2_147_483_648`` to ``2_147_483_647``).
 |
 |  Method resolution order:
........................... integer ...........................
Help on class integer in module numpy:

class integer(number)
 |  Abstract base class of all integer scalar types.
 |
 |  Method resolution order:
 |      integer
 |      number
 |      generic
 |      builtins.object
........................... interp ...........................
Help on _ArrayFunctionDispatcher in module numpy:

interp(x, xp, fp, left=None, right=None, period=None)
    One-dimensional linear interpolation for monotonically increasing sample points.

    Returns the one-dimensional piecewise linear interpolant to a function
    with given discrete data points (`xp`, `fp`), evaluated at `x`.

    Parameters
    ----------
........................... intersect1d ...........................
Help on _ArrayFunctionDispatcher in module numpy:

intersect1d(ar1, ar2, assume_unique=False, return_indices=False)
    Find the intersection of two arrays.

    Return the sorted, unique values that are in both of the input arrays.

    Parameters
    ----------
    ar1, ar2 : array_like
........................... intp ...........................
Help on class int64 in module numpy:

class int64(signedinteger)
 |  Default signed integer type, 64bit on 64bit systems and 32bit on 32bit
 |  systems.
 |
 |  :Character code: ``'l'``
 |  :Canonical name: `numpy.int_`
 |  :Alias on this platform (Linux x86_64): `numpy.int64`: 64-bit signed integer (``-9_223_372_036_854_775_808`` to ``9_223_372_036_854_775_807``).
 |  :Alias on this platform (Linux x86_64): `numpy.intp`: Signed integer large enough to fit pointer, compatible with C ``intptr_t``.
........................... invert ...........................
Help on ufunc in module numpy:

invert = <ufunc 'invert'>
    invert(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Compute bit-wise inversion, or bit-wise NOT, element-wise.

    Computes the bit-wise NOT of the underlying binary representation of
    the integers in the input arrays. This ufunc implements the C/Python
    operator ``~``.
........................... is_busday ...........................
Help on _ArrayFunctionDispatcher in module numpy:

is_busday(...)
    is_busday(
        dates,
        weekmask='1111100',
        holidays=None,
        busdaycal=None,
        out=None
    )
........................... isclose ...........................
Help on _ArrayFunctionDispatcher in module numpy:

isclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False)
    Returns a boolean array where two arrays are element-wise equal within a
    tolerance.

    The tolerance values are positive, typically very small numbers.  The
    relative difference (`rtol` * abs(`b`)) and the absolute difference
    `atol` are added together to compare against the absolute difference
    between `a` and `b`.
........................... iscomplex ...........................
Help on _ArrayFunctionDispatcher in module numpy:

iscomplex(x)
    Returns a bool array, where True if input element is complex.

    What is tested is whether the input has a non-zero imaginary part, not if
    the input type is complex.

    Parameters
    ----------
........................... iscomplexobj ...........................
Help on _ArrayFunctionDispatcher in module numpy:

iscomplexobj(x)
    Check for a complex type or an array of complex numbers.

    The type of the input is checked, not the value. Even if the input
    has an imaginary part equal to zero, `iscomplexobj` evaluates to True.

    Parameters
    ----------
........................... isdtype ...........................
Help on function isdtype in module numpy:

isdtype(dtype, kind)
    Determine if a provided dtype is of a specified data type ``kind``.

    This function only supports built-in NumPy's data types.
    Third-party dtypes are not yet supported.

    Parameters
    ----------
........................... isfinite ...........................
Help on ufunc in module numpy:

isfinite = <ufunc 'isfinite'>
    isfinite(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Test element-wise for finiteness (not infinity and not Not a Number).

    The result is returned as a boolean array.

    Parameters
........................... isfortran ...........................
Help on function isfortran in module numpy:

isfortran(a)
    Check if the array is Fortran contiguous but *not* C contiguous.

    This function is obsolete. If you only want to check if an array is Fortran
    contiguous use ``a.flags.f_contiguous`` instead.

    Parameters
    ----------
........................... isin ...........................
Help on _ArrayFunctionDispatcher in module numpy:

isin(element, test_elements, assume_unique=False, invert=False, *, kind=None)
    Calculates ``element in test_elements``, broadcasting over `element` only.
    Returns a boolean array of the same shape as `element` that is True
    where an element of `element` is in `test_elements` and False otherwise.

    Parameters
    ----------
    element : array_like
........................... isinf ...........................
Help on ufunc in module numpy:

isinf = <ufunc 'isinf'>
    isinf(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Test element-wise for positive or negative infinity.

    Returns a boolean array of the same shape as `x`, True where ``x ==
    +/-inf``, otherwise False.

........................... isnan ...........................
Help on ufunc in module numpy:

isnan = <ufunc 'isnan'>
    isnan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Test element-wise for NaN and return result as a boolean array.

    Parameters
    ----------
    x : array_like
........................... isnat ...........................
Help on ufunc in module numpy:

isnat = <ufunc 'isnat'>
    isnat(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Test element-wise for NaT (not a time) and return result as a boolean array.

    Parameters
    ----------
    x : array_like
........................... isneginf ...........................
Help on _ArrayFunctionDispatcher in module numpy:

isneginf(x, out=None)
    Test element-wise for negative infinity, return result as bool array.

    Parameters
    ----------
    x : array_like
        The input array.
    out : array_like, optional
........................... isposinf ...........................
Help on _ArrayFunctionDispatcher in module numpy:

isposinf(x, out=None)
    Test element-wise for positive infinity, return result as bool array.

    Parameters
    ----------
    x : array_like
        The input array.
    out : array_like, optional
........................... isreal ...........................
Help on _ArrayFunctionDispatcher in module numpy:

isreal(x)
    Returns a bool array, where True if input element is real.

    If element has complex type with zero imaginary part, the return value
    for that element is True.

    Parameters
    ----------
........................... isrealobj ...........................
Help on _ArrayFunctionDispatcher in module numpy:

isrealobj(x)
    Return True if x is a not complex type or an array of complex numbers.

    The type of the input is checked, not the value. So even if the input
    has an imaginary part equal to zero, `isrealobj` evaluates to False
    if the data type is complex.

    Parameters
........................... isscalar ...........................
Help on function isscalar in module numpy:

isscalar(element)
    Returns True if the type of `element` is a scalar type.

    Parameters
    ----------
    element : any
        Input argument, can be of any type and shape.

    +....................................+...............+...................+
    | PEP 3141 numeric objects           | ``True``      | ``True``          |
    | (including builtins)               |               |                   |
    +------------------------------------+---------------+-------------------+
    | builtin string and buffer objects  | ``True``      | ``True``          |
    +------------------------------------+---------------+-------------------+
    | other builtin objects, like        | ``False``     | ``True``          |
    | `pathlib.Path`, `Exception`,       |               |                   |
    | the result of `re.compile`         |               |                   |
    +------------------------------------+---------------+-------------------+
    | third-party objects like           | ``False``     | ``True``          |
........................... issubdtype ...........................
Help on function issubdtype in module numpy:

issubdtype(arg1, arg2)
    Returns True if first argument is a typecode lower/equal in type hierarchy.

    This is like the builtin :func:`issubclass`, but for `dtype`\ s.

    Parameters
    ----------
    arg1, arg2 : dtype_like
........................... iterable ...........................
Help on function iterable in module numpy:

iterable(y)
    Check whether or not an object can be iterated over.

    Parameters
    ----------
    y : object
      Input object.

........................... ix_ ...........................
Help on _ArrayFunctionDispatcher in module numpy:

ix_(*args)
    Construct an open mesh from multiple sequences.

    This function takes N 1-D sequences and returns N outputs with N
    dimensions each, such that the shape is 1 in all but one dimension
    and the dimension with the non-unit shape value cycles through all
    N dimensions.

........................... kaiser ...........................
Help on function kaiser in module numpy:

kaiser(M, beta)
    Return the Kaiser window.

    The Kaiser window is a taper formed by using a Bessel function.

    Parameters
    ----------
    M : int
    ....  .......................
    beta  Window shape
    ====  =======================
    0     Rectangular
    5     Similar to a Hamming
    6     Similar to a Hanning
    8.6   Similar to a Blackman
    ====  =======================

    A beta value of 14 is probably a good starting point. Note that as beta
    gets large, the window narrows, and so the number of samples needs to be
........................... kron ...........................
Help on _ArrayFunctionDispatcher in module numpy:

kron(a, b)
    Kronecker product of two arrays.

    Computes the Kronecker product, a composite array made of blocks of the
    second array scaled by the first.

    Parameters
    ----------
........................... lcm ...........................
Help on ufunc in module numpy:

lcm = <ufunc 'lcm'>
    lcm(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Returns the lowest common multiple of ``|x1|`` and ``|x2|``

    Parameters
    ----------
    x1, x2 : array_like, int
........................... ldexp ...........................
Help on ufunc in module numpy:

ldexp = <ufunc 'ldexp'>
    ldexp(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Returns x1 * 2**x2, element-wise.

    The mantissas `x1` and twos exponents `x2` are used to construct
    floating point numbers ``x1 * 2**x2``.

........................... left_shift ...........................
Help on ufunc in module numpy:

left_shift = <ufunc 'left_shift'>
    left_shift(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Shift the bits of an integer to the left.

    Bits are shifted to the left by appending `x2` 0s at the right of `x1`.
    Since the internal representation of numbers is in binary format, this
    operation is equivalent to multiplying `x1` by ``2**x2``.
........................... less ...........................
Help on ufunc in module numpy:

less = <ufunc 'less'>
    less(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Return the truth value of (x1 < x2) element-wise.

    Parameters
    ----------
    x1, x2 : array_like
........................... less_equal ...........................
Help on ufunc in module numpy:

less_equal = <ufunc 'less_equal'>
    less_equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Return the truth value of (x1 <= x2) element-wise.

    Parameters
    ----------
    x1, x2 : array_like
........................... lexsort ...........................
Help on _ArrayFunctionDispatcher in module numpy:

lexsort(...)
    lexsort(keys, axis=-1)

    Perform an indirect stable sort using a sequence of keys.

    Given multiple sorting keys, lexsort returns an array of integer indices
    that describes the sort order by multiple keys. The last key in the
    sequence is used for the primary sort order, ties are broken by the
........................... lib ...........................
Help on package numpy.lib in numpy:

NAME
    numpy.lib

DESCRIPTION
    ``numpy.lib`` is mostly a space for implementing functions that don't
    belong in core or in another NumPy submodule with a clear purpose
    (e.g. ``random``, ``fft``, ``linalg``, ``ma``).

........................... linalg ...........................
Help on package numpy.linalg in numpy:

NAME
    numpy.linalg

DESCRIPTION
    ``numpy.linalg``
    ================

    The NumPy linear algebra functions rely on BLAS and LAPACK to provide efficient
            .....  ............................
            p      norm for matrices
            =====  ============================
            None   2-norm, computed directly using the ``SVD``
            'fro'  Frobenius norm
            inf    max(sum(abs(x), axis=1))
            -inf   min(sum(abs(x), axis=1))
            1      max(sum(abs(x), axis=0))
            -1     min(sum(abs(x), axis=0))
            2      2-norm (largest sing. value)
            -2     smallest singular value
            .....  ............................

            inf means the `numpy.inf` object, and the Frobenius norm is
            the root-of-sum-of-squares norm.

        Returns
        -------
        c : {float, inf}
            The condition number of the matrix. May be infinite.

        See Also
        .....  ............................  ..........................
        ord    norm for matrices             norm for vectors
        =====  ============================  ==========================
        None   Frobenius norm                2-norm
        'fro'  Frobenius norm                --
        'nuc'  nuclear norm                  --
        inf    max(sum(abs(x), axis=1))      max(abs(x))
        -inf   min(sum(abs(x), axis=1))      min(abs(x))
        0      --                            sum(x != 0)
        1      max(sum(abs(x), axis=0))      as below
        -1     min(sum(abs(x), axis=0))      as below
        .....  ............................  ..........................

        The Frobenius norm is given by [1]_:

        :math:`||A||_F = [\sum_{i,j} abs(a_{i,j})^2]^{1/2}`

        The nuclear norm is the sum of the singular values.

        Both the Frobenius and nuclear norm orders are only defined for
        matrices and raise a ValueError when ``x.ndim != 2``.

........................... linspace ...........................
Help on _ArrayFunctionDispatcher in module numpy:

linspace(
    start,
    stop,
    num=50,
    endpoint=True,
    retstep=False,
    dtype=None,
    axis=0,
........................... little_endian ...........................
Help on bool object:

class bool(int)
 |  bool(object=False, /)
 |
 |  Returns True when the argument is true, False otherwise.
 |  The builtins True and False are the only two instances of the class bool.
 |  The class bool is a subclass of the class int, and cannot be subclassed.
 |
 |  Method resolution order:
........................... load ...........................
Help on function load in module numpy:

load(
    file,
    mmap_mode=None,
    allow_pickle=False,
    fix_imports=True,
    encoding='ASCII',
    *,
    max_header_size=10000
........................... loadtxt ...........................
Help on function loadtxt in module numpy:

loadtxt(
    fname,
    dtype=<class 'float'>,
    comments='#',
    delimiter=None,
    converters=None,
    skiprows=0,
    usecols=None,
........................... log ...........................
Help on ufunc in module numpy:

log = <ufunc 'log'>
    log(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Natural logarithm, element-wise.

    The natural logarithm `log` is the inverse of the exponential function,
    so that `log(exp(x)) = x`. The natural logarithm is logarithm in base
    `e`.
........................... log10 ...........................
Help on ufunc in module numpy:

log10 = <ufunc 'log10'>
    log10(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Return the base 10 logarithm of the input array, element-wise.

    Parameters
    ----------
    x : array_like
........................... log1p ...........................
Help on ufunc in module numpy:

log1p = <ufunc 'log1p'>
    log1p(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Return the natural logarithm of one plus the input array, element-wise.

    Calculates ``log(1 + x)``.

    Parameters
........................... log2 ...........................
Help on ufunc in module numpy:

log2 = <ufunc 'log2'>
    log2(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Base-2 logarithm of `x`.

    Parameters
    ----------
    x : array_like
........................... logaddexp ...........................
Help on ufunc in module numpy:

logaddexp = <ufunc 'logaddexp'>
    logaddexp(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Logarithm of the sum of exponentiations of the inputs.

    Calculates ``log(exp(x1) + exp(x2))``. This function is useful in
    statistics where the calculated probabilities of events may be so small
    as to exceed the range of normal floating point numbers.  In such cases
........................... logaddexp2 ...........................
Help on ufunc in module numpy:

logaddexp2 = <ufunc 'logaddexp2'>
    logaddexp2(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Logarithm of the sum of exponentiations of the inputs in base-2.

    Calculates ``log2(2**x1 + 2**x2)``. This function is useful in machine
    learning when the calculated probabilities of events may be so small as
    to exceed the range of normal floating point numbers.  In such cases
........................... logical_and ...........................
Help on ufunc in module numpy:

logical_and = <ufunc 'logical_and'>
    logical_and(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Compute the truth value of x1 AND x2 element-wise.

    Parameters
    ----------
    x1, x2 : array_like
........................... logical_not ...........................
Help on ufunc in module numpy:

logical_not = <ufunc 'logical_not'>
    logical_not(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Compute the truth value of NOT x element-wise.

    Parameters
    ----------
    x : array_like
........................... logical_or ...........................
Help on ufunc in module numpy:

logical_or = <ufunc 'logical_or'>
    logical_or(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Compute the truth value of x1 OR x2 element-wise.

    Parameters
    ----------
    x1, x2 : array_like
........................... logical_xor ...........................
Help on ufunc in module numpy:

logical_xor = <ufunc 'logical_xor'>
    logical_xor(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Compute the truth value of x1 XOR x2, element-wise.

    Parameters
    ----------
    x1, x2 : array_like
........................... logspace ...........................
Help on _ArrayFunctionDispatcher in module numpy:

logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0)
    Return numbers spaced evenly on a log scale.

    In linear space, the sequence starts at ``base ** start``
    (`base` to the power of `start`) and ends with ``base ** stop``
    (see `endpoint` below).

    .. versionchanged:: 1.25.0
........................... long ...........................
Help on class int64 in module numpy:

class int64(signedinteger)
 |  Default signed integer type, 64bit on 64bit systems and 32bit on 32bit
 |  systems.
 |
 |  :Character code: ``'l'``
 |  :Canonical name: `numpy.int_`
 |  :Alias on this platform (Linux x86_64): `numpy.int64`: 64-bit signed integer (``-9_223_372_036_854_775_808`` to ``9_223_372_036_854_775_807``).
 |  :Alias on this platform (Linux x86_64): `numpy.intp`: Signed integer large enough to fit pointer, compatible with C ``intptr_t``.
........................... longdouble ...........................
Help on class longdouble in module numpy:

class longdouble(floating)
 |  Extended-precision floating-point number type, compatible with C
 |  ``long double`` but not necessarily with IEEE 754 quadruple-precision.
 |
 |  :Character code: ``'g'``
 |  :Alias on this platform (Linux x86_64): `numpy.float128`: 128-bit extended-precision floating-point number type.
 |
 |  Method resolution order:
........................... longlong ...........................
Help on class longlong in module numpy:

class longlong(signedinteger)
 |  Signed integer type, compatible with C ``long long``.
 |
 |  :Character code: ``'q'``
 |
 |  Method resolution order:
 |      longlong
 |      signedinteger
........................... ma ...........................
Help on package numpy.ma in numpy:

NAME
    numpy.ma

DESCRIPTION
    =============
    Masked Arrays
    =============

        ...... ...... ................
        `x1`   `x2`   `arctan2(x1,x2)`
        ====== ====== ================
        +/- 0  +0     +/- 0
        +/- 0  -0     +/- pi
         > 0   +/-inf +0 / +pi
         < 0   +/-inf -0 / -pi
        +/-inf +inf   +/- (pi/4)
        +/-inf -inf   +/- (3*pi/4)
        ====== ====== ================

........................... mask_indices ...........................
Help on function mask_indices in module numpy:

mask_indices(n, mask_func, k=0)
    Return the indices to access (n, n) arrays, given a masking function.

    Assume `mask_func` is a function that, for a square array a of size
    ``(n, n)`` with a possible offset argument `k`, when called as
    ``mask_func(a, k)`` returns a new array with zeros in certain locations
    (functions like `triu` or `tril` do precisely this). Then this function
    returns the indices where the non-zero values would be located.
........................... matmul ...........................
Help on ufunc in module numpy:

matmul = <ufunc 'matmul'>
    matmul(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])

    Matrix product of two arrays.

    Parameters
    ----------
    x1, x2 : array_like
........................... matrix ...........................
Help on class matrix in module numpy:

class matrix(ndarray)
 |  matrix(data, dtype=None, copy=True)
 |
 |  matrix(data, dtype=None, copy=True)
 |
 |  Returns a matrix from an array-like object, or from a string of data.
 |
 |  A matrix is a specialized 2-D array that retains its 2-D nature
........................... matrix_transpose ...........................
Help on _ArrayFunctionDispatcher in module numpy:

matrix_transpose(x, /)
    Transposes a matrix (or a stack of matrices) ``x``.

    This function is Array API compatible.

    Parameters
    ----------
    x : array_like
........................... matvec ...........................
Help on ufunc in module numpy:

matvec = <ufunc 'matvec'>
    matvec(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])

    Matrix-vector dot product of two arrays.

    Given a matrix (or stack of matrices) :math:`\mathbf{A}` in ``x1`` and
    a vector (or stack of vectors) :math:`\mathbf{v}` in ``x2``, the
    matrix-vector product is defined as:
........................... max ...........................
Help on _ArrayFunctionDispatcher in module numpy:

max(
    a,
    axis=None,
    out=None,
    keepdims=<no value>,
    initial=<no value>,
    where=<no value>
)
........................... maximum ...........................
Help on ufunc in module numpy:

maximum = <ufunc 'maximum'>
    maximum(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Element-wise maximum of array elements.

    Compare two arrays and return a new array containing the element-wise
    maxima. If one of the elements being compared is a NaN, then that
    element is returned. If both elements are NaNs then the first is
........................... may_share_memory ...........................
Help on _ArrayFunctionDispatcher in module numpy:

may_share_memory(...)
    may_share_memory(a, b, /, max_work=None)

    Determine if two arrays might share memory

    A return of True does not necessarily mean that the two arrays
    share any element.  It just means that they *might*.

........................... mean ...........................
Help on _ArrayFunctionDispatcher in module numpy:

mean(
    a,
    axis=None,
    dtype=None,
    out=None,
    keepdims=<no value>,
    *,
    where=<no value>
........................... median ...........................
Help on _ArrayFunctionDispatcher in module numpy:

median(a, axis=None, out=None, overwrite_input=False, keepdims=False)
    Compute the median along the specified axis.

    Returns the median of the array elements.

    Parameters
    ----------
    a : array_like
........................... memmap ...........................
Help on class memmap in module numpy:

class memmap(ndarray)
 |  memmap(
 |      filename,
 |      dtype=<class 'numpy.uint8'>,
 |      mode='r+',
 |      offset=0,
 |      shape=None,
 |      order='C'
........................... meshgrid ...........................
Help on _ArrayFunctionDispatcher in module numpy:

meshgrid(*xi, copy=True, sparse=False, indexing='xy')
    Return a tuple of coordinate matrices from coordinate vectors.

    Make N-D coordinate arrays for vectorized evaluations of
    N-D scalar/vector fields over N-D grids, given
    one-dimensional coordinate arrays x1, x2,..., xn.

    Parameters
........................... mgrid ...........................
Help on MGridClass in module numpy.lib._index_tricks_impl object:

class MGridClass(nd_grid)
 |  An instance which returns a dense multi-dimensional "meshgrid".
 |
 |  An instance which returns a dense (or fleshed out) mesh-grid
 |  when indexed, so that each returned argument has the same shape.
 |  The dimensions and number of the output arrays are equal to the
 |  number of indexing dimensions.  If the step length is not a complex
 |  number, then the stop is not inclusive.
........................... min ...........................
Help on _ArrayFunctionDispatcher in module numpy:

min(
    a,
    axis=None,
    out=None,
    keepdims=<no value>,
    initial=<no value>,
    where=<no value>
)
........................... min_scalar_type ...........................
Help on _ArrayFunctionDispatcher in module numpy:

min_scalar_type(...)
    min_scalar_type(a, /)

    For scalar ``a``, returns the data type with the smallest size
    and smallest scalar kind which can hold its value.  For non-scalar
    array ``a``, returns the vector's dtype unmodified.

    Floating point values are not demoted to integers,
........................... minimum ...........................
Help on ufunc in module numpy:

minimum = <ufunc 'minimum'>
    minimum(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Element-wise minimum of array elements.

    Compare two arrays and return a new array containing the element-wise
    minima. If one of the elements being compared is a NaN, then that
    element is returned. If both elements are NaNs then the first is
........................... mintypecode ...........................
Help on function mintypecode in module numpy:

mintypecode(typechars, typeset='GDFgdf', default='d')
    Return the character for the minimum-size type to which given types can
    be safely cast.

    The returned type character must represent the smallest size dtype such
    that an array of the returned type can handle the data from an array of
    all types in `typechars` (or if `typechars` is an array, then its
    dtype.char).
........................... mod ...........................
Help on ufunc in module numpy:

remainder = <ufunc 'remainder'>
    remainder(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Returns the element-wise remainder of division.

    Computes the remainder complementary to the `floor_divide` function.  It is
    equivalent to the Python modulus operator ``x1 % x2`` and has the same sign
    as the divisor `x2`. The MATLAB function equivalent to ``np.remainder``
........................... modf ...........................
Help on ufunc in module numpy:

modf = <ufunc 'modf'>
    modf(x[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Return the fractional and integral parts of an array, element-wise.

    The fractional and integral parts are negative if the given number is
    negative.

........................... moveaxis ...........................
Help on _ArrayFunctionDispatcher in module numpy:

moveaxis(a, source, destination)
    Move axes of an array to new positions.

    Other axes remain in their original order.

    Parameters
    ----------
    a : np.ndarray
........................... multiply ...........................
Help on ufunc in module numpy:

multiply = <ufunc 'multiply'>
    multiply(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Multiply arguments element-wise.

    Parameters
    ----------
    x1, x2 : array_like
........................... nan ...........................
Help on float object:

class float(object)
 |  float(x=0, /)
 |
 |  Convert a string or number to a floating-point number, if possible.
 |
 |  Methods defined here:
 |
 |  __abs__(self, /)
........................... nan_to_num ...........................
Help on _ArrayFunctionDispatcher in module numpy:

nan_to_num(x, copy=True, nan=0.0, posinf=None, neginf=None)
    Replace NaN with zero and infinity with large finite numbers (default
    behaviour) or with the numbers defined by the user using the `nan`,
    `posinf` and/or `neginf` keywords.

    If `x` is inexact, NaN is replaced by zero or by the user defined value in
    `nan` keyword, infinity is replaced by the largest finite floating point
    values representable by ``x.dtype`` or by the user defined value in
........................... nanargmax ...........................
Help on _ArrayFunctionDispatcher in module numpy:

nanargmax(a, axis=None, out=None, *, keepdims=<no value>)
    Return the indices of the maximum values in the specified axis ignoring
    NaNs. For all-NaN slices ``ValueError`` is raised. Warning: the
    results cannot be trusted if a slice contains only NaNs and -Infs.


    Parameters
    ----------
........................... nanargmin ...........................
Help on _ArrayFunctionDispatcher in module numpy:

nanargmin(a, axis=None, out=None, *, keepdims=<no value>)
    Return the indices of the minimum values in the specified axis ignoring
    NaNs. For all-NaN slices ``ValueError`` is raised. Warning: the results
    cannot be trusted if a slice contains only NaNs and Infs.

    Parameters
    ----------
    a : array_like
........................... nancumprod ...........................
Help on _ArrayFunctionDispatcher in module numpy:

nancumprod(a, axis=None, dtype=None, out=None)
    Return the cumulative product of array elements over a given axis treating Not a
    Numbers (NaNs) as one.  The cumulative product does not change when NaNs are
    encountered and leading NaNs are replaced by ones.

    Ones are returned for slices that are all-NaN or empty.

    Parameters
........................... nancumsum ...........................
Help on _ArrayFunctionDispatcher in module numpy:

nancumsum(a, axis=None, dtype=None, out=None)
    Return the cumulative sum of array elements over a given axis treating Not a
    Numbers (NaNs) as zero.  The cumulative sum does not change when NaNs are
    encountered and leading NaNs are replaced by zeros.

    Zeros are returned for slices that are all-NaN or empty.

    Parameters
........................... nanmax ...........................
Help on _ArrayFunctionDispatcher in module numpy:

nanmax(
    a,
    axis=None,
    out=None,
    keepdims=<no value>,
    initial=<no value>,
    where=<no value>
)
........................... nanmean ...........................
Help on _ArrayFunctionDispatcher in module numpy:

nanmean(
    a,
    axis=None,
    dtype=None,
    out=None,
    keepdims=<no value>,
    *,
    where=<no value>
........................... nanmedian ...........................
Help on _ArrayFunctionDispatcher in module numpy:

nanmedian(a, axis=None, out=None, overwrite_input=False, keepdims=<no value>)
    Compute the median along the specified axis, while ignoring NaNs.

    Returns the median of the array elements.

    Parameters
    ----------
    a : array_like
........................... nanmin ...........................
Help on _ArrayFunctionDispatcher in module numpy:

nanmin(
    a,
    axis=None,
    out=None,
    keepdims=<no value>,
    initial=<no value>,
    where=<no value>
)
........................... nanpercentile ...........................
Help on _ArrayFunctionDispatcher in module numpy:

nanpercentile(
    a,
    q,
    axis=None,
    out=None,
    overwrite_input=False,
    method='linear',
    keepdims=<no value>,
........................... nanprod ...........................
Help on _ArrayFunctionDispatcher in module numpy:

nanprod(
    a,
    axis=None,
    dtype=None,
    out=None,
    keepdims=<no value>,
    initial=<no value>,
    where=<no value>
........................... nanquantile ...........................
Help on _ArrayFunctionDispatcher in module numpy:

nanquantile(
    a,
    q,
    axis=None,
    out=None,
    overwrite_input=False,
    method='linear',
    keepdims=<no value>,
........................... nanstd ...........................
Help on _ArrayFunctionDispatcher in module numpy:

nanstd(
    a,
    axis=None,
    dtype=None,
    out=None,
    ddof=0,
    keepdims=<no value>,
    *,
........................... nansum ...........................
Help on _ArrayFunctionDispatcher in module numpy:

nansum(
    a,
    axis=None,
    dtype=None,
    out=None,
    keepdims=<no value>,
    initial=<no value>,
    where=<no value>
........................... nanvar ...........................
Help on _ArrayFunctionDispatcher in module numpy:

nanvar(
    a,
    axis=None,
    dtype=None,
    out=None,
    ddof=0,
    keepdims=<no value>,
    *,
........................... ndarray ...........................
Help on class ndarray in module numpy:

class ndarray(builtins.object)
 |  ndarray(shape, dtype=float, buffer=None, offset=0,
 |          strides=None, order=None)
 |
 |  An array object represents a multidimensional, homogeneous array
 |  of fixed-size items.  An associated data-type object describes the
 |  format of each element in the array (its byte-order, how many bytes it
 |  occupies in memory, whether it is an integer, a floating point number,
........................... ndenumerate ...........................
Help on class ndenumerate in module numpy:

class ndenumerate(builtins.object)
 |  ndenumerate(arr)
 |
 |  Multidimensional index iterator.
 |
 |  Return an iterator yielding pairs of array coordinates and values.
 |
 |  Parameters
........................... ndim ...........................
Help on _ArrayFunctionDispatcher in module numpy:

ndim(a)
    Return the number of dimensions of an array.

    Parameters
    ----------
    a : array_like
        Input array.  If it is not already an ndarray, a conversion is
        attempted.
........................... ndindex ...........................
Help on class ndindex in module numpy:

class ndindex(builtins.object)
 |  ndindex(*shape)
 |
 |  An N-dimensional iterator object to index arrays.
 |
 |  Given the shape of an array, an `ndindex` instance iterates over
 |  the N-dimensional index of the array. At each iteration a tuple
 |  of indices is returned, the last dimension is iterated over first.
........................... nditer ...........................
Help on class nditer in module numpy:

class nditer(builtins.object)
 |  nditer(op, flags=None, op_flags=None, op_dtypes=None, order='K',
 |      casting='safe', op_axes=None, itershape=None, buffersize=0)
 |
 |  Efficient multi-dimensional iterator object to iterate over arrays.
 |  To get started using this object, see the
 |  :ref:`introductory guide to array iteration <arrays.nditer>`.
 |
........................... negative ...........................
Help on ufunc in module numpy:

negative = <ufunc 'negative'>
    negative(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Numerical negative, element-wise.

    Parameters
    ----------
    x : array_like or scalar
........................... nested_iters ...........................
Help on built-in function nested_iters in module numpy:

nested_iters(...)
    nested_iters(op, axes, flags=None, op_flags=None, op_dtypes=None,     order="K", casting="safe", buffersize=0)

    Create nditers for use in nested loops

    Create a tuple of `nditer` objects which iterate in nested loops over
    different axes of the op argument. The first iterator is used in the
    outermost loop, the last in the innermost loop. Advancing one will change
........................... newaxis ...........................
Help on NoneType object:

class NoneType(object)
 |  The type of the None singleton.
 |
 |  Methods defined here:
 |
 |  __bool__(self, /)
 |      True if self else False
 |
........................... nextafter ...........................
Help on ufunc in module numpy:

nextafter = <ufunc 'nextafter'>
    nextafter(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Return the next floating-point value after x1 towards x2, element-wise.

    Parameters
    ----------
    x1 : array_like
........................... nonzero ...........................
Help on _ArrayFunctionDispatcher in module numpy:

nonzero(a)
    Return the indices of the elements that are non-zero.

    Returns a tuple of arrays, one for each dimension of `a`,
    containing the indices of the non-zero elements in that
    dimension. The values in `a` are always tested and returned in
    row-major, C-style order.

........................... not_equal ...........................
Help on ufunc in module numpy:

not_equal = <ufunc 'not_equal'>
    not_equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Return (x1 != x2) element-wise.

    Parameters
    ----------
    x1, x2 : array_like
........................... number ...........................
Help on class number in module numpy:

class number(generic)
 |  Abstract base class of all numeric scalar types.
 |
 |  Method resolution order:
 |      number
 |      generic
 |      builtins.object
 |
........................... object_ ...........................
Help on class object_ in module numpy:

class object_(generic)
 |  Any Python object.
 |
 |  :Character code: ``'O'``
 |
 |  Method resolution order:
 |      object_
 |      generic
........................... ogrid ...........................
Help on OGridClass in module numpy.lib._index_tricks_impl object:

class OGridClass(nd_grid)
 |  An instance which returns an open multi-dimensional "meshgrid".
 |
 |  An instance which returns an open (i.e. not fleshed out) mesh-grid
 |  when indexed, so that only one dimension of each returned array is
 |  greater than 1.  The dimension and number of the output arrays are
 |  equal to the number of indexing dimensions.  If the step length is
 |  not a complex number, then the stop is not inclusive.
........................... ones ...........................
Help on function ones in module numpy:

ones(shape, dtype=None, order='C', *, device=None, like=None)
    Return a new array of given shape and type, filled with ones.

    Parameters
    ----------
    shape : int or sequence of ints
        Shape of the new array, e.g., ``(2, 3)`` or ``2``.
    dtype : data-type, optional
........................... ones_like ...........................
Help on _ArrayFunctionDispatcher in module numpy:

ones_like(a, dtype=None, order='K', subok=True, shape=None, *, device=None)
    Return an array of ones with the same shape and type as a given array.

    Parameters
    ----------
    a : array_like
        The shape and data-type of `a` define these same attributes of
        the returned array.
........................... outer ...........................
Help on _ArrayFunctionDispatcher in module numpy:

outer(a, b, out=None)
    Compute the outer product of two vectors.

    Given two vectors `a` and `b` of length ``M`` and ``N``, respectively,
    the outer product [1]_ is::

      [[a_0*b_0  a_0*b_1 ... a_0*b_{N-1} ]
       [a_1*b_0    .
........................... packbits ...........................
Help on _ArrayFunctionDispatcher in module numpy:

packbits(...)
    packbits(a, /, axis=None, bitorder='big')

    Packs the elements of a binary-valued array into bits in a uint8 array.

    The result is padded to full bytes by inserting zero bits at the end.

    Parameters
........................... pad ...........................
Help on _ArrayFunctionDispatcher in module numpy:

pad(array, pad_width, mode='constant', **kwargs)
    Pad an array.

    Parameters
    ----------
    array : array_like of rank N
        The array to pad.
    pad_width : {sequence, array_like, int}
........................... partition ...........................
Help on _ArrayFunctionDispatcher in module numpy:

partition(a, kth, axis=-1, kind='introselect', order=None)
    Return a partitioned copy of an array.

    Creates a copy of the array and partially sorts it in such a way that
    the value of the element in k-th position is in the position it would be
    in a sorted array. In the output array, all elements smaller than the k-th
    element are located to the left of this element and all equal or greater
    are located to its right. The ordering of the elements in the two
    ................. ....... ............. ............ .......
       kind            speed   worst case    work space  stable
    ================= ======= ============= ============ =======
    'introselect'        1        O(n)           0         no
    ================= ======= ============= ============ =======

    All the partition algorithms make temporary copies of the data when
    partitioning along any but the last axis.  Consequently,
    partitioning along the last axis is faster and uses less space than
    partitioning along any other axis.

........................... percentile ...........................
Help on _ArrayFunctionDispatcher in module numpy:

percentile(
    a,
    q,
    axis=None,
    out=None,
    overwrite_input=False,
    method='linear',
    keepdims=False,
........................... permute_dims ...........................
Help on _ArrayFunctionDispatcher in module numpy:

transpose(a, axes=None)
    Returns an array with axes transposed.

    For a 1-D array, this returns an unchanged view of the original array, as a
    transposed vector is simply the same vector.
    To convert a 1-D array into a 2-D column vector, an additional dimension
    must be added, e.g., ``np.atleast_2d(a).T`` achieves this, as does
    ``a[:, np.newaxis]``.
........................... pi ...........................
Help on float object:

class float(object)
 |  float(x=0, /)
 |
 |  Convert a string or number to a floating-point number, if possible.
 |
 |  Methods defined here:
 |
 |  __abs__(self, /)
........................... piecewise ...........................
Help on _ArrayFunctionDispatcher in module numpy:

piecewise(x, condlist, funclist, *args, **kw)
    Evaluate a piecewise-defined function.

    Given a set of conditions and corresponding functions, evaluate each
    function on the input data wherever its condition is true.

    Parameters
    ----------
........................... place ...........................
Help on _ArrayFunctionDispatcher in module numpy:

place(arr, mask, vals)
    Change elements of an array based on conditional and input values.

    Similar to ``np.copyto(arr, vals, where=mask)``, the difference is that
    `place` uses the first N elements of `vals`, where N is the number of
    True values in `mask`, while `copyto` uses the elements where `mask`
    is True.

........................... poly ...........................
Help on _ArrayFunctionDispatcher in module numpy:

poly(seq_of_zeros)
    Find the coefficients of a polynomial with the given sequence of roots.

    .. note::
       This forms part of the old polynomial API. Since version 1.4, the
       new polynomial API defined in `numpy.polynomial` is preferred.
       A summary of the differences can be found in the
       :doc:`transition guide </reference/routines.polynomials>`.
........................... poly1d ...........................
Help on class poly1d in module numpy:

class poly1d(builtins.object)
 |  poly1d(c_or_r, r=False, variable=None)
 |
 |  A one-dimensional polynomial class.
 |
 |  .. note::
 |     This forms part of the old polynomial API. Since version 1.4, the
 |     new polynomial API defined in `numpy.polynomial` is preferred.
........................... polyadd ...........................
Help on _ArrayFunctionDispatcher in module numpy:

polyadd(a1, a2)
    Find the sum of two polynomials.

    .. note::
       This forms part of the old polynomial API. Since version 1.4, the
       new polynomial API defined in `numpy.polynomial` is preferred.
       A summary of the differences can be found in the
       :doc:`transition guide </reference/routines.polynomials>`.
........................... polyder ...........................
Help on _ArrayFunctionDispatcher in module numpy:

polyder(p, m=1)
    Return the derivative of the specified order of a polynomial.

    .. note::
       This forms part of the old polynomial API. Since version 1.4, the
       new polynomial API defined in `numpy.polynomial` is preferred.
       A summary of the differences can be found in the
       :doc:`transition guide </reference/routines.polynomials>`.
........................... polydiv ...........................
Help on _ArrayFunctionDispatcher in module numpy:

polydiv(u, v)
    Returns the quotient and remainder of polynomial division.

    .. note::
       This forms part of the old polynomial API. Since version 1.4, the
       new polynomial API defined in `numpy.polynomial` is preferred.
       A summary of the differences can be found in the
       :doc:`transition guide </reference/routines.polynomials>`.
........................... polyfit ...........................
Help on _ArrayFunctionDispatcher in module numpy:

polyfit(x, y, deg, rcond=None, full=False, w=None, cov=False)
    Least squares polynomial fit.

    .. note::
       This forms part of the old polynomial API. Since version 1.4, the
       new polynomial API defined in `numpy.polynomial` is preferred.
       A summary of the differences can be found in the
       :doc:`transition guide </reference/routines.polynomials>`.
........................... polyint ...........................
Help on _ArrayFunctionDispatcher in module numpy:

polyint(p, m=1, k=None)
    Return an antiderivative (indefinite integral) of a polynomial.

    .. note::
       This forms part of the old polynomial API. Since version 1.4, the
       new polynomial API defined in `numpy.polynomial` is preferred.
       A summary of the differences can be found in the
       :doc:`transition guide </reference/routines.polynomials>`.
........................... polymul ...........................
Help on _ArrayFunctionDispatcher in module numpy:

polymul(a1, a2)
    Find the product of two polynomials.

    .. note::
       This forms part of the old polynomial API. Since version 1.4, the
       new polynomial API defined in `numpy.polynomial` is preferred.
       A summary of the differences can be found in the
       :doc:`transition guide </reference/routines.polynomials>`.
........................... polynomial ...........................
Help on package numpy.polynomial in numpy:

NAME
    numpy.polynomial - A sub-package for efficiently dealing with polynomials.

DESCRIPTION
    Within the documentation for this sub-package, a "finite power series,"
    i.e., a polynomial (also referred to simply as a "series") is represented
    by a 1-D numpy array of the polynomial's coefficients, ordered from lowest
    order term to highest.  For example, array([1,2,3]) represents
    ........................    ................
    **Name**                    **Provides**
    ========================    ================
    `~polynomial.Polynomial`    Power series
    `~chebyshev.Chebyshev`      Chebyshev series
    `~legendre.Legendre`        Legendre series
    `~laguerre.Laguerre`        Laguerre series
    `~hermite.Hermite`          Hermite series
    `~hermite_e.HermiteE`       HermiteE series
    ========================    ================

    ...................

    The following lists the various constants and methods common to all of
    the classes representing the various kinds of polynomials. In the following,
    the term ``Poly`` represents any one of the convenience classes (e.g.
    `~polynomial.Polynomial`, `~chebyshev.Chebyshev`, `~hermite.Hermite`, etc.)
    while the lowercase ``p`` represents an **instance** of a polynomial class.

    Constants
    ---------

........................... polysub ...........................
Help on _ArrayFunctionDispatcher in module numpy:

polysub(a1, a2)
    Difference (subtraction) of two polynomials.

    .. note::
       This forms part of the old polynomial API. Since version 1.4, the
       new polynomial API defined in `numpy.polynomial` is preferred.
       A summary of the differences can be found in the
       :doc:`transition guide </reference/routines.polynomials>`.
........................... polyval ...........................
Help on _ArrayFunctionDispatcher in module numpy:

polyval(p, x)
    Evaluate a polynomial at specific values.

    .. note::
       This forms part of the old polynomial API. Since version 1.4, the
       new polynomial API defined in `numpy.polynomial` is preferred.
       A summary of the differences can be found in the
       :doc:`transition guide </reference/routines.polynomials>`.
........................... positive ...........................
Help on ufunc in module numpy:

positive = <ufunc 'positive'>
    positive(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Numerical positive, element-wise.

    Parameters
    ----------
    x : array_like or scalar
........................... pow ...........................
Help on ufunc in module numpy:

power = <ufunc 'power'>
    power(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    First array elements raised to powers from second array, element-wise.

    Raise each base in `x1` to the positionally-corresponding power in
    `x2`.  `x1` and `x2` must be broadcastable to the same shape.

........................... power ...........................
Help on ufunc in module numpy:

power = <ufunc 'power'>
    power(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    First array elements raised to powers from second array, element-wise.

    Raise each base in `x1` to the positionally-corresponding power in
    `x2`.  `x1` and `x2` must be broadcastable to the same shape.

........................... printoptions ...........................
Help on function printoptions in module numpy:

printoptions(*args, **kwargs)
    Context manager for setting print options.

    Set print options for the scope of the `with` block, and restore the old
    options at the end. See `set_printoptions` for the full description of
    available options.

    Examples
........................... prod ...........................
Help on _ArrayFunctionDispatcher in module numpy:

prod(
    a,
    axis=None,
    dtype=None,
    out=None,
    keepdims=<no value>,
    initial=<no value>,
    where=<no value>
........................... promote_types ...........................
Help on built-in function promote_types in module numpy:

promote_types(...)
    promote_types(type1, type2)

    Returns the data type with the smallest size and smallest scalar
    kind to which both ``type1`` and ``type2`` may be safely cast.
    The returned data type is always considered "canonical", this mainly
    means that the promoted dtype will always be in native byte order.

........................... ptp ...........................
Help on _ArrayFunctionDispatcher in module numpy:

ptp(a, axis=None, out=None, keepdims=<no value>)
    Range of values (maximum - minimum) along an axis.

    The name of the function comes from the acronym for 'peak to peak'.

    .. warning::
        `ptp` preserves the data type of the array. This means the
        return value for an input of signed integers with n bits
........................... put ...........................
Help on _ArrayFunctionDispatcher in module numpy:

put(a, ind, v, mode='raise')
    Replaces specified elements of an array with given values.

    The indexing works on the flattened target array. `put` is roughly
    equivalent to:

    ::

........................... put_along_axis ...........................
Help on _ArrayFunctionDispatcher in module numpy:

put_along_axis(arr, indices, values, axis)
    Put values into the destination array by matching 1d index and data slices.

    This iterates over matching 1d slices oriented along the specified axis in
    the index and data arrays, and uses the former to place values into the
    latter. These slices can be different lengths.

    Functions returning an index along an axis, like `argsort` and
........................... putmask ...........................
Help on _ArrayFunctionDispatcher in module numpy:

putmask(...)
    putmask(a, mask, values)

    Changes elements of an array based on conditional and input values.

    Sets ``a.flat[n] = values[n]`` for each n where ``mask.flat[n]==True``.

    If `values` is not the same size as `a` and `mask` then it will repeat.
........................... quantile ...........................
Help on _ArrayFunctionDispatcher in module numpy:

quantile(
    a,
    q,
    axis=None,
    out=None,
    overwrite_input=False,
    method='linear',
    keepdims=False,
    ............................... ............... ...............
    ``method``                      number in H&F   ``m``
    =============================== =============== ===============
    ``interpolated_inverted_cdf``   4               ``0``
    ``hazen``                       5               ``1/2``
    ``weibull``                     6               ``q``
    ``linear`` (default)            7               ``1 - q``
    ``median_unbiased``             8               ``q/3 + 1/3``
    ``normal_unbiased``             9               ``q/4 + 3/8``
    =============================== =============== ===============

........................... r_ ...........................
Help on RClass in module numpy.lib._index_tricks_impl object:

class RClass(AxisConcatenator)
 |  Translates slice objects to concatenation along the first axis.
 |
 |  This is a simple way to build up arrays quickly. There are two use cases.
 |
 |  1. If the index expression contains comma separated arrays, then stack
 |     them along their first axis.
 |  2. If the index expression contains slice notation or scalars then create
........................... rad2deg ...........................
Help on ufunc in module numpy:

rad2deg = <ufunc 'rad2deg'>
    rad2deg(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Convert angles from radians to degrees.

    Parameters
    ----------
    x : array_like
........................... radians ...........................
Help on ufunc in module numpy:

radians = <ufunc 'radians'>
    radians(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Convert angles from degrees to radians.

    Parameters
    ----------
    x : array_like
........................... random ...........................
Help on package numpy.random in numpy:

NAME
    numpy.random

DESCRIPTION
    ========================
    Random Number Generation
    ========================

    ............... .........................................................
    Generator
    --------------- ---------------------------------------------------------
    Generator       Class implementing all of the random number distributions
    default_rng     Default constructor for ``Generator``
    =============== =========================================================

    ============================================= ===
    BitGenerator Streams that work with Generator
    --------------------------------------------- ---
    MT19937
    ............................................. ...

    ============================================= ===
    Getting entropy to initialize a BitGenerator
    --------------------------------------------- ---
    SeedSequence
    ============================================= ===


    Legacy
    ------
    .................... .........................................................
    Utility functions
    -------------------- ---------------------------------------------------------
    random               Uniformly distributed floats over ``[0, 1)``
    bytes                Uniformly distributed random bytes.
    permutation          Randomly permute a sequence / generate a random sequence.
    shuffle              Randomly permute a sequence in place.
    choice               Random sample from 1-D array.
    ==================== =========================================================

    ==================== =========================================================
    .................... .........................................................

    ==================== =========================================================
    Univariate
    distributions
    -------------------- ---------------------------------------------------------
    beta                 Beta distribution over ``[0, 1]``.
    binomial             Binomial distribution.
    chisquare            :math:`\chi^2` distribution.
    exponential          Exponential distribution.
    f                    F (Fisher-Snedecor) distribution.
    .................... .........................................................

    ==================== ==========================================================
    Multivariate
    distributions
    -------------------- ----------------------------------------------------------
    dirichlet            Multivariate generalization of Beta distribution.
    multinomial          Multivariate generalization of the binomial distribution.
    multivariate_normal  Multivariate generalization of the normal distribution.
    ==================== ==========================================================

    .................... .........................................................
    Standard
    distributions
    -------------------- ---------------------------------------------------------
    standard_cauchy      Standard Cauchy-Lorentz distribution.
    standard_exponential Standard exponential distribution.
    standard_gamma       Standard Gamma distribution.
    standard_normal      Standard normal distribution.
    standard_t           Standard Student's t-distribution.
    ==================== =========================================================

    .................... .........................................................
    Internal functions
    -------------------- ---------------------------------------------------------
    get_state            Get tuple representing internal state of generator.
    set_state            Set state of generator.
    ==================== =========================================================

PACKAGE CONTENTS
    _bounded_integers
    _common
    _generator
........................... ravel ...........................
Help on _ArrayFunctionDispatcher in module numpy:

ravel(a, order='C')
    Return a contiguous flattened array.

    A 1-D array, containing the elements of the input, is returned.  A copy is
    made only if needed.

    As of NumPy 1.10, the returned array will have the same type as the input
    array. (for example, a masked array will be returned for a masked array
........................... ravel_multi_index ...........................
Help on _ArrayFunctionDispatcher in module numpy:

ravel_multi_index(...)
    ravel_multi_index(multi_index, dims, mode='raise', order='C')

    Converts a tuple of index arrays into an array of flat
    indices, applying boundary modes to the multi-index.

    Parameters
    ----------
........................... real ...........................
Help on _ArrayFunctionDispatcher in module numpy:

real(val)
    Return the real part of the complex argument.

    Parameters
    ----------
    val : array_like
        Input array.

........................... real_if_close ...........................
Help on _ArrayFunctionDispatcher in module numpy:

real_if_close(a, tol=100)
    If input is complex with all imaginary parts close to zero, return
    real parts.

    "Close to zero" is defined as `tol` * (machine epsilon of the type for
    `a`).

    Parameters
........................... rec ...........................
Help on package numpy.rec in numpy:

NAME
    numpy.rec - This module contains a set of functions for record arrays.

PACKAGE CONTENTS


CLASSES
    builtins.object
........................... recarray ...........................
Help on class recarray in module numpy.rec:

class recarray(numpy.ndarray)
 |  recarray(
 |      shape,
 |      dtype=None,
 |      buf=None,
 |      offset=0,
 |      strides=None,
 |      formats=None,
........................... reciprocal ...........................
Help on ufunc in module numpy:

reciprocal = <ufunc 'reciprocal'>
    reciprocal(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Return the reciprocal of the argument, element-wise.

    Calculates ``1/x``.

    Parameters
........................... record ...........................
Help on class record in module numpy:

class record(void)
 |  A data-type scalar that allows field access as attribute lookup.
 |
 |  Method resolution order:
 |      record
 |      void
 |      flexible
 |      generic
........................... remainder ...........................
Help on ufunc in module numpy:

remainder = <ufunc 'remainder'>
    remainder(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Returns the element-wise remainder of division.

    Computes the remainder complementary to the `floor_divide` function.  It is
    equivalent to the Python modulus operator ``x1 % x2`` and has the same sign
    as the divisor `x2`. The MATLAB function equivalent to ``np.remainder``
........................... repeat ...........................
Help on _ArrayFunctionDispatcher in module numpy:

repeat(a, repeats, axis=None)
    Repeat each element of an array after themselves

    Parameters
    ----------
    a : array_like
        Input array.
    repeats : int or array of ints
........................... require ...........................
Help on function require in module numpy:

require(a, dtype=None, requirements=None, *, like=None)
    Return an ndarray of the provided type that satisfies requirements.

    This function is useful to be sure that an array with the correct flags
    is returned for passing to compiled code (perhaps through ctypes).

    Parameters
    ----------
........................... reshape ...........................
Help on _ArrayFunctionDispatcher in module numpy:

reshape(a, /, shape=None, order='C', *, newshape=None, copy=None)
    Gives a new shape to an array without changing its data.

    Parameters
    ----------
    a : array_like
        Array to be reshaped.
    shape : int or tuple of ints
........................... resize ...........................
Help on _ArrayFunctionDispatcher in module numpy:

resize(a, new_shape)
    Return a new array with the specified shape.

    If the new array is larger than the original array, then the new
    array is filled with repeated copies of `a`.  Note that this behavior
    is different from a.resize(new_shape) which fills with zeros instead
    of repeated copies of `a`.

........................... result_type ...........................
Help on _ArrayFunctionDispatcher in module numpy:

result_type(...)
    result_type(*arrays_and_dtypes)

    Returns the type that results from applying the NumPy
    type promotion rules to the arguments.

    Type promotion in NumPy works similarly to the rules in languages
    like C++, with some slight differences.  When both scalars and
........................... right_shift ...........................
Help on ufunc in module numpy:

right_shift = <ufunc 'right_shift'>
    right_shift(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Shift the bits of an integer to the right.

    Bits are shifted to the right `x2`.  Because the internal
    representation of numbers is in binary format, this operation is
    equivalent to dividing `x1` by ``2**x2``.
........................... rint ...........................
Help on ufunc in module numpy:

rint = <ufunc 'rint'>
    rint(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Round elements of the array to the nearest integer.

    Parameters
    ----------
    x : array_like
........................... roll ...........................
Help on _ArrayFunctionDispatcher in module numpy:

roll(a, shift, axis=None)
    Roll array elements along a given axis.

    Elements that roll beyond the last position are re-introduced at
    the first.

    Parameters
    ----------
........................... rollaxis ...........................
Help on _ArrayFunctionDispatcher in module numpy:

rollaxis(a, axis, start=0)
    Roll the specified axis backwards, until it lies in a given position.

    This function continues to be supported for backward compatibility, but you
    should prefer `moveaxis`. The `moveaxis` function was added in NumPy
    1.11.

    Parameters
           +...................+......................+
           | ``-(arr.ndim+1)`` | raise ``AxisError``  |
           +-------------------+----------------------+
           | ``-arr.ndim``     | 0                    |
           +-------------------+----------------------+
           | |vdots|           | |vdots|              |
           +-------------------+----------------------+
           | ``-1``            | ``arr.ndim-1``       |
           +-------------------+----------------------+
           | ``0``             | ``0``                |
           +-------------------+----------------------+
........................... roots ...........................
Help on _ArrayFunctionDispatcher in module numpy:

roots(p)
    Return the roots of a polynomial with coefficients given in p.

    .. note::
       This forms part of the old polynomial API. Since version 1.4, the
       new polynomial API defined in `numpy.polynomial` is preferred.
       A summary of the differences can be found in the
       :doc:`transition guide </reference/routines.polynomials>`.
........................... rot90 ...........................
Help on _ArrayFunctionDispatcher in module numpy:

rot90(m, k=1, axes=(0, 1))
    Rotate an array by 90 degrees in the plane specified by axes.

    Rotation direction is from the first towards the second axis.
    This means for a 2D array with the default `k` and `axes`, the
    rotation will be counterclockwise.

    Parameters
........................... round ...........................
Help on _ArrayFunctionDispatcher in module numpy:

round(a, decimals=0, out=None)
    Evenly round to the given number of decimals.

    Parameters
    ----------
    a : array_like
        Input data.
    decimals : int, optional
........................... row_stack ...........................
Help on function row_stack in module numpy:

row_stack(tup, *, dtype=None, casting='same_kind')
    Stack arrays in sequence vertically (row wise).

    This is equivalent to concatenation along the first axis after 1-D arrays
    of shape `(N,)` have been reshaped to `(1,N)`. Rebuilds arrays divided by
    `vsplit`.

    This function makes most sense for arrays with up to 3 dimensions. For
........................... s_ ...........................
Help on IndexExpression in module numpy.lib._index_tricks_impl object:

class IndexExpression(builtins.object)
 |  IndexExpression(maketuple)
 |
 |  A nicer way to build up index tuples for arrays.
 |
 |  .. note::
 |     Use one of the two predefined instances ``index_exp`` or `s_`
 |     rather than directly using `IndexExpression`.
........................... save ...........................
Help on _ArrayFunctionDispatcher in module numpy:

save(file, arr, allow_pickle=True, fix_imports=<no value>)
    Save an array to a binary file in NumPy ``.npy`` format.

    Parameters
    ----------
    file : file, str, or pathlib.Path
        File or filename to which the data is saved. If file is a file-object,
        then the filename is unchanged.  If file is a string or Path,
........................... savetxt ...........................
Help on _ArrayFunctionDispatcher in module numpy:

savetxt(
    fname,
    X,
    fmt='%.18e',
    delimiter=' ',
    newline='\n',
    header='',
    footer='',
........................... savez ...........................
Help on _ArrayFunctionDispatcher in module numpy:

savez(file, *args, allow_pickle=True, **kwds)
    Save several arrays into a single file in uncompressed ``.npz`` format.

    Provide arrays as keyword arguments to store them under the
    corresponding name in the output file: ``savez(fn, x=x, y=y)``.

    If arrays are specified as positional arguments, i.e., ``savez(fn,
    x, y)``, their names will be `arr_0`, `arr_1`, etc.
........................... savez_compressed ...........................
Help on _ArrayFunctionDispatcher in module numpy:

savez_compressed(file, *args, allow_pickle=True, **kwds)
    Save several arrays into a single file in compressed ``.npz`` format.

    Provide arrays as keyword arguments to store them under the
    corresponding name in the output file: ``savez_compressed(fn, x=x, y=y)``.

    If arrays are specified as positional arguments, i.e.,
    ``savez_compressed(fn, x, y)``, their names will be `arr_0`, `arr_1`, etc.
........................... sctypeDict ...........................
Help on dict object:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
........................... searchsorted ...........................
Help on _ArrayFunctionDispatcher in module numpy:

searchsorted(a, v, side='left', sorter=None)
    Find indices where elements should be inserted to maintain order.

    Find the indices into a sorted array `a` such that, if the
    corresponding elements in `v` were inserted before the indices, the
    order of `a` would be preserved.

    Assuming that `a` is sorted:
    ......  ............................
    `side`  returned index `i` satisfies
    ======  ============================
    left    ``a[i-1] < v <= a[i]``
    right   ``a[i-1] <= v < a[i]``
    ======  ============================

    Parameters
    ----------
    a : 1-D array_like
        Input array. If `sorter` is None, then it must be sorted in
........................... select ...........................
Help on _ArrayFunctionDispatcher in module numpy:

select(condlist, choicelist, default=0)
    Return an array drawn from elements in choicelist, depending on conditions.

    Parameters
    ----------
    condlist : list of bool ndarrays
        The list of conditions which determine from which array in `choicelist`
        the output elements are taken. When multiple conditions are satisfied,
........................... set_printoptions ...........................
Help on function set_printoptions in module numpy:

set_printoptions(
    precision=None,
    threshold=None,
    edgeitems=None,
    linewidth=None,
    suppress=None,
    nanstr=None,
    infstr=None,
........................... setbufsize ...........................
Help on function setbufsize in module numpy:

setbufsize(size)
    Set the size of the buffer used in ufuncs.

    .. versionchanged:: 2.0
        The scope of setting the buffer is tied to the `numpy.errstate`
        context.  Exiting a ``with errstate():`` will also restore the bufsize.

    Parameters
........................... setdiff1d ...........................
Help on _ArrayFunctionDispatcher in module numpy:

setdiff1d(ar1, ar2, assume_unique=False)
    Find the set difference of two arrays.

    Return the unique values in `ar1` that are not in `ar2`.

    Parameters
    ----------
    ar1 : array_like
........................... seterr ...........................
Help on function seterr in module numpy:

seterr(all=None, divide=None, over=None, under=None, invalid=None)
    Set how floating-point errors are handled.

    Note that operations on integer scalar types (such as `int16`) are
    handled like floating point, and are affected by these settings.

    Parameters
    ----------
........................... seterrcall ...........................
Help on function seterrcall in module numpy:

seterrcall(func)
    Set the floating-point error callback function or log object.

    There are two ways to capture floating-point error messages.  The first
    is to set the error-handler to 'call', using `seterr`.  Then, set
    the function to call using this function.

    The second is to set the error-handler to 'log', using `seterr`.
........................... setxor1d ...........................
Help on _ArrayFunctionDispatcher in module numpy:

setxor1d(ar1, ar2, assume_unique=False)
    Find the set exclusive-or of two arrays.

    Return the sorted, unique values that are in only one (not both) of the
    input arrays.

    Parameters
    ----------
........................... shape ...........................
Help on _ArrayFunctionDispatcher in module numpy:

shape(a)
    Return the shape of an array.

    Parameters
    ----------
    a : array_like
        Input array.

........................... shares_memory ...........................
Help on _ArrayFunctionDispatcher in module numpy:

shares_memory(...)
    shares_memory(a, b, /, max_work=None)

    Determine if two arrays share memory.

    .. warning::

       This function can be exponentially slow for some inputs, unless
........................... short ...........................
Help on class int16 in module numpy:

class int16(signedinteger)
 |  Signed integer type, compatible with C ``short``.
 |
 |  :Character code: ``'h'``
 |  :Canonical name: `numpy.short`
 |  :Alias on this platform (Linux x86_64): `numpy.int16`: 16-bit signed integer (``-32_768`` to ``32_767``).
 |
 |  Method resolution order:
........................... show_config ...........................
Help on function show_config in module numpy:

show_config(mode='stdout')
    Show libraries and system information on which NumPy was built
    and is being used

    Parameters
    ----------
    mode : {`'stdout'`, `'dicts'`}, optional.
        Indicates how to display the config information.
........................... show_runtime ...........................
Help on function show_runtime in module numpy:

show_runtime()
    Print information about various resources in the system
    including available intrinsic support and BLAS/LAPACK library
    in use

    .. versionadded:: 1.24.0

    See Also
........................... sign ...........................
Help on ufunc in module numpy:

sign = <ufunc 'sign'>
    sign(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Returns an element-wise indication of the sign of a number.

    The `sign` function returns ``-1 if x < 0, 0 if x==0, 1 if x > 0``.  nan
    is returned for nan inputs.

........................... signbit ...........................
Help on ufunc in module numpy:

signbit = <ufunc 'signbit'>
    signbit(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Returns element-wise True where signbit is set (less than zero).

    Parameters
    ----------
    x : array_like
........................... signedinteger ...........................
Help on class signedinteger in module numpy:

class signedinteger(integer)
 |  Abstract base class of all signed integer scalar types.
 |
 |  Method resolution order:
 |      signedinteger
 |      integer
 |      number
 |      generic
........................... sin ...........................
Help on ufunc in module numpy:

sin = <ufunc 'sin'>
    sin(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Trigonometric sine, element-wise.

    Parameters
    ----------
    x : array_like
........................... sinc ...........................
Help on _ArrayFunctionDispatcher in module numpy:

sinc(x)
    Return the normalized sinc function.

    The sinc function is equal to :math:`\sin(\pi x)/(\pi x)` for any argument
    :math:`x\ne 0`. ``sinc(0)`` takes the limit value 1, making ``sinc`` not
    only everywhere continuous but also infinitely differentiable.

    .. note::
........................... single ...........................
Help on class float32 in module numpy:

class float32(floating)
 |  Single-precision floating-point number type, compatible with C ``float``.
 |
 |  :Character code: ``'f'``
 |  :Canonical name: `numpy.single`
 |  :Alias on this platform (Linux x86_64): `numpy.float32`: 32-bit-precision floating-point number type: sign bit, 8 bits exponent, 23 bits mantissa.
 |
 |  Method resolution order:
........................... sinh ...........................
Help on ufunc in module numpy:

sinh = <ufunc 'sinh'>
    sinh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Hyperbolic sine, element-wise.

    Equivalent to ``1/2 * (np.exp(x) - np.exp(-x))`` or
    ``-1j * np.sin(1j*x)``.

........................... size ...........................
Help on _ArrayFunctionDispatcher in module numpy:

size(a, axis=None)
    Return the number of elements along a given axis.

    Parameters
    ----------
    a : array_like
        Input data.
    axis : int, optional
........................... sort ...........................
Help on _ArrayFunctionDispatcher in module numpy:

sort(a, axis=-1, kind=None, order=None, *, stable=None)
    Return a sorted copy of an array.

    Parameters
    ----------
    a : array_like
        Array to be sorted.
    axis : int or None, optional
........................... sort_complex ...........................
Help on _ArrayFunctionDispatcher in module numpy:

sort_complex(a)
    Sort a complex array using the real part first, then the imaginary part.

    Parameters
    ----------
    a : array_like
        Input array

........................... spacing ...........................
Help on ufunc in module numpy:

spacing = <ufunc 'spacing'>
    spacing(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Return the distance between x and the nearest adjacent number.

    Parameters
    ----------
    x : array_like
........................... split ...........................
Help on _ArrayFunctionDispatcher in module numpy:

split(ary, indices_or_sections, axis=0)
    Split an array into multiple sub-arrays as views into `ary`.

    Parameters
    ----------
    ary : ndarray
        Array to be divided into sub-arrays.
    indices_or_sections : int or 1-D array
........................... sqrt ...........................
Help on ufunc in module numpy:

sqrt = <ufunc 'sqrt'>
    sqrt(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Return the non-negative square-root of an array, element-wise.

    Parameters
    ----------
    x : array_like
........................... square ...........................
Help on ufunc in module numpy:

square = <ufunc 'square'>
    square(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Return the element-wise square of the input.

    Parameters
    ----------
    x : array_like
........................... squeeze ...........................
Help on _ArrayFunctionDispatcher in module numpy:

squeeze(a, axis=None)
    Remove axes of length one from `a`.

    Parameters
    ----------
    a : array_like
        Input data.
    axis : None or int or tuple of ints, optional
........................... stack ...........................
Help on _ArrayFunctionDispatcher in module numpy:

stack(arrays, axis=0, out=None, *, dtype=None, casting='same_kind')
    Join a sequence of arrays along a new axis.

    The ``axis`` parameter specifies the index of the new axis in the
    dimensions of the result. For example, if ``axis=0`` it will be the first
    dimension and if ``axis=-1`` it will be the last dimension.

    Parameters
........................... std ...........................
Help on _ArrayFunctionDispatcher in module numpy:

std(
    a,
    axis=None,
    dtype=None,
    out=None,
    ddof=0,
    keepdims=<no value>,
    *,
........................... str_ ...........................
Help on class str_ in module numpy:

class str_(builtins.str, character)
 |  A unicode string.
 |
 |  This type strips trailing null codepoints.
 |
 |  >>> s = np.str_("abc\x00")
 |  >>> s
 |  'abc'
........................... strings ...........................
Help on package numpy.strings in numpy:

NAME
    numpy.strings

DESCRIPTION
    This module contains a set of functions for vectorized string
    operations.

PACKAGE CONTENTS
........................... subtract ...........................
Help on ufunc in module numpy:

subtract = <ufunc 'subtract'>
    subtract(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Subtract arguments, element-wise.

    Parameters
    ----------
    x1, x2 : array_like
........................... sum ...........................
Help on _ArrayFunctionDispatcher in module numpy:

sum(
    a,
    axis=None,
    dtype=None,
    out=None,
    keepdims=<no value>,
    initial=<no value>,
    where=<no value>
........................... swapaxes ...........................
Help on _ArrayFunctionDispatcher in module numpy:

swapaxes(a, axis1, axis2)
    Interchange two axes of an array.

    Parameters
    ----------
    a : array_like
        Input array.
    axis1 : int
........................... take ...........................
Help on _ArrayFunctionDispatcher in module numpy:

take(a, indices, axis=None, out=None, mode='raise')
    Take elements from an array along an axis.

    When axis is not None, this function does the same thing as "fancy"
    indexing (indexing arrays using arrays); however, it can be easier to use
    if you need elements along a given axis. A call such as
    ``np.take(arr, indices, axis=3)`` is equivalent to
    ``arr[:,:,:,indices,...]``.
........................... take_along_axis ...........................
Help on _ArrayFunctionDispatcher in module numpy:

take_along_axis(arr, indices, axis)
    Take values from the input array by matching 1d index and data slices.

    This iterates over matching 1d slices oriented along the specified axis in
    the index and data arrays, and uses the former to look up values in the
    latter. These slices can be different lengths.

    Functions returning an index along an axis, like `argsort` and
........................... tan ...........................
Help on ufunc in module numpy:

tan = <ufunc 'tan'>
    tan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Compute tangent element-wise.

    Equivalent to ``np.sin(x)/np.cos(x)`` element-wise.

    Parameters
........................... tanh ...........................
Help on ufunc in module numpy:

tanh = <ufunc 'tanh'>
    tanh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Compute hyperbolic tangent element-wise.

    Equivalent to ``np.sinh(x)/np.cosh(x)`` or ``-1j * np.tan(1j*x)``.

    Parameters
........................... tensordot ...........................
Help on _ArrayFunctionDispatcher in module numpy:

tensordot(a, b, axes=2)
    Compute tensor dot product along specified axes.

    Given two tensors, `a` and `b`, and an array_like object containing
    two array_like objects, ``(a_axes, b_axes)``, sum the products of
    `a`'s and `b`'s elements (components) over the axes specified by
    ``a_axes`` and ``b_axes``. The third argument can be a single non-negative
    integer_like scalar, ``N``; if it is such, then the last ``N`` dimensions
........................... test ...........................
Help on PytestTester in module numpy object:

class PytestTester(builtins.object)
 |  PytestTester(module_name)
 |
 |  Pytest test runner.
 |
 |  A test function is typically added to a package's __init__.py like so::
 |
 |    from numpy._pytesttester import PytestTester
........................... testing ...........................
Help on package numpy.testing in numpy:

NAME
    numpy.testing - Common test support for all numpy test scripts.

DESCRIPTION
    This single module should provide all the common functionality for numpy tests
    in a single location, so that test scripts can just import it and work right
    away.

........................... tile ...........................
Help on _ArrayFunctionDispatcher in module numpy:

tile(A, reps)
    Construct an array by repeating A the number of times given by reps.

    If `reps` has length ``d``, the result will have dimension of
    ``max(d, A.ndim)``.

    If ``A.ndim < d``, `A` is promoted to be d-dimensional by prepending new
    axes. So a shape (3,) array is promoted to (1, 3) for 2-D replication,
........................... timedelta64 ...........................
Help on class timedelta64 in module numpy:

class timedelta64(signedinteger)
 |  A timedelta stored as a 64-bit integer.
 |
 |  See :ref:`arrays.datetime` for more information.
 |
 |  :Character code: ``'m'``
 |
 |  Method resolution order:
........................... trace ...........................
Help on _ArrayFunctionDispatcher in module numpy:

trace(a, offset=0, axis1=0, axis2=1, dtype=None, out=None)
    Return the sum along diagonals of the array.

    If `a` is 2-D, the sum along its diagonal with the given offset
    is returned, i.e., the sum of elements ``a[i,i+offset]`` for all i.

    If `a` has more than two dimensions, then the axes specified by axis1 and
    axis2 are used to determine the 2-D sub-arrays whose traces are returned.
........................... transpose ...........................
Help on _ArrayFunctionDispatcher in module numpy:

transpose(a, axes=None)
    Returns an array with axes transposed.

    For a 1-D array, this returns an unchanged view of the original array, as a
    transposed vector is simply the same vector.
    To convert a 1-D array into a 2-D column vector, an additional dimension
    must be added, e.g., ``np.atleast_2d(a).T`` achieves this, as does
    ``a[:, np.newaxis]``.
........................... trapezoid ...........................
Help on _ArrayFunctionDispatcher in module numpy:

trapezoid(y, x=None, dx=1.0, axis=-1)
    Integrate along the given axis using the composite trapezoidal rule.

    If `x` is provided, the integration happens in sequence along its
    elements - they are not sorted.

    Integrate `y` (`x`) along each 1d slice on the given axis, compute
    :math:`\int y(x) dx`.
........................... trapz ...........................
Help on function trapz in module numpy:

trapz(y, x=None, dx=1.0, axis=-1)
    `trapz` is deprecated in NumPy 2.0.

    Please use `trapezoid` instead, or one of the numerical integration
    functions in `scipy.integrate`.

=========================== tri ===========================
Help on function tri in module numpy:
........................... tril ...........................
Help on _ArrayFunctionDispatcher in module numpy:

tril(m, k=0)
    Lower triangle of an array.

    Return a copy of an array with elements above the `k`-th diagonal zeroed.
    For arrays with ``ndim`` exceeding 2, `tril` will apply to the final two
    axes.

    Parameters
........................... tril_indices ...........................
Help on function tril_indices in module numpy:

tril_indices(n, k=0, m=None)
    Return the indices for the lower-triangle of an (n, m) array.

    Parameters
    ----------
    n : int
        The row dimension of the arrays for which the returned
        indices will be valid.
........................... tril_indices_from ...........................
Help on _ArrayFunctionDispatcher in module numpy:

tril_indices_from(arr, k=0)
    Return the indices for the lower-triangle of arr.

    See `tril_indices` for full details.

    Parameters
    ----------
    arr : array_like
........................... trim_zeros ...........................
Help on _ArrayFunctionDispatcher in module numpy:

trim_zeros(filt, trim='fb', axis=None)
    Remove values along a dimension which are zero along all other.

    Parameters
    ----------
    filt : array_like
        Input array.
    trim : {"fb", "f", "b"}, optional
........................... triu ...........................
Help on _ArrayFunctionDispatcher in module numpy:

triu(m, k=0)
    Upper triangle of an array.

    Return a copy of an array with the elements below the `k`-th diagonal
    zeroed. For arrays with ``ndim`` exceeding 2, `triu` will apply to the
    final two axes.

    Please refer to the documentation for `tril` for further details.
........................... triu_indices ...........................
Help on function triu_indices in module numpy:

triu_indices(n, k=0, m=None)
    Return the indices for the upper-triangle of an (n, m) array.

    Parameters
    ----------
    n : int
        The size of the arrays for which the returned indices will
        be valid.
........................... triu_indices_from ...........................
Help on _ArrayFunctionDispatcher in module numpy:

triu_indices_from(arr, k=0)
    Return the indices for the upper-triangle of arr.

    See `triu_indices` for full details.

    Parameters
    ----------
    arr : ndarray, shape(N, N)
........................... true_divide ...........................
Help on ufunc in module numpy:

divide = <ufunc 'divide'>
    divide(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Divide arguments element-wise.

    Parameters
    ----------
    x1 : array_like
........................... trunc ...........................
Help on ufunc in module numpy:

trunc = <ufunc 'trunc'>
    trunc(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

    Return the truncated value of the input, element-wise.

    The truncated value of the scalar `x` is the nearest integer `i` which
    is closer to zero than `x` is. In short, the fractional part of the
    signed number `x` is discarded.
........................... typecodes ...........................
Help on dict object:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
........................... typename ...........................
Help on function typename in module numpy:

typename(char)
    Return a description for the given data type code.

    Parameters
    ----------
    char : str
        Data type code.

........................... typing ...........................
Help on package numpy.typing in numpy:

NAME
    numpy.typing

DESCRIPTION
    ============================
    Typing (:mod:`numpy.typing`)
    ============================

........................... ubyte ...........................
Help on class uint8 in module numpy:

class uint8(unsignedinteger)
 |  Unsigned integer type, compatible with C ``unsigned char``.
 |
 |  :Character code: ``'B'``
 |  :Canonical name: `numpy.ubyte`
 |  :Alias on this platform (Linux x86_64): `numpy.uint8`: 8-bit unsigned integer (``0`` to ``255``).
 |
 |  Method resolution order:
........................... ufunc ...........................
Help on class ufunc in module numpy:

class ufunc(builtins.object)
 |  Functions that operate element by element on whole arrays.
 |
 |  To see the documentation for a specific ufunc, use `info`.  For
 |  example, ``np.info(np.sin)``.  Because ufuncs are written in C
 |  (for speed) and linked into Python with NumPy's ufunc facility,
 |  Python's help() function finds this page whenever help() is called
 |  on a ufunc.
........................... uint ...........................
Help on class uint64 in module numpy:

class uint64(unsignedinteger)
 |  Unsigned signed integer type, 64bit on 64bit systems and 32bit on 32bit
 |  systems.
 |
 |  :Character code: ``'L'``
 |  :Canonical name: `numpy.uint`
 |  :Alias on this platform (Linux x86_64): `numpy.uint64`: 64-bit unsigned integer (``0`` to ``18_446_744_073_709_551_615``).
 |  :Alias on this platform (Linux x86_64): `numpy.uintp`: Unsigned integer large enough to fit pointer, compatible with C ``uintptr_t``.
........................... uint16 ...........................
Help on class uint16 in module numpy:

class uint16(unsignedinteger)
 |  Unsigned integer type, compatible with C ``unsigned short``.
 |
 |  :Character code: ``'H'``
 |  :Canonical name: `numpy.ushort`
 |  :Alias on this platform (Linux x86_64): `numpy.uint16`: 16-bit unsigned integer (``0`` to ``65_535``).
 |
 |  Method resolution order:
........................... uint32 ...........................
Help on class uint32 in module numpy:

class uint32(unsignedinteger)
 |  Unsigned integer type, compatible with C ``unsigned int``.
 |
 |  :Character code: ``'I'``
 |  :Canonical name: `numpy.uintc`
 |  :Alias on this platform (Linux x86_64): `numpy.uint32`: 32-bit unsigned integer (``0`` to ``4_294_967_295``).
 |
 |  Method resolution order:
........................... uint64 ...........................
Help on class uint64 in module numpy:

class uint64(unsignedinteger)
 |  Unsigned signed integer type, 64bit on 64bit systems and 32bit on 32bit
 |  systems.
 |
 |  :Character code: ``'L'``
 |  :Canonical name: `numpy.uint`
 |  :Alias on this platform (Linux x86_64): `numpy.uint64`: 64-bit unsigned integer (``0`` to ``18_446_744_073_709_551_615``).
 |  :Alias on this platform (Linux x86_64): `numpy.uintp`: Unsigned integer large enough to fit pointer, compatible with C ``uintptr_t``.
........................... uint8 ...........................
Help on class uint8 in module numpy:

class uint8(unsignedinteger)
 |  Unsigned integer type, compatible with C ``unsigned char``.
 |
 |  :Character code: ``'B'``
 |  :Canonical name: `numpy.ubyte`
 |  :Alias on this platform (Linux x86_64): `numpy.uint8`: 8-bit unsigned integer (``0`` to ``255``).
 |
 |  Method resolution order:
........................... uintc ...........................
Help on class uint32 in module numpy:

class uint32(unsignedinteger)
 |  Unsigned integer type, compatible with C ``unsigned int``.
 |
 |  :Character code: ``'I'``
 |  :Canonical name: `numpy.uintc`
 |  :Alias on this platform (Linux x86_64): `numpy.uint32`: 32-bit unsigned integer (``0`` to ``4_294_967_295``).
 |
 |  Method resolution order:
........................... uintp ...........................
Help on class uint64 in module numpy:

class uint64(unsignedinteger)
 |  Unsigned signed integer type, 64bit on 64bit systems and 32bit on 32bit
 |  systems.
 |
 |  :Character code: ``'L'``
 |  :Canonical name: `numpy.uint`
 |  :Alias on this platform (Linux x86_64): `numpy.uint64`: 64-bit unsigned integer (``0`` to ``18_446_744_073_709_551_615``).
 |  :Alias on this platform (Linux x86_64): `numpy.uintp`: Unsigned integer large enough to fit pointer, compatible with C ``uintptr_t``.
........................... ulong ...........................
Help on class uint64 in module numpy:

class uint64(unsignedinteger)
 |  Unsigned signed integer type, 64bit on 64bit systems and 32bit on 32bit
 |  systems.
 |
 |  :Character code: ``'L'``
 |  :Canonical name: `numpy.uint`
 |  :Alias on this platform (Linux x86_64): `numpy.uint64`: 64-bit unsigned integer (``0`` to ``18_446_744_073_709_551_615``).
 |  :Alias on this platform (Linux x86_64): `numpy.uintp`: Unsigned integer large enough to fit pointer, compatible with C ``uintptr_t``.
........................... ulonglong ...........................
Help on class ulonglong in module numpy:

class ulonglong(unsignedinteger)
 |  Signed integer type, compatible with C ``unsigned long long``.
 |
 |  :Character code: ``'Q'``
 |
 |  Method resolution order:
 |      ulonglong
 |      unsignedinteger
........................... union1d ...........................
Help on _ArrayFunctionDispatcher in module numpy:

union1d(ar1, ar2)
    Find the union of two arrays.

    Return the unique, sorted array of values that are in either of the two
    input arrays.

    Parameters
    ----------
........................... unique ...........................
Help on _ArrayFunctionDispatcher in module numpy:

unique(
    ar,
    return_index=False,
    return_inverse=False,
    return_counts=False,
    axis=None,
    *,
    equal_nan=True
........................... unique_all ...........................
Help on _ArrayFunctionDispatcher in module numpy:

unique_all(x)
    Find the unique elements of an array, and counts, inverse, and indices.

    This function is an Array API compatible alternative to::

        np.unique(x, return_index=True, return_inverse=True,
                  return_counts=True, equal_nan=False)

........................... unique_counts ...........................
Help on _ArrayFunctionDispatcher in module numpy:

unique_counts(x)
    Find the unique elements and counts of an input array `x`.

    This function is an Array API compatible alternative to::

        np.unique(x, return_counts=True, equal_nan=False)

    but returns a namedtuple for easier access to each output.
........................... unique_inverse ...........................
Help on _ArrayFunctionDispatcher in module numpy:

unique_inverse(x)
    Find the unique elements of `x` and indices to reconstruct `x`.

    This function is an Array API compatible alternative to::

        np.unique(x, return_inverse=True, equal_nan=False)

    but returns a namedtuple for easier access to each output.
........................... unique_values ...........................
Help on _ArrayFunctionDispatcher in module numpy:

unique_values(x)
    Returns the unique elements of an input array `x`.

    This function is an Array API compatible alternative to::

        np.unique(x, equal_nan=False)

    Parameters
........................... unpackbits ...........................
Help on _ArrayFunctionDispatcher in module numpy:

unpackbits(...)
    unpackbits(a, /, axis=None, count=None, bitorder='big')

    Unpacks elements of a uint8 array into a binary-valued output array.

    Each element of `a` represents a bit-field that should be unpacked
    into a binary-valued output array. The shape of the output array is
    either 1-D (if `axis` is ``None``) or the same shape as the input
........................... unravel_index ...........................
Help on _ArrayFunctionDispatcher in module numpy:

unravel_index(...)
    unravel_index(indices, shape, order='C')

    Converts a flat index or array of flat indices into a tuple
    of coordinate arrays.

    Parameters
    ----------
........................... unsignedinteger ...........................
Help on class unsignedinteger in module numpy:

class unsignedinteger(integer)
 |  Abstract base class of all unsigned integer scalar types.
 |
 |  Method resolution order:
 |      unsignedinteger
 |      integer
 |      number
 |      generic
........................... unstack ...........................
Help on _ArrayFunctionDispatcher in module numpy:

unstack(x, /, *, axis=0)
    Split an array into a sequence of arrays along the given axis.

    The ``axis`` parameter specifies the dimension along which the array will
    be split. For example, if ``axis=0`` (the default) it will be the first
    dimension and if ``axis=-1`` it will be the last dimension.

    The result is a tuple of arrays split along ``axis``.
........................... unwrap ...........................
Help on _ArrayFunctionDispatcher in module numpy:

unwrap(p, discont=None, axis=-1, *, period=6.283185307179586)
    Unwrap by taking the complement of large deltas with respect to the period.

    This unwraps a signal `p` by changing elements which have an absolute
    difference from their predecessor of more than ``max(discont, period/2)``
    to their `period`-complementary values.

    For the default case where `period` is :math:`2\pi` and `discont` is
........................... ushort ...........................
Help on class uint16 in module numpy:

class uint16(unsignedinteger)
 |  Unsigned integer type, compatible with C ``unsigned short``.
 |
 |  :Character code: ``'H'``
 |  :Canonical name: `numpy.ushort`
 |  :Alias on this platform (Linux x86_64): `numpy.uint16`: 16-bit unsigned integer (``0`` to ``65_535``).
 |
 |  Method resolution order:
........................... vander ...........................
Help on _ArrayFunctionDispatcher in module numpy:

vander(x, N=None, increasing=False)
    Generate a Vandermonde matrix.

    The columns of the output matrix are powers of the input vector. The
    order of the powers is determined by the `increasing` boolean argument.
    Specifically, when `increasing` is False, the `i`-th output column is
    the input vector raised element-wise to the power of ``N - i - 1``. Such
    a matrix with a geometric progression in each row is named for Alexandre-
........................... var ...........................
Help on _ArrayFunctionDispatcher in module numpy:

var(
    a,
    axis=None,
    dtype=None,
    out=None,
    ddof=0,
    keepdims=<no value>,
    *,
........................... vdot ...........................
Help on _ArrayFunctionDispatcher in module numpy:

vdot(...)
    vdot(a, b, /)

    Return the dot product of two vectors.

    The `vdot` function handles complex numbers differently than `dot`:
    if the first argument is complex, it is replaced by its complex conjugate
    in the dot product calculation. `vdot` also handles multidimensional
........................... vecdot ...........................
Help on ufunc in module numpy:

vecdot = <ufunc 'vecdot'>
    vecdot(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])

    Vector dot product of two arrays.

    Let :math:`\mathbf{a}` be a vector in `x1` and :math:`\mathbf{b}` be
    a corresponding vector in `x2`. The dot product is defined as:

........................... vecmat ...........................
Help on ufunc in module numpy:

vecmat = <ufunc 'vecmat'>
    vecmat(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])

    Vector-matrix dot product of two arrays.

    Given a vector (or stack of vector) :math:`\mathbf{v}` in ``x1`` and
    a matrix (or stack of matrices) :math:`\mathbf{A}` in ``x2``, the
    vector-matrix product is defined as:
........................... vectorize ...........................
Help on class vectorize in module numpy:

class vectorize(builtins.object)
 |  vectorize(
 |      pyfunc=<no value>,
 |      otypes=None,
 |      doc=None,
 |      excluded=None,
 |      cache=False,
 |      signature=None
........................... void ...........................
Help on class void in module numpy:

class void(flexible)
 |  np.void(length_or_data, /, dtype=None)
 |
 |  Create a new structured or unstructured void scalar.
 |
 |  Parameters
 |  ----------
 |  length_or_data : int, array-like, bytes-like, object
........................... vsplit ...........................
Help on _ArrayFunctionDispatcher in module numpy:

vsplit(ary, indices_or_sections)
    Split an array into multiple sub-arrays vertically (row-wise).

    Please refer to the ``split`` documentation.  ``vsplit`` is equivalent
    to ``split`` with `axis=0` (default), the array is always split along the
    first axis regardless of the array dimension.

    See Also
........................... vstack ...........................
Help on _ArrayFunctionDispatcher in module numpy:

vstack(tup, *, dtype=None, casting='same_kind')
    Stack arrays in sequence vertically (row wise).

    This is equivalent to concatenation along the first axis after 1-D arrays
    of shape `(N,)` have been reshaped to `(1,N)`. Rebuilds arrays divided by
    `vsplit`.

    This function makes most sense for arrays with up to 3 dimensions. For
........................... where ...........................
Help on _ArrayFunctionDispatcher in module numpy:

where(...)
    where(condition, [x, y], /)

    Return elements chosen from `x` or `y` depending on `condition`.

    .. note::
        When only `condition` is provided, this function is a shorthand for
        ``np.asarray(condition).nonzero()``. Using `nonzero` directly should be
........................... zeros ...........................
Help on built-in function zeros in module numpy:

zeros(...)
    zeros(shape, dtype=float, order='C', *, like=None)

    Return a new array of given shape and type, filled with zeros.

    Parameters
    ----------
    shape : int or tuple of ints
........................... zeros_like ...........................
Help on _ArrayFunctionDispatcher in module numpy:

zeros_like(a, dtype=None, order='K', subok=True, shape=None, *, device=None)
    Return an array of zeros with the same shape and type as a given array.

    Parameters
    ----------
    a : array_like
        The shape and data-type of `a` define these same attributes of
        the returned array.
