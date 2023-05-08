
salary = int(input('월급 입력 : '))
income = 0 #연봉
tax = 0 #세금

#연봉 구하기
if salary >= 500:
    income = 12 * salary
else:
    income = 13 * salary

if income >= 10000:
    tax = 0.2 * income
elif income >= 7000:
    tax = 0.15 * income
elif income >= 5000:
    tax = 0.12 * income
elif income >= 1000:
    tax = 0.1 * income
else:
    tax = 0
print("월급 : %d" % (salary))
print("연봉 : %d" % (income))
print("세금 : %.2f" % (tax))