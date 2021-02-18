# App based on tutorial from Python Engineer
# https://www.youtube.com/watch?v=Klqn--Mu2pE&list=TLPQMTQwMjIwMjHWayHe3_rfPg&index=5

import streamlit as st
from sklearn import datasets
import numpy as np
import mathplotlib.pyplot as plt

#Classifiers to import
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.decomposition import PCA

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

st.title("Streamlit ML App")

st.write("""
# Explore different classifiers
Which one is the best?
""")

dataset_name = st.sidebar.selectbox("Select Dataset", ("Iris", "Breast Cancer", "Diabetes", "Boston Housing", "Digits"))
classifier_name = st.sidebar.selectbox("Select ML Algorithmn", ("KNN", "SVC RBF", "SVR", "Random Forest Regressor","Random Forest Classifier", "Logistic Regression", "Decision Tree", "Linear Regression", "Naive Bayes", "K-Means Clustering", "Guassian Process" ))

def get_dataset(dataset_name):
    if dataset_name == "Iris":
        data = datasets.load_iris()
    elif dataset_name == "Breast Cancer":
        data = datasets.load_breast_cancer()
    elif dataset_name == "Diabetes":
        data = datasets.load_diabetes()
    elif dataset_name == "Boston Housing":
        data = datasets.load_boston()
    else:
        data = datasets.load_digits()
    X = data.data
    Y = data.target
    return X, Y

X, Y = get_dataset(dataset_name)
st.write(f"""
# Selected dataset: *{dataset_name}*""")
st.write(f"Shape of *{dataset_name}* dataset", X.shape)
st.write("Number of classes", len(np.unique(Y)))

def add_parameter_ui(clf_name):
    params = dict()
    if clf_name == "KNN":
        K = st.sidebar.slider("K", 1, 15)
        params["K"] = K
    elif clf_name == "SVC RBF":
        C = st.sidebar.slider("C", 0.01, 10.0)
        gamma = st.sidebar.slider("gamma", 1, 10)
        params["C"] = C
        params["gamma"] = gamma
    elif clf_name == "Logistic Regression":
        C = st.sidebar.slider("C", 0.01, 10.0)
        max_iter = st.sidebar.slider("max_iter", 2, 200)
        params["C"] = C
        params["max_iter"] = max_iter
    elif clf_name == "Decision Tree":
        max_depth = st.sidebar.slider("max_depth", 2, 15)
        params["max_depth"] = max_depth
    elif clf_name == "Naive Bayes":
        pass
    elif clf_name == "Random Forest Classifier":
        max_depth = st.sidebar.slider("max_depth", 2, 15)
        n_estimators = st.sidebar.slider("n_estimators", 1, 100)
        params["max_depth"] = max_depth
        params["n_estimators"] = n_estimators
    elif clf_name == "Guassian Process":
        pass

    elif clf_name == "SVR":
        pass
    elif clf_name == "Linear Regression": 
        pass
    elif clf_name == "K-Means Clustering": 
        max_iter = st.sidebar.slider("max_iter", 2, 200)
        n_clusters = st.sidebar.slider("n_clusters", 2, 20)
        params["max_iter"] = max_iter
        params["n_clusters"] = n_clusters
    else:
        max_depth = st.sidebar.slider("max_depth", 2, 15)
        n_estimators = st.sidebar.slider("n_estimators", 1, 100)
        params["max_depth"] = max_depth
        params["n_estimators"] = n_estimators
    return params

params = add_parameter_ui(classifier_name)

def get_classifier(clf_name, params):
    if clf_name =="KNN":
        clf = KNeighborsClassifier(n_neighbors=params["K"])
    elif clf_name == "SVC":
        clf=SVC(C=params["C"])
    elif clf_name == "Random Forest Classifier":
        clf = RandomForestClassifier(n_estimators=params["n_estimators"],
                                    max_depth=params["max_depth"], random_state=1682)
    else:
        clf = RandomForestRegressor(n_estimators=params["n_estimators"],
                                    max_depth=params["max_depth"], random_state=1682)
    return clf

clf = get_classifier(classifier_name, params)

# Classification
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=1682)

clf.fit(X_train, Y_train)
y_pred = clf.predict(X_test)

acc = accuracy_score(Y_test, Y_pred)
st.write(f"classifier = {classifier_name}")
st.write("accuracy = {acc}")

#Plot
pca = PCA(2)
X_projected = pca.fit_transform(X)

x1 = X_projected[:,0]
x2 = X_projected[:,1]

fig = plt.figure()
plt.scatter(x1, x2, c=y, alpha=0.8, cmap="virdis")
plt.xlabel("Principle Component 1")
plt.ylabel("Principle Component 2")
plt.colorbar()

st.pyplot()

