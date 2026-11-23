import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

N = 6
df = pd.DataFrame(np.random.random((N, N)))
sns.clustermap(data=df, linewidths=5, figsize=(3, 3))

plt.show()
