import web_scraper as ws
from subprocess import call
import yt_scraper as ys
import stopwords as sw
import test_acc as accuracy
import training as t

option = 0

def elim_diacritics_url(text):
    text = text.replace('â', 'a')
    text = text.replace('ă', 'a')
    text = text.replace('î', 'i')
    text = text.replace('ț', 't')
    text = text.replace('ș', 's')
    return text

def menu():
    global option
    print("What method of input do you prefer?")
    print("1 - Keyboard")
    print("2 - URL")
    print("3 - Exit app")
    option= int(input("Select one option : "))

def domain_name(url):
    return url.split("www.")[-1].split("//")[-1].split(".")[0]

class CallPy(object):

    def __init__(self, path='/web_scraper.py'):
        self.path=path

    def call_python_file(self):
        call([ "{}".format(self.path)])

menu()

if option == 1:
    text=input("Enter the text bellow:\n")
    sw.mainfunc(text)
    t.train()
    accuracy.nn_info()

elif option  == 2:
    url = input("Enter the URL here: ")
    url = elim_diacritics_url(url)
    domain = domain_name(url)
    t.train()
    if domain == "youtube":
        ys.scrap_yt(url)
        accuracy.nn_info()
    else:
        ws.scrap_web(url)
        accuracy.nn_info()
elif option == 3:
    exit()
else:
    print("Invalid option! \n")