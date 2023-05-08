mystring = 'Roman cavarly choires are singing be my sword and shield'

mylist = mystring.split()

print(mylist)

for i in range(len(mylist)):
    if i % 2== 0:
        mylist[i] = mylist[i].upper()
    else:
        mylist[i] = mylist[i].lower()

print(mylist)

result = '#'.join(mylist)
print(result)

result = ' '.join(mylist)
print(result)