"""Crawled with Danawa"""
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://prod.danawa.com/list/?cate=112758&shortcutKeyword=%EB%85%B8%ED%8A%B8%EB%B6%81")
notebook_names = driver.find_elements(By.CSS_SELECTOR, '[name="productName"]')

for name in notebook_names:
    print(name.text)

while True:
    try:
        if len(driver.window_handles) == 0:
            raise NoSuchWindowException
    except NoSuchWindowException:
        break
