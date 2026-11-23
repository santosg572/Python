import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')

sns.lmplot(data=df, x="bill_length_mm", y="bill_depth_mm", hue="species")

plt.show()
