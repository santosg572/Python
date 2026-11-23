import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
species = iris.pop("species")
sns.clustermap(iris)

plt.show()
