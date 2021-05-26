'''README'''
'''OLDR.py script is only for debugging purposes because
it doesn't trigger the GUI - For normal use, use interface.py'''

import web_scraper as ws
from subprocess import call
import yt_scraper as ys
import stopwords as sw
import test_acc as accuracy
import training as t

option = 0
classifier = 0

def elim_diacritics_url(text):
    text = text.replace('â', 'a')
    text = text.replace('ă', 'a')
    text = text.replace('î', 'i')
    text = text.replace('ț', 't')
    text = text.replace('ș', 's')
    return text

def menu():
    global option
    global classifier
    print("What method of input do you prefer?")
    print("1 - Keyboard")
    print("2 - URL")
    print("3 - Exit app")
    option= int(input("Select one option : "))
    print("What classifier do you want to use??")
    print("1 - LineaSVC (best results)")
    print("2 - KNeighbors")
    print("3 - GaussianNB")
    classifier = int(input("Select one option : "))

def domain_name(url):
    return url.split("www.")[-1].split("//")[-1].split(".")[0]

def choose_classifier(classifier):
    if classifier == 1:
        t.train_SVC()
        accuracy.nn_info("SVC")
    elif classifier == 2:
        t.train_KN()
        accuracy.nn_info("KN")
    elif classifier == 3:
        t.train_NB()
        accuracy.nn_info("NB")
    else:
        print("Unknown classifier: " + str(classifier))

class CallPy(object):

    def __init__(self, path='/web_scraper.py'):
        self.path=path

    def call_python_file(self):
        call([ "{}".format(self.path)])

menu()

if option == 1:
    text=input("Enter the text bellow:\n")
    sw.mainfunc(text)
    choose_classifier(classifier)
elif option  == 2:
    url = input("Enter the URL here: ")
    url = elim_diacritics_url(url)
    domain = domain_name(url)
    if domain == "youtube":
        ys.scrap_yt(url)
        choose_classifier(classifier)
    else:
        ws.scrap_web(url)
        choose_classifier(classifier)
elif option == 3:
    exit()
else:
    print("Invalid option! \n")