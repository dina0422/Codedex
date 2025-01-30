#transformation

#map(function, data)

def divide_by_2(x):
    return x / 2

halved_numbers = map(divide_by_2, [2, 4, 6, 8, 10])

print(list(halved_numbers))

##filter(function, data)

def filter_even(x):
    return x % 2 == 0

even_numbers = filter(filter_even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(list(even_numbers))

##reduce(function, data)
from functools import reduce

def multiply(x, y):
    return x * y

product = reduce(multiply, [1, 2, 3, 4, 5])

print(product)