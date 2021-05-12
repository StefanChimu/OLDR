from tkinter import *
from tkinter import ttk
import web_scraper as wb
import yt_scraper as yt
import stopwords as sw
import time
import test_acc as accuracy
import training as t

root = Tk()
root.geometry("800x500")

def domain_name(url):
    return url.split("www.")[-1].split("//")[-1].split(".")[0]

def elim_diacritics_url(text):
    text = text.replace('â', 'a')
    text = text.replace('ă', 'a')
    text = text.replace('î', 'i')
    text = text.replace('ț', 't')
    text = text.replace('ș', 's')
    return text

Label(root,text="OLDR",fg = "red",font= ('times', 24, 'italic')).pack()

def click1():
    link=entry.get()
    url = elim_diacritics_url(link)
    domain = domain_name(link)
    if domain == "youtube":
        t.train()
        yt.scrap_yt(link)
        accuracy.nn_info()
    else:
        t.train()
        wb.scrap_web(link)
        accuracy.nn_info()
    myLabel=Label(bottomframe, text="You choose the URL option", fg = "red",font= ('times', 16, 'italic'))
    myLabel.pack(pady=10)
    my_finishURL.config(text="Done with succes! Check the output file!")

def click2():
    text=entry.get()
    sw.mainfunc(text)
    t.train()
    accuracy.nn_info()
    myLabel = Label(bottomframe, text="You choose the Keyboard option", fg="red", font=('times', 16, 'italic'))
    myLabel.pack(pady=10)
    my_finishURL.config(text="Done with succes! Check the output file!")

topframe = Frame(root)
entry = Entry(topframe , width=50)
entry.pack()
entry.insert(0,"Enter a URL link or a text from Keyboard")

Label(topframe,text="",fg = "red").pack()

button1 = Button(topframe, text="Search after URL", bg='black', fg='white',command=click1)
button1.pack(side=LEFT)
button2 = Button(topframe, text="Search from Keyboard", bg='black', fg='white', command=click2)
button2.pack(side=RIGHT)

topframe.pack(side = TOP)

bottomframe = Frame(root)

my_finishURL=Label(bottomframe,text="")
my_finishURL.pack(pady=20)

bottomframe.pack()

root.mainloop()