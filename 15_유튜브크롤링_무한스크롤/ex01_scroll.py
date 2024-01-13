"""Count titlels on Youtube(0)"""
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

while True:
    before_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
    time.sleep(2)
    after_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
    time.sleep(2)
    if before_scroll_height == after_scroll_height:
        break

time.sleep(10)

titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
# titles = driver.find_elements(By.ID, "video-title")

print("영상 갯수: ", len(titles))
for title in titles:
    print(title.text)

while True:
    try:
        pass
    except NoSuchWindowException:
        break
    finally:
        driver.close()
