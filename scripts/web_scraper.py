from urllib.request import urlopen as urlopen
from bs4 import BeautifulSoup as bsoup 

# only works for pages with exposed content (content in wikipedia is unde body -> divs -> p's)
# for YT, Facebook and Twitter, they are dinamically generated and BeautifulSoup will not be able
# to grab text content from them.

myurl = input("Enter URL:\n")

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

print(elim_diacritics(cleanup(str(paragraphs))))