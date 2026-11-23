import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')

sns.boxplot(x=df["age"])

plt.show()
