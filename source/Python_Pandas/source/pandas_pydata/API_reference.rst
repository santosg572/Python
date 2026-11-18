API reference
=============

https://pandas.pydata.org/docs/reference/index.html

API reference
This page gives an overview of all public pandas objects, functions and methods. All classes and 
functions exposed in pandas.* namespace are public.

The following subpackages are public.

pandas.errors: Custom exception and warnings classes that are raised by pandas.

pandas.plotting: Plotting public API.

pandas.testing: Functions that are useful for writing tests involving pandas objects.

pandas.api.extensions: Functions and classes for extending pandas objects.

pandas.api.indexers: Functions and classes for rolling window indexers.

pandas.api.interchange: DataFrame interchange protocol.

pandas.api.types: Datatype classes and functions.

pandas.api.typing: Classes that may be necessary for type-hinting. These are classes that are 
encountered as intermediate results but should not be instantiated directly by users. These classes 
are not to be confused with classes from the pandas-stubs package which has classes in addition to 
those that occur in pandas for type-hinting.

In addition, public functions in pandas.io, pandas.tseries, pandas.util submodules are explicitly 
mentioned in the documentation. Further APIs in these modules are not guaranteed to be stable.

Warning

The pandas.core, pandas.compat top-level modules are PRIVATE. Stable functionality in such modules 
is not guaranteed.

Input/output
Pickling
Flat file
Clipboard
Excel
JSON
HTML
XML
Latex
HDFStore: PyTables (HDF5)
Feather
Parquet
Iceberg
ORC
SAS
SPSS
SQL
STATA
General functions
Data manipulations
Top-level missing data
Top-level dealing with numeric data
Top-level dealing with datetimelike data
Top-level dealing with Interval data
Top-level evaluation
Datetime formats
Hashing
Importing from other DataFrame libraries
Series
Constructor
Attributes
Conversion
Indexing, iteration
Binary operator functions
Function application, GroupBy & window
Computations / descriptive stats
Reindexing / selection / label manipulation
Missing data handling
Reshaping, sorting
Combining / comparing / joining / merging
Time Series-related
Accessors
Plotting
Serialization / IO / conversion
DataFrame
Constructor
Attributes and underlying data
Conversion
Indexing, iteration
Binary operator functions
Function application, GroupBy & window
Computations / descriptive stats
Reindexing / selection / label manipulation
Missing data handling
Reshaping, sorting, transposing
Combining / comparing / joining / merging
Time Series-related
Flags
Metadata
Plotting
Sparse accessor
Serialization / IO / conversion
pandas arrays, scalars, and data types
Objects
Utilities
Index objects
Index
Numeric Index
CategoricalIndex
IntervalIndex
MultiIndex
DatetimeIndex
TimedeltaIndex
PeriodIndex
Date offsets
DateOffset
BusinessDay
BusinessHour
CustomBusinessDay
CustomBusinessHour
MonthEnd
MonthBegin
BusinessMonthEnd
BusinessMonthBegin
CustomBusinessMonthEnd
CustomBusinessMonthBegin
SemiMonthEnd
SemiMonthBegin
Week
WeekOfMonth
LastWeekOfMonth
BQuarterEnd
BQuarterBegin
QuarterEnd
QuarterBegin
BHalfYearEnd
BHalfYearBegin
HalfYearEnd
HalfYearBegin
BYearEnd
BYearBegin
YearEnd
YearBegin
FY5253
FY5253Quarter
Easter
Tick
Day
Hour
Minute
Second
Milli
Micro
Nano
Frequencies
pandas.tseries.frequencies.to_offset
Window
Rolling window functions
Weighted window functions
Expanding window functions
Exponentially-weighted window functions
Window indexer
GroupBy
Indexing, iteration
Function application helper
Function application
DataFrameGroupBy computations / descriptive stats
SeriesGroupBy computations / descriptive stats
Plotting and visualization
Resampling
Indexing, iteration
Function application
Upsampling
Computations / descriptive stats
Style
Styler constructor
Styler properties
Style application
Builtin styles
Style export and import
Plotting
pandas.plotting.andrews_curves
pandas.plotting.autocorrelation_plot
pandas.plotting.bootstrap_plot
pandas.plotting.boxplot
pandas.plotting.deregister_matplotlib_converters
pandas.plotting.lag_plot
pandas.plotting.parallel_coordinates
pandas.plotting.plot_params
pandas.plotting.radviz
pandas.plotting.register_matplotlib_converters
pandas.plotting.scatter_matrix
pandas.plotting.table
Options and settings
Working with options
Numeric formatting
Extensions
pandas.api.extensions.register_extension_dtype
pandas.api.extensions.register_dataframe_accessor
pandas.api.extensions.register_series_accessor
pandas.api.extensions.register_index_accessor
pandas.api.extensions.ExtensionDtype
pandas.api.extensions.ExtensionArray
pandas.arrays.NumpyExtensionArray
pandas.api.indexers.check_array_indexer
Testing
Assertion functions
Exceptions and warnings
Bug report function
Test suite runner
Missing values
pandas.NA
pandas.NaT
pandas typing aliases
Typing aliases

**Input/output**

Pickling
read_pickle(filepath_or_buffer[, ...])

Load pickled pandas object (or any object) from file and return unpickled object.

DataFrame.to_pickle(path, *[, compression, ...])

Pickle (serialize) object to file.

Flat file
read_table(filepath_or_buffer, *[, sep, ...])

Read general delimited file into DataFrame.

read_csv(filepath_or_buffer, *[, sep, ...])

Read a comma-separated values (csv) file into DataFrame.

DataFrame.to_csv([path_or_buf, sep, na_rep, ...])

Write object to a comma-separated values (csv) file.

read_fwf(filepath_or_buffer, *[, colspecs, ...])

Read a table of fixed-width formatted lines into DataFrame.

Clipboard
read_clipboard([sep, dtype_backend])

Read text from clipboard and pass to read_csv().

DataFrame.to_clipboard(*[, excel, sep])

Copy object to the system clipboard.

Excel
read_excel(io[, sheet_name, header, names, ...])

Read an Excel file into a DataFrame.

DataFrame.to_excel(excel_writer, *[, ...])

Write object to an Excel sheet.

ExcelFile(path_or_buffer[, engine, ...])

Class for parsing tabular Excel sheets into DataFrame objects.

ExcelFile.book

Gets the Excel workbook.

ExcelFile.sheet_names

Names of the sheets in the document.

ExcelFile.parse([sheet_name, header, names, ...])

Parse specified sheet(s) into a DataFrame.

Styler.to_excel(excel_writer[, sheet_name, ...])

Write Styler to an Excel sheet.

ExcelWriter(path[, engine, date_format, ...])

Class for writing DataFrame objects into excel sheets.

JSON
read_json(path_or_buf, *[, orient, typ, ...])

Convert a JSON string to pandas object.

json_normalize(data[, record_path, meta, ...])

Normalize semi-structured JSON data into a flat table.

DataFrame.to_json([path_or_buf, orient, ...])

Convert the object to a JSON string.

build_table_schema(data[, index, ...])

Create a Table schema from data.

HTML
read_html(io, *[, match, flavor, header, ...])

Read HTML tables into a list of DataFrame objects.

DataFrame.to_html([buf, columns, col_space, ...])

Render a DataFrame as an HTML table.

Styler.to_html([buf, table_uuid, ...])

Write Styler to a file, buffer or string in HTML-CSS format.

XML
read_xml(path_or_buffer, *[, xpath, ...])

Read XML document into a DataFrame object.

DataFrame.to_xml([path_or_buffer, index, ...])

Render a DataFrame to an XML document.

Latex
DataFrame.to_latex([buf, columns, header, ...])

Render object to a LaTeX tabular, longtable, or nested table.

Styler.to_latex([buf, column_format, ...])

Write Styler to a file, buffer or string in LaTeX format.

HDFStore: PyTables (HDF5)
read_hdf(path_or_buf[, key, mode, errors, ...])

Read from the store, close it if we opened it.

HDFStore.put(key, value[, format, index, ...])

Store object in HDFStore.

HDFStore.append(key, value[, format, axes, ...])

Append to Table in file.

HDFStore.get(key)

Retrieve pandas object stored in file.

HDFStore.select(key[, where, start, stop, ...])

Retrieve pandas object stored in file, optionally based on where criteria.

HDFStore.info()

Print detailed information on the store.

HDFStore.keys([include])

Return a list of keys corresponding to objects stored in HDFStore.

HDFStore.groups()

Return a list of all the top-level nodes.

HDFStore.walk([where])

Walk the pytables group hierarchy for pandas objects.

Warning

One can store a subclass of DataFrame or Series to HDF5, but the type of the subclass is lost upon 
storing.

Feather
read_feather(path[, columns, use_threads, ...])

Load a feather-format object from the file path.

DataFrame.to_feather(path, **kwargs)

Write a DataFrame to the binary Feather format.

Parquet
read_parquet(path[, engine, columns, ...])

Load a parquet object from the file path, returning a DataFrame.

DataFrame.to_parquet([path, engine, ...])

Write a DataFrame to the binary parquet format.

Iceberg
read_iceberg(table_identifier[, ...])

Read an Apache Iceberg table into a pandas DataFrame.

DataFrame.to_iceberg(table_identifier[, ...])

Write a DataFrame to an Apache Iceberg table.

Warning

read_iceberg is experimental and may change without warning.

ORC
read_orc(path[, columns, dtype_backend, ...])

Load an ORC object from the file path, returning a DataFrame.

DataFrame.to_orc([path, engine, index, ...])

Write a DataFrame to the Optimized Row Columnar (ORC) format.

SAS
read_sas(filepath_or_buffer, *[, format, ...])

Read SAS files stored as either XPORT or SAS7BDAT format files.

SPSS
read_spss(path[, usecols, ...])

Load an SPSS file from the file path, returning a DataFrame.

SQL
read_sql_table(table_name, con[, schema, ...])

Read SQL database table into a DataFrame.

read_sql_query(sql, con[, index_col, ...])

Read SQL query into a DataFrame.

read_sql(sql, con[, index_col, ...])

Read SQL query or database table into a DataFrame.

DataFrame.to_sql(name, con, *[, schema, ...])

Write records stored in a DataFrame to a SQL database.

STATA
read_stata(filepath_or_buffer, *[, ...])

Read Stata file into DataFrame.

DataFrame.to_stata(path, *[, convert_dates, ...])

Export DataFrame object to Stata dta format.

StataReader.data_label

Return data label of Stata file.

StataReader.value_labels()

Return a nested dict associating each variable name to its value and label.

StataReader.variable_labels()

Return a dict associating each variable name with corresponding label.

StataWriter.write_file()

Export DataFrame object to Stata dta format.


