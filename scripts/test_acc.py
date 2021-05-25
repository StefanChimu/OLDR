from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from make_prediction import predict, predict_prob, predict_NB, predict_prob_NB
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import pandas as pd
import numpy as np
import os
from os import path

def nn_info(classifier):
    if path.exists("result.csv") == True:
        os.remove("result.csv")
    data = pd.read_csv('obtained_data.csv')
    texts = data['word'].astype(str)
    new_output = []
    print("[log] You choosed " + classifier + " classifier.")
    if classifier == "NB":
        is_offensive = max(predict_NB(texts))
    else:
        is_offensive = max(predict(texts))
    if is_offensive == 1:
        if classifier == "NB":
            probabilities = predict_prob_NB(texts)
        else: 
            probabilities = predict_prob(texts)
        for i in range (0, len(probabilities)):
            if probabilities[i] >= 0.85:
                new_output.append((str(texts[i]), str(probabilities[i])))
                output = pd.DataFrame(new_output, columns=['text', 'offensiveness'])
                output.to_csv('result.csv', index=False)
        print("[log] Done! Check the result.csv file.")
    else:
        print("There are no offensive words in the given dataset!")

def test_acc_on_trained_dataset(classifier):
    data = pd.read_csv('training_data.csv')
    y = data['offensive']
    texts = data['text'].astype(str)

    default_off_count = 0
    training_model_off_count = 0
    if classifier == "NB":
        probabilities = predict_prob_NB(texts)
    else:
        probabilities = predict_prob(texts)
    probs_arr = []

    for i in range(0, len(y)):
        if y[i] == 1:
            default_off_count += 1

    for i in range (0, len(probabilities)):
        if probabilities[i] >= 0.8:
            training_model_off_count += 1
            probs_arr.append(1)
        else:
            probs_arr.append(0)
            
    print("Offensive labels count: " + str(default_off_count) + "; Number of offensive words found: " + str(training_model_off_count))
    print("Accuracy: " + str(accuracy_score(y, probs_arr)))
    print("Precision: " + str(precision_score(y, probs_arr, average='macro')))
    print("F1: " + str(f1_score(y, probs_arr, average='macro')))
    print("Recall: " + str(recall_score(y, probs_arr, average='macro')))
