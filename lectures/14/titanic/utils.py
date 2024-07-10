import numpy as np
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm


def plot_k_means_solution(kmeans, reduced_data):
    h = 0.02  # point in the mesh [x_min, x_max]x[y_min, y_max].

    # Plot the decision boundary. For that, we will assign a color to each
    x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
    y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # Obtain labels for each point in mesh. Use last trained model.
    Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Put the result into a color plot
    plt.figure(1)
    plt.clf()
    plt.imshow(
        Z,
        interpolation="nearest",
        extent=(xx.min(), xx.max(), yy.min(), yy.max()),
        cmap=plt.cm.Paired,
        aspect="auto",
        origin="lower",
    )
    # Plot the centroids as a white X
    plt.plot(reduced_data[:, 0], reduced_data[:, 1], "k.", markersize=2)
    centroids = kmeans.cluster_centers_
    plt.scatter(
        centroids[:, 0],
        centroids[:, 1],
        marker="x",
        s=169,
        linewidths=3,
        color="w",
        zorder=10,
    )
    plt.title(
        "K-means clustering on the digit images (after PCA)\n"
        "Centroids are marked with white cross"
    )
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())
    plt.savefig(f"./cx_out/clustered_digits.png", bbox_inches="tight")


def plot_digits(reduced_data, labels):
    plt.figure()
    x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
    y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
    reduced_data_dig = np.concatenate((reduced_data, np.array([labels]).T), axis=1)
    color_map = iter(cm.rainbow(np.linspace(0, 1, 9)))
    for dig_label in range(9):
        data_dig_filt = reduced_data_dig[reduced_data_dig[:, -1] == dig_label]
        plt.plot(data_dig_filt[:, 0], data_dig_filt[:, 1], ".", markersize=2, color=next(color_map))

    plt.title("Digit images (after PCA).\n The color indicates the digit in the image.")
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())
    plt.savefig(f"./cx_out/digits.png", bbox_inches="tight")