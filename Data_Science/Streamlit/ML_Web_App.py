# App based on tutorial from Python Engineer
# https://www.youtube.com/watch?v=Klqn--Mu2pE&list=TLPQMTQwMjIwMjHWayHe3_rfPg&index=5

import streamlit as st
from sklearn import datasets
import numpy as np

st.title("Streamlit ML App")

st.write("""
# Explore different classifiers
Which one is the best?
""")

dataset_name = st.sidebar.selectbox("Select Dataset", ("Iris", "Breast Cancer", "Diabetes", "Boston Housing", "Digits"))
classifier_name = st.sidebar.selectbox("Select Classifier", ("KNN", "SVM", "Random Forest", "Logistic Regression", "Decision Tree", "Linear Regression", "Naive Bayes", "K-Means Clustering" ))

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


