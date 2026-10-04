Ejemplos
========

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

agg = aggregate(self, func=None, axis: 'Axis' = 0, *args, **kwargs)


