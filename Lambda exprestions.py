
myList = [5, 4, 3]
square_list = list(map(lambda num: num ** 2, myList))
print(square_list)


a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key = lambda x: x[1])
print(a)
