tuple1 = (1, 2, 3, 5, 8)
tuple2 = (8, 2, 5)

x = list(tuple1)
x.insert(2, tuple2)
tuple1 = tuple(x)

print(tuple1)
