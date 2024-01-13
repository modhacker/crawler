from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
# driver.execute_script("document.documentElement.scrollHeight")
h1 = driver.execute_script("return document.documentElement.scrollHeight")
print(h1)
