import io
import csv
import nltk
import pickle
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

def elim_diacritics(text):
    text = text.replace('â', 'a')
    text = text.replace('ă', 'a')
    text = text.replace('Ă', 'A')
    text = text.replace('Â', 'A')
    text = text.replace('î', 'i')
    text = text.replace('Î', 'I')
    text = text.replace('ț', 't')
    text = text.replace('Ț', 'T')
    text = text.replace('ș', 's')
    text = text.replace('Ș', 'S')
    return text

def elim_punct(text):
    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('?', '')
    text = text.replace('!', '')
    text = text.replace(':', '')
    text = text.replace(';', '')
    text = text.replace('"', '')
    text = text.replace("'", "")
    text = text.replace('(', '')
    text = text.replace(')', '')
    text = text.replace('[', '')
    text = text.replace(']', '')
    text = text.replace('{', '')
    text = text.replace('}', '')
    return text

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


def mainfunc(text):
    checker = 0

    f = io.open('output.txt', "w", encoding="utf-8")

    filtered_text = elim_punct(elim_diacritics(cleanup(str(text))))

    stop_words = set(stopwords.words('romanian'))

    word_tokens = word_tokenize(filtered_text)

    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    for w in word_tokens:
        if w not in stop_words:
            if w != "„" and w != "”" and w != "«" and w != "»" and w != "[" and w != "]" and w != "…" and w != "km²":
                f.writelines(w)
                f.write("\n")
                if checker == 0:
                    checker = 1
    f.close()

    if checker == 1:
        print("\nDone with succes! Check the output file!\n")