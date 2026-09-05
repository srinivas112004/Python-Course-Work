
>>> l=[1,2,3,4,5]
>>> l=[10,9,ArithmeticError 6,1,2,3,4]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> l=[10,9, 6,1,2,3,4]
>>> l
[10, 9, 6, 1, 2, 3, 4]
>>> id(l)
2315801842048
>>> l.append(12)
>>> l
[10, 9, 6, 1, 2, 3, 4, 12]
>>> l.append(14)
>>> l
[10, 9, 6, 1, 2, 3, 4, 12, 14]
>>> id(l)
2315801842048
>>> l.insert(1,13)
>>> l
[10, 13, 9, 6, 1, 2, 3, 4, 12, 14]
>>> l.extend([52,32,42])
>>> l
[10, 13, 9, 6, 1, 2, 3, 4, 12, 14, 52, 32, 42]
>>> id(l)
2315801842048
>>> l[3]
6
>>> l[3]=60
>>> l
[10, 13, 9, 60, 1, 2, 3, 4, 12, 14, 52, 32, 42]
>>> l[5]=20
>>> l
[10, 13, 9, 60, 1, 20, 3, 4, 12, 14, 52, 32, 42]
>>> id(l)
2315801842048
>>> l.pop()
42
>>> l
[10, 13, 9, 60, 1, 20, 3, 4, 12, 14, 52, 32]
>>> l.pop()
32
>>> l
[10, 13, 9, 60, 1, 20, 3, 4, 12, 14, 52]
>>> l.pop(1)
13
>>> l
[10, 9, 60, 1, 20, 3, 4, 12, 14, 52]
>>> l.pop(4)
20
l
[10, 9, 60, 1, 3, 4, 12, 14, 52]
l.remove(4)
l
[10, 9, 60, 1, 3, 12, 14, 52]
del l[1]
l
[10, 60, 1, 3, 12, 14, 52]
l.clear()
l
[]
id(l)
2315801842048
l=[10,9,1,20,3,12,14]
l
[10, 9, 1, 20, 3, 12, 14]
max(l)
20
min(l)
1
sorted(l)
[1, 3, 9, 10, 12, 14, 20]
l
[10, 9, 1, 20, 3, 12, 14]
l.reverse()
l
[14, 12, 3, 20, 1, 9, 10]
l.sort()
l
[1, 3, 9, 10, 12, 14, 20]
l.sort(reverse=True)
l
[20, 14, 12, 10, 9, 3, 1]
sum(l)
69
l=[1,2,3]
m=[1,2,3]
l
[1, 2, 3]
n=l
n.append(4)
n
[1, 2, 3, 4]
l
[1, 2, 3, 4]
m=l.copy()
m
[1, 2, 3, 4]
m.append(10)
m
[1, 2, 3, 4, 10]
l
[1, 2, 3, 4]
all([0,'',[],(),set(),{},False])
False
all([1,'',[],(),set(),{},False])
False
any([1,'',[],(),set(),{},False])
True
l
[1, 2, 3, 4]
l.index(3)
2
l.index(5)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    l.index(5)
ValueError: 5 is not in list
lo
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    lo
NameError: name 'lo' is not defined. Did you mean: 'l'?
l
[1, 2, 3, 4]
l.count(3)
1
l.count(5)
0
l
[1, 2, 3, 4]
l=[[1,2,3,4],[5,6,7,8]
   l
   
SyntaxError: '[' was never closed
l=[[1,2,3,4],[5,6,7,8]]
   
l
   
[[1, 2, 3, 4], [5, 6, 7, 8]]
l[0]
   
[1, 2, 3, 4]
l[1]
   
[5, 6, 7, 8]
l[0][2]
   
3
l[1][3]
   
8
l[-1][-1]
   
8
l[::][::]
   
[[1, 2, 3, 4], [5, 6, 7, 8]]
#Tuple operations
   
t=()
   
