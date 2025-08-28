s1 = 'hello, world'
s2 = "你好，世界！❤"
print(s1)
print(s2)

s3 = '\'hello, world!\''
s4 = '\\hello, world!\\'
print(s3)
print(s4)

s2 = r'\it \is \time \to \read \now'
print(s1)
print(s2)

s1 = 'hello' + ', ' + 'world'
print(s1)
s2 = '!' * 3
print(s2)
s1 += s2
print(s1)
s1 *= 3
print(s1)

print('wo' in s1)
print('wo' not in s1)

print(len(s1))

print(s1[4])
print(s1[24])

s = 'hello'
for elem in s:
    print(elem)

s1 = 'hello, world'
# 字符串首字母大写
print(s1.capitalize())
# 字符串每个单词首字母大写
print(s1.title())
print(s1.upper())
s2 = 'DOGE'
print(s2.lower())

print(s1.find('or'))
print(s1.index('or'))

print(s1.rfind('o'))
print(s1.startswith('he'))
print(s1.startswith('He'))
s2 = 'abc12345'
print(s2.isdigit())
print(s2.isalpha())
print(s2.isalnum())

print(s1.center(20, '*'))
print(s1.rjust(20))
print(s1.ljust(20))
print('33'.zfill(6))

a = 321
b = 123
print('%d * %d = %d' % (a, b, a * b))
print('{0} + {1} = {2}'.format(a, b, a + b))
print(f'{a} * {b} = {a * b}')

s1 = '   cwp714@126.com  '
print(s1.strip())
s2 = '~cwp~'
print(s2.lstrip('~'))
print(s2.rstrip('~'))

s = 'hello, good world'
print(s.replace('o',  '@'))
print(s.replace('o',  '@', 2))

s = 'I love you'
words = s.split()
print(words)
print('~'.join(words))
s = 'I!love!you'
words = s.split('!')
print(words)
s = '陈哥'
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))