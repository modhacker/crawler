from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

q = input("검색어를 입력하세요: ")
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query="+q)
time.sleep(5)
titles = driver.find_elements(By.ID, "video-title")
time.sleep(2)
for title in titles:
    print(title.text)