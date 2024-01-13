import pandas as pd

scores_dict = {"국어": [96, 76, 60, 85, 80],
                "영어": [88, 92, 100, 55, 70],
                "수학": [10, 20, 30, 40, 50]}

scores = pd.DataFrame(scores_dict)
print(scores)

# 인덱스 지정
scores = pd.DataFrame(scores_dict, index=[1, 2, 3, 4, 5])
print(scores)