Pandas
======

Pandas es una biblioteca de código abierto para el lenguaje de programación Python, diseñada específicamente para la manipulación y el análisis de datos.

Funciona de manera similar a una hoja de cálculo (como Microsoft Excel) o una tabla de una base de datos relacional (como SQL), pero con mucha mayor velocidad, flexibilidad y 
capacidad para automatizar procesos.

**Estructuras de datos principales**

Pandas introduce dos estructuras fundamentales construidas por encima de la biblioteca NumPy:

• Serie (Series): Es una matriz unidimensional etiquetada capaz de almacenar cualquier tipo de dato (números, texto, booleanos) con un índice asociado.
• DataFrame: Es la estructura estrella de Pandas. Representa una tabla de datos bidimensional con filas y columnas etiquetadas, ideal para trabajar con datos estructurados.


**¿Para qué sirve?**

• Cargar y exportar datos: Permite leer y guardar información desde y hacia múltiples formatos de archivo, como CSV, Excel (.xlsx), JSON, bases de datos SQL y más.
• Limpieza de datos (Data Cleaning): Facilita la detección, corrección o eliminación de valores nulos, duplicados o datos incompletos.
• Transformación y filtrado: Permite ordenar, agrupar (groupby), combinar, pivotar y filtrar grandes cantidades de filas y columnas con pocas líneas de código.
• Análisis estadístico y series temporales: Incluye funciones rápidas para calcular medias, medianas, correlaciones y trabajar con marcas de tiempo y fechas.

Es una de las herramientas indispensables dentro del ecosistema de la ciencia de datos en Python, usándose habitualmente junto a **Matplotlib** (para gráficos) y 
**Scikit-learn** (para 
aprendizaje automático o machine learning).

**Serie Pandas**


Una Serie de Pandas es una matriz unidimensional etiquetada capaz de almacenar datos de cualquier tipo. Se puede crear a partir de listas de Python, matrices NumPy, 
diccionarios, valores escalares o datos cargados desde fuentes externas como archivos CSV, archivos de Excel y bases de datos. Las etiquetas asociadas a una Serie se denominan 
su índice.

**Ejemplos**

1)

.. code:: Python

   import pandas as pd
   import numpy as np

   data = np.array(['g', 'e', 'e', 'k', 's'])
   s = pd.Series(data)
   print("Pandas Series:")
   print(s)

2)

.. code:: Python

   s = pd.Series([1, 3, 5, np.nan, 6, 8])


**DataFrame de Pandas**

Un DataFrame de Pandas es una estructura de datos bidimensional con ejes etiquetados (filas y columnas). Se crea cargando conjuntos de datos desde un almacenamiento existente, 
que puede ser una base de datos SQL, un archivo CSV o un archivo de Excel. Puede crearse a partir de listas, diccionarios, listas de diccionarios, etc.

**Ejemplo**

1)

.. code:: Python

   import pandas as pd 
   
   df = pd.DataFrame() 
   print(df)
   lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks'] 
  
   df = pd.DataFrame(lst) 
   print(df)

2)

.. code:: Python

   dates = pd.date_range("20130101", periods=6)
   df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

4)

.. code:: Python

   df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
   )

   df2.dtypes

**Viewing data**

.. code:: Python

   df.head()

   df.tail(3)

   df.index

   df.columns

   df.to_numpy()

   df.describe()

   df.T

   df.sort_values(by="B")

**Selección**

.. code:: Python

   df["A"]

   df.A

   df[["B", "A"]]

   df[0:3]

   df["20130102":"20130104"]

**Selección por etiqueta**

.. code:: Python

   df.loc[dates[0]]

   df.loc[:, ["A", "B"]]

   df.loc["20130102":"20130104", ["A", "B"]]

   df.loc[dates[0], "A"]

   df.at[dates[0], "A"]

**Selección por su posición**

.. code:: Python

   df.iloc[3]

   df.iloc[3:5, 0:2]

   df.iloc[[1, 2, 4], [0, 2]]

   df.iloc[1:3, :]

   df.iloc[:, 1:3]

   df.iloc[1, 1]

   df.iat[1, 1]

**Por indices Booleanos**

.. code:: Python

   df[df["A"] > 0]

   df[df > 0]

   df2 = df.copy()

   df2["E"] = ["one", "one", "two", "three", "four", "three"]

   df2[df2["E"].isin(["two", "four"])]

**Operaciones**

.. code:: Python

   df.mean()

   df.mean(axis=1)

    

**Operaciones en Pandas**

1. Carga de datos : Esta operación lee datos de archivos como CSV, Excel o JSON y los carga en un DataFrame.

.. code:: Python

   import pandas as pd

   df = pd.read_csv("data.csv")
   print(df.head())

2. Visualización y exploración de datos

.. code:: Python

   df.info()

3. Manejo de datos faltantes : Los conjuntos de datos a menudo contienen valores vacíos o faltantes . Pandas proporciona funciones para detectar, eliminar o reemplazar estos 
valores.

.. code:: Python

   print(df.isnull().sum())
   df = df.fillna(0)

**4. Selección y filtrado de datos :** Esta operación recupera columnas, filas o registros específicos que cumplen una condición. Permite la extracción precisa de la información 
requerida.

.. code:: Python

   ages = df[df['age'] > 25]
   print(ages)

**5. Agregar y eliminar columnas :** Puede crear nuevas columnas a partir de las existentes o eliminar las columnas no deseadas del DataFrame.

.. code:: Python
   
   df['total'] = df['a'] + df['b']
   print(df.head())

**6. Agrupación de datos (GroupBy) :** La agrupación permite organizar los datos en categorías y calcular valores para cada grupo, por ejemplo, sumas, recuentos o promedios.

.. code:: Python

   res = df.groupby('category')['sales'].sum()
   print(res)


