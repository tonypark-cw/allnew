myfile1 = open('sample2.txt', 'rt', encoding='UTF-8')
lines = myfile1.readlines()
myfile1.close()


myfile2 = open('result2.txt', 'wt', encoding='UTF-8')
for line in lines:

    name, id = line.split(',')
    id = int(id)
    print(name, id)
    if id >= 19:
        val = '성인'
    else:
        val = '미성년자'
    pline = name + ',' + str(id) + ',' + val + '\n'
    myfile2.write(pline)
    print(pline)

myfile2.close()
