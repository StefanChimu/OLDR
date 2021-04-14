from urllib.request import urlopen as urlopen
from bs4 import BeautifulSoup as bsoup
import stopwords as sw

# only works for pages with exposed content (content in wikipedia is unde body -> divs -> p's)
def scrap_web(url):
    client = urlopen(url)
    page_html = client.read()

    # offloading the page
    page_soup = bsoup(page_html, "html.parser")

    # taking the content that we need
    paragraphs = page_soup.findAll("p")
    sw.mainfunc(str(paragraphs))
