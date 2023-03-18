from functools import reduce

li = [2, 11, 32, 14, 53, 10, 23, 33, 46]

evens = list(filter(lambda a: a % 2 == 0, li))
doubles = list(map(lambda a: a * 2, evens))
sum = reduce(lambda a, b: a + b, doubles)

print(evens)
print(doubles)
print(sum)
