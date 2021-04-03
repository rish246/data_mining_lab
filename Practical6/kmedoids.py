import pandas as pd 
import numpy as np 
import random
import matplotlib.pyplot as plt


iris_dataset = pd.read_csv('iris.data', header=None)
iris_dataset.pop(4)


# get initial KMediods 
K = 3
max_iter = 1000

initial_medoids_indices = {random.choice(range(0, 150)) for _ in range(K)}

initial_medoids = [iris_dataset.loc[idx] for idx in initial_medoids_indices]


non_mediods_data = []

for i in range(150):
    if i not in initial_medoids_indices:
        non_mediods_data.append(iris_dataset.loc[i])


def swap(medoids, non_medoids, med_idx, non_med_idx):
    temp = non_medoids[non_med_idx]
    non_medoids[non_med_idx] = medoids[med_idx]
    medoids[med_idx] = temp


def compute_cost(medoids, non_medoids):
    clusters = [[] for _ in range(len(medoids))]
    cost = 0

    for non_med in non_medoids:
        dists = [np.linalg.norm(non_med - medoid) for medoid in medoids]
        min_dist_idx = dists.index(min(dists))

        cost += dists[min_dist_idx]
        clusters[min_dist_idx].append(non_med)

    return cost, clusters




init_cost, init_clusters = compute_cost(initial_medoids, non_mediods_data)

i_iters = 0

while True:
    i_iters += 1
    # print(f'Non Medoids = {non_mediods_data}')
    med_copy = initial_medoids.copy()
    non_med_copy = non_mediods_data.copy()

    med_swap_idx = random.randint(0, K-1)
    print(med_swap_idx)
    non_med_swap_idx = random.randint(0, len(non_med_copy) - 1)
    print(non_med_swap_idx)
    swap(initial_medoids, non_mediods_data, med_swap_idx, non_med_swap_idx)

    new_cost, new_clusters = compute_cost(initial_medoids, non_mediods_data)

    if(new_cost > init_cost):
        initial_medoids = med_copy
        non_mediods_data = non_med_copy
        break

    init_clusters = new_clusters
    init_cost = new_cost


colors = ["r", "g", "b"]



######### mark the centroids
for i in range(len(initial_medoids)):
    plt.scatter(initial_medoids[i][2], initial_medoids[i][3], color= "k", marker="o")


i = 0
for cluster in init_clusters:

    color_for_this_cluster = colors[i]
    
    i += 1

    for point in cluster:

        plt.scatter(point[2], point[3], color = color_for_this_cluster, marker="x")



print(f'Number of iterations = {i_iters}')

plt.title("K-Medoids on iris dataset")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show()