import pandas as pd

scores = pd.DataFrame(
    {
        "국어": [96, 76, 60, 85, 80],
        "영어": [88, 92, 100, 55, 70],
        "수학": [10, 20, 30, 40, 50]
    }, index=[1, 2, 3, 4, 5]
)
print(scores)