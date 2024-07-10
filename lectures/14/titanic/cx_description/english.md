# Predicting survival in the Titanic with decision trees

This Python script implements a decision tree classifier on the Titanic dataset.

First, it reads the preprocessed dataset from a CSV file named 'titanic.csv' using the pandas function `pd.read_csv`.

Then it separates the target variable (in this case 'Survived', i.e., whether the passenger survived or not) from the features. The features (i.e., the input variables for the model) are stored in the variable `X`, while the target variable is stored in `y`.

The dataset contains categorical variables such as 'Sex', 'Embarked', and 'Pclass'. Categorical variables often need to be encoded before they can be input into a model, as models usually require numeric inputs. In this script, a method called one-hot encoding is used to encode the categorical variables.

Afterwards, the dataset is split into two parts: a training set and a test set. The training set is used to train the model, and the test set is used to test the model's accuracy. The parameter `test_size=0.2` determines that 20% of the data is reserved for the test set, while the remainder is used for the training set.

A decision tree classifier is trained by applying the `fit` method to the training set. Finally, the accuracy of the model on the test set is calculated and outputted.