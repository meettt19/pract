import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler


iris = load_iris()
X = iris.data
y = iris.target


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


k = 3


clf = KNeighborsClassifier(n_neighbors=k)
clf.fit(X_train, y_train)


y_pred = clf.predict(X_test)


classification_accuracy = accuracy_score(y_test, y_pred)

print("Classification Accuracy:", classification_accuracy)
