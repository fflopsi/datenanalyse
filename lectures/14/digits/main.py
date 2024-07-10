import numpy as np
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from utils import plot_k_means_solution
from utils import plot_digits


if __name__ == "__main__":
    data, labels = load_digits(return_X_y=True)
    (n_samples, n_features), n_digits = data.shape, np.unique(labels).size

    reduced_data = PCA(n_components=2).fit_transform(StandardScaler().fit_transform(data))
    kmeans = KMeans(init="k-means++", n_clusters=n_digits, n_init=4)
    kmeans.fit(reduced_data)

    plot_k_means_solution(kmeans, reduced_data)
    plot_digits(reduced_data, labels)

    print("Done! See the output in the image files.")
