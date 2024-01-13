"""Search By Class"""
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# 접속
driver.get("https://www.naver.com")

# 검색창에 오늘 날씨이라고 입력하고 검색버튼 클릭해보기
search = driver.find_element(By.XPATH, '//*[@id="query"]')
search.send_keys("오늘 날씨")
# 입력하는 것 까지 확인하고 검색 버튼 클릭
search_button = driver.find_element(By.XPATH, '//*[@id="search-btn"]')
search_button.click()
while True:
    try:
        pass
    except NoSuchWindowException:
        break
    finally:
        driver.close()
