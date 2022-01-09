# -*- coding: utf-8 -*-
"""BreastCancerPrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fspQMck8EhpICRg1ghikyikv5zXr5vhJ

Predicting Bening or Malignant Breast Cancer Using K-Means Algorithm
"""

import numpy as np
from sklearn import preprocessing, neighbors, svm
from sklearn.cluster import KMeans
from sklearn.model_selection import cross_validate, train_test_split
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

"""Loading the Wisconsin Breast Cancer Data"""

from google.colab import files
uploaded = files.upload()
df = pd.read_csv('breastCancer.csv')
df.replace('?', 0, inplace = True)

df.drop(['id'], axis = 1, inplace=True)
df.head()

"""Analysing The Data"""

df.describe()

df.info()

"""Visualizing Each Feature On Histogram"""

df.hist(figsize=(10,10))
plt.show()

"""Analysing the feature parameters of malignant cancer"""

df[df['class']==4].head(10)

df[df['class']==4].describe()

"""Applying K-Neighbors Algorithm on our dataset"""

X = np.array(df.drop(columns=['class']))
y = np.array(df['class'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy*100)

"""Testing The Data On New Data Points"""

example_measures = np.array([[10,2,1,7,1,10,3,2,1],[1,2,1,2,3,4,5,3,1]])
prediction = clf.predict(example_measures)
cancer_name = []
for cancer in prediction:
  if cancer == 2:
    cancer_name.append('bening(2)')
  else:
    cancer_name.append('malignant(4)')
print(cancer_name)

"""Applying K-Means Algorithm on our dataset"""

x = df.iloc[:, :].values
model = KMeans(n_clusters=2, init='k-means++', max_iter=250, n_init=15, random_state=0)
y = model.fit_predict(x)
print(y)

"""Visualizing The Cluster"""

kmns = KMeans(n_clusters=2, init='k-means++', n_init=10, max_iter=300, tol=0.0001, verbose=0, random_state=None, copy_x=True, algorithm='auto')
kY = kmns.fit_predict(x)

from sklearn.manifold import TSNE
tsne = TSNE(verbose=1, perplexity=40, n_iter= 4000)
Y = tsne.fit_transform(X)

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)

ax1.scatter(Y[:,0],Y[:,1],  c=kY, cmap = "jet", edgecolor = "None", alpha=0.35)
ax1.set_title('k-means clustering plot')

ax2.scatter(Y[:,0],Y[:,1],  c = df['class'], cmap = "jet", edgecolor = "None", alpha=0.35)
ax2.set_title('Actual clusters')



X = np.array(df.drop(columns=['class']))
y = np.array(df['class'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = KMeans(n_clusters=2, init='k-means++', max_iter=250, n_init=15, random_state=0)
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy*100)