Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
float(a)
10.0
list(a)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
complex(a)
(10+0j)
tuple(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
str(a)
'10'
b=9.99
int(b)
9
complex(b)
(9.99+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
list(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
c=10+1j
int(c)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
list(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
str(c)
'(10+1j)'
tuple(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
str="Hello123"
str
'Hello123'
int(str)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int(str)
ValueError: invalid literal for int() with base 10: 'Hello123'
float(str)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    float(str)
ValueError: could not convert string to float: 'Hello123'
complex(str)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    complex(str)
ValueError: complex() arg is a malformed string
list(str)
['H', 'e', 'l', 'l', 'o', '1', '2', '3']
tuple(str))
SyntaxError: unmatched ')'
tuple(str)
('H', 'e', 'l', 'l', 'o', '1', '2', '3')
set(str)
{'e', '2', '3', 'l', '1', 'H', 'o'}
dict(str)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    dict(str)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
list=[1,2,3,4,5]
l=[1,2,3,4,5,6]
int(l)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
str(l)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    str(l)
TypeError: 'str' object is not callable
tuple(str)
('H', 'e', 'l', 'l', 'o', '1', '2', '3')
set(l)
{1, 2, 3, 4, 5, 6}
dict(l)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
t=(1,2,3,4,5)
int(t)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
>>> str(t)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    str(t)
TypeError: 'str' object is not callable
>>> complex(t)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
>>> list(t)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    list(t)
TypeError: 'list' object is not callable
>>> set(t)
{1, 2, 3, 4, 5}
>>> dict(t)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> s={1,2,3,4,5}
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
>>> float(s)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
>>> complex(s)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'set'
>>> list(s)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    list(s)
TypeError: 'list' object is not callable
>>> set(s)
{1, 2, 3, 4, 5}
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
d={"name":"Srinivas","Batch":63}
d
{'name': 'Srinivas', 'Batch': 63}
int(d)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(d)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(d)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    complex(d)
TypeError: complex() first argument must be a string or a number, not 'dict'
list(d)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    list(d)
TypeError: 'list' object is not callable
tuple(d)
('name', 'Batch')
set(d)
{'Batch', 'name'}
bol=True
int(bol)
1
float(bol)
1.0
complex(bol)
(1+0j)
list(bol)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    list(bol)
TypeError: 'list' object is not callable
set(bol)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    set(bol)
TypeError: 'bool' object is not iterable
tuple(bol)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    tuple(bol)
TypeError: 'bool' object is not iterable
dict(bol)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    dict(bol)
TypeError: 'bool' object is not iterable
