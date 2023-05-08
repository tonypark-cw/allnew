# myfile01 = open('sample.txt', 'rt', encoding='UTF-8')
# linelists = myfile01.readlines()
# myfile01.close()
# print(linelists)
#
# total = 0
# for one in linelists:
#     score = int(one)
#     total += score
# average = total / len(linelists)
#
# myfile02 = open('result.txt', 'wt', encoding='UTF-8')
# myfile02.write('총점 : ' + str(total) + '\n')
# myfile02.write('평균 : ' + str(average))
# myfile02.close()
# print("done~!!")
#
# myfile03 = open('result.txt', 'rt', encoding='UTF-8')
# line = 1
# while line:
#     line = myfile03.readline()
#     print(line)
# myfile03.close()
#
#
# myfile05 = open('sample.txt', 'rt', encoding='UTF-8')
# myfile04 = open('result.txt', 'wt', encoding='UTF-8')
# line = 1
# score = 0
# row = 1
# cnt = 1
# while line:
#     line = myfile05.readline()
#     line = line.replace('\n', '')
#     if line:
#         score = int(line)
#     else:
#         continue
#     total += score
#     average = total / cnt
#     cnt += 1
#     row += 1
#     myfile04.write('총점 : ' + str(total) + '\n')
#     myfile04.write('평균 : ' + str(average))
#     print(line)
#
# myfile05.close()
# myfile04.close()

myfile01 = open('sample.txt', 'rt', encoding='UTF-8')
linelists = myfile01.readlines()
myfile01.close()
print(linelists)

myfile02 = open('result.txt', 'wt', encoding='UTF-8')

total = 0
for one in linelists:
    score = int(one)
    total += score
    myfile02.write('total = ' + str(total) + ', value = ' + str(score) + '\n')
average = total / len(linelists)

myfile02.write('총점 : ' + str(total) + '\n')
myfile02.write('평균 : ' + str(average))
myfile02.close()
print("done~!!")

myfile03 = open('result.txt', 'rt', encoding='UTF-8')
line = 1
while line:
    line = myfile03.readline()
    print(line)
myfile03.close()