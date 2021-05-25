import joblib
import pandas as pd
import numpy as np
from sklearn.svm import LinearSVC
import prepare_dataset as prepare
from sklearn.calibration import CalibratedClassifierCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

'''Linear SVC'''

def train_SVC():
    # Read data by csv columns (first column will be the labels)

    # print("[log] Preparing training data (This will take some time).")
    # prepare.main() # preparing dataset
    # print("[log] Preparing training data - Done!")

    print("[log] Reading data from csv.")
    data = pd.read_csv('training_data.csv')
    print("[log] Reading data from csv - Done!")

    print("[log] Spliting the content.")
    y = data['offensive']
    texts = data['text'].astype(str)
    print("[log] Spliting the content - Done!")

    # Vectorize the text - TF-IDF
    print("[log] Vectorizing (TF-IDF) ...")
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts) 
    print("[log] Vectorizing - Done!")

    # Train the model
    print("[log] Training ...")
    model = LinearSVC(class_weight="balanced", dual=False, tol=1e-2, max_iter=1e5)
    cclf = CalibratedClassifierCV(base_estimator=model)
    cclf.fit(X, y)
    print("[log] Training - Done!")

    # Save the model
    print("[log] Saving the model.")
    joblib.dump(vectorizer, 'vectorizer.joblib')
    joblib.dump(cclf, 'model.joblib')
    print("[log] Training script finished with succes!")

'''KN'''

def train_KN():
    # Read data by csv columns (first column will be the labels)

    # print("[log] Preparing training data (This will take some time).")
    # prepare.main() # preparing dataset
    # print("[log] Preparing training data - Done!")

    print("[log] Reading data from csv.")
    data = pd.read_csv('training_data.csv')
    print("[log] Reading data from csv - Done!")

    print("[log] Spliting the content.")
    y = data['offensive']
    texts = data['text'].astype(str)
    print("[log] Spliting the content - Done!")

    # Vectorize the text - TF-IDF
    print("[log] Vectorizing (TF-IDF) ...")
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts) 
    print("[log] Vectorizing - Done!")

    # Train the model
    print("[log] Training ...")
    model = KNeighborsClassifier(n_neighbors=3)
    cclf = CalibratedClassifierCV(base_estimator=model)
    cclf.fit(X, y)
    print("[log] Training - Done!")

    # Save the model
    print("[log] Saving the model.")
    joblib.dump(vectorizer, 'vectorizer.joblib')
    joblib.dump(cclf, 'model.joblib')
    print("[log] Training script finished with succes!")

''' NB '''

def train_NB():
    # Read data by csv columns (first column will be the labels)

    # print("[log] Preparing training data (This will take some time).")
    # prepare.main() # preparing dataset
    # print("[log] Preparing training data - Done!")

    print("[log] Reading data from csv.")
    data = pd.read_csv('training_data.csv')
    print("[log] Reading data from csv - Done!")

    print("[log] Spliting the content.")
    y = data['offensive']
    texts = data['text'].astype(str)
    print("[log] Spliting the content - Done!")

    # Vectorize the text - TF-IDF
    print("[log] Vectorizing (TF-IDF) ...")
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts) 
    print("[log] Vectorizing - Done!")

    # Train the model
    print("[log] Training ...")
    model = GaussianNB()
    cclf = CalibratedClassifierCV(base_estimator=model)
    cclf.fit(X.toarray(), y)
    print("[log] Training - Done!")

    # Save the model
    print("[log] Saving the model.")
    joblib.dump(vectorizer, 'vectorizer.joblib')
    joblib.dump(cclf, 'model.joblib')
    print("[log] Training script finished with succes!")
