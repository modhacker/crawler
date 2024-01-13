import matplotlib as mpl
import matplotlib.pyplot as plt

# x축, y축 값 함께 정의 
# plt.plot([1, 2, 3, 4], [2, 5, 6, 10])
x_values = [1, 2, 3, 4]
y_values = [2, 5, 6, 10]
plt.plot(x_values, y_values)
# 축 label 표시하기 
plt.xlabel("x axis label")
plt.ylabel("y axis label")
plt.show()