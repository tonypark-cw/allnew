import numpy as np

a = np.array([-1, 3, 2, -6])
b = np.array([[3, 6, 1, 2]])
print(a)
print(a.T)
print(b)
print(b.T)


A = np.reshape(a, [2, 2])
B = np.reshape(b, [2, 2])
print("sol1")
print(A)
print("sol2")
print(B)

result3_1 = np.matmul(A, B)
result3_2 = np.matmul(B, A)
print("sol3-1")
print(result3_1)
print("sol3-2")
print(result3_2)


b = np.reshape(b, [1, 4])
a = np.reshape(a, [1, 4])
b2 = np.transpose(b)
print("sol4-1")
print(b2)

result4 = np.matmul(a, b2)
print("sol4-2")
print(result4)


a = "Chanwoo is going down"
print(a)