import re
import time
import stopwords as sw
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def remove_emoji(str):
    return str.encode('ascii', 'ignore').decode('ascii')

def scrap_yt(url):
    # using chrome driver for browser emulation
    driver_exe = 'chromedriver'
    all_comms = []

    # selenium by default opens a web view -- for hiding that we'll use headless parameter
    options = Options()
    # options.add_argument("--headless") 
    driver = webdriver.Chrome(driver_exe, options=options)
    wait = WebDriverWait(driver,20)
    driver.get(url)

    item = 50
    while item > 0:
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(3)
        item -= 1

    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        all_comms.append(remove_emoji(comment.text))
    
    sw.mainfunc(all_comms)