import pandas as pd

# Series 생성 
# 국어성적 정보
score_korean = pd.Series([98, 76, 60, 85, 80])
print(score_korean)

# 인덱스를 지정하여 Series 생성
score_korean = pd.Series([98, 76, 60, 85, 80], index=[1, 2, 3, 4, 5])
print(score_korean)

# range 함수 활용
score_korean = pd.Series([98, 76, 60, 85, 80], index=range(1,6))
print(score_korean)

# index 값 따로 선언 후 활용
student_number = [1, 2, 3, 4, 5]
score_korean = pd.Series([98, 76, 60, 85, 80], index=student_number)
print(score_korean)

# 성적 데이터도 리스트로 선언하여 활용 가능
korean_list = [98, 76, 60, 85, 80]
score_korean = pd.Series(korean_list, index=student_number)
print(score_korean)

# 영어 성적 추가 
english_list = [88, 92, 100, 55, 70]
score_english = pd.Series(english_list, index=student_number)
print(score_english)

# 국어, 영어 학생별 성적 합산 
total = score_korean + score_english
print(total)

# 수학 성적 추가(인덱스 번호가 1~5로 순차적이지 않음)
score_math = pd.Series([30, 20, 10, 40, 50], index=[3, 2, 1, 4, 5])
print(score_math)
print(score_math.sort_index())

# 전체 성적 합산(pandas가 인덱스 별로 계산을 수행함)
total = score_korean + score_english + score_math
print(total)

# 인덱스 기준 오름차순 정렬
print(total.sort_index())
# 인덱스 기준 내림차순 정렬
print(total.sort_index(ascending=False))
# 값 기준 오름차순 정렬
print(total.sort_values())
# 값 기준 내림차순 정렬
print(total.sort_values(ascending=False))
