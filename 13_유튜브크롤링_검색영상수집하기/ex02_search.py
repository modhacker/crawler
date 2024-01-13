from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=뉴진스")

titles = driver.find_elements(By.ID, "video-title")
for title in titles:
    print(title.text)