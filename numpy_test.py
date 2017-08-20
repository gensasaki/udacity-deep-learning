import numpy as np

m = np.array([[1, 2, 3],[4, 5, 6]])
print(m)

n = m * 0.25
print(n)

print(m * n)

np.multiply(m, n)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(a)
print(a.shape)

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(b)
print(b.shape)

c = np.matmul(a, b)
print(c)
print(c.shape)


x = np.array([[1, 2], [3, 4]])
print(x)

np.dot(x, x)
x.dot(a)
np.matmul(x, x)

# transpose

o = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [99, 10, 11, 12]])
print(o)
print(o.T)
o_t = o.T
o_t[3][1] = 200
print(o_t)
