Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name=input("Enter Your Name: ")
Enter Your Name: Srinivas
>>> name
'Srinivas'
>>> val=input("Enter a number : "))
SyntaxError: unmatched ')'
>>> val=input("Enter a number : ")
Enter a number : 1
>>> val
'1'
>>> int(val)
1
>>> val
'1'
>>> val=int(input("Enter the value : "))
Enter the value : 12
>>> val
12
>>> price=float(input("Enter the price:"))
Enter the price:45
>>> price
45.0
>>> names=input("Enter the names : ").split(" ")
Enter the names : C Java Python C#
>>> names
['C', 'Java', 'Python', 'C#']
>>> name=list(map(int,input("Enter the vaues: ").split()))
Enter the vaues: 1 2 3 4
>>> name
[1, 2, 3, 4]
>>> values=list(map(float,input("Enter the prices: ").split()))
Enter the prices: 1000 99.99 499.99
>>> values
[1000.0, 99.99, 499.99]
names=tuple(input("Enter the names : ").split(" "))
Enter the names : C Java Python C#
names
('C', 'Java', 'Python', 'C#')
values=tuple(map(int,input("Enter the vaues: ").split()))
Enter the vaues: 1 2 3 4 5
values
(1, 2, 3, 4, 5)
values=tuple(map(float,input("Enter the prices: ").split()))
Enter the prices: 100.99 156.99 45 
vlaues
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    vlaues
NameError: name 'vlaues' is not defined. Did you mean: 'values'?
values
(100.99, 156.99, 45.0)
names=set(input("Enter the names : ").split(" "))
Enter the names : c java python c#
names
{'c#', 'c', 'java', 'python'}
values=set(map(int,input("Enter the vaues: ").split()))
Enter the vaues: 1 2 3 4 5
values
{1, 2, 3, 4, 5}
values=set(map(float,input("Enter the prices: ").split()))
Enter the prices: 99.99 599.99 699.99 366
values
{99.99, 699.99, 366.0, 599.99}
v=list(map(int,input("Enter the vaues: ").strip("[]").split()))
Enter the vaues: [1,2,3,4,5]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    v=list(map(int,input("Enter the vaues: ").strip("[]").split()))
ValueError: invalid literal for int() with base 10: '1,2,3,4,5'
v=list(map(int,input("Enter the vaues: ").strip('[]').split()))
Enter the vaues: [1,2,3,4]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    v=list(map(int,input("Enter the vaues: ").strip('[]').split()))
ValueError: invalid literal for int() with base 10: '1,2,3,4'
v=list(map(int,input("Enter the vaues: ").strip('[]').split(',')))
Enter the vaues: [1,2,3,4,5]
v
[1, 2, 3, 4, 5]
names=set(input("Enter the names : ").split(" "))
C Java Python Node React
SyntaxError: multiple statements found while compiling a single statement
names=set(input("Enter the names : ").split())
Enter the names : c Java
names
{'Java', 'c'}
names.sort
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    names.sort
AttributeError: 'set' object has no attribute 'sort'
names.sort()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    names.sort()
AttributeError: 'set' object has no attribute 'sort'
list(names.sort())
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    list(names.sort())
AttributeError: 'set' object has no attribute 'sort'
a,b=[1,2]
a
1
b
2
a,b=(1,2)
a
1
b
2
email,password=input("Enter the Email and password: ").split()
Enter the Email and password: sample@gmail.com 123456
email
'sample@gmail.com'
password
'123456'
name,marks=input()
name,marks=input().split()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    name,marks=input()
ValueError: too many values to unpack (expected 2)
name,marks=input().split()
srinivas 99
name
'srinivas'
marks
'99'
e=eval(input())
1
e
1
e=eval(input())
Srinivas
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    e=eval(input())
  File "<string>", line 1, in <module>
NameError: name 'Srinivas' is not defined
e=eval(input())
12.55
e
12.55
e=eval(input())
"Srinivas"
e
'Srinivas'
e=eval(input())
[1,2,3,4,5,6]
e=eval(input())
(1,2,3,4)
e
(1, 2, 3, 4)
e=eval(input())
{1,2,3,4}
e
{1, 2, 3, 4}
e=eval(input())
{1:1,2:3,3:4}
e
{1: 1, 2: 3, 3: 4}
type(e)
<class 'dict'>
