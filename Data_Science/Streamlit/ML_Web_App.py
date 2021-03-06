# App based on tutorial from Python Engineer
# https://www.youtube.com/watch?v=Klqn--Mu2pE&list=TLPQMTQwMjIwMjHWayHe3_rfPg&index=5

import streamlit as st
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

#Classifiers to import
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.decomposition import PCA

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

st.title("Streamlit Machine Learning App")

st.write("""
## Explore different classifiers
Select a dataset and a classifier from the sidebar. Which classifier gives the best results?
""")

dataset_name = st.sidebar.selectbox("Select Dataset", ("Iris", "Breast Cancer", "Digits"))
classifier_name = st.sidebar.selectbox("Select an ML Classifier", ("KNN", "SVC RBF", "Random Forest Classifier", "Logistic Regression", "Decision Tree", "Naive Bayes", "K-Means Clustering", "Guassian Process Classifier"))

def get_dataset(dataset_name):
    if dataset_name == "Iris":
        data = datasets.load_iris()
    elif dataset_name == "Breast Cancer":
        data = datasets.load_breast_cancer()
    else:
        data = datasets.load_digits()
    X = data.data
    Y = data.target
    return X, Y

X, Y = get_dataset(dataset_name)
st.write(f"""
## **Selected dataset: *{dataset_name}* **""")
st.write(f"Shape of *{dataset_name}* dataset", X.shape)
st.write("Number of classes", len(np.unique(Y)))

def add_parameter_ui(clf_name):
    params = dict()
    if clf_name == "KNN":
        K = st.sidebar.slider("K", 1, 20,2)
        params["K"] = K
    elif clf_name == "SVC RBF":
        C = st.sidebar.slider("C", 0.01, 15.0, 7.0)
        gamma = st.sidebar.slider("gamma", 1, 20, 2)
        params["C"] = C
        params["gamma"] = gamma
    elif clf_name == "Logistic Regression":
        C = st.sidebar.slider("C", 0.01, 15.0, 7.0)
        max_iter = st.sidebar.slider("max_iter", 2, 1000, 10)
        params["C"] = C
        params["max_iter"] = max_iter
    elif clf_name == "Decision Tree":
        max_depth = st.sidebar.slider("max_depth", 2, 100, 10)
        params["max_depth"] = max_depth
    elif clf_name == "Naive Bayes":
        pass
    elif clf_name == "Guassian Process Classifier":
        pass
    elif clf_name == "K-Means Clustering": 
        max_iter = st.sidebar.slider("max_iter", 2, 1000, 10)
        n_clusters = st.sidebar.slider("n_clusters", 2, 100, 3)
        params["max_iter"] = max_iter
        params["n_clusters"] = n_clusters
    else:
        max_depth = st.sidebar.slider("max_depth", 2, 100, 10)
        n_estimators = st.sidebar.slider("n_estimators", 1, 1000, 100)
        params["max_depth"] = max_depth
        params["n_estimators"] = n_estimators
    return params

params = add_parameter_ui(classifier_name)

def get_classifier(clf_name, params):
    if clf_name =="KNN":
        clf = KNeighborsClassifier(n_neighbors=params["K"])
    elif clf_name == "SVC RBF":
        clf=SVC(C=params["C"],gamma = params["gamma"] )
    elif clf_name == "Logistic Regression":
        clf = LogisticRegression(C=params["C"], max_iter = params["max_iter"] )
    elif clf_name == "Decision Tree":
        clf = DecisionTreeClassifier(max_depth=params["max_depth"])
    elif clf_name == "Naive Bayes":
        clf = GaussianNB()
    elif clf_name == "Guassian Process Classifier":
        clf =GaussianProcessClassifier()

    elif clf_name == "K-Means Clustering": 
        clf = KMeans(max_iter= params["max_iter"], n_clusters=params["n_clusters"])
    else:
        clf = RandomForestClassifier(n_estimators=params["n_estimators"],
                        max_depth=params["max_depth"], random_state=1682)
    return clf

clf = get_classifier(classifier_name, params)

# Classification
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=1682)

clf.fit(X_train, Y_train)
Y_pred = clf.predict(X_test)

acc = accuracy_score(Y_test, Y_pred)
st.write(f"classifier = {classifier_name}")
st.write(f"accuracy = {acc}")
st.write("---")
st.write("**X Values**")
st.write(X)

#Plot
pca = PCA(2)
X_projected = pca.fit_transform(X)

x1 = X_projected[:,0]
x2 = X_projected[:,1]

st.write("---")
st.write("**Principle Component Analysis**")
fig = plt.figure()
plt.scatter(x1, x2, c=Y, alpha=0.8, cmap="jet")
plt.xlabel("Principle Component 1")
plt.ylabel("Principle Component 2")
plt.colorbar()
st.pyplot(fig)




