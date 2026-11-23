import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')

sns.boxplot(data=df, x="class", y="age", hue="alive", fill=False, gap=.1)

plt.show()
