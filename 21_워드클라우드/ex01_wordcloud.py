from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

okt = Okt()

wc =  WordCloud(font_path = 'NanumGothic.ttf', width=400, height=400)

text = "안녕하세요 파이썬 입니다. 파이썬을 배우고 있습니다. 파이썬은 재미있습니다. 크롤링도 배우고 있습니다."

word_list = []

for word, tag in okt.pos(text):
    if tag in ['Noun', 'Adjective']:
        word_list.append(word)

print(Counter(word_list))
word_list_count = Counter(word_list)
result = wc.generate_from_frequencies(word_list_count)
# x,y축 생략
plt.axis('off')
# 워드클라우드 결과를 이미지로 준비
plt.imshow(result)
# 이미지 출력
plt.show()

wc.to_file('result.png')

