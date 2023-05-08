def factorial(n):
    if n == 1 or n==0:
        return 1
    return factorial(n-1)*n



class Factorial:
    def __init__(self, value):
        self.value = value
    def factorial(self):
        if self.value == 1 or self.value==0:
            return 1
        return factorial(self.value-1)*self.value

f = Factorial(10)

print(f.factorial())