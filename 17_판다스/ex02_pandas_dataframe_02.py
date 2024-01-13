import pandas as pd

scores = pd.DataFrame([
    [96, 76, 60, 85, 80], [88, 92, 100, 55, 70], [10, 20, 30, 40, 50]
], index=["국어", "영어", "수학"])
print(scores)

scores = pd.DataFrame([
    [96, 88, 10], [76, 92, 20], [60, 100, 30], [85, 55, 40], [80, 70, 50]
], index=[1, 2, 3, 4, 5])
print(scores)