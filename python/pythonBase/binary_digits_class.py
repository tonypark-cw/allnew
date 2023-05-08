import random

class Binary:
    def __init__(self, value):
        self.value = value
    def binary_digits(self):
        result = []
        if self.value == 1 or self.value==0:
            return result.append(self.value)
        else:
            while self.value >= 2:
                if self.value >= 2:
                    if len(result) > 1:
                        result.pop()
                    t = self.value %2
                    m = self.value // 2
                    result.append(t)
                    result.append(m)
                    self.value = (self.value // 2)
                    # print(self.value)
                else:
                    result.append(self.value)
                    # print(self.value)
            result.reverse()
        return result
numb = random.randrange(4,17)
print('numb : ', numb , Binary(numb).binary_digits())

