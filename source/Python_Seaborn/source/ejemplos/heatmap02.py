import seaborn as sns
import matplotlib.pyplot as plt

glue = sns.load_dataset("glue").pivot(index="Model", columns="Task", values="Score")
sns.heatmap(glue, annot=True, fmt=".1f")

plt.show()
