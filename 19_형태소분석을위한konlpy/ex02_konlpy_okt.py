from konlpy.tag import Okt

okt = Okt()

print(okt.morphs(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기.'))
print(okt.nouns(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기.'))
print(okt.pos(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기.'))
print(okt.normalize(u'안녕하세욬ㅋㅋ'))

