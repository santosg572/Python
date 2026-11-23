import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(2)
data = np.random.rand(6, 6)

sns.clustermap(data)

plt.show()
