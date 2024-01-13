from collections import Counter
import matplotlib.pyplot as plt

# 한글처리를 위한 설정
plt.rcParams['font.family'] = 'Malgun Gothic'

# 연습용 데이터
word_list = ['빨강', '노랑', '파랑', '빨강', '파랑', '빨강']

# 동일 단어 횟수 추출  
word_list_count = Counter(word_list)
# 단어, 횟수 형태로 출력확인

# Counter만 적용
print(type(word_list_count))
# 타입확인
print(word_list_count)
# most_common() 적용
print(type(word_list_count.most_common()))
# 타입확인
print(word_list_count.most_common())



# 단어로 이루어진 리스트 생성
words = []
for word, count in word_list_count.most_common():
    words.append(word)
# 아래 문장처럼 한 문장으로도 표현 가능
# words = [word for word, count in word_list_count.most_common()]

# 횟수로 이루어진 리스트 생성 
counts = [count for word, count in word_list_count.most_common()]

# 단어를 가로축으로, 세로축은 횟수로
plt.bar(words, counts)
plt.show()