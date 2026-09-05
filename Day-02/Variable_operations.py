Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> A=20
>>> a
10
>>> A
20
>>> a=10
>>> a=b=c=10
>>> a,b,c=10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> a,b=b,a
>>> a
20
>>> b
10
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a
NameError: name 'a' is not defined. Did you mean: 'A'?
