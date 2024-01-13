from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/feed/trending")

def scroll():
    while True:
        before_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(2)
        after_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
        time.sleep(2)
        if before_scroll_height == after_scroll_height:
            break
    time.sleep(2)
    titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
    print("영상 갯수: ", len(titles))
    return titles

titles = scroll()

for title in titles:
    print(title.text)