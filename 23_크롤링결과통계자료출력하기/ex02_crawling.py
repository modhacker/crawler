from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 셀레니움으로 인기급상승 주소 접속 
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/feed/trending")
# driver.get("https://www.youtube.com")

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
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
time.sleep(2)

# 제목, 조회수 리스트 선언 
hits_list = []
title_list = []

# 제목, 조회수 리스트 데이터 수집
for title in titles:
    # shorts 영상, YouTube 영화, 제목데이터 없는 컨텐츠 
    if title.get_attribute("aria-label") and title.text and "YouTube 영화" not in title.get_attribute("aria-label"): 
        aria_label = title.get_attribute("aria-label")
        start_index = aria_label.rfind("조회수")+4
        end_index = aria_label.rfind("회")
        hits = aria_label[start_index:end_index]
        # 조회수 값 범위에 따라 분리 
        # 조회수 없는 영상은 0으로, 조회수가 1000미만인 영상은 , 처리 생략 
        # 조회수 1,000 이상 영상
        if "," in hits:
            hits = int(hits.replace(",",""))
        # 조회수 없는 영상 
        elif not hits:
            hits = 0
        # 조회수 1,000 미만 
        else:
            hits = int(hits)            
        # 동일한 제목 영상은 한 번만 
        if title.text not in title_list:
            title_list.append(title.text)
            hits_list.append(hits)

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

# 단어로 이루어진 리스트 생성
words = []
for word, count in word_list_count.most_common(10):
    words.append(word)

# words = [word for word, count in word_list_count.most_common(5)]
# 횟수로 이루어진 리스트 생성 
counts = [count for word, count in word_list_count.most_common(10)]
plt.bar(words, counts)
plt.show()

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

dataFrame.sort_values(by=["hits"], ascending=False).to_csv("result.csv", encoding="utf-8-sig")