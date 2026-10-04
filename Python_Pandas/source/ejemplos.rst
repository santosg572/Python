Ejemplos
========

**class DataFrame**

Constructing DataFrame from a dictionary.

>>> d = {'col1': [1, 2], 'col2': [3, 4]}
>>> df = pd.DataFrame(data=d)
>>> df
col1 col2
0 1 3
1 2 4

Notice that the inferred dtype is int64.

>>> df.dtypes
col1 int64
col2 int64
dtype: object

To enforce a single dtype:

>>> df = pd.DataFrame(data=d, dtype=np.int8)
>>> df.dtypes
col1 int8
col2 int8
dtype: object

Constructing DataFrame from a dictionary including Series:

>>> d = {'col1': [0, 1, 2, 3], 'col2': pd.Series([2, 3], index=[2, 3])}
>>> pd.DataFrame(data=d, index=[0, 1, 2, 3])
col1 col2
0 0 NaN
1 1 NaN
2 2 2.0
3 3 3.0


Constructing DataFrame from numpy ndarray:

>>> df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
... columns=['a', 'b', 'c'])
>>> df2
a b c
0 1 2 3
1 4 5 6
2 7 8 9

Constructing DataFrame from a numpy ndarray that has labeled columns:

>>> data = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)],
... dtype=[("a", "i4"), ("b", "i4"), ("c", "i4")])

>>> df3 = pd.DataFrame(data, columns=['c', 'a'])
...

>>> df3
c a
0 3 1
1 6 4
2 9 7


Constructing DataFrame from dataclass:

>>> from dataclasses import make_dataclass
>>> Point = make_dataclass("Point", [("x", int), ("y", int)])
>>> pd.DataFrame([Point(0, 0), Point(0, 3), Point(2, 3)])
x y
0 0 0
1 0 3
2 2 3

Constructing DataFrame from Series/DataFrame:

>>> ser = pd.Series([1, 2, 3], index=["a", "b", "c"])
>>> df = pd.DataFrame(data=ser, index=["a", "c"])
>>> df
0
a 1
c 3

>>> df1 = pd.DataFrame([1, 2, 3], index=["a", "b", "c"], columns=["x"])
>>> df2 = pd.DataFrame(data=df1, index=["a", "c"])
>>> df2
x
a 1
c 3

**Examples-02**

>>> df = pd.DataFrame({'angles': [0, 3, 4],
... 'degrees': [360, 180, 360]},
... index=['circle', 'triangle', 'rectangle'])
>>> df
angles degrees
circle 0 360
triangle 3 180
rectangle 4 360

Add a scalar with operator version which return the same
results.

>>> df + 1
angles degrees
circle 1 361
triangle 4 181
rectangle 5 361

>>> df.add(1)
angles degrees
circle 1 361
triangle 4 181
rectangle 5 361

Divide by constant with reverse version.

>>> df.div(10)
angles degrees
circle 0.0 36.0
triangle 0.3 18.0
rectangle 0.4 36.0

>>> df.rdiv(10)
angles degrees
circle inf 0.027778
triangle 3.333333 0.055556
rectangle 2.500000 0.027778

Subtract a list and Series by axis with operator version.

>>> df - [1, 2]
angles degrees
circle -1 358
triangle 2 178
rectangle 3 358

>>> df.sub([1, 2], axis='columns')
angles degrees
circle -1 358
triangle 2 178
rectangle 3 358

>>> df.sub(pd.Series([1, 1, 1], index=['circle', 'triangle', 'rectangle']),
... axis='index')
angles degrees
circle -1 359
triangle 2 179
rectangle 3 359

Multiply a dictionary by axis.

>>> df.mul({'angles': 0, 'degrees': 2})
angles degrees
circle 0 720
triangle 0 360
rectangle 0 720

>>> df.mul({'circle': 0, 'triangle': 2, 'rectangle': 3}, axis='index')
angles degrees
circle 0 0
triangle 6 360
rectangle 12 1080

Multiply a DataFrame of different shape with operator version.

>>> other = pd.DataFrame({'angles': [0, 3, 4]},
... index=['circle', 'triangle', 'rectangle'])
>>> other
angles
circle 0
triangle 3
rectangle 4

>>> df * other
angles degrees
circle 0 NaN
triangle 9 NaN
rectangle 16 NaN

>>> df.mul(other, fill_value=0)
angles degrees
circle 0 0.0
triangle 9 0.0
rectangle 16 0.0

Divide by a MultiIndex by level.

>>> df_multindex = pd.DataFrame({'angles': [0, 3, 4, 4, 5, 6],
... 'degrees': [360, 180, 360, 360, 540, 720]},
... index=[['A', 'A', 'A', 'B', 'B', 'B'],
... ['circle', 'triangle', 'rectangle',
... 'square', 'pentagon', 'hexagon']])
>>> df_multindex
angles degrees
A circle 0 360
triangle 3 180
rectangle 4 360
B square 4 360
pentagon 5 540
hexagon 6 720

>>> df.div(df_multindex, level=1, fill_value=0)
angles degrees
A circle NaN 1.0
triangle 1.0 1.0
rectangle 1.0 1.0
B square 0.0 0.0
pentagon 0.0 0.0
hexagon 0.0 0.0

**Ejemplos Aggregate**

>>> df = pd.DataFrame([[1, 2, 3],
... [4, 5, 6],
... [7, 8, 9],
... [np.nan, np.nan, np.nan]],
... columns=['A', 'B', 'C'])

9999

Aggregate these functions over the rows.

>>> df.agg(['sum', 'min'])
A B C
sum 12.0 15.0 18.0
min 1.0 2.0 3.0

Different aggregations per column.

>>> df.agg({'A' : ['sum', 'min'], 'B' : ['min', 'max']})
A B
sum 12.0 NaN
min 1.0 2.0
max NaN 8.0

Aggregate different functions over the columns and rename the index of the resulting
DataFrame.

>>> df.agg(x=('A', 'max'), y=('B', 'min'), z=('C', 'mean'))
A B C
x 7.0 NaN NaN
y NaN 2.0 NaN
z NaN NaN 6.0

Aggregate over the columns.

>>> df.agg("mean", axis="columns")
0 2.0
1 5.0
2 8.0
3 NaN
dtype: float64

**Ejemplos**

Series

>>> pd.Series([True, True]).all()
True
>>> pd.Series([True, False]).all()
False
>>> pd.Series([], dtype="float64").all()
True
>>> pd.Series([np.nan]).all()
True
>>> pd.Series([np.nan]).all(skipna=False)
True

DataFrames

Create a dataframe from a dictionary.

>>> df = pd.DataFrame({'col1': [True, True], 'col2': [True, False]})
>>> df
col1 col2
0 True True
1 True False

Default behaviour checks if values in each column all return True.

>>> df.all()
col1 True
col2 False
dtype: bool

Specify axis='columns' to check if values in each row all return True.

>>> df.all(axis='columns')
0 True
1 False
dtype: bool

Or axis=None for whether every value is True.

>>> df.all(axis=None)
False

Examples
--------
Series

For Series input, the output is a scalar indicating whether any element
is True.

>>> pd.Series([False, False]).any()
False
>>> pd.Series([True, False]).any()
True
>>> pd.Series([], dtype="float64").any()
False
>>> pd.Series([np.nan]).any()
False
>>> pd.Series([np.nan]).any(skipna=False)
True

DataFrame

Whether each column contains at least one True element (the default).

>>> df = pd.DataFrame({"A": [1, 2], "B": [0, 2], "C": [0, 0]})
>>> df
A B C
0 1 0 0
1 2 2 0

>>> df.any()
A True
B True
C False
dtype: bool

Aggregating over the columns.

>>> df = pd.DataFrame({"A": [True, False], "B": [1, 2]})
>>> df
A B
0 True 1
1 False 2

>>> df.any(axis='columns')
0 True
1 True
dtype: bool

>>> df = pd.DataFrame({"A": [True, False], "B": [1, 0]})
>>> df
A B
0 True 1
1 False 0

>>> df.any(axis='columns')
0 True
1 False
dtype: bool

Aggregating over the entire DataFrame with axis=None.

>>> df.any(axis=None)
True

any for an empty DataFrame is an empty Series.

>>> pd.DataFrame([]).any()
Series([], dtype: bool)

Examples
--------
>>> df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
>>> df
A B
0 4 9
1 4 9
2 4 9


Using a numpy universal function (in this case the same as
np.sqrt(df)):

>>> df.apply(np.sqrt)
A B
0 2.0 3.0
1 2.0 3.0
2 2.0 3.0

Using a reducing function on either axis

>>> df.apply(np.sum, axis=0)
A 12
B 27
dtype: int64

>>> df.apply(np.sum, axis=1)
0 13
1 13
2 13
dtype: int64

Returning a list-like will result in a Series

>>> df.apply(lambda x: [1, 2], axis=1)
0 [1, 2]
1 [1, 2]
2 [1, 2]
dtype: object

Passing result_type='expand' will expand list-like results
to columns of a Dataframe

>>> df.apply(lambda x: [1, 2], axis=1, result_type='expand')
0 1
0 1 2
1 1 2
2 1 2

Returning a Series inside the function is similar to passing
result_type='expand'. The resulting column names
will be the Series index.

>>> df.apply(lambda x: pd.Series([1, 2], index=['foo', 'bar']), axis=1)
foo bar
0 1 2
1 1 2
2 1 2

Passing result_type='broadcast' will ensure the same shape
result, whether list-like or scalar is returned by the function,
and broadcast it along the axis. The resulting column names will
be the originals.

>>> df.apply(lambda x: [1, 2], axis=1, result_type='broadcast')
A B
0 1 2
1 1 2
2 1 2

Examples
--------
>>> df = pd.DataFrame([[1, 2.12], [3.356, 4.567]])
>>> df
0 1
0 1.000 2.120
1 3.356 4.567

>>> df.map(lambda x: len(str(x)))
0 1
0 3 4
1 5 5


Examples
--------
>>> df = pd.DataFrame({'temp_c': [17.0, 25.0]},
... index=['Portland', 'Berkeley'])
>>> df
temp_c
Portland 17.0
Berkeley 25.0

Where the value is a callable, evaluated on df:

>>> df.assign(temp_f=lambda x: x.temp_c * 9 / 5 + 32)
temp_c temp_f
Portland 17.0 62.6
Berkeley 25.0 77.0


Alternatively, the same behavior can be achieved by directly
referencing an existing Series or sequence:

>>> df.assign(temp_f=df['temp_c'] * 9 / 5 + 32)
temp_c temp_f
Portland 17.0 62.6
Berkeley 25.0 77.0


You can create multiple columns within the same assign where one
of the columns depends on another one defined within the same assign:

>>> df.assign(temp_f=lambda x: x['temp_c'] * 9 / 5 + 32,
... temp_k=lambda x: (x['temp_f'] + 459.67) * 5 / 9)
temp_c temp_f temp_k
Portland 17.0 62.6 290.15
Berkeley 25.0 77.0 298.15

Examples
--------

Boxplots can be created for every column in the dataframe
by df.boxplot() or indicating the columns to be used:

.. plot::
:context: close-figs

>>> np.random.seed(1234)
>>> df = pd.DataFrame(np.random.randn(10, 4),
... columns=['Col1', 'Col2', 'Col3', 'Col4'])
>>> boxplot = df.boxplot(column=['Col1', 'Col2', 'Col3']) # doctest: +SKIP

Boxplots of variables distributions grouped by the values of a third
variable can be created using the option by. For instance:

.. plot::
:context: close-figs

>>> df = pd.DataFrame(np.random.randn(10, 2),
... columns=['Col1', 'Col2'])
>>> df['X'] = pd.Series(['A', 'A', 'A', 'A', 'A',
... 'B', 'B', 'B', 'B', 'B'])
>>> boxplot = df.boxplot(by='X')

A list of strings (i.e. ['X', 'Y']) can be passed to boxplot
in order to group the data by combination of the variables in the x-axis:

.. plot::
:context: close-figs

>>> df = pd.DataFrame(np.random.randn(10, 3),
... columns=['Col1', 'Col2', 'Col3'])
>>> df['X'] = pd.Series(['A', 'A', 'A', 'A', 'A',
... 'B', 'B', 'B', 'B', 'B'])
>>> df['Y'] = pd.Series(['A', 'B', 'A', 'B', 'A',
... 'B', 'A', 'B', 'A', 'B'])
>>> boxplot = df.boxplot(column=['Col1', 'Col2'], by=['X', 'Y'])

The layout of boxplot can be adjusted giving a tuple to layout:

.. plot::
:context: close-figs

>>> boxplot = df.boxplot(column=['Col1', 'Col2'], by='X',
... layout=(2, 1))

Additional formatting can be done to the boxplot, like suppressing the grid
(grid=False), rotating the labels in the x-axis (i.e. rot=45)
or changing the fontsize (i.e. fontsize=15):

.. plot::
:context: close-figs

>>> boxplot = df.boxplot(grid=False, rot=45, fontsize=15) # doctest: +SKIP

The parameter return_type can be used to select the type of element
returned by boxplot. When return_type='axes' is selected,
the matplotlib axes on which the boxplot is drawn are returned:

>>> boxplot = df.boxplot(column=['Col1', 'Col2'], return_type='axes')
>>> type(boxplot)
<class 'matplotlib.axes._axes.Axes'>

When grouping with by, a Series mapping columns to return_type
is returned:

>>> boxplot = df.boxplot(column=['Col1', 'Col2'], by='X',
... return_type='axes')
>>> type(boxplot)
<class 'pandas.core.series.Series'>

If return_type is None, a NumPy array of axes with the same shape
as layout is returned:

>>> boxplot = df.boxplot(column=['Col1', 'Col2'], by='X',
... return_type=None)
>>> type(boxplot)
<class 'numpy.ndarray'>


**combine**

Examples
--------
Combine using a simple function that chooses the smaller column.

>>> df1 = pd.DataFrame({'A': [0, 0], 'B': [4, 4]})
>>> df2 = pd.DataFrame({'A': [1, 1], 'B': [3, 3]})
>>> take_smaller = lambda s1, s2: s1 if s1.sum() < s2.sum() else s2
>>> df1.combine(df2, take_smaller)
A B
0 0 3
1 0 3

Example using a true element-wise combine function.

>>> df1 = pd.DataFrame({'A': [5, 0], 'B': [2, 4]})
>>> df2 = pd.DataFrame({'A': [1, 1], 'B': [3, 3]})
>>> df1.combine(df2, np.minimum)
A B
0 1 2
1 0 3

Using fill_value fills Nones prior to passing the column to the
merge function.

>>> df1 = pd.DataFrame({'A': [0, 0], 'B': [None, 4]})
>>> df2 = pd.DataFrame({'A': [1, 1], 'B': [3, 3]})
>>> df1.combine(df2, take_smaller, fill_value=-5)
A B
0 0 -5.0
1 0 4.0

>>> df1 = pd.DataFrame({'A': [0, 0], 'B': [None, 4]})
>>> df2 = pd.DataFrame({'A': [1, 1], 'B': [None, 3]})
>>> df1.combine(df2, take_smaller, fill_value=-5)
A B
0 0 -5.0
1 0 3.0

Example that demonstrates the use of overwrite and behavior when
the axis differ between the dataframes.

>>> df1 = pd.DataFrame({'A': [0, 0], 'B': [4, 4]})
>>> df2 = pd.DataFrame({'B': [3, 3], 'C': [-10, 1], }, index=[1, 2])
>>> df1.combine(df2, take_smaller)
A B C
0 NaN NaN NaN
1 NaN 3.0 -10.0
2 NaN 3.0 1.0

>>> df1.combine(df2, take_smaller, overwrite=False)
A B C
0 0.0 NaN NaN
1 0.0 3.0 -10.0
2 NaN 3.0 1.0

Demonstrating the preference of the passed in dataframe.

>>> df2 = pd.DataFrame({'B': [3, 3], 'C': [1, 1], }, index=[1, 2])
>>> df2.combine(df1, take_smaller)
A B C
0 0.0 NaN NaN
1 0.0 3.0 NaN
2 NaN 3.0 NaN

>>> df2.combine(df1, take_smaller, overwrite=False)
A B C
0 0.0 NaN NaN
1 0.0 3.0 1.0
2 NaN 3.0 1.0

**combine_first**

Combine two DataFrame objects by filling null values

