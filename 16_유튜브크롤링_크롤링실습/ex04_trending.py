from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/feed/trending")
time.sleep(2)
elements = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
time.sleep(2)
hits_list = []
title_list = []
for element in elements:
    # shorts를 제외하기 위한 조건문
    if element.get_attribute("aria-label"):
        # 제목, 조회수를 포함하는 전체 텍스트
        hits_text = element.get_attribute("aria-label")
        start_index = hits_text.rfind("조회수")+4
        end_index = hits_text.rfind("회")
        # 조회수 숫자값만 추출
        hits = hits_text[start_index:end_index]
        # , 부분 없애기
        hits = int(hits.replace(",", ""))
        # 제목은 제목 리스트에 추가
        title_list.append(element.text)
        # 조회수는 조회수 리스트에 추가
        hits_list.append(hits)
    else:
        print("조회수 데이터 없음")

for title, hits in zip(title_list, hits_list):
    print(title, hits)
