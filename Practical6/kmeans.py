import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

iris_data_path = "./iris.data"

iris_dataset = pd.read_csv(iris_data_path, header=None)

iris_dataset.pop(4)

K = 3


iris_dataset = iris_dataset.sample(frac=1).reset_index(drop=True)

# lets generate k random indices and then apply this algo
k_random_indices = [random.randrange(0, 149) for _ in range(K)]
centroids = [iris_dataset.loc[i] for i in k_random_indices]

max_iterations = 1000
tol = 0.000001
clusters = [[] for _ in range(K)]


for i_iter in range(max_iterations):


    clusters = [[] for _ in range(K)]


    for i in range(iris_dataset.shape[0]):
        
        # find dists from all the centroids
        dists_from_centroid = [np.linalg.norm(iris_dataset.loc[i] - centroids[j]) for j in range(0, K)]

        # get the min dist from centroid
        min_dist_idx = dists_from_centroid.index(min(dists_from_centroid))

        clusters[min_dist_idx].append(iris_dataset.loc[i])

    prev_centroids = centroids

    centroids = [np.average(cluster, axis=0) for cluster in clusters]

    # if optimized, then break else go for another round
    is_optimized = True

    for i in range(K):
        original_centroid = prev_centroids[i]
        curr_centroid = centroids[i]

        diff = np.sum((curr_centroid - original_centroid) / original_centroid * 100.0)
        print(diff)
        if diff > tol:
            is_optimized = False

    if is_optimized:
        print(f'{i_iter} iterations to find the optimal solutions')
        break




colors = ["r", "g", "b"]



######### mark the centroids
for i in range(len(centroids)):
    plt.scatter(centroids[i][2], centroids[i][3], color= "k", marker="o")


i = 0
for cluster in clusters:

    color_for_this_cluster = colors[i]
    
    i += 1

    for point in cluster:

        plt.scatter(point[2], point[3], color = color_for_this_cluster, marker="x")


plt.title("K-Means on iris dataset")
plt.xlabel("Petal Width")
plt.xlabel("Petal Length")
plt.show()