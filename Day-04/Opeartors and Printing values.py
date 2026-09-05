Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
a//b
2
a**b
10240000000000
a%b
0
 a<b
 
SyntaxError: unexpected indent
a<b
False
a>b
True
a<=b
False
a>=b
True
a!=b
True
a==b
False
c=10
c+=10
c
20
c=c+10
c
30
c-=10

c
20
c*=10
c
200
c//2=2
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
c//=2
c
100
c**=2
c
10000
True and True
True
True and False
False
n=10
not True
False
n%2==0
True
n%3==0
False
n%2==0 and n%3==0
False
n%2==0 or n%3==0
True
not n<5
True
True
True
#Membership Operators
s="Srinivas"
'S' in s
True
'r' in s
True
'o' in s
False
'U' not in s
True
l=list(1,2,3)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    l=list(1,2,3)
TypeError: list expected at most 1 argument, got 3
l=list((1,2,3))
l
[1, 2, 3]
1 in l
True
2 in l
True
5 in l
False
3 not in l
False
9 not in l
True
t=tuple((1,2,3))
t
(1, 2, 3)
1 in t
True
2 in t
True
3 in t
True
4 in t
False
2 not in t
False
s={1,2,3,4,5}
1 in s
True
2 in s
True
3 not in s
False
8 not in s
True
d={
    "Name":"Srinivas",
    "Batch":63
  }
d
{'Name': 'Srinivas', 'Batch': 63}
"Name" in d
True
"Srinivas" in d
False
"Batch" in d
True
63 not in d
True
63 in d
False
#Identity Operators
l=[1,2,3,4]
m=[1,2,3,4]
l is m
False
l is not m
True
n=l
id(l) id(n)
SyntaxError: invalid syntax
id(l)
2307446914048
id(n)
2307446914048
n is l
True
l is not n
False
#Mutable and Immuatable dataypes
a=10
id(a)
140722714757848
a+=1
id(a)
140722714757880
lst=[1,2,3,4]
id(lst)
2307446942016
lst.append(2)
lst
[1, 2, 3, 4, 2]
id(lst)
2307446942016
s={1,2,3,4}
id(s)
2307442094624
s.add(5)
s
{1, 2, 3, 4, 5}
id(s)
2307442094624
f={
    "Name":"Srinivas",
    "Batch":63
    }
f
{'Name': 'Srinivas', 'Batch': 63}
f.update("Rollno":32)
SyntaxError: invalid syntax
f.update({"Rollno":32})
f
{'Name': 'Srinivas', 'Batch': 63, 'Rollno': 32}
id(f)
2307446943168
~-45
44
#Bitwise opertors
9&8
8
9|8
9
9>>2
2
9<<2
36
~9
-10
~0
-1
print(lst)
[1, 2, 3, 4, 2]
>>> #print Statements
>>> a=10
>>> b=10.3
>>> c="code"
>>> print(a,b,c)
10 10.3 code
>>> print("Value of a is \t",a)
Value of a is 	 10
>>> print(a,b,c)
10 10.3 code
>>> print(a,b,c,sep=" ")
10 10.3 code
>>> print(a,b,c,sep='')
1010.3code
>>> print(a,b,c,sep="\n")
10
10.3
code
>>> print(a,b,c,sep="\t")
10	10.3	code
>>> print(a,b,c,sep='\t')
10	10.3	code
>>> print(a,b,c,sep='\t',end='@')
10	10.3	code@
>>> print(a,b,c,sep="\t",end="\n\n")
10	10.3	code

>>> print(f"a={a} b={b} c={c}")
a=10 b=10.3 c=code
>>> print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=10.300000 c=code
>>> print("a={} b={} c={}".format(a,b,c))
a=10 b=10.3 c=code
>>> print("a={1} b={0} c={2}".format(a,b,c))
a=10.3 b=10 c=code
