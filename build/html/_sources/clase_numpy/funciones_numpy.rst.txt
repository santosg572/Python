Alguno métodos de numpy
=======================

&&&&&&&&&&&&&&&&&&&&&& ndarray &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on class ndarray in module numpy:

class ndarray(builtins.object)
 |  ndarray(shape, dtype=float, buffer=None, offset=0,
 |          strides=None, order=None)
 |
 |  An array object represents a multidimensional, homogeneous array
 |  of fixed-size items.  An associated data-type object describes the
 |  format of each element in the array (its byte-order, how many bytes it
 |  occupies in memory, whether it is an integer, a floating point number,
 |  or something else, etc.)
 |
 |  Arrays should be constructed using `array`, `zeros` or `empty` (refer
 |  to the See Also section below).  The parameters given here refer to
 |  a low-level method (`ndarray(...)`) for instantiating an array.
 |
 |  For more information, refer to the `numpy` module and examine the
 |  methods and attributes of an array.
 |
 |  Parameters
 |  ----------
 |  (for the __new__ method; see Notes below)
 |
 |  shape : tuple of ints
 |      Shape of created array.
 |  dtype : data-type, optional
 |      Any object that can be interpreted as a numpy data type.
 |  buffer : object exposing buffer interface, optional
 |      Used to fill the array with data.
 |  offset : int, optional
 |      Offset of array data in buffer.
 |  strides : tuple of ints, optional
 |      Strides of data in memory.
 |  order : {'C', 'F'}, optional
 |      Row-major (C-style) or column-major (Fortran-style) order.
 |
 |  Attributes
 |  ----------
 |  T : ndarray
 |      Transpose of the array.
 |  data : buffer
 |      The array's elements, in memory.
 |  dtype : dtype object
 |      Describes the format of the elements in the array.
 |  flags : dict
 |      Dictionary containing information related to memory use, e.g.,
 |      'C_CONTIGUOUS', 'OWNDATA', 'WRITEABLE', etc.
 |  flat : numpy.flatiter object
 |      Flattened version of the array as an iterator.  The iterator
 |      allows assignments, e.g., ``x.flat = 3`` (See `ndarray.flat` for
 |      assignment examples; TODO).
 |  imag : ndarray
 |      Imaginary part of the array.
 |  real : ndarray
 |      Real part of the array.
 |  size : int
 |      Number of elements in the array.
 |  itemsize : int
 |      The memory use of each array element in bytes.
 |  nbytes : int
 |      The total number of bytes required to store the array data,
 |      i.e., ``itemsize * size``.
 |  ndim : int
 |      The array's number of dimensions.
 |  shape : tuple of ints
 |      Shape of the array.
 |  strides : tuple of ints
 |      The step-size required to move from one element to the next in
 |      memory. For example, a contiguous ``(3, 4)`` array of type
 |      ``int16`` in C-order has strides ``(8, 2)``.  This implies that
 |      to move from element to element in memory requires jumps of 2 bytes.
 |      To move from row-to-row, one needs to jump 8 bytes at a time
 |      (``2 * 4``).
 |  ctypes : ctypes object
 |      Class containing properties of the array needed for interaction
 |      with ctypes.
 |  base : ndarray
 |      If the array is a view into another array, that array is its `base`
 |      (unless that array is also a view).  The `base` array is where the
 |      array data is actually stored.
 |
 |  See Also
 |  --------
 |  array : Construct an array.
 |  zeros : Create an array, each element of which is zero.
 |  empty : Create an array, but leave its allocated memory unchanged (i.e.,
 |          it contains "garbage").
 |  dtype : Create a data-type.
 |  numpy.typing.NDArray : An ndarray alias :term:`generic <generic type>`
 |                         w.r.t. its `dtype.type <numpy.dtype.type>`.
 |
 |  Notes
 |  -----
 |  There are two modes of creating an array using ``__new__``:
 |
 |  1. If `buffer` is None, then only `shape`, `dtype`, and `order`
 |     are used.
 |  2. If `buffer` is an object exposing the buffer interface, then
 |     all keywords are interpreted.
 |
 |  No ``__init__`` method is needed because the array is fully initialized
 |  after the ``__new__`` method.
 |
 |  Examples
 |  --------
 |  These examples illustrate the low-level `ndarray` constructor.  Refer
 |  to the `See Also` section above for easier ways of constructing an
 |  ndarray.
 |
 |  First mode, `buffer` is None:
 |
 |  >>> np.ndarray(shape=(2,2), dtype=float, order='F')
 |  array([[0.0e+000, 0.0e+000], # random
 |         [     nan, 2.5e-323]])
 |
 |  Second mode:
 |
 |  >>> np.ndarray((2,), buffer=np.array([1,2,3]),
 |  ...            offset=np.int_().itemsize,
 |  ...            dtype=int) # offset = 1*itemsize, i.e. skip first element
 |  array([2, 3])
 |
 |  Methods defined here:
 |
 |  __abs__(self, /)
 |      abs(self)
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __and__(self, value, /)
 |      Return self&value.
 |
 |  __array__(...)
 |      a.__array__([dtype], /)
 |
 |      Returns either a new reference to self if dtype is not given or a new array
 |      of provided data type if dtype is different from the current dtype of the
 |      array.
 |
 |  __array_finalize__(...)
 |      a.__array_finalize__(obj, /)
 |
 |      Present so subclasses can call super. Does nothing.
 |
 |  __array_function__(...)
 |
 |  __array_prepare__(...)
 |      a.__array_prepare__(array[, context], /)
 |
 |      Returns a view of `array` with the same type as self.
 |
 |  __array_ufunc__(...)
 |
 |  __array_wrap__(...)
 |      a.__array_wrap__(array[, context], /)
 |
 |      Returns a view of `array` with the same type as self.
 |
 |  __bool__(self, /)
 |      True if self else False
 |
 |  __buffer__(self, flags, /)
 |      Return a buffer object that exposes the underlying memory of the object.
 |
 |  __complex__(...)
 |
 |  __contains__(self, key, /)
 |      Return bool(key in self).
 |
 |  __copy__(...)
 |      a.__copy__()
 |
 |      Used if :func:`copy.copy` is called on an array. Returns a copy of the array.
 |
 |      Equivalent to ``a.copy(order='K')``.
 |
 |  __deepcopy__(...)
 |      a.__deepcopy__(memo, /)
 |
 |      Used if :func:`copy.deepcopy` is called on an array.
 |
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |
 |  __dlpack__(...)
 |      a.__dlpack__(*, stream=None)
 |
 |      DLPack Protocol: Part of the Array API.
 |
 |  __dlpack_device__(...)
 |      a.__dlpack_device__()
 |
 |      DLPack Protocol: Part of the Array API.
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __float__(self, /)
 |      float(self)
 |
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |
 |  __format__(...)
 |      Default object formatter.
 |
 |      Return str(self) if format_spec is empty. Raise TypeError otherwise.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getitem__(self, key, /)
 |      Return self[key].
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __iadd__(self, value, /)
 |      Return self+=value.
 |
 |  __iand__(self, value, /)
 |      Return self&=value.
 |
 |  __ifloordiv__(self, value, /)
 |      Return self//=value.
 |
 |  __ilshift__(self, value, /)
 |      Return self<<=value.
 |
 |  __imatmul__(self, value, /)
 |      Return self@=value.
 |
 |  __imod__(self, value, /)
 |      Return self%=value.
 |
 |  __imul__(self, value, /)
 |      Return self*=value.
 |
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |
 |  __int__(self, /)
 |      int(self)
 |
 |  __invert__(self, /)
 |      ~self
 |
 |  __ior__(self, value, /)
 |      Return self|=value.
 |
 |  __ipow__(self, value, /)
 |      Return self**=value.
 |
 |  __irshift__(self, value, /)
 |      Return self>>=value.
 |
 |  __isub__(self, value, /)
 |      Return self-=value.
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __itruediv__(self, value, /)
 |      Return self/=value.
 |
 |  __ixor__(self, value, /)
 |      Return self^=value.
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __len__(self, /)
 |      Return len(self).
 |
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __matmul__(self, value, /)
 |      Return self@value.
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
 |  __or__(self, value, /)
 |      Return self|value.
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
 |  __rand__(self, value, /)
 |      Return value&self.
 |
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |
 |  __reduce__(...)
 |      a.__reduce__()
 |
 |      For pickling.
 |
 |  __reduce_ex__(...)
 |      Helper for pickle.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |
 |  __rmatmul__(self, value, /)
 |      Return value@self.
 |
 |  __rmod__(self, value, /)
 |      Return value%self.
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __ror__(self, value, /)
 |      Return value|self.
 |
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |
 |  __rsub__(self, value, /)
 |      Return value-self.
 |
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |
 |  __rxor__(self, value, /)
 |      Return value^self.
 |
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |
 |  __setstate__(...)
 |      a.__setstate__(state, /)
 |
 |      For unpickling.
 |
 |      The `state` argument must be a sequence that contains the following
 |      elements:
 |
 |      Parameters
 |      ----------
 |      version : int
 |          optional pickle version. If omitted defaults to 0.
 |      shape : tuple
 |      dtype : data-type
 |      isFortran : bool
 |      rawdata : string or list
 |          a binary string with the data (or a list if 'a' is an object array)
 |
 |  __sizeof__(...)
 |      Size of object in memory, in bytes.
 |
 |  __str__(self, /)
 |      Return str(self).
 |
 |  __sub__(self, value, /)
 |      Return self-value.
 |
 |  __truediv__(self, value, /)
 |      Return self/value.
 |
 |  __xor__(self, value, /)
 |      Return self^value.
 |
 |  all(...)
 |      a.all(axis=None, out=None, keepdims=False, *, where=True)
 |
 |      Returns True if all elements evaluate to True.
 |
 |      Refer to `numpy.all` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.all : equivalent function
 |
 |  any(...)
 |      a.any(axis=None, out=None, keepdims=False, *, where=True)
 |
 |      Returns True if any of the elements of `a` evaluate to True.
 |
 |      Refer to `numpy.any` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.any : equivalent function
 |
 |  argmax(...)
 |      a.argmax(axis=None, out=None, *, keepdims=False)
 |
 |      Return indices of the maximum values along the given axis.
 |
 |      Refer to `numpy.argmax` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.argmax : equivalent function
 |
 |  argmin(...)
 |      a.argmin(axis=None, out=None, *, keepdims=False)
 |
 |      Return indices of the minimum values along the given axis.
 |
 |      Refer to `numpy.argmin` for detailed documentation.
 |
 |      See Also
 |      --------
 |      numpy.argmin : equivalent function
 |
 |  argpartition(...)
 |      a.argpartition(kth, axis=-1, kind='introselect', order=None)
 |
 |      Returns the indices that would partition this array.
 |
 |      Refer to `numpy.argpartition` for full documentation.
 |
 |      .. versionadded:: 1.8.0
 |
 |      See Also
 |      --------
 |      numpy.argpartition : equivalent function
 |
 |  argsort(...)
 |      a.argsort(axis=-1, kind=None, order=None)
 |
 |      Returns the indices that would sort this array.
 |
 |      Refer to `numpy.argsort` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.argsort : equivalent function
 |
 |  astype(...)
 |      a.astype(dtype, order='K', casting='unsafe', subok=True, copy=True)
 |
 |      Copy of the array, cast to a specified type.
 |
 |      Parameters
 |      ----------
 |      dtype : str or dtype
 |          Typecode or data-type to which the array is cast.
 |      order : {'C', 'F', 'A', 'K'}, optional
 |          Controls the memory layout order of the result.
 |          'C' means C order, 'F' means Fortran order, 'A'
 |          means 'F' order if all the arrays are Fortran contiguous,
 |          'C' order otherwise, and 'K' means as close to the
 |          order the array elements appear in memory as possible.
 |          Default is 'K'.
 |      casting : {'no', 'equiv', 'safe', 'same_kind', 'unsafe'}, optional
 |          Controls what kind of data casting may occur. Defaults to 'unsafe'
 |          for backwards compatibility.
 |
 |            * 'no' means the data types should not be cast at all.
 |            * 'equiv' means only byte-order changes are allowed.
 |            * 'safe' means only casts which can preserve values are allowed.
 |            * 'same_kind' means only safe casts or casts within a kind,
 |              like float64 to float32, are allowed.
 |            * 'unsafe' means any data conversions may be done.
 |      subok : bool, optional
 |          If True, then sub-classes will be passed-through (default), otherwise
 |          the returned array will be forced to be a base-class array.
 |      copy : bool, optional
 |          By default, astype always returns a newly allocated array. If this
 |          is set to false, and the `dtype`, `order`, and `subok`
 |          requirements are satisfied, the input array is returned instead
 |          of a copy.
 |
 |      Returns
 |      -------
 |      arr_t : ndarray
 |          Unless `copy` is False and the other conditions for returning the input
 |          array are satisfied (see description for `copy` input parameter), `arr_t`
 |          is a new array of the same shape as the input array, with dtype, order
 |          given by `dtype`, `order`.
 |
 |      Notes
 |      -----
 |      .. versionchanged:: 1.17.0
 |         Casting between a simple data type and a structured one is possible only
 |         for "unsafe" casting.  Casting to multiple fields is allowed, but
 |         casting from multiple fields is not.
 |
 |      .. versionchanged:: 1.9.0
 |         Casting from numeric to string types in 'safe' casting mode requires
 |         that the string dtype length is long enough to store the max
 |         integer/float value converted.
 |
 |      Raises
 |      ------
 |      ComplexWarning
 |          When casting from complex to float or int. To avoid this,
 |          one should use ``a.real.astype(t)``.
 |
 |      Examples
 |      --------
 |      >>> x = np.array([1, 2, 2.5])
 |      >>> x
 |      array([1. ,  2. ,  2.5])
 |
 |      >>> x.astype(int)
 |      array([1, 2, 2])
 |
 |  byteswap(...)
 |      a.byteswap(inplace=False)
 |
 |      Swap the bytes of the array elements
 |
 |      Toggle between low-endian and big-endian data representation by
 |      returning a byteswapped array, optionally swapped in-place.
 |      Arrays of byte-strings are not swapped. The real and imaginary
 |      parts of a complex number are swapped individually.
 |
 |      Parameters
 |      ----------
 |      inplace : bool, optional
 |          If ``True``, swap bytes in-place, default is ``False``.
 |
 |      Returns
 |      -------
 |      out : ndarray
 |          The byteswapped array. If `inplace` is ``True``, this is
 |          a view to self.
 |
 |      Examples
 |      --------
 |      >>> A = np.array([1, 256, 8755], dtype=np.int16)
 |      >>> list(map(hex, A))
 |      ['0x1', '0x100', '0x2233']
 |      >>> A.byteswap(inplace=True)
 |      array([  256,     1, 13090], dtype=int16)
 |      >>> list(map(hex, A))
 |      ['0x100', '0x1', '0x3322']
 |
 |      Arrays of byte-strings are not swapped
 |
 |      >>> A = np.array([b'ceg', b'fac'])
 |      >>> A.byteswap()
 |      array([b'ceg', b'fac'], dtype='|S3')
 |
 |      ``A.newbyteorder().byteswap()`` produces an array with the same values
 |        but different representation in memory
 |
 |      >>> A = np.array([1, 2, 3])
 |      >>> A.view(np.uint8)
 |      array([1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0,
 |             0, 0], dtype=uint8)
 |      >>> A.newbyteorder().byteswap(inplace=True)
 |      array([1, 2, 3])
 |      >>> A.view(np.uint8)
 |      array([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0,
 |             0, 3], dtype=uint8)
 |
 |  choose(...)
 |      a.choose(choices, out=None, mode='raise')
 |
 |      Use an index array to construct a new array from a set of choices.
 |
 |      Refer to `numpy.choose` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.choose : equivalent function
 |
 |  clip(...)
 |      a.clip(min=None, max=None, out=None, **kwargs)
 |
 |      Return an array whose values are limited to ``[min, max]``.
 |      One of max or min must be given.
 |
 |      Refer to `numpy.clip` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.clip : equivalent function
 |
 |  compress(...)
 |      a.compress(condition, axis=None, out=None)
 |
 |      Return selected slices of this array along given axis.
 |
 |      Refer to `numpy.compress` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.compress : equivalent function
 |
 |  conj(...)
 |      a.conj()
 |
 |      Complex-conjugate all elements.
 |
 |      Refer to `numpy.conjugate` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.conjugate : equivalent function
 |
 |  conjugate(...)
 |      a.conjugate()
 |
 |      Return the complex conjugate, element-wise.
 |
 |      Refer to `numpy.conjugate` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.conjugate : equivalent function
 |
 |  copy(...)
 |      a.copy(order='C')
 |
 |      Return a copy of the array.
 |
 |      Parameters
 |      ----------
 |      order : {'C', 'F', 'A', 'K'}, optional
 |          Controls the memory layout of the copy. 'C' means C-order,
 |          'F' means F-order, 'A' means 'F' if `a` is Fortran contiguous,
 |          'C' otherwise. 'K' means match the layout of `a` as closely
 |          as possible. (Note that this function and :func:`numpy.copy` are very
 |          similar but have different default values for their order=
 |          arguments, and this function always passes sub-classes through.)
 |
 |      See also
 |      --------
 |      numpy.copy : Similar function with different default behavior
 |      numpy.copyto
 |
 |      Notes
 |      -----
 |      This function is the preferred method for creating an array copy.  The
 |      function :func:`numpy.copy` is similar, but it defaults to using order 'K',
 |      and will not pass sub-classes through by default.
 |
 |      Examples
 |      --------
 |      >>> x = np.array([[1,2,3],[4,5,6]], order='F')
 |
 |      >>> y = x.copy()
 |
 |      >>> x.fill(0)
 |
 |      >>> x
 |      array([[0, 0, 0],
 |             [0, 0, 0]])
 |
 |      >>> y
 |      array([[1, 2, 3],
 |             [4, 5, 6]])
 |
 |      >>> y.flags['C_CONTIGUOUS']
 |      True
 |
 |  cumprod(...)
 |      a.cumprod(axis=None, dtype=None, out=None)
 |
 |      Return the cumulative product of the elements along the given axis.
 |
 |      Refer to `numpy.cumprod` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.cumprod : equivalent function
 |
 |  cumsum(...)
 |      a.cumsum(axis=None, dtype=None, out=None)
 |
 |      Return the cumulative sum of the elements along the given axis.
 |
 |      Refer to `numpy.cumsum` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.cumsum : equivalent function
 |
 |  diagonal(...)
 |      a.diagonal(offset=0, axis1=0, axis2=1)
 |
 |      Return specified diagonals. In NumPy 1.9 the returned array is a
 |      read-only view instead of a copy as in previous NumPy versions.  In
 |      a future version the read-only restriction will be removed.
 |
 |      Refer to :func:`numpy.diagonal` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.diagonal : equivalent function
 |
 |  dot(...)
 |
 |  dump(...)
 |      a.dump(file)
 |
 |      Dump a pickle of the array to the specified file.
 |      The array can be read back with pickle.load or numpy.load.
 |
 |      Parameters
 |      ----------
 |      file : str or Path
 |          A string naming the dump file.
 |
 |          .. versionchanged:: 1.17.0
 |              `pathlib.Path` objects are now accepted.
 |
 |  dumps(...)
 |      a.dumps()
 |
 |      Returns the pickle of the array as a string.
 |      pickle.loads will convert the string back to an array.
 |
 |      Parameters
 |      ----------
 |      None
 |
 |  fill(...)
 |      a.fill(value)
 |
 |      Fill the array with a scalar value.
 |
 |      Parameters
 |      ----------
 |      value : scalar
 |          All elements of `a` will be assigned this value.
 |
 |      Examples
 |      --------
 |      >>> a = np.array([1, 2])
 |      >>> a.fill(0)
 |      >>> a
 |      array([0, 0])
 |      >>> a = np.empty(2)
 |      >>> a.fill(1)
 |      >>> a
 |      array([1.,  1.])
 |
 |      Fill expects a scalar value and always behaves the same as assigning
 |      to a single array element.  The following is a rare example where this
 |      distinction is important:
 |
 |      >>> a = np.array([None, None], dtype=object)
 |      >>> a[0] = np.array(3)
 |      >>> a
 |      array([array(3), None], dtype=object)
 |      >>> a.fill(np.array(3))
 |      >>> a
 |      array([array(3), array(3)], dtype=object)
 |
 |      Where other forms of assignments will unpack the array being assigned:
 |
 |      >>> a[...] = np.array(3)
 |      >>> a
 |      array([3, 3], dtype=object)
 |
 |  flatten(...)
 |      a.flatten(order='C')
 |
 |      Return a copy of the array collapsed into one dimension.
 |
 |      Parameters
 |      ----------
 |      order : {'C', 'F', 'A', 'K'}, optional
 |          'C' means to flatten in row-major (C-style) order.
 |          'F' means to flatten in column-major (Fortran-
 |          style) order. 'A' means to flatten in column-major
 |          order if `a` is Fortran *contiguous* in memory,
 |          row-major order otherwise. 'K' means to flatten
 |          `a` in the order the elements occur in memory.
 |          The default is 'C'.
 |
 |      Returns
 |      -------
 |      y : ndarray
 |          A copy of the input array, flattened to one dimension.
 |
 |      See Also
 |      --------
 |      ravel : Return a flattened array.
 |      flat : A 1-D flat iterator over the array.
 |
 |      Examples
 |      --------
 |      >>> a = np.array([[1,2], [3,4]])
 |      >>> a.flatten()
 |      array([1, 2, 3, 4])
 |      >>> a.flatten('F')
 |      array([1, 3, 2, 4])
 |
 |  getfield(...)
 |      a.getfield(dtype, offset=0)
 |
 |      Returns a field of the given array as a certain type.
 |
 |      A field is a view of the array data with a given data-type. The values in
 |      the view are determined by the given type and the offset into the current
 |      array in bytes. The offset needs to be such that the view dtype fits in the
 |      array dtype; for example an array of dtype complex128 has 16-byte elements.
 |      If taking a view with a 32-bit integer (4 bytes), the offset needs to be
 |      between 0 and 12 bytes.
 |
 |      Parameters
 |      ----------
 |      dtype : str or dtype
 |          The data type of the view. The dtype size of the view can not be larger
 |          than that of the array itself.
 |      offset : int
 |          Number of bytes to skip before beginning the element view.
 |
 |      Examples
 |      --------
 |      >>> x = np.diag([1.+1.j]*2)
 |      >>> x[1, 1] = 2 + 4.j
 |      >>> x
 |      array([[1.+1.j,  0.+0.j],
 |             [0.+0.j,  2.+4.j]])
 |      >>> x.getfield(np.float64)
 |      array([[1.,  0.],
 |             [0.,  2.]])
 |
 |      By choosing an offset of 8 bytes we can select the complex part of the
 |      array for our view:
 |
 |      >>> x.getfield(np.float64, offset=8)
 |      array([[1.,  0.],
 |             [0.,  4.]])
 |
 |  item(...)
 |      a.item(*args)
 |
 |      Copy an element of an array to a standard Python scalar and return it.
 |
 |      Parameters
 |      ----------
 |      \*args : Arguments (variable number and type)
 |
 |          * none: in this case, the method only works for arrays
 |            with one element (`a.size == 1`), which element is
 |            copied into a standard Python scalar object and returned.
 |
 |          * int_type: this argument is interpreted as a flat index into
 |            the array, specifying which element to copy and return.
 |
 |          * tuple of int_types: functions as does a single int_type argument,
 |            except that the argument is interpreted as an nd-index into the
 |            array.
 |
 |      Returns
 |      -------
 |      z : Standard Python scalar object
 |          A copy of the specified element of the array as a suitable
 |          Python scalar
 |
 |      Notes
 |      -----
 |      When the data type of `a` is longdouble or clongdouble, item() returns
 |      a scalar array object because there is no available Python scalar that
 |      would not lose information. Void arrays return a buffer object for item(),
 |      unless fields are defined, in which case a tuple is returned.
 |
 |      `item` is very similar to a[args], except, instead of an array scalar,
 |      a standard Python scalar is returned. This can be useful for speeding up
 |      access to elements of the array and doing arithmetic on elements of the
 |      array using Python's optimized math.
 |
 |      Examples
 |      --------
 |      >>> np.random.seed(123)
 |      >>> x = np.random.randint(9, size=(3, 3))
 |      >>> x
 |      array([[2, 2, 6],
 |             [1, 3, 6],
 |             [1, 0, 1]])
 |      >>> x.item(3)
 |      1
 |      >>> x.item(7)
 |      0
 |      >>> x.item((0, 1))
 |      2
 |      >>> x.item((2, 2))
 |      1
 |
 |  itemset(...)
 |      a.itemset(*args)
 |
 |      Insert scalar into an array (scalar is cast to array's dtype, if possible)
 |
 |      There must be at least 1 argument, and define the last argument
 |      as *item*.  Then, ``a.itemset(*args)`` is equivalent to but faster
 |      than ``a[args] = item``.  The item should be a scalar value and `args`
 |      must select a single item in the array `a`.
 |
 |      Parameters
 |      ----------
 |      \*args : Arguments
 |          If one argument: a scalar, only used in case `a` is of size 1.
 |          If two arguments: the last argument is the value to be set
 |          and must be a scalar, the first argument specifies a single array
 |          element location. It is either an int or a tuple.
 |
 |      Notes
 |      -----
 |      Compared to indexing syntax, `itemset` provides some speed increase
 |      for placing a scalar into a particular location in an `ndarray`,
 |      if you must do this.  However, generally this is discouraged:
 |      among other problems, it complicates the appearance of the code.
 |      Also, when using `itemset` (and `item`) inside a loop, be sure
 |      to assign the methods to a local variable to avoid the attribute
 |      look-up at each loop iteration.
 |
 |      Examples
 |      --------
 |      >>> np.random.seed(123)
 |      >>> x = np.random.randint(9, size=(3, 3))
 |      >>> x
 |      array([[2, 2, 6],
 |             [1, 3, 6],
 |             [1, 0, 1]])
 |      >>> x.itemset(4, 0)
 |      >>> x.itemset((2, 2), 9)
 |      >>> x
 |      array([[2, 2, 6],
 |             [1, 0, 6],
 |             [1, 0, 9]])
 |
 |  max(...)
 |      a.max(axis=None, out=None, keepdims=False, initial=<no value>, where=True)
 |
 |      Return the maximum along a given axis.
 |
 |      Refer to `numpy.amax` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.amax : equivalent function
 |
 |  mean(...)
 |      a.mean(axis=None, dtype=None, out=None, keepdims=False, *, where=True)
 |
 |      Returns the average of the array elements along given axis.
 |
 |      Refer to `numpy.mean` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.mean : equivalent function
 |
 |  min(...)
 |      a.min(axis=None, out=None, keepdims=False, initial=<no value>, where=True)
 |
 |      Return the minimum along a given axis.
 |
 |      Refer to `numpy.amin` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.amin : equivalent function
 |
 |  newbyteorder(...)
 |      arr.newbyteorder(new_order='S', /)
 |
 |      Return the array with the same data viewed with a different byte order.
 |
 |      Equivalent to::
 |
 |          arr.view(arr.dtype.newbytorder(new_order))
 |
 |      Changes are also made in all fields and sub-arrays of the array data
 |      type.
 |
 |
 |
 |      Parameters
 |      ----------
 |      new_order : string, optional
 |          Byte order to force; a value from the byte order specifications
 |          below. `new_order` codes can be any of:
 |
 |          * 'S' - swap dtype from current to opposite endian
 |          * {'<', 'little'} - little endian
 |          * {'>', 'big'} - big endian
 |          * {'=', 'native'} - native order, equivalent to `sys.byteorder`
 |          * {'|', 'I'} - ignore (no change to byte order)
 |
 |          The default value ('S') results in swapping the current
 |          byte order.
 |
 |
 |      Returns
 |      -------
 |      new_arr : array
 |          New array object with the dtype reflecting given change to the
 |          byte order.
 |
 |  nonzero(...)
 |      a.nonzero()
 |
 |      Return the indices of the elements that are non-zero.
 |
 |      Refer to `numpy.nonzero` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.nonzero : equivalent function
 |
 |  partition(...)
 |      a.partition(kth, axis=-1, kind='introselect', order=None)
 |
 |      Rearranges the elements in the array in such a way that the value of the
 |      element in kth position is in the position it would be in a sorted array.
 |      All elements smaller than the kth element are moved before this element and
 |      all equal or greater are moved behind it. The ordering of the elements in
 |      the two partitions is undefined.
 |
 |      .. versionadded:: 1.8.0
 |
 |      Parameters
 |      ----------
 |      kth : int or sequence of ints
 |          Element index to partition by. The kth element value will be in its
 |          final sorted position and all smaller elements will be moved before it
 |          and all equal or greater elements behind it.
 |          The order of all elements in the partitions is undefined.
 |          If provided with a sequence of kth it will partition all elements
 |          indexed by kth of them into their sorted position at once.
 |
 |          .. deprecated:: 1.22.0
 |              Passing booleans as index is deprecated.
 |      axis : int, optional
 |          Axis along which to sort. Default is -1, which means sort along the
 |          last axis.
 |      kind : {'introselect'}, optional
 |          Selection algorithm. Default is 'introselect'.
 |      order : str or list of str, optional
 |          When `a` is an array with fields defined, this argument specifies
 |          which fields to compare first, second, etc. A single field can
 |          be specified as a string, and not all fields need to be specified,
 |          but unspecified fields will still be used, in the order in which
 |          they come up in the dtype, to break ties.
 |
 |      See Also
 |      --------
 |      numpy.partition : Return a partitioned copy of an array.
 |      argpartition : Indirect partition.
 |      sort : Full sort.
 |
 |      Notes
 |      -----
 |      See ``np.partition`` for notes on the different algorithms.
 |
 |      Examples
 |      --------
 |      >>> a = np.array([3, 4, 2, 1])
 |      >>> a.partition(3)
 |      >>> a
 |      array([2, 1, 3, 4])
 |
 |      >>> a.partition((1, 3))
 |      >>> a
 |      array([1, 2, 3, 4])
 |
 |  prod(...)
 |      a.prod(axis=None, dtype=None, out=None, keepdims=False, initial=1, where=True)
 |
 |      Return the product of the array elements over the given axis
 |
 |      Refer to `numpy.prod` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.prod : equivalent function
 |
 |  ptp(...)
 |      a.ptp(axis=None, out=None, keepdims=False)
 |
 |      Peak to peak (maximum - minimum) value along a given axis.
 |
 |      Refer to `numpy.ptp` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.ptp : equivalent function
 |
 |  put(...)
 |      a.put(indices, values, mode='raise')
 |
 |      Set ``a.flat[n] = values[n]`` for all `n` in indices.
 |
 |      Refer to `numpy.put` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.put : equivalent function
 |
 |  ravel(...)
 |      a.ravel([order])
 |
 |      Return a flattened array.
 |
 |      Refer to `numpy.ravel` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.ravel : equivalent function
 |
 |      ndarray.flat : a flat iterator on the array.
 |
 |  repeat(...)
 |      a.repeat(repeats, axis=None)
 |
 |      Repeat elements of an array.
 |
 |      Refer to `numpy.repeat` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.repeat : equivalent function
 |
 |  reshape(...)
 |      a.reshape(shape, order='C')
 |
 |      Returns an array containing the same data with a new shape.
 |
 |      Refer to `numpy.reshape` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.reshape : equivalent function
 |
 |      Notes
 |      -----
 |      Unlike the free function `numpy.reshape`, this method on `ndarray` allows
 |      the elements of the shape parameter to be passed in as separate arguments.
 |      For example, ``a.reshape(10, 11)`` is equivalent to
 |      ``a.reshape((10, 11))``.
 |
 |  resize(...)
 |      a.resize(new_shape, refcheck=True)
 |
 |      Change shape and size of array in-place.
 |
 |      Parameters
 |      ----------
 |      new_shape : tuple of ints, or `n` ints
 |          Shape of resized array.
 |      refcheck : bool, optional
 |          If False, reference count will not be checked. Default is True.
 |
 |      Returns
 |      -------
 |      None
 |
 |      Raises
 |      ------
 |      ValueError
 |          If `a` does not own its own data or references or views to it exist,
 |          and the data memory must be changed.
 |          PyPy only: will always raise if the data memory must be changed, since
 |          there is no reliable way to determine if references or views to it
 |          exist.
 |
 |      SystemError
 |          If the `order` keyword argument is specified. This behaviour is a
 |          bug in NumPy.
 |
 |      See Also
 |      --------
 |      resize : Return a new array with the specified shape.
 |
 |      Notes
 |      -----
 |      This reallocates space for the data area if necessary.
 |
 |      Only contiguous arrays (data elements consecutive in memory) can be
 |      resized.
 |
 |      The purpose of the reference count check is to make sure you
 |      do not use this array as a buffer for another Python object and then
 |      reallocate the memory. However, reference counts can increase in
 |      other ways so if you are sure that you have not shared the memory
 |      for this array with another Python object, then you may safely set
 |      `refcheck` to False.
 |
 |      Examples
 |      --------
 |      Shrinking an array: array is flattened (in the order that the data are
 |      stored in memory), resized, and reshaped:
 |
 |      >>> a = np.array([[0, 1], [2, 3]], order='C')
 |      >>> a.resize((2, 1))
 |      >>> a
 |      array([[0],
 |             [1]])
 |
 |      >>> a = np.array([[0, 1], [2, 3]], order='F')
 |      >>> a.resize((2, 1))
 |      >>> a
 |      array([[0],
 |             [2]])
 |
 |      Enlarging an array: as above, but missing entries are filled with zeros:
 |
 |      >>> b = np.array([[0, 1], [2, 3]])
 |      >>> b.resize(2, 3) # new_shape parameter doesn't have to be a tuple
 |      >>> b
 |      array([[0, 1, 2],
 |             [3, 0, 0]])
 |
 |      Referencing an array prevents resizing...
 |
 |      >>> c = a
 |      >>> a.resize((1, 1))
 |      Traceback (most recent call last):
 |      ...
 |      ValueError: cannot resize an array that references or is referenced ...
 |
 |      Unless `refcheck` is False:
 |
 |      >>> a.resize((1, 1), refcheck=False)
 |      >>> a
 |      array([[0]])
 |      >>> c
 |      array([[0]])
 |
 |  round(...)
 |      a.round(decimals=0, out=None)
 |
 |      Return `a` with each element rounded to the given number of decimals.
 |
 |      Refer to `numpy.around` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.around : equivalent function
 |
 |  searchsorted(...)
 |      a.searchsorted(v, side='left', sorter=None)
 |
 |      Find indices where elements of v should be inserted in a to maintain order.
 |
 |      For full documentation, see `numpy.searchsorted`
 |
 |      See Also
 |      --------
 |      numpy.searchsorted : equivalent function
 |
 |  setfield(...)
 |      a.setfield(val, dtype, offset=0)
 |
 |      Put a value into a specified place in a field defined by a data-type.
 |
 |      Place `val` into `a`'s field defined by `dtype` and beginning `offset`
 |      bytes into the field.
 |
 |      Parameters
 |      ----------
 |      val : object
 |          Value to be placed in field.
 |      dtype : dtype object
 |          Data-type of the field in which to place `val`.
 |      offset : int, optional
 |          The number of bytes into the field at which to place `val`.
 |
 |      Returns
 |      -------
 |      None
 |
 |      See Also
 |      --------
 |      getfield
 |
 |      Examples
 |      --------
 |      >>> x = np.eye(3)
 |      >>> x.getfield(np.float64)
 |      array([[1.,  0.,  0.],
 |             [0.,  1.,  0.],
 |             [0.,  0.,  1.]])
 |      >>> x.setfield(3, np.int32)
 |      >>> x.getfield(np.int32)
 |      array([[3, 3, 3],
 |             [3, 3, 3],
 |             [3, 3, 3]], dtype=int32)
 |      >>> x
 |      array([[1.0e+000, 1.5e-323, 1.5e-323],
 |             [1.5e-323, 1.0e+000, 1.5e-323],
 |             [1.5e-323, 1.5e-323, 1.0e+000]])
 |      >>> x.setfield(np.eye(3), np.int32)
 |      >>> x
 |      array([[1.,  0.,  0.],
 |             [0.,  1.,  0.],
 |             [0.,  0.,  1.]])
 |
 |  setflags(...)
 |      a.setflags(write=None, align=None, uic=None)
 |
 |      Set array flags WRITEABLE, ALIGNED, WRITEBACKIFCOPY,
 |      respectively.
 |
 |      These Boolean-valued flags affect how numpy interprets the memory
 |      area used by `a` (see Notes below). The ALIGNED flag can only
 |      be set to True if the data is actually aligned according to the type.
 |      The WRITEBACKIFCOPY and flag can never be set
 |      to True. The flag WRITEABLE can only be set to True if the array owns its
 |      own memory, or the ultimate owner of the memory exposes a writeable buffer
 |      interface, or is a string. (The exception for string is made so that
 |      unpickling can be done without copying memory.)
 |
 |      Parameters
 |      ----------
 |      write : bool, optional
 |          Describes whether or not `a` can be written to.
 |      align : bool, optional
 |          Describes whether or not `a` is aligned properly for its type.
 |      uic : bool, optional
 |          Describes whether or not `a` is a copy of another "base" array.
 |
 |      Notes
 |      -----
 |      Array flags provide information about how the memory area used
 |      for the array is to be interpreted. There are 7 Boolean flags
 |      in use, only four of which can be changed by the user:
 |      WRITEBACKIFCOPY, WRITEABLE, and ALIGNED.
 |
 |      WRITEABLE (W) the data area can be written to;
 |
 |      ALIGNED (A) the data and strides are aligned appropriately for the hardware
 |      (as determined by the compiler);
 |
 |      WRITEBACKIFCOPY (X) this array is a copy of some other array (referenced
 |      by .base). When the C-API function PyArray_ResolveWritebackIfCopy is
 |      called, the base array will be updated with the contents of this array.
 |
 |      All flags can be accessed using the single (upper case) letter as well
 |      as the full name.
 |
 |      Examples
 |      --------
 |      >>> y = np.array([[3, 1, 7],
 |      ...               [2, 0, 0],
 |      ...               [8, 5, 9]])
 |      >>> y
 |      array([[3, 1, 7],
 |             [2, 0, 0],
 |             [8, 5, 9]])
 |      >>> y.flags
 |        C_CONTIGUOUS : True
 |        F_CONTIGUOUS : False
 |        OWNDATA : True
 |        WRITEABLE : True
 |        ALIGNED : True
 |        WRITEBACKIFCOPY : False
 |      >>> y.setflags(write=0, align=0)
 |      >>> y.flags
 |        C_CONTIGUOUS : True
 |        F_CONTIGUOUS : False
 |        OWNDATA : True
 |        WRITEABLE : False
 |        ALIGNED : False
 |        WRITEBACKIFCOPY : False
 |      >>> y.setflags(uic=1)
 |      Traceback (most recent call last):
 |        File "<stdin>", line 1, in <module>
 |      ValueError: cannot set WRITEBACKIFCOPY flag to True
 |
 |  sort(...)
 |      a.sort(axis=-1, kind=None, order=None)
 |
 |      Sort an array in-place. Refer to `numpy.sort` for full documentation.
 |
 |      Parameters
 |      ----------
 |      axis : int, optional
 |          Axis along which to sort. Default is -1, which means sort along the
 |          last axis.
 |      kind : {'quicksort', 'mergesort', 'heapsort', 'stable'}, optional
 |          Sorting algorithm. The default is 'quicksort'. Note that both 'stable'
 |          and 'mergesort' use timsort under the covers and, in general, the
 |          actual implementation will vary with datatype. The 'mergesort' option
 |          is retained for backwards compatibility.
 |
 |          .. versionchanged:: 1.15.0
 |             The 'stable' option was added.
 |
 |      order : str or list of str, optional
 |          When `a` is an array with fields defined, this argument specifies
 |          which fields to compare first, second, etc.  A single field can
 |          be specified as a string, and not all fields need be specified,
 |          but unspecified fields will still be used, in the order in which
 |          they come up in the dtype, to break ties.
 |
 |      See Also
 |      --------
 |      numpy.sort : Return a sorted copy of an array.
 |      numpy.argsort : Indirect sort.
 |      numpy.lexsort : Indirect stable sort on multiple keys.
 |      numpy.searchsorted : Find elements in sorted array.
 |      numpy.partition: Partial sort.
 |
 |      Notes
 |      -----
 |      See `numpy.sort` for notes on the different sorting algorithms.
 |
 |      Examples
 |      --------
 |      >>> a = np.array([[1,4], [3,1]])
 |      >>> a.sort(axis=1)
 |      >>> a
 |      array([[1, 4],
 |             [1, 3]])
 |      >>> a.sort(axis=0)
 |      >>> a
 |      array([[1, 3],
 |             [1, 4]])
 |
 |      Use the `order` keyword to specify a field to use when sorting a
 |      structured array:
 |
 |      >>> a = np.array([('a', 2), ('c', 1)], dtype=[('x', 'S1'), ('y', int)])
 |      >>> a.sort(order='y')
 |      >>> a
 |      array([(b'c', 1), (b'a', 2)],
 |            dtype=[('x', 'S1'), ('y', '<i8')])
 |
 |  squeeze(...)
 |      a.squeeze(axis=None)
 |
 |      Remove axes of length one from `a`.
 |
 |      Refer to `numpy.squeeze` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.squeeze : equivalent function
 |
 |  std(...)
 |      a.std(axis=None, dtype=None, out=None, ddof=0, keepdims=False, *, where=True)
 |
 |      Returns the standard deviation of the array elements along given axis.
 |
 |      Refer to `numpy.std` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.std : equivalent function
 |
 |  sum(...)
 |      a.sum(axis=None, dtype=None, out=None, keepdims=False, initial=0, where=True)
 |
 |      Return the sum of the array elements over the given axis.
 |
 |      Refer to `numpy.sum` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.sum : equivalent function
 |
 |  swapaxes(...)
 |      a.swapaxes(axis1, axis2)
 |
 |      Return a view of the array with `axis1` and `axis2` interchanged.
 |
 |      Refer to `numpy.swapaxes` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.swapaxes : equivalent function
 |
 |  take(...)
 |      a.take(indices, axis=None, out=None, mode='raise')
 |
 |      Return an array formed from the elements of `a` at the given indices.
 |
 |      Refer to `numpy.take` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.take : equivalent function
 |
 |  tobytes(...)
 |      a.tobytes(order='C')
 |
 |      Construct Python bytes containing the raw data bytes in the array.
 |
 |      Constructs Python bytes showing a copy of the raw contents of
 |      data memory. The bytes object is produced in C-order by default.
 |      This behavior is controlled by the ``order`` parameter.
 |
 |      .. versionadded:: 1.9.0
 |
 |      Parameters
 |      ----------
 |      order : {'C', 'F', 'A'}, optional
 |          Controls the memory layout of the bytes object. 'C' means C-order,
 |          'F' means F-order, 'A' (short for *Any*) means 'F' if `a` is
 |          Fortran contiguous, 'C' otherwise. Default is 'C'.
 |
 |      Returns
 |      -------
 |      s : bytes
 |          Python bytes exhibiting a copy of `a`'s raw data.
 |
 |      See also
 |      --------
 |      frombuffer
 |          Inverse of this operation, construct a 1-dimensional array from Python
 |          bytes.
 |
 |      Examples
 |      --------
 |      >>> x = np.array([[0, 1], [2, 3]], dtype='<u2')
 |      >>> x.tobytes()
 |      b'\x00\x00\x01\x00\x02\x00\x03\x00'
 |      >>> x.tobytes('C') == x.tobytes()
 |      True
 |      >>> x.tobytes('F')
 |      b'\x00\x00\x02\x00\x01\x00\x03\x00'
 |
 |  tofile(...)
 |      a.tofile(fid, sep="", format="%s")
 |
 |      Write array to a file as text or binary (default).
 |
 |      Data is always written in 'C' order, independent of the order of `a`.
 |      The data produced by this method can be recovered using the function
 |      fromfile().
 |
 |      Parameters
 |      ----------
 |      fid : file or str or Path
 |          An open file object, or a string containing a filename.
 |
 |          .. versionchanged:: 1.17.0
 |              `pathlib.Path` objects are now accepted.
 |
 |      sep : str
 |          Separator between array items for text output.
 |          If "" (empty), a binary file is written, equivalent to
 |          ``file.write(a.tobytes())``.
 |      format : str
 |          Format string for text file output.
 |          Each entry in the array is formatted to text by first converting
 |          it to the closest Python type, and then using "format" % item.
 |
 |      Notes
 |      -----
 |      This is a convenience function for quick storage of array data.
 |      Information on endianness and precision is lost, so this method is not a
 |      good choice for files intended to archive data or transport data between
 |      machines with different endianness. Some of these problems can be overcome
 |      by outputting the data as text files, at the expense of speed and file
 |      size.
 |
 |      When fid is a file object, array contents are directly written to the
 |      file, bypassing the file object's ``write`` method. As a result, tofile
 |      cannot be used with files objects supporting compression (e.g., GzipFile)
 |      or file-like objects that do not support ``fileno()`` (e.g., BytesIO).
 |
 |  tolist(...)
 |      a.tolist()
 |
 |      Return the array as an ``a.ndim``-levels deep nested list of Python scalars.
 |
 |      Return a copy of the array data as a (nested) Python list.
 |      Data items are converted to the nearest compatible builtin Python type, via
 |      the `~numpy.ndarray.item` function.
 |
 |      If ``a.ndim`` is 0, then since the depth of the nested list is 0, it will
 |      not be a list at all, but a simple Python scalar.
 |
 |      Parameters
 |      ----------
 |      none
 |
 |      Returns
 |      -------
 |      y : object, or list of object, or list of list of object, or ...
 |          The possibly nested list of array elements.
 |
 |      Notes
 |      -----
 |      The array may be recreated via ``a = np.array(a.tolist())``, although this
 |      may sometimes lose precision.
 |
 |      Examples
 |      --------
 |      For a 1D array, ``a.tolist()`` is almost the same as ``list(a)``,
 |      except that ``tolist`` changes numpy scalars to Python scalars:
 |
 |      >>> a = np.uint32([1, 2])
 |      >>> a_list = list(a)
 |      >>> a_list
 |      [1, 2]
 |      >>> type(a_list[0])
 |      <class 'numpy.uint32'>
 |      >>> a_tolist = a.tolist()
 |      >>> a_tolist
 |      [1, 2]
 |      >>> type(a_tolist[0])
 |      <class 'int'>
 |
 |      Additionally, for a 2D array, ``tolist`` applies recursively:
 |
 |      >>> a = np.array([[1, 2], [3, 4]])
 |      >>> list(a)
 |      [array([1, 2]), array([3, 4])]
 |      >>> a.tolist()
 |      [[1, 2], [3, 4]]
 |
 |      The base case for this recursion is a 0D array:
 |
 |      >>> a = np.array(1)
 |      >>> list(a)
 |      Traceback (most recent call last):
 |        ...
 |      TypeError: iteration over a 0-d array
 |      >>> a.tolist()
 |      1
 |
 |  tostring(...)
 |      a.tostring(order='C')
 |
 |      A compatibility alias for `tobytes`, with exactly the same behavior.
 |
 |      Despite its name, it returns `bytes` not `str`\ s.
 |
 |      .. deprecated:: 1.19.0
 |
 |  trace(...)
 |      a.trace(offset=0, axis1=0, axis2=1, dtype=None, out=None)
 |
 |      Return the sum along diagonals of the array.
 |
 |      Refer to `numpy.trace` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.trace : equivalent function
 |
 |  transpose(...)
 |      a.transpose(*axes)
 |
 |      Returns a view of the array with axes transposed.
 |
 |      Refer to `numpy.transpose` for full documentation.
 |
 |      Parameters
 |      ----------
 |      axes : None, tuple of ints, or `n` ints
 |
 |       * None or no argument: reverses the order of the axes.
 |
 |       * tuple of ints: `i` in the `j`-th place in the tuple means that the
 |         array's `i`-th axis becomes the transposed array's `j`-th axis.
 |
 |       * `n` ints: same as an n-tuple of the same ints (this form is
 |         intended simply as a "convenience" alternative to the tuple form).
 |
 |      Returns
 |      -------
 |      p : ndarray
 |          View of the array with its axes suitably permuted.
 |
 |      See Also
 |      --------
 |      transpose : Equivalent function.
 |      ndarray.T : Array property returning the array transposed.
 |      ndarray.reshape : Give a new shape to an array without changing its data.
 |
 |      Examples
 |      --------
 |      >>> a = np.array([[1, 2], [3, 4]])
 |      >>> a
 |      array([[1, 2],
 |             [3, 4]])
 |      >>> a.transpose()
 |      array([[1, 3],
 |             [2, 4]])
 |      >>> a.transpose((1, 0))
 |      array([[1, 3],
 |             [2, 4]])
 |      >>> a.transpose(1, 0)
 |      array([[1, 3],
 |             [2, 4]])
 |
 |      >>> a = np.array([1, 2, 3, 4])
 |      >>> a
 |      array([1, 2, 3, 4])
 |      >>> a.transpose()
 |      array([1, 2, 3, 4])
 |
 |  var(...)
 |      a.var(axis=None, dtype=None, out=None, ddof=0, keepdims=False, *, where=True)
 |
 |      Returns the variance of the array elements, along given axis.
 |
 |      Refer to `numpy.var` for full documentation.
 |
 |      See Also
 |      --------
 |      numpy.var : equivalent function
 |
 |  view(...)
 |      a.view([dtype][, type])
 |
 |      New view of array with the same data.
 |
 |      .. note::
 |          Passing None for ``dtype`` is different from omitting the parameter,
 |          since the former invokes ``dtype(None)`` which is an alias for
 |          ``dtype('float_')``.
 |
 |      Parameters
 |      ----------
 |      dtype : data-type or ndarray sub-class, optional
 |          Data-type descriptor of the returned view, e.g., float32 or int16.
 |          Omitting it results in the view having the same data-type as `a`.
 |          This argument can also be specified as an ndarray sub-class, which
 |          then specifies the type of the returned object (this is equivalent to
 |          setting the ``type`` parameter).
 |      type : Python type, optional
 |          Type of the returned view, e.g., ndarray or matrix.  Again, omission
 |          of the parameter results in type preservation.
 |
 |      Notes
 |      -----
 |      ``a.view()`` is used two different ways:
 |
 |      ``a.view(some_dtype)`` or ``a.view(dtype=some_dtype)`` constructs a view
 |      of the array's memory with a different data-type.  This can cause a
 |      reinterpretation of the bytes of memory.
 |
 |      ``a.view(ndarray_subclass)`` or ``a.view(type=ndarray_subclass)`` just
 |      returns an instance of `ndarray_subclass` that looks at the same array
 |      (same shape, dtype, etc.)  This does not cause a reinterpretation of the
 |      memory.
 |
 |      For ``a.view(some_dtype)``, if ``some_dtype`` has a different number of
 |      bytes per entry than the previous dtype (for example, converting a regular
 |      array to a structured array), then the last axis of ``a`` must be
 |      contiguous. This axis will be resized in the result.
 |
 |      .. versionchanged:: 1.23.0
 |         Only the last axis needs to be contiguous. Previously, the entire array
 |         had to be C-contiguous.
 |
 |      Examples
 |      --------
 |      >>> x = np.array([(1, 2)], dtype=[('a', np.int8), ('b', np.int8)])
 |
 |      Viewing array data using a different type and dtype:
 |
 |      >>> y = x.view(dtype=np.int16, type=np.matrix)
 |      >>> y
 |      matrix([[513]], dtype=int16)
 |      >>> print(type(y))
 |      <class 'numpy.matrix'>
 |
 |      Creating a view on a structured array so it can be used in calculations
 |
 |      >>> x = np.array([(1, 2),(3,4)], dtype=[('a', np.int8), ('b', np.int8)])
 |      >>> xv = x.view(dtype=np.int8).reshape(-1,2)
 |      >>> xv
 |      array([[1, 2],
 |             [3, 4]], dtype=int8)
 |      >>> xv.mean(0)
 |      array([2.,  3.])
 |
 |      Making changes to the view changes the underlying array
 |
 |      >>> xv[0,1] = 20
 |      >>> x
 |      array([(1, 20), (3,  4)], dtype=[('a', 'i1'), ('b', 'i1')])
 |
 |      Using a view to convert an array to a recarray:
 |
 |      >>> z = x.view(np.recarray)
 |      >>> z.a
 |      array([1, 3], dtype=int8)
 |
 |      Views share data:
 |
 |      >>> x[0] = (9, 10)
 |      >>> z[0]
 |      (9, 10)
 |
 |      Views that change the dtype size (bytes per entry) should normally be
 |      avoided on arrays defined by slices, transposes, fortran-ordering, etc.:
 |
 |      >>> x = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int16)
 |      >>> y = x[:, ::2]
 |      >>> y
 |      array([[1, 3],
 |             [4, 6]], dtype=int16)
 |      >>> y.view(dtype=[('width', np.int16), ('length', np.int16)])
 |      Traceback (most recent call last):
 |          ...
 |      ValueError: To change to a dtype of a different size, the last axis must be contiguous
 |      >>> z = y.copy()
 |      >>> z.view(dtype=[('width', np.int16), ('length', np.int16)])
 |      array([[(1, 3)],
 |             [(4, 6)]], dtype=[('width', '<i2'), ('length', '<i2')])
 |
 |      However, views that change dtype are totally fine for arrays with a
 |      contiguous last axis, even if the rest of the axes are not C-contiguous:
 |
 |      >>> x = np.arange(2 * 3 * 4, dtype=np.int8).reshape(2, 3, 4)
 |      >>> x.transpose(1, 0, 2).view(np.int16)
 |      array([[[ 256,  770],
 |              [3340, 3854]],
 |      <BLANKLINE>
 |             [[1284, 1798],
 |              [4368, 4882]],
 |      <BLANKLINE>
 |             [[2312, 2826],
 |              [5396, 5910]]], dtype=int16)
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __class_getitem__(...) from builtins.type
 |      a.__class_getitem__(item, /)
 |
 |      Return a parametrized wrapper around the `~numpy.ndarray` type.
 |
 |      .. versionadded:: 1.22
 |
 |      Returns
 |      -------
 |      alias : types.GenericAlias
 |          A parametrized `~numpy.ndarray` type.
 |
 |      Examples
 |      --------
 |      >>> from typing import Any
 |      >>> import numpy as np
 |
 |      >>> np.ndarray[Any, np.dtype[Any]]
 |      numpy.ndarray[typing.Any, numpy.dtype[typing.Any]]
 |
 |      See Also
 |      --------
 |      :pep:`585` : Type hinting generics in standard collections.
 |      numpy.typing.NDArray : An ndarray alias :term:`generic <generic type>`
 |                          w.r.t. its `dtype.type <numpy.dtype.type>`.
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
 |  T
 |      View of the transposed array.
 |
 |      Same as ``self.transpose()``.
 |
 |      Examples
 |      --------
 |      >>> a = np.array([[1, 2], [3, 4]])
 |      >>> a
 |      array([[1, 2],
 |             [3, 4]])
 |      >>> a.T
 |      array([[1, 3],
 |             [2, 4]])
 |
 |      >>> a = np.array([1, 2, 3, 4])
 |      >>> a
 |      array([1, 2, 3, 4])
 |      >>> a.T
 |      array([1, 2, 3, 4])
 |
 |      See Also
 |      --------
 |      transpose
 |
 |  __array_interface__
 |      Array protocol: Python side.
 |
 |  __array_priority__
 |      Array priority.
 |
 |  __array_struct__
 |      Array protocol: C-struct side.
 |
 |  base
 |      Base object if memory is from some other object.
 |
 |      Examples
 |      --------
 |      The base of an array that owns its memory is None:
 |
 |      >>> x = np.array([1,2,3,4])
 |      >>> x.base is None
 |      True
 |
 |      Slicing creates a view, whose memory is shared with x:
 |
 |      >>> y = x[2:]
 |      >>> y.base is x
 |      True
 |
 |  ctypes
 |      An object to simplify the interaction of the array with the ctypes
 |      module.
 |
 |      This attribute creates an object that makes it easier to use arrays
 |      when calling shared libraries with the ctypes module. The returned
 |      object has, among others, data, shape, and strides attributes (see
 |      Notes below) which themselves return ctypes objects that can be used
 |      as arguments to a shared library.
 |
 |      Parameters
 |      ----------
 |      None
 |
 |      Returns
 |      -------
 |      c : Python object
 |          Possessing attributes data, shape, strides, etc.
 |
 |      See Also
 |      --------
 |      numpy.ctypeslib
 |
 |      Notes
 |      -----
 |      Below are the public attributes of this object which were documented
 |      in "Guide to NumPy" (we have omitted undocumented public attributes,
 |      as well as documented private attributes):
 |
 |      .. autoattribute:: numpy.core._internal._ctypes.data
 |          :noindex:
 |
 |      .. autoattribute:: numpy.core._internal._ctypes.shape
 |          :noindex:
 |
 |      .. autoattribute:: numpy.core._internal._ctypes.strides
 |          :noindex:
 |
 |      .. automethod:: numpy.core._internal._ctypes.data_as
 |          :noindex:
 |
 |      .. automethod:: numpy.core._internal._ctypes.shape_as
 |          :noindex:
 |
 |      .. automethod:: numpy.core._internal._ctypes.strides_as
 |          :noindex:
 |
 |      If the ctypes module is not available, then the ctypes attribute
 |      of array objects still returns something useful, but ctypes objects
 |      are not returned and errors may be raised instead. In particular,
 |      the object will still have the ``as_parameter`` attribute which will
 |      return an integer equal to the data attribute.
 |
 |      Examples
 |      --------
 |      >>> import ctypes
 |      >>> x = np.array([[0, 1], [2, 3]], dtype=np.int32)
 |      >>> x
 |      array([[0, 1],
 |             [2, 3]], dtype=int32)
 |      >>> x.ctypes.data
 |      31962608 # may vary
 |      >>> x.ctypes.data_as(ctypes.POINTER(ctypes.c_uint32))
 |      <__main__.LP_c_uint object at 0x7ff2fc1fc200> # may vary
 |      >>> x.ctypes.data_as(ctypes.POINTER(ctypes.c_uint32)).contents
 |      c_uint(0)
 |      >>> x.ctypes.data_as(ctypes.POINTER(ctypes.c_uint64)).contents
 |      c_ulong(4294967296)
 |      >>> x.ctypes.shape
 |      <numpy.core._internal.c_long_Array_2 object at 0x7ff2fc1fce60> # may vary
 |      >>> x.ctypes.strides
 |      <numpy.core._internal.c_long_Array_2 object at 0x7ff2fc1ff320> # may vary
 |
 |  data
 |      Python buffer object pointing to the start of the array's data.
 |
 |  dtype
 |      Data-type of the array's elements.
 |
 |      .. warning::
 |
 |          Setting ``arr.dtype`` is discouraged and may be deprecated in the
 |          future.  Setting will replace the ``dtype`` without modifying the
 |          memory (see also `ndarray.view` and `ndarray.astype`).
 |
 |      Parameters
 |      ----------
 |      None
 |
 |      Returns
 |      -------
 |      d : numpy dtype object
 |
 |      See Also
 |      --------
 |      ndarray.astype : Cast the values contained in the array to a new data-type.
 |      ndarray.view : Create a view of the same data but a different data-type.
 |      numpy.dtype
 |
 |      Examples
 |      --------
 |      >>> x
 |      array([[0, 1],
 |             [2, 3]])
 |      >>> x.dtype
 |      dtype('int32')
 |      >>> type(x.dtype)
 |      <type 'numpy.dtype'>
 |
 |  flags
 |      Information about the memory layout of the array.
 |
 |      Attributes
 |      ----------
 |      C_CONTIGUOUS (C)
 |          The data is in a single, C-style contiguous segment.
 |      F_CONTIGUOUS (F)
 |          The data is in a single, Fortran-style contiguous segment.
 |      OWNDATA (O)
 |          The array owns the memory it uses or borrows it from another object.
 |      WRITEABLE (W)
 |          The data area can be written to.  Setting this to False locks
 |          the data, making it read-only.  A view (slice, etc.) inherits WRITEABLE
 |          from its base array at creation time, but a view of a writeable
 |          array may be subsequently locked while the base array remains writeable.
 |          (The opposite is not true, in that a view of a locked array may not
 |          be made writeable.  However, currently, locking a base object does not
 |          lock any views that already reference it, so under that circumstance it
 |          is possible to alter the contents of a locked array via a previously
 |          created writeable view onto it.)  Attempting to change a non-writeable
 |          array raises a RuntimeError exception.
 |      ALIGNED (A)
 |          The data and all elements are aligned appropriately for the hardware.
 |      WRITEBACKIFCOPY (X)
 |          This array is a copy of some other array. The C-API function
 |          PyArray_ResolveWritebackIfCopy must be called before deallocating
 |          to the base array will be updated with the contents of this array.
 |      FNC
 |          F_CONTIGUOUS and not C_CONTIGUOUS.
 |      FORC
 |          F_CONTIGUOUS or C_CONTIGUOUS (one-segment test).
 |      BEHAVED (B)
 |          ALIGNED and WRITEABLE.
 |      CARRAY (CA)
 |          BEHAVED and C_CONTIGUOUS.
 |      FARRAY (FA)
 |          BEHAVED and F_CONTIGUOUS and not C_CONTIGUOUS.
 |
 |      Notes
 |      -----
 |      The `flags` object can be accessed dictionary-like (as in ``a.flags['WRITEABLE']``),
 |      or by using lowercased attribute names (as in ``a.flags.writeable``). Short flag
 |      names are only supported in dictionary access.
 |
 |      Only the WRITEBACKIFCOPY, WRITEABLE, and ALIGNED flags can be
 |      changed by the user, via direct assignment to the attribute or dictionary
 |      entry, or by calling `ndarray.setflags`.
 |
 |      The array flags cannot be set arbitrarily:
 |
 |      - WRITEBACKIFCOPY can only be set ``False``.
 |      - ALIGNED can only be set ``True`` if the data is truly aligned.
 |      - WRITEABLE can only be set ``True`` if the array owns its own memory
 |        or the ultimate owner of the memory exposes a writeable buffer
 |        interface or is a string.
 |
 |      Arrays can be both C-style and Fortran-style contiguous simultaneously.
 |      This is clear for 1-dimensional arrays, but can also be true for higher
 |      dimensional arrays.
 |
 |      Even for contiguous arrays a stride for a given dimension
 |      ``arr.strides[dim]`` may be *arbitrary* if ``arr.shape[dim] == 1``
 |      or the array has no elements.
 |      It does *not* generally hold that ``self.strides[-1] == self.itemsize``
 |      for C-style contiguous arrays or ``self.strides[0] == self.itemsize`` for
 |      Fortran-style contiguous arrays is true.
 |
 |  flat
 |      A 1-D iterator over the array.
 |
 |      This is a `numpy.flatiter` instance, which acts similarly to, but is not
 |      a subclass of, Python's built-in iterator object.
 |
 |      See Also
 |      --------
 |      flatten : Return a copy of the array collapsed into one dimension.
 |
 |      flatiter
 |
 |      Examples
 |      --------
 |      >>> x = np.arange(1, 7).reshape(2, 3)
 |      >>> x
 |      array([[1, 2, 3],
 |             [4, 5, 6]])
 |      >>> x.flat[3]
 |      4
 |      >>> x.T
 |      array([[1, 4],
 |             [2, 5],
 |             [3, 6]])
 |      >>> x.T.flat[3]
 |      5
 |      >>> type(x.flat)
 |      <class 'numpy.flatiter'>
 |
 |      An assignment example:
 |
 |      >>> x.flat = 3; x
 |      array([[3, 3, 3],
 |             [3, 3, 3]])
 |      >>> x.flat[[1,4]] = 1; x
 |      array([[3, 1, 3],
 |             [3, 1, 3]])
 |
 |  imag
 |      The imaginary part of the array.
 |
 |      Examples
 |      --------
 |      >>> x = np.sqrt([1+0j, 0+1j])
 |      >>> x.imag
 |      array([ 0.        ,  0.70710678])
 |      >>> x.imag.dtype
 |      dtype('float64')
 |
 |  itemsize
 |      Length of one array element in bytes.
 |
 |      Examples
 |      --------
 |      >>> x = np.array([1,2,3], dtype=np.float64)
 |      >>> x.itemsize
 |      8
 |      >>> x = np.array([1,2,3], dtype=np.complex128)
 |      >>> x.itemsize
 |      16
 |
 |  nbytes
 |      Total bytes consumed by the elements of the array.
 |
 |      Notes
 |      -----
 |      Does not include memory consumed by non-element attributes of the
 |      array object.
 |
 |      See Also
 |      --------
 |      sys.getsizeof
 |          Memory consumed by the object itself without parents in case view.
 |          This does include memory consumed by non-element attributes.
 |
 |      Examples
 |      --------
 |      >>> x = np.zeros((3,5,2), dtype=np.complex128)
 |      >>> x.nbytes
 |      480
 |      >>> np.prod(x.shape) * x.itemsize
 |      480
 |
 |  ndim
 |      Number of array dimensions.
 |
 |      Examples
 |      --------
 |      >>> x = np.array([1, 2, 3])
 |      >>> x.ndim
 |      1
 |      >>> y = np.zeros((2, 3, 4))
 |      >>> y.ndim
 |      3
 |
 |  real
 |      The real part of the array.
 |
 |      Examples
 |      --------
 |      >>> x = np.sqrt([1+0j, 0+1j])
 |      >>> x.real
 |      array([ 1.        ,  0.70710678])
 |      >>> x.real.dtype
 |      dtype('float64')
 |
 |      See Also
 |      --------
 |      numpy.real : equivalent function
 |
 |  shape
 |      Tuple of array dimensions.
 |
 |      The shape property is usually used to get the current shape of an array,
 |      but may also be used to reshape the array in-place by assigning a tuple of
 |      array dimensions to it.  As with `numpy.reshape`, one of the new shape
 |      dimensions can be -1, in which case its value is inferred from the size of
 |      the array and the remaining dimensions. Reshaping an array in-place will
 |      fail if a copy is required.
 |
 |      .. warning::
 |
 |          Setting ``arr.shape`` is discouraged and may be deprecated in the
 |          future.  Using `ndarray.reshape` is the preferred approach.
 |
 |      Examples
 |      --------
 |      >>> x = np.array([1, 2, 3, 4])
 |      >>> x.shape
 |      (4,)
 |      >>> y = np.zeros((2, 3, 4))
 |      >>> y.shape
 |      (2, 3, 4)
 |      >>> y.shape = (3, 8)
 |      >>> y
 |      array([[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
 |             [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
 |             [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]])
 |      >>> y.shape = (3, 6)
 |      Traceback (most recent call last):
 |        File "<stdin>", line 1, in <module>
 |      ValueError: total size of new array must be unchanged
 |      >>> np.zeros((4,2))[::2].shape = (-1,)
 |      Traceback (most recent call last):
 |        File "<stdin>", line 1, in <module>
 |      AttributeError: Incompatible shape for in-place modification. Use
 |      `.reshape()` to make a copy with the desired shape.
 |
 |      See Also
 |      --------
 |      numpy.shape : Equivalent getter function.
 |      numpy.reshape : Function similar to setting ``shape``.
 |      ndarray.reshape : Method similar to setting ``shape``.
 |
 |  size
 |      Number of elements in the array.
 |
 |      Equal to ``np.prod(a.shape)``, i.e., the product of the array's
 |      dimensions.
 |
 |      Notes
 |      -----
 |      `a.size` returns a standard arbitrary precision Python integer. This
 |      may not be the case with other methods of obtaining the same value
 |      (like the suggested ``np.prod(a.shape)``, which returns an instance
 |      of ``np.int_``), and may be relevant if the value is used further in
 |      calculations that may overflow a fixed size integer type.
 |
 |      Examples
 |      --------
 |      >>> x = np.zeros((3, 5, 2), dtype=np.complex128)
 |      >>> x.size
 |      30
 |      >>> np.prod(x.shape)
 |      30
 |
 |  strides
 |      Tuple of bytes to step in each dimension when traversing an array.
 |
 |      The byte offset of element ``(i[0], i[1], ..., i[n])`` in an array `a`
 |      is::
 |
 |          offset = sum(np.array(i) * a.strides)
 |
 |      A more detailed explanation of strides can be found in the
 |      "ndarray.rst" file in the NumPy reference guide.
 |
 |      .. warning::
 |
 |          Setting ``arr.strides`` is discouraged and may be deprecated in the
 |          future.  `numpy.lib.stride_tricks.as_strided` should be preferred
 |          to create a new view of the same data in a safer way.
 |
 |      Notes
 |      -----
 |      Imagine an array of 32-bit integers (each 4 bytes)::
 |
 |        x = np.array([[0, 1, 2, 3, 4],
 |                      [5, 6, 7, 8, 9]], dtype=np.int32)
 |
 |      This array is stored in memory as 40 bytes, one after the other
 |      (known as a contiguous block of memory).  The strides of an array tell
 |      us how many bytes we have to skip in memory to move to the next position
 |      along a certain axis.  For example, we have to skip 4 bytes (1 value) to
 |      move to the next column, but 20 bytes (5 values) to get to the same
 |      position in the next row.  As such, the strides for the array `x` will be
 |      ``(20, 4)``.
 |
 |      See Also
 |      --------
 |      numpy.lib.stride_tricks.as_strided
 |
 |      Examples
 |      --------
 |      >>> y = np.reshape(np.arange(2*3*4), (2,3,4))
 |      >>> y
 |      array([[[ 0,  1,  2,  3],
 |              [ 4,  5,  6,  7],
 |              [ 8,  9, 10, 11]],
 |             [[12, 13, 14, 15],
 |              [16, 17, 18, 19],
 |              [20, 21, 22, 23]]])
 |      >>> y.strides
 |      (48, 16, 4)
 |      >>> y[1,1,1]
 |      17
 |      >>> offset=sum(y.strides * np.array((1,1,1)))
 |      >>> offset/y.itemsize
 |      17
 |
 |      >>> x = np.reshape(np.arange(5*6*7*8), (5,6,7,8)).transpose(2,3,1,0)
 |      >>> x.strides
 |      (32, 4, 224, 1344)
 |      >>> i = np.array([3,5,2,2])
 |      >>> offset = sum(i * x.strides)
 |      >>> x[3,5,2,2]
 |      813
 |      >>> offset / x.itemsize
 |      813
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __hash__ = None

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
&&&&&&&&&&&&&&&&&&&&&& linspace &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Help on _ArrayFunctionDispatcher in module numpy:

linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
    Return evenly spaced numbers over a specified interval.

    Returns `num` evenly spaced samples, calculated over the
    interval [`start`, `stop`].

    The endpoint of the interval can optionally be excluded.

    .. versionchanged:: 1.16.0
        Non-scalar `start` and `stop` are now supported.

    .. versionchanged:: 1.20.0
        Values are rounded towards ``-inf`` instead of ``0`` when an
        integer ``dtype`` is specified. The old behavior can
        still be obtained with ``np.linspace(start, stop, num).astype(int)``

    Parameters
    ----------
    start : array_like
        The starting value of the sequence.
    stop : array_like
        The end value of the sequence, unless `endpoint` is set to False.
        In that case, the sequence consists of all but the last of ``num + 1``
        evenly spaced samples, so that `stop` is excluded.  Note that the step
        size changes when `endpoint` is False.
    num : int, optional
        Number of samples to generate. Default is 50. Must be non-negative.
    endpoint : bool, optional
        If True, `stop` is the last sample. Otherwise, it is not included.
        Default is True.
    retstep : bool, optional
        If True, return (`samples`, `step`), where `step` is the spacing
        between samples.
    dtype : dtype, optional
        The type of the output array.  If `dtype` is not given, the data type
        is inferred from `start` and `stop`. The inferred dtype will never be
        an integer; `float` is chosen even if the arguments would produce an
        array of integers.

        .. versionadded:: 1.9.0

    axis : int, optional
        The axis in the result to store the samples.  Relevant only if start
        or stop are array-like.  By default (0), the samples will be along a
        new axis inserted at the beginning. Use -1 to get an axis at the end.

        .. versionadded:: 1.16.0

    Returns
    -------
    samples : ndarray
        There are `num` equally spaced samples in the closed interval
        ``[start, stop]`` or the half-open interval ``[start, stop)``
        (depending on whether `endpoint` is True or False).
    step : float, optional
        Only returned if `retstep` is True

        Size of spacing between samples.


    See Also
    --------
    arange : Similar to `linspace`, but uses a step size (instead of the
             number of samples).
    geomspace : Similar to `linspace`, but with numbers spaced evenly on a log
                scale (a geometric progression).
    logspace : Similar to `geomspace`, but with the end points specified as
               logarithms.
    :ref:`how-to-partition`

    Examples
    --------
    >>> np.linspace(2.0, 3.0, num=5)
    array([2.  , 2.25, 2.5 , 2.75, 3.  ])
    >>> np.linspace(2.0, 3.0, num=5, endpoint=False)
    array([2. ,  2.2,  2.4,  2.6,  2.8])
    >>> np.linspace(2.0, 3.0, num=5, retstep=True)
    (array([2.  ,  2.25,  2.5 ,  2.75,  3.  ]), 0.25)

    Graphical illustration:

    >>> import matplotlib.pyplot as plt
    >>> N = 8
    >>> y = np.zeros(N)
    >>> x1 = np.linspace(0, 10, N, endpoint=True)
    >>> x2 = np.linspace(0, 10, N, endpoint=False)
    >>> plt.plot(x1, y, 'o')
    [<matplotlib.lines.Line2D object at 0x...>]
    >>> plt.plot(x2, y + 0.5, 'o')
    [<matplotlib.lines.Line2D object at 0x...>]
    >>> plt.ylim([-0.5, 1])
    (-0.5, 1)
    >>> plt.show()

None
