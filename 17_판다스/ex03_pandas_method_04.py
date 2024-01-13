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
# 처음 2줄만 조회
print(scores.head(2))
# 마지막 2줄만 조회
print(scores.tail(2))






