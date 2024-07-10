import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

data = pd.read_csv('titanic.csv')
y = data['Survived']
X = data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']]

# Define preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('num', SimpleImputer(strategy='median'), ['Age', 'SibSp', 'Parch']),
        ('cat', Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
            ('onehot', OneHotEncoder())]), ['Sex', 'Pclass'])])

# Preprocess the data
X_processed = preprocessor.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)
dt = DecisionTreeClassifier()
prams = {"max_depth" : range(2, 10)}
grid = GridSearchCV(dt, param_grid=prams, cv=5)
grid.fit(X_train, y_train)

# Get feature names
feature_names = ['Age', 'SibSp', 'Parch'] + list(preprocessor.transformers_[1][1]['onehot'].get_feature_names_out(['Sex', 'Pclass']))

print(f"Accuracy on test data: {accuracy_score(y_test, grid.predict(X_test)):.2f}")

# Plot the tree
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=300)
plot_tree(grid.best_estimator_, feature_names = feature_names, class_names=True, filled = True)
plt.savefig("titanic.pdf")

# Predict for Jack and Rose
jack = pd.DataFrame([{'Pclass': 3, 'Sex': 'male', 'Age': 20, 'SibSp': 0, 'Parch': 0}])
rose = pd.DataFrame([{'Pclass': 1, 'Sex': 'female', 'Age': 17, 'SibSp': 0, 'Parch': 2}])

jack_survival = grid.predict(preprocessor.transform(jack))
rose_survival = grid.predict(preprocessor.transform(rose))

print(f"Did Jack survive? {'Yes' if jack_survival else 'No'}")
print(f"Did Rose survive? {'Yes' if rose_survival else 'No'}")
