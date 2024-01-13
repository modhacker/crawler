from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://prod.danawa.com/list/?cate=112758&shortcutKeyword=%EB%85%B8%ED%8A%B8%EB%B6%81")
notebook_names = driver.find_elements(By.CSS_SELECTOR, '[name="productName"]')
time.sleep(5)
for name in notebook_names:
    print(name.text)    