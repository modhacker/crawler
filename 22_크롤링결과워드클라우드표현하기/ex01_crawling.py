from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

# 셀레니움으로 인기급상승 주소 접속 
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/feed/trending")

# 무한스크롤 함수
def scroll():
    while True:
        before_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(2)
        after_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
        time.sleep(2)
        if before_scroll_height == after_scroll_height:
            break
    time.sleep(2)

# 무한스크롤 함수 호출
scroll()

# 제목, 조회수 텍스트 포함된 요소 선택
elements = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
time.sleep(2)

# 제목, 조회수 리스트 선언 
hits_list = []
title_list = []

# 제목, 조회수 리스트 데이터 수집
for element in elements:
    if element.get_attribute("aria-label"): # shorts 영상 제외
        hits_text = element.get_attribute("aria-label")
        start_index = hits_text.rfind("조회수")+4
        end_index = hits_text.rfind("회")
        hits = hits_text[start_index:end_index]
        hits = int(hits.replace(",", ""))
        if element.text not in title_list: # 동일한 영상은 제외
            title_list.append(element.text)
            hits_list.append(hits)
    else:
        print("조회수 데이터 없음")

# 제목 리스트에서 명사, 형용사 추출 
okt = Okt()
word_list = []
for title in title_list:
    # print("제목", title)
    for word, tag in okt.pos(title):
        # print(word, tag)
        if tag in ['Noun', 'Adjective']:
            word_list.append(word)

# 동일 단어 횟수 추출  
word_list_count = Counter(word_list)

# 워드클라우드 객체 선언 및 출력 
wc =  WordCloud(font_path = 'NanumGothic.ttf', width=400, height=400)
result = wc.generate_from_frequencies(word_list_count)
plt.axis('off')
plt.imshow(result)
plt.show()
wc.to_file('result.png')

# csv 파일로 저장
crawling_result = {
    "title": title_list,
    "hits": hits_list
}

dataFrame = pd.DataFrame(crawling_result)

dataFrame.sort_values(by=["hits"], ascending=False).to_csv("result.csv", encoding="utf-8-sig")
