import numpy as np

# 배열 합치기
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = np.concatenate((a, b))
print(c)