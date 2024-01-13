import pandas as pd

scores = pd.DataFrame(
    {
        "이름": ["김파이", "이파이", "박파이", "최파이", "정파이", "조파이"],
        "국어": [96, 76, 60, 85, 80, 100],
        "영어": [88, 92, 100, 55, 70, 100],
        "수학": [10, 20, 30, 40, 50, 100],
    }, index=[1, 2, 3, 4, 5, 6]
)
print(scores)
# 이름 기준 오름차순 정렬
print(scores.sort_values(by="이름", ascending=True))
# 이름 기준 내림차순 정렬
print(scores.sort_values(by="이름", ascending=False))
# 수학 기준 오름차순 정렬
print(scores.sort_values(by="수학", ascending=True))








