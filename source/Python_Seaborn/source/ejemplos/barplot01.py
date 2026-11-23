import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')

sns.barplot(df, x="island", y="body_mass_g")

plt.show()
