import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer

data = pd.read_csv('titanic.csv')
y = data['Survived']
X = data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Cabin']]
#X = data.drop('Survived', axis=1)

# use one-hot encoding
encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=0)
dt = DecisionTreeClassifier()
prams = {"max_depth" : range(2, 10)}
grid = GridSearchCV(dt, param_grid=prams, cv=5)
grid.fit(X_train, y_train)

# Get feature names
feature_names = encoder.get_feature_names_out(X.columns)

print(f"Accuracy on test data: {accuracy_score(y_test, grid.predict(X_test)):.2f}")

# Plot the tree
fig, axes = plt.subplots(nrows = 1,ncols = 1, figsize = (4,4), dpi=300)
plot_tree(grid.best_estimator_, feature_names = feature_names, class_names=True, filled = True)
plt.savefig("titanic.pdf")
