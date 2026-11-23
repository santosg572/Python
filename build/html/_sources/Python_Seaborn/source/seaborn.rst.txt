Seaborn
========

Seaborn es una biblioteca de Python para crear visualizaciones estadísticas. Ofrece estilos predeterminados depurados y 
paletas de colores, lo que hace que los gráficos resulten más atractivos y fáciles de leer. Al estar construida sobre 
Matplotlib e integrada con las estructuras de datos de pandas, Seaborn hace que la visualización de datos sea más sencilla 
y coherente.


* Seaborn destaca la visualización como una parte esencial del análisis de datos.

* Sus API orientadas a conjuntos de datos permiten alternar entre distintos tipos de gráficos para las mismas variables.

* Ayuda a comprender patrones, tendencias y relaciones dentro de los datos.


**Ejemplos**

**1. Lineplot**

El gráfico de líneas se utiliza para mostrar la relación entre dos variables continuas. Se emplea habitualmente para series 
temporales o datos ordenados.

.. code:: Python

   import seaborn as sns
   import matplotlib.pyplot as plt

   fmri = sns.load_dataset("fmri")
   sns.lineplot(x="timepoint", y="signal", hue="region", data=fmri)
   plt.show()

**2. Scatterplot**

El diagrama de dispersión se utiliza para mostrar la relación entre dos variables numéricas. Ayuda a identificar patrones o 
correlaciones.

**Ejemplo:** Relación entre el importe total de la cuenta y la propina

.. code:: Python

   import seaborn as sns
   import matplotlib.pyplot as plt

   tips = sns.load_dataset("tips")

   sns.scatterplot(x="total_bill", y="tip", hue="day", data=tips)
   plt.show()

**3. Barplot**

El gráfico de barras se utiliza para comparar valores numéricos entre categorías. Muestra el valor promedio junto con 
intervalos de confianza.

**Ejemplo**: Factura total promedio por día

.. code:: Python

   import seaborn as sns
   import matplotlib.pyplot as plt

   tips = sns.load_dataset("tips")

   sns.barplot(x="day", y="total_bill", data=tips)
   plt.show()

**4. Boxplot**

El diagrama de caja se utiliza para mostrar la distribución de los datos a partir de los cuartiles. Ayuda a identificar la 
dispersión y los valores atípicos.


**Ejemplo**: Distribución del importe total por día

.. code:: Python

   import seaborn as sns
   import matplotlib.pyplot as plt

   tips = sns.load_dataset("tips")

   sns.boxplot(x="day", y="total_bill", data=tips)
   plt.show()


**5. Histplot**

Histplot se utiliza para visualizar la distribución de una única variable numérica.

**Ejemplo**: Distribución del importe total de la factura


.. code:: Python

   import seaborn as sns
   import matplotlib.pyplot as plt

   tips = sns.load_dataset("tips")

   sns.histplot(tips["total_bill"], kde=True)
   plt.show()

**6. Heatmap**

Un mapa de calor se utiliza para visualizar datos con estructura matricial mediante el uso de colores. Se emplea 
habitualmente para matrices de correlación.


**Ejemplo**: Mapa de calor de correlación

.. code:: Python

   import seaborn as sns
   import matplotlib.pyplot as plt

   tips = sns.load_dataset("tips")
   corr = tips.corr(numeric_only=True)

   sns.heatmap(corr, annot=True, cmap="coolwarm")
   plt.show()


**7. Pairplot**

Pairplot se utiliza para representar las relaciones por pares entre múltiples variables numéricas.

**Ejemplo**: Relaciones por pares en el conjunto de datos

.. code:: Python

   import seaborn as sns
   import matplotlib.pyplot as plt

   iris = sns.load_dataset("iris")
   sns.pairplot(iris, hue="species")
   plt.show()










