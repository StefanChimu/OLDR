from tkinter import *
from tkinter import ttk
import web_scraper as wb
import yt_scraper as yt
import stopwords as sw
import time
import test_acc as accuracy
import training as t
import string
import charts as ch

root = Tk()
root.geometry("600x400")


def domain_name(url):
    return url.split("www.")[-1].split("//")[-1].split(".")[0]


def elim_diacritics_url(text):
    text = text.replace('â', 'a')
    text = text.replace('ă', 'a')
    text = text.replace('î', 'i')
    text = text.replace('ț', 't')
    text = text.replace('ș', 's')
    return text


Label(root, text="OLDR", fg="red", font=('times', 24, 'italic')).pack()
Label(root, text="", fg="red").pack()

def chart():
    print()

def choose_classifier(classifier):
    if classifier == "LinearSVC":
        t.train_SVC()
        accuracy.nn_info("SVC")
    elif classifier == "KNeighbors":
        t.train_KN()
        accuracy.nn_info("KN")
    elif classifier == "GaussianNB":
        t.train_NB()
        accuracy.nn_info("NB")
    else:
        print("Unknown classifier: " + str(classifier))

def click1():
    link = entry.get()
    url = elim_diacritics_url(link)
    domain = domain_name(link)
    if domain == "youtube":
        yt.scrap_yt(link)
        choose_classifier(clicked.get())
    else:
        wb.scrap_web(link)
        choose_classifier(clicked.get())
    myLabel = Label(bottomframe, text="Done with succes! " + clicked.get(), fg="red")
    myLabel.pack(pady=10)
    my_finishURL.config(text="You choose the URL option")


def click2():
    text = entry.get()
    if len(text) == 0:
        notext = Label(bottomframe, text="Please introduce text", fg="red")
        notext.pack(pady=10)
    else:
        sw.mainfunc(text)
        choose_classifier(clicked.get())
        myLabel = Label(bottomframe, text="Done with succes! " + clicked.get(), fg="red")
        myLabel.pack(pady=10)
        my_finishURL.config(text="You choose the Keyboard option")



topframe = Frame(root)
entry = Entry(topframe, width=50)
entry.pack()

options = ["LinearSVC", "KNeighbors", "GaussianNB"]
clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(topframe, clicked, *options)
drop.pack()
selector = clicked.get()

Label(topframe, text="", fg="red").pack()

button1 = Button(topframe, text="Search after URL", bg='black', fg='white', command=click1)
button1.pack(side=LEFT)
button2 = Button(topframe, text="Search from Keyboard", bg='black', fg='white', command=click2)
button2.pack(side=RIGHT)
button3 = Button(topframe, text="Graphic", bg='black', fg='white', command=chart())
button3.pack()

topframe.pack(side=TOP)

bottomframe = Frame(root)


def clear_frame():
    for widgets in bottomframe.winfo_children():
        widgets.destroy()


Button(bottomframe, text="Clear", font=('Helvetica bold', 10), command=clear_frame).pack(pady=20)

my_finishURL = Label(bottomframe, text="")
my_finishURL.pack(pady=20)
bottomframe.pack()
root.mainloop()
