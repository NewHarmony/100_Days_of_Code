# App based on tutorial from Python Engineer
# https://www.youtube.com/watch?v=Klqn--Mu2pE&list=TLPQMTQwMjIwMjHWayHe3_rfPg&index=5

import streamlit as st
from sklearn import datasets
import numpy as np

#Models to import
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



st.title("Streamlit ML App")

st.write("""
# Explore different classifiers
Which one is the best?
""")

dataset_name = st.sidebar.selectbox("Select Dataset", ("Iris", "Breast Cancer", "Diabetes", "Boston Housing", "Digits"))
classifier_name = st.sidebar.selectbox("Select Classifier", ("KNN", "SVC RBF", "SVR", "Random Forest", "Logistic Regression", "Decision Tree", "Linear Regression", "Naive Bayes", "K-Means Clustering", "Guassian Process" ))

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
    elif clf_name == "SVC":
        C = st.sidebar.slider("C", 0.01, 10.0)
        params["C"] = C
    else:
        max_depth = st.sidebar.slider("max_depth", 2, 15)
        n_estimators = st.sidebar.slider("n_estimators", 1, 100)
        params["max_depth"] = max_depth
        params["n_estimators"] = n_estimators
    return params
add_parameter_ui(classifier_name)



