tuple0 = (1,2,3,4)

print(tuple0)

tuple0 = tuple0 + (4,5,6)

print(tuple0)

tuple01 = 1,2,3,4

mylist = [1,2,3,4]
tuple02 = tuple(mylist)

if tuple01 == tuple02:
    print('둘이 같다')
else:
    print('안 같다')

tuple03 = (1,2,3)
tuple04 = (4,5,6)
tuple05 = tuple03 + tuple04
print(tuple05)

tuple06 = tuple05*3
print(tuple06)

a,b=(1,2)
print('a',a,'b',b)
a,b = b,a
print('a',a,'b',b)

tuple07=(11,22,33,44,55,66)
print(tuple07[1:3])
print(tuple07[3:])