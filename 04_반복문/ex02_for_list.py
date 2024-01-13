list1 = [10, 20, 30, 40, 50]
for num in list1:
    print(num)

list2 = ["빨강", "주황", "노랑", "초록", "파랑"]
for color in list2:
    print(color)

list3 = ["빨강", "주황", "노랑", "초록", "파랑", ["분홍", "연한분홍", "진한분홍"]]
for color in list3:
    print(color, end="\t")
    