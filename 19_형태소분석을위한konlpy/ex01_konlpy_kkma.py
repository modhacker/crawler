from konlpy.tag import Kkma

kkma = Kkma()

print(kkma.morphs('안녕하세요 반갑습니다. 파이썬으로 크롤링하기.'))
print(kkma.nouns(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기.'))
print(kkma.pos(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기.'))
