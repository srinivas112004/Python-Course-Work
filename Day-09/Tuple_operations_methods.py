Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t=()
t=type(t)
type(t)
<class 'type'>
t=tuple()
type(t)
<class 'tuple'>
t=(10)
type(t)
<class 'int'>
print('TUPLE OPERATIONS:')
TUPLE OPERATIONS:
a=(1,2)
b=(3,4)
a+b
(1, 2, 3, 4)
a*3
(1, 2, 1, 2, 1, 2)
a[1]
2
a[:1]
(1,)
>>> 2 in a
True
>>> 3 not in a
True
>>> len(a)
2
>>> max(a)
2
>>> min(a)
1
>>> sum(a)
3
>>> sorted(a)
[1, 2]
>>> a.count(2)
1
>>> a.count(3)
0
>>> a.index(2)
1
>>> a.index(3)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.index(3)
ValueError: tuple.index(x): x not in tuple
>>> a=(10,20,30)
>>> a
(10, 20, 30)
>>> data=(10,20,30)
>>> a,b,c=data
>>> a
10
>>> b
20
>>> c
30
>>> data=10,20,30
>>> data
(10, 20, 30)
>>> data = ((1, 2), (3, 4))
>>> data[1]
(3, 4)
>>> data[1][0]
3
>>> data = (10, [20, 30], 40)
>>> data[1].append(50)
>>> data
(10, [20, 30, 50], 40)
