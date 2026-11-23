import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')

sns.pairplot(df, kind="kde")

plt.show()
