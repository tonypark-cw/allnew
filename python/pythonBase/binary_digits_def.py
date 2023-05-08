import random
def binary_digits(n):
    if n == 1 or n==0:
        return [n]
    return binary_digits(n//2)+[(n%2)]

print(binary_digits(random.random(4,17)))
