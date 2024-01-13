from konlpy.tag import Kkma
from konlpy.tag import Okt

okt = Okt()
kkma = Kkma()

text = "안녕하세요 파이썬 입니다. 파이썬을 배우고 있습니다. 파이썬은 재미있습니다."

print(kkma.pos(text))
print(okt.pos(text))

for word, tag in kkma.pos(text):
    print("kkma", word, tag)

for word, tag in okt.pos(text):
    print("okt", word, tag)
