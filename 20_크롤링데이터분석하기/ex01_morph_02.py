from konlpy.tag import Okt

okt = Okt()

text = "안녕하세요 파이썬 입니다. 파이썬을 배우고 있습니다. 파이썬은 재미있습니다."

# 명사만 출력하기 
for word, tag in okt.pos(text):
    if tag in 'Noun':
        print(word, tag)

# 형용사만 출력하기 
for word, tag in okt.pos(text):
    if tag in 'Adjective':
        print(word, tag)

# 명사, 형용사 출력하기 
for word, tag in okt.pos(text):
    if tag in ['Noun', 'Adjective']:
        print(word, tag)

