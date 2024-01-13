from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

# 셀레니움으로 검색결과 페이지 접속 
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=뉴진스")

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
    # shorts 영상 및 YouTube 영화는 제외 
    if element.get_attribute("aria-label") and "YouTube 영화" not in element.get_attribute("aria-label"):
        hits_text = element.get_attribute("aria-label")        
        start_index = hits_text.rfind("조회수")+4
        end_index = hits_text.rfind("회")
        hits = hits_text[start_index:end_index]
        # 조회수가 1000 이상인 경우(1,000 1,000,000 등)
        if "," in hits:
            hits = int(hits.replace(",", ""))
            # print(hits)
        # 조회수 값이 없는 경우 0 으로(조회수 없음)
        elif not hits: 
            print("조회수없음", hits)
            hits = 0
        # 조회수가 1000 미만인 경우(999 10 등 ,가 없어서 replace 에서 에러 발생)
        elif "," not in hits:
            hits = int(hits)
            # print(hits)

        if element.text not in title_list: # 동일한 영상은 제외
            title_list.append(element.text)
            hits_list.append(hits)
    else:
        print("shorts 영상")

# 제목 리스트에서 명사, 형용사 추출 
okt = Okt()
word_list = []
for title in title_list:
    for word, tag in okt.pos(title):
        if tag in ['Noun', 'Adjective']:
            word_list.append(word)

# 동일 단어 횟수 추출  
word_list_count = Counter(word_list)

# 워드클라우드 객체 선언 및 출력 
wc =  WordCloud(font_path = 'malgun', width=400, height=400)
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

dataFrame.sort_values(by=["hits"], ascending=False).to_csv("result12.csv", encoding="utf-8-sig")
