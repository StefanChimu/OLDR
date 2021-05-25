import io
import re
import csv
import nltk
import pickle
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# nltk.download('stopwords')
# nltk.download('punkt')

from nltk.stem.snowball import SnowballStemmer

stm = SnowballStemmer("romanian") # used for stemming words

def elim_diacritics(text):
    text = text.replace('â', 'a')
    text = text.replace('ă', 'a')
    text = text.replace('Ă', 'A')
    text = text.replace('Â', 'A')
    text = text.replace('î', 'i')
    text = text.replace('î', 'I')
    text = text.replace('ț', 't')
    text = text.replace('Ț', 'T')
    text = text.replace('ș', 's')
    text = text.replace('Ș', 'S')
    return text

def elim_noise(text):
    noises = ['.', ',', '(', ')', '[', ']', '{', '}', '@', '!', '#', '$', '%', '^', '&', '*', '-', '+', ':', ';', '/', '`', '"', "'"]

    for noise in noises:
        text = text.replace(noise, '')

    return re.sub(r'[^a-zA-Z]', ' ', text)

def cleanup(text):
    setter = 0
    new_string = ''
    for i in range(0, len(text)):
        if text[i] == '<':
            setter = 1
        elif text[i] == '>':
            setter = 0
        if setter == 0:
            if text[i] != '>':
                new_string = new_string + text[i]
    return new_string

def elim_sw(text):
    filtered_text = elim_noise(elim_diacritics(cleanup(str(text))))

    stop_words = set(stopwords.words('romanian'))

    word_tokens = word_tokenize(filtered_text)

    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    clean_output = []

    for w in word_tokens:
        if w not in stop_words:
            if w != "„" and w != "”" and w != "«" and w != "»" and w != "[" and w != "]" and w != "…" and w != "km²":
                clean_output.append(w.lower())
    return clean_output

def mainfunc(text):
    output_text = elim_sw(text)
    output = pd.DataFrame(output_text, columns=['word'])
    output.to_csv('obtained_data.csv', index=False)
