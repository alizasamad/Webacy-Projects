# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.cluster.hierarchy as sch
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import fcluster

# Load dataset
data = pd.read_excel('/Users/alizasamad/downloads/Externships/Webacy/compiled_risk_data.xlsx', sheet_name = 'Data')
print(data.head())

# Feature selection
print(data.columns)
data_new = data.copy()
feature_1 = 'encode_packed_collision'
feature_2 = 'is_airdrop_scam'
feature_3 = 'is_fake_token'
#feature_4 = ''
#feature_5 = ''

selected_features = data_new[[feature_1, feature_2, feature_3]]

print("Features selected for clustering")
print(selected_features.head())

# Compute Jaccard Distance
distance_matrix = pdist(selected_features, 'jaccard')
distance_square_matrix = squareform(distance_matrix)
print(distance_square_matrix)

# Create linkage matrix
linkage_matrix = sch.linkage(distance_matrix, method = 'ward')
print(linkage_matrix)

# Plot the Dendrogram
plt.figure(figsize =(12,8))
dendrogram = sch.dendrogram(linkage_matrix)

plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Data points')
plt.ylabel('Jaccard distance')

leaves = dendrogram['leaves']
num_leaves = len(leaves)
step_size = max(1,num_leaves // 10)

plt.xticks(ticks=np.arange(0, num_leaves, step_size),
           labels=np.arange(0, num_leaves, step_size),
           rotation=90)

# Visualizing Clusters
cluster_labels = fcluster(linkage_matrix, t=8, criterion='distance')
data_new['cluster']=cluster_labels
cluster_summary=data_new[[feature_1, feature_2, feature_3, 'cluster']].groupby('cluster').agg(['mean','std','median','count'])
pd.set_option('display.max_columns', None)
print(cluster_summary)

# Bar Graph
plt.figure(figsize=(8,6))
plt.hist(cluster_labels, bins=np.arange(1,np.max(cluster_labels)+2)-0.5, rwidth=0.8, color='blue', alpha=0.7)
plt.title('Histogram of Cluster Sizes')
plt.xlabel('Cluster')
plt.ylabel('Number of Points')
plt.xticks(np.arange(1,np.max(cluster_labels)+1))

# Heatmap of Centroids
cluster_centers = data_new[[feature_1, feature_2, feature_3, 'cluster']].groupby('cluster').mean()
plt.figure(figsize=(12,8))
sns.heatmap(cluster_centers, annot=True, cmap='coolwarm')
plt.title('Heatmap of Cluster Centroids')

plt.tight_layout()
plt.show()
