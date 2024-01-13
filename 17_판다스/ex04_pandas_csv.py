import pandas as pd

scores = pd.DataFrame(
    {
        "이름": ["김파이", "이파이", "박파이", "최파이", "정파이", "조파이"],
        "국어": [96, 76, 60, 85, 80, 100],
        "영어": [88, 92, 100, 55, 70, 100],
        "수학": [10, 20, 30, 40, 50, 100],
    }, index=[1, 2, 3, 4, 5, 6]
)

# 현재폴더에 scores.csv 라는 이름으로 파일 생성 
scores.to_csv("./scores.csv", encoding="utf-8-sig")




