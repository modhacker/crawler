"""Infinite Scrolling"""
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchWindowException
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 실행
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.youtube.com/")
# driver.execute_script("document.documentElement.scrollHeight")
h1 = driver.execute_script("return document.documentElement.scrollHeight")
print(h1)

while True:
    try:
        pass
    except NoSuchWindowException:
        break
    finally:
        driver.close()
