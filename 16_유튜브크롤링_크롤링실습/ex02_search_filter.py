"""Crawled 뉴진스 with Youtube(1)"""
import time
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException
from webdriver_manager.chrome import ChromeDriverManager

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

# 브라우저 실행
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.youtube.com/")
# 검색어 입력
search_input = driver.find_element(By.CSS_SELECTOR, "input#search")
search_input.send_keys("뉴진스")
# 검색버튼 클릭
search_button = driver.find_element(By.CSS_SELECTOR, "button#search-icon-legacy")
search_button.click()
time.sleep(2)
# 필터버튼 클릭
filter_button = driver.find_element(By.XPATH, '//*[@id="container"]/ytd-toggle-button-renderer')
filter_button.click()
time.sleep(2)
# 조회수 클릭
hits_button = driver.find_element(By.XPATH, '/html/body/ytd-app'
                                  '/div[1]/ytd-page-manager/ytd-search'
                                  '/div[1]/ytd-two-column-search-results-renderer'
                                  '/div/ytd-section-list-renderer/div[1]/div[2]'
                                  '/ytd-search-sub-menu-renderer/div[1]/iron-collapse'
                                  '/div/ytd-search-filter-group-renderer[5]'
                                  '/ytd-search-filter-renderer[3]/a')
hits_button.click()
time.sleep(2)
# 무한 스크롤 함수 호출
titles = scroll()

for title in titles:
    print(title.text)

while True:
    try:
        if len(driver.window_handles) == 0:
            raise NoSuchWindowException
    except NoSuchWindowException:
        break