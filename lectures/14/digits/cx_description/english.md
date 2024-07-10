# Unsupervised recognition of handwritten digits

This Python script demonstrates the use of clustering and dimensionality reduction techniques on the MNIST digit dataset (Handwritten digits).

First, it imports the MNIST digit dataset by using the `load_digits` function from the `sklearn.datasets` module. This function returns the dataset as two separate arrays - the data and the corresponding labels.

The data consists of handwritten digits represented as 8x8 images, and are therefore 64-dimensional. However, such high-dimensional data can be difficult to analyze, hence the dimensionality reduction technique PCA (Principal Component Analysis) is applied to reduce the dimensionality of the data to two. Before applying PCA, the data is normalized, meaning that it is scaled such that it has a mean value of 0 and a standard deviation of 1.

Afterwards, KMeans clustering is applied on the reduced data. KMeans is an algorithm that divides the data into `k` groups or "clusters", with `k` determined in advance. In this case, `k` corresponds to the number of unique labels in the dataset (i.e., the numbers 0-9, so 10 clusters). The initial placement of centroids is determined using the "k-means++" method, and the algorithm is run four times (parameter `n_init=4`), each time with a different random initialization.

Finally, the script calls two functions for plotting the results of the KMeans clustering and the data after PCA.