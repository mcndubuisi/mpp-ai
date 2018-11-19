%matplotlib inline
# K-Means Clustering
# import dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# generate random data in a two dimensional space
X= -2 * np.random.rand(100,2)
X1 = 1 + 2 * np.random.rand(50,2)

# divide data into two groups
X[50:100, :] = X1


Kmean = KMeans(n_clusters=2)
Kmean.fit(X)

# find center of the clusters
Kmean.cluster_centers_

plt.scatter(X[ : , 0], X[ : , 1], s =50, c='b')

# display clusters' centroids
plt.scatter(-0.94665068, -0.97138368, s=100, c='g')
plt.scatter(2.01559419, 2.02597093, s=100, c='r')
plt.show()

# return labels property
Kmean.labels_


sample_test = np.array([2,4])
second_test = sample_test.reshape(1, -1)
Kmean.predict(second_test)
