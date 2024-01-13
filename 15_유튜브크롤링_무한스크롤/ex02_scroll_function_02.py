"""Count titlels on Youtube(2)"""
import time
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 실행
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.youtube.com/")

def scroll():
    """Auto scroll down"""
    while True:
        before_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(2)
        after_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
        time.sleep(2)
        if before_scroll_height == after_scroll_height:
            break
    time.sleep(2)
    _titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
    print("영상 갯수: ", len(_titles))
    return _titles

titles = scroll()

for title in titles:
    print(title.text)

while True:
    try:
        if len(driver.window_handles) == 0:
            raise NoSuchWindowException
    except NoSuchWindowException:
        break
