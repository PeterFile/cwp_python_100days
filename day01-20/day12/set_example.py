set1 = {1, 2, 3, 4, 4, 2}
print(set1)

set2 = {'banana', 'pitaya', 'apple', 'apple', 'banana', 'grape'}
print(set2)

set3 = set('hello')
print(set3)

set4 = set([1, 2, 3, 3, 2, 4, 55])
print(set4)

set5 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
print(set5)

print(len(set5))
for elem in set5:
    print(elem)

set1 = {11, 12, 13, 14, 15}
print(10 in set1)
print(15 in set1)
set2 = {'Python', 'Java', 'C++', 'Swift'}
print('Python' not in set2)
print('Java' in set2)

set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# 交集
print(set2 & set1)
print(set1.intersection(set2))

# 并集
print(set1 | set2)
print(set1.union(set2))

# 差集
print(set1 - set2)
print(set1.difference(set2))

# 对称差
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

set1 = {1, 3, 5, 7}
set2 = {2, 4, 6}
set1 |= set2
print(set1)
set3 = {3, 6, 9}
set1 &= set3
print(set1)
set2 -= set1
print(set2)

set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
set3 = {5, 4, 3, 2, 1}
print(set1 < set2)
print(set1 <= set2)
print(set1 <= set3)

set1 = {1, 10, 100}
set1.add(1000)
set1.add(10000)
print(set1)

set1.discard(10)
print(set1)
if 100 in set1:
    set1.remove(100)
print(set1)

set1.clear()
print(set1)

set1 = {'Java', 'Python', 'C++', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}

print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))

fset1 = frozenset(set1)
print(fset1)
