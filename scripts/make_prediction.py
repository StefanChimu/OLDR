import numpy as np
import joblib
import training as t
import os.path
from os import path

vectorizer = joblib.load('vectorizer.joblib')
model = joblib.load('model.joblib')

def offensive_prob(prob):
    return prob[1]

def predict(texts):
    return model.predict(vectorizer.transform(texts))

def predict_prob(texts):
    return np.apply_along_axis(offensive_prob, 1, model.predict_proba(vectorizer.transform(texts)))