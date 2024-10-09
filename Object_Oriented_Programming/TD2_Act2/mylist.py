MyList = list()
l = MyList
l.append(1)
l.append(2)
l.append(3)
for e in l:
    print(e)
print(l[0])
print(l[-1])
l.map(lambda x: x * 2)
for e in l:
    print(e)
l2 = l.copy()
print(l == l2)