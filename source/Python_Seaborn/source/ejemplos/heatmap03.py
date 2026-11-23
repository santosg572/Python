import seaborn as sns
import matplotlib.pyplot as plt

glue = sns.load_dataset("glue").pivot(index="Model", columns="Task", values="Score")
sns.heatmap(glue, cmap=sns.cubehelix_palette(as_cmap=True))

plt.show()
