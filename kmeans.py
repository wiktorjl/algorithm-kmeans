import math
import matplotlib.pyplot as plt
import numpy as np
import random
from collections import defaultdict


def plot_clusters(clusters):
    for c in clusters.keys():
        plt.scatter([x[0] for x in clusters[c]], [x[1] for x in clusters[c]], color=np.random.rand(3, 1))
    plt.axis('equal')
    plt.show()


def read_data(filename):
    output = []
    with open(filename) as f:
        for line in f:
            output.append(tuple([float(s) for s in line.strip().split(" ")]))

    return output


def get_distance(a, b):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


def assign_labels(centroids, data):
    clusters = defaultdict(list)
    for d in data:
        p = None
        for c in centroids:
            if p is None:
                p = c
            else:
                if get_distance(d, c) < get_distance(d, p):
                    p = c
        clusters[p].append(d)
    return clusters


def recalcuate_centroids(clusters):
    for cluster_key in clusters.keys():
        new_key = (math.fsum([x[0] for x in clusters[cluster_key]]) / len(clusters[cluster_key]), math.fsum([x[1] for x in clusters[cluster_key]]) / len(clusters[cluster_key]))
        clusters[new_key] = clusters[cluster_key]
        if not cluster_key == new_key:
            del clusters[cluster_key]


def kmeans():
    data = read_data("data/geo_trimmed.dat")
    clusters = {key: [] for key in random.sample(data, 10)}
    old_centroids = []

    while not set(old_centroids) == set(clusters.keys()):
        clusters = assign_labels(clusters.keys(), data)
        old_centroids = list(clusters.keys())
        recalcuate_centroids(clusters)

    plot_clusters(clusters)


if __name__ == "__main__":
    kmeans()