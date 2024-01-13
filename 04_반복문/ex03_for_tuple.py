tuple1 = ("apple", "banana", "melon", "cherry", "tomato")
for fruit in tuple1:
    print(fruit)

tuple2 = ("apple", "banana", "melon", "cherry", "tomato", ("strawberry", "blueberry"))
for fruit in tuple2:
    print(fruit)

tuple3 = ((1, "python"), (2, "java"), (3, "c"), (4, "javascript"))
for index, lang in tuple3:
    print(index, lang)