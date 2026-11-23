import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')

sns.barplot(df, x="body_mass_g", y="island", hue="island", legend=False)

plt.show()
