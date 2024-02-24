import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Load the data
output = pd.read_csv("output.csv")

# Select 150 random samples from the data
quanti_small = output.sample(n=100, random_state=7)[["Category 1", "Category 2"]]

# Create the distance matrix
D = linkage(quanti_small, method='single')

# Plot the dendrogram
plt.figure(figsize=(15, 5))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(D, leaf_rotation=90., leaf_font_size=8., labels=quanti_small.index)

# Screeplot of distances vs fusion distance
plt.figure(figsize=(15, 5))
plt.plot(D[:, 2])
plt.title("Screeplot of distances vs fusion distance")
plt.xlabel("Fusion distance")
plt.ylabel("Distance")
plt.show()









