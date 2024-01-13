from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/feed/trending")
time.sleep(2)
elements = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
time.sleep(2)
hits_list = []
title_list = []
for element in elements:
    if element.get_attribute("aria-label"):
        hits_text = element.get_attribute("aria-label")
        start_index = hits_text.rfind("조회수")+4
        end_index = hits_text.rfind("회")
        hits = hits_text[start_index:end_index]
        hits = int(hits.replace(",", ""))
        title_list.append(element.text)
        hits_list.append(hits)
    else:
        print("조회수 데이터 없음")

crawling_result = {
    "title": title_list,
    "hits": hits_list
}

dataFrame = pd.DataFrame(crawling_result)

dataFrame.to_csv("result.csv", encoding="utf-8-sig")
