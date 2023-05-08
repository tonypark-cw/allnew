def nolamda(x, y):
    return 3 * x + 2 * y

x, y = 3, 5

result = nolamda(x, y)
print('일반 함수 방식 : % d' % (result))

yeslambda = lambda x, y : 3 * x + 2 * y
result = yeslambda(x,y)
print('람다 함수 방식 1 : % d' % (result))

result = yeslambda(5,7)
print('람다 함수 방식 2 : % d' % (result))
