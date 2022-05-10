# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-ra00T7e2pOSCAJlKbdmXmhxkZ3SELed
"""

import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors as mcolors
from sklearn.preprocessing import StandardScaler
from yellowbrick.cluster import KElbowVisualizer

df_perf_test=pd.read_csv('train.csv')
data = df_perf_test.drop('flag',axis = 1)
data.head()

data.shape

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)
pd.DataFrame(data_scaled).describe()

"""ELBOW"""

model = KMeans()
visualizer = KElbowVisualizer(model, k=(1,10)).fit(data)
visualizer.show()

"""KMEANS"""

clusters = 3
kmeans = KMeans(n_clusters = clusters)
kmeans.fit(data_scaled)
print(kmeans.labels_)

df_perf_test['Kmeans_Cluster']=kmeans.labels_
df_perf_test.head()

df_perf_test.to_csv("cluster_train.csv",index=False)

"""VISUALIZATION"""

pca = PCA(n_components=3)
pca.fit(data_scaled)
pca_data = pd.DataFrame(pca.transform(data_scaled))
pca_data.head()
print('Explained variation per principal component: {}'.format(pca.explained_variance_ratio_))
print('Cumulative variance explained by 3 principal components: {:.2%}'.format(np.sum(pca.explained_variance_ratio_)))

pca_2 = PCA(n_components=2)
pca_2_result = pca_2.fit_transform(data_scaled)
print('Explained variation per principal component: {}'.format(pca_2.explained_variance_ratio_))

print('Cumulative variance explained by 2 principal components: {:.2%}'.format(np.sum(pca_2.explained_variance_ratio_)))

pd.DataFrame(pca_data).describe()

''' Generating different colors in ascending order
								of their hsv values '''
colors = list(zip(*sorted((
					tuple(mcolors.rgb_to_hsv(
						mcolors.to_rgba(color)[:3])), name)
					for name, color in dict(
							mcolors.BASE_COLORS, **mcolors.CSS4_COLORS
													).items())))[1]


# number of steps to taken generate n(clusters) colors
skips = math.floor(len(colors[5 : -5])/clusters)
cluster_colors = colors[5 : -5 : skips]

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(pca_data[0], pca_data[1], pca_data[2],
		c = list(map(lambda label : cluster_colors[label],
											kmeans.labels_)))

str_labels = list(map(lambda label:'% s' % label, kmeans.labels_))

list(map(lambda data1, data2, data3, str_label:'', pca_data[0], pca_data[1],
		pca_data[2], str_labels))

plt.show()

# generating correlation heatmap
sns.heatmap(data.corr(), annot = True)
 
# posting correlation heatmap to output console
plt.show()