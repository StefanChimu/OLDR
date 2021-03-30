from urllib.request import urlopen as urlopen
from bs4 import BeautifulSoup as bsoup
import csv
import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import pickle
import io

# nltk.download('stopwords')
# nltk.download('punkt')

myurl = input("Enter URL:\n")
# https://ro.wikipedia.org/wiki/Rom%C3%A2nia

client = urlopen(myurl)
page_html = client.read()

# offloading the page
page_soup = bsoup(page_html, "html.parser")

# taking the content that we need
paragraphs = page_soup.findAll("p")

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

f = io.open('file.txt', "w", encoding="utf-8")

example_sent = elim_diacritics(cleanup(str(paragraphs)))

stop_words = set(stopwords.words('Romanian'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
print(filtered_sentence)

for w in word_tokens:
    if w not in stop_words:
        if w != "„" and w != "”" and w != "«" and w != "»" and w != "[" and w != "]" and w != "…" and w != "km²":
            f.writelines(w)
            f.write("\n")
f.close()

# print(word_tokens)



