import timeit

t1 = (11, 22, 33)
t2 = ('Python', 1.23, 1223, True)

print(type(t1))
print(type(t2))

print(len(t1))
print(len(t2))

print(t1[2])
print(t2[2])
print(t2[:4:2])

for elem in t1:
    print(elem)

t3 = t1 + t2
print(t3)

a = 1, 10, 100, 1000, 2, 3, 4
print(type(a))
print(a)
i, j, *k = a
print(i, j, k)

z, x, *c = range(1, 10)
print(z, x, c)

x1 = 19
x2 = 91
print(x1, x2)
x1, x2 = x2, x1
print(x1, x2)

print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))
