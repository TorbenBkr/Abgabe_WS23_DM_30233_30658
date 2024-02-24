import pandas as pd
import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.cluster.hierarchy import dendrogram, linkage

# CSV-Datei einlesen
data = pd.read_csv('./output.csv')

# Convert data to numeric values
data = data.apply(pd.to_numeric, errors='coerce')

# Multivariate Datenmatrix erstellen
matrix = data.values
#print(matrix)

# Distanzmatrix erstellen
matrix_filled = matrix.copy()
dist_matrix = pd.DataFrame(distance_matrix(matrix_filled, matrix_filled))
#print(dist_matrix)

# Untersuchung von Varianzen
variances = np.var(matrix, axis=0)
#print(variances)

# Distanzmatrix auf Basis der skalierten Daten
matrix_scaled = matrix.copy()
matrix_scaled = (matrix_scaled - np.mean(matrix_scaled, axis=0)) / np.std(matrix_scaled, axis=0)
dist_matrix_scaled = pd.DataFrame(distance_matrix(matrix_scaled, matrix_scaled))
#print(dist_matrix_scaled)

# Aufteilung in Cluster
kmeans = KMeans(n_clusters=3, random_state=0).fit(matrix)
clusters = kmeans.labels_
#print(clusters)

'''
# Define the variables
df_2cluster = pd.DataFrame()
df_3cluster = pd.DataFrame()
df_4cluster = pd.DataFrame()
df_5cluster = pd.DataFrame()


# Assign objects to clusters based on a given number of clusters
df_2cluster["single"] = pd.cut(pd.Series(D[:, 2]), bins=2, labels=False)
df_3cluster["single"] = pd.cut(pd.Series(D[:, 2]), bins=3, labels=False)
df_4cluster["single"] = pd.cut(pd.Series(D[:, 2]), bins=4, labels=False)
df_5cluster["single"] = pd.cut(pd.Series(D[:, 2]), bins=5, labels=False)
'''