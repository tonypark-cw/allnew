def fibo(n):
    if n == 1 or n == 2 :
        return 1
    else :
        return fibo(n-1) + fibo(n-2)

print(fibo(7))

# 1 1 2 3 5 8 13