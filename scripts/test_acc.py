from make_prediction import predict, predict_prob
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

def nn_info():
    data = pd.read_csv('obtained_data.csv')
    texts = data['word'].astype(str)

    is_offensive = max(predict(texts))

    if is_offensive == 1:
        probabilities = predict_prob(texts)
        for i in range (0, len(probabilities)):
            if probabilities[i] >= 0.8:
                print("Word: " + str(texts[i]) + " is detected as offensive with the prob: " + str(probabilities[i]))
    else:
        print("There are no offensive words in the given dataset!")

def test_acc_on_trained_dataset():
    data = pd.read_csv('training_data.csv')
    y = data['offensive']
    texts = data['text'].astype(str)

    default_off_count = 0
    training_model_off_count = 0
    probabilities = predict_prob(texts)
    probs_arr = []

    for i in range(0, len(y)):
        if y[i] == 1:
            default_off_count += 1

    for i in range (0, len(probabilities)):
        if probabilities[i] >= 0.9:
            training_model_off_count += 1
            probs_arr.append(1)
        else:
            probs_arr.append(0)
    print("Offensive labels count: " + str(default_off_count) + "; Number of offensive words found: " + str(training_model_off_count))
    print(accuracy_score(y, probs_arr))
