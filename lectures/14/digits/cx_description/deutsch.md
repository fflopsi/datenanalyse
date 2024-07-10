# Unbeaufsichtige Erkennung von handgeschriebenen Ziffern

Dieses Python-Skript demonstriert den Einsatz von Clustering- und Dimensionsreduktionstechniken auf den MNIST-Zifferndatensatz (Handgeschriebene Ziffern).

Zuerst importiert es den MNIST-Zifferndatensatz, indem es die Funktion `load_digits` aus dem `sklearn.datasets` Modul verwendet. Diese Funktion gibt das Dataset als zwei separate Arrays zurück - die Daten und die entsprechenden Labels.

Die Daten bestehen aus handgeschriebenen Ziffern, die als 8x8 Bilder dargestellt werden, und sind daher 64-dimensional. Solch hochdimensionale Daten können jedoch schwer zu analysieren sein, daher wird die Dimensionsreduktionstechnik PCA (Principal Component Analysis) angewendet, um die Dimensionalität der Daten auf zwei zu reduzieren. Vor der Anwendung von PCA werden die Daten normalisiert, was bedeutet, dass sie so skaliert werden, dass sie einen Durchschnittswert von 0 und eine Standardabweichung von 1 haben.

Danach wird das KMeans-Clustering auf den reduzierten Daten angewendet. KMeans ist ein Algorithmus, der die Daten in `k` Gruppen oder "Cluster" einteilt, wobei `k` im Voraus festgelegt wird. In diesem Fall entspricht `k` der Anzahl der eindeutigen Labels im Datensatz (also die Zahlen 0-9, also 10 Cluster). Die initiale Platzierung der Zentroide wird mit der Methode "k-means++" festgelegt, und der Algorithmus wird viermal ausgeführt (Parameter `n_init=4`), jedes Mal mit einer anderen Zufallsinitialisierung.

Schliesslich ruft das Skript zwei Funktionen auf, um die Ergebnisse des KMeans-Clustering und die reduzierten Daten darzustellen, aber diese Beschreibung konzentriert sich nicht auf diese Teile des Codes.