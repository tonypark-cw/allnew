class Calculater(object):
    def __init__(self, first, second):
        self.first=first
        self.second=second

    def add(self):
        result = self.first + self.second
        return ('add result :  {}'.format(result))

    def sub(self):
        result = self.first - self.second
        return ('sub result :  {}'.format(result))

    def mul(self):
        result = self.first * self.second
        return ('mul result :  {}'.format(result))

    def dvm(self):
        if self.second == 0:
            self.second = 5
        result = (self.first // self.second , self.first % self.second)
        return ('dvm result :  {}'.format(result))

calc = Calculater(10, 3)
print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.dvm())