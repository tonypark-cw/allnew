mystring = "Life is an egg"
print(mystring)
mylist = mystring.split()
print(mylist)

for idx in range(len(mylist)):
    if idx % 2 == 0:
        mylist[idx] = mylist[idx].upper()
    else:
        mylist[idx] = mylist[idx].lower()

print(mylist)

result = ' '.join(mylist)
print('result : ', result)
