from konlpy.tag import Okt
from collections import Counter

okt = Okt()

text = "안녕하세요 파이썬 입니다. 파이썬을 배우고 있습니다. 파이썬은 재미있습니다. 크롤링도 배우고 있습니다."

word_list = []

for word, tag in okt.pos(text):
    if tag in ['Noun', 'Adjective']:
        word_list.append(word)

print(Counter(word_list))
