# Entscheidungsbaum auf dem Titanic-Datensatz mit Python"

Dieses Python-Skript implementiert einen Entscheidungsbaum-Klassifikator auf dem Titanic-Datensatz. 

Zuerst liest es den vorverarbeiteten Datensatz aus einer CSV-Datei mit dem Namen 'titanic.csv' mit der Pandas-Funktion `pd.read_csv`. 

Dann separiert es die Zielvariable (in diesem Fall 'Survived', d.h. ob der Passagier überlebt hat oder nicht) von den Merkmalen. Die Merkmale (d.h. die Eingabevariablen für das Modell) werden in der Variable `X` gespeichert, während die Zielvariable in `y` gespeichert wird. 

Der Datensatz enthält kategorische Variablen, wie 'Sex', 'Embarked' und 'Pclass'. Kategorische Variablen müssen oft codiert werden, bevor sie in ein Modell eingegeben werden können, da Modelle in der Regel numerische Eingaben benötigen. In diesem Skript wird eine Methode namens One-Hot-Encoding verwendet, um die kategorischen Variablen zu codieren. 

Danach wird der Datensatz in zwei Teile geteilt: einen Trainingssatz und einen Testsatz. Der Trainingssatz wird verwendet, um das Modell zu trainieren, und der Testsatz wird verwendet, um die Genauigkeit des Modells zu testen. Der Parameter `test_size=0.2` bestimmt, dass 20% der Daten für den Testsatz reserviert werden, während der Rest für den Trainingssatz verwendet wird. 

Ein Entscheidungsbaum-Klassifikator wird trainiert, indem die Methode `fit` auf den Trainingssatz angewendet wird. Schließlich wird die Genauigkeit des Modells auf dem Testsatz berechnet und ausgegeben. 
