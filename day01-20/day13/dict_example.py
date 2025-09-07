xinhua = {
    '麓': '山脚下',
    '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
    '蕗': '甘草的别名',
    '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
}

print(xinhua)

person = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': '成都市武侯区科华北路62号1栋101',
    'tel': '13122334455',
    'emergence contact': '13800998877'
}
print(person)

person = dict(name = '王大锤', age=55, height=168, weight=60, addr='成都市武侯区科华北路62号1栋101')
print(person)

items1 = dict(zip('ABCDE', '12345'))
print(items1)

items2 = {x: x ** 3 for x in range(1, 6)}
print(items2)

for x in person:
    print(x)
    print(person.get(x))

person = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': ['成都市武侯区科华北路62号1栋101', '北京市西城区百万庄大街1号'],
    'car': {
        'brand': 'BMW X7',
        'maxSpeed': '250',
        'length': 5170,
        'width': 2000,
        'height': 1835,
        'displacement': 3.0
    }
}
print(person)

person = {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}

# 成员运算
print('name' in person)  # True
print('tel' in person)   # False

# 索引运算
print(person['name'])
print(person['addr'])
person['age'] = 25
person['height'] = 178
person['tel'] = '13122334455'
person['signature'] = '你的男朋友是一个盖世垃圾，他会踏着五彩祥云去迎娶你的闺蜜'
print(person)

# 循环遍历
for key in person:
    print(f'{key}:\t{person[key]}')

person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.get('name'))
print(person.get('name1'))

print(person.keys())
print(person.values())
print(person.items())

for k, v in person.items():
    print(f'{k}:\t{v}')
person2 = {'age': 45, 'addr': '成都市武侯区科华北路62号1栋101'}
person |= person2
print(person)

sentence = input('请输入一段话：')
counter = {}
for c in sentence:
    if 'A' <= c <= 'Z' or 'a' <= c <= 'z':
        counter[c] = counter.get(c, 0) + 1
sorted_keys = sorted(counter, key = counter.get, reverse=True)
for k in sorted_keys:
    print(f'{k}出现了 {counter[k]} 次.')

stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
stocks2 = {key: value for key, value in stocks.items() if value > 100}
print(stocks2)