a = [2,3,4,5,6,7]
print(a)
a.append('Python')
print(a[0])
print(a[-1])
print(a[2:4])
print('Length is {}'.format(len(a)))
print('6 has {} index'.format(a.index(6)))
a.remove('Python')
print(a)