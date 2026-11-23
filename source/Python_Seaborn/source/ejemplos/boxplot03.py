import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')

sns.boxplot(data=df, x="class", y="age", hue="alive")

plt.show()
