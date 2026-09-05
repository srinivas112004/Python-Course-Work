c='strings.py'
c.startswith('str')
True
c.startswith('python')
False
c.endswith('python')
False
c.endswith('py')
True
c.islower()
True
c.isupper()
False
'PYTHONV13'.isupper()
True
c.isalpha()
False
c.isalnum()
False
's123'.isalnum()
True
's,123'.isalnum()
False
'      '.isspace()
True
'h     '.isspace()
False
>>> 'this is title'.istitle()
False
>>> 'This Is Title'.istitle()
True
>>> 'my@var'.isidentifer()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    'my@var'.isidentifer()
AttributeError: 'str' object has no attribute 'isidentifer'. Did you mean: 'isidentifier'?
>>> 'my@var'.isidentifier()
False
>>> 'my_var'.isidentifier()
True
>>> l=[]
>>> l=list[]
SyntaxError: invalid syntax
>>> l=list()
>>> l=[1,12.3,(2+3j),'str',[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},none,True]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    l=[1,12.3,(2+3j),'str',[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},none,True]
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> l=[1,12.3,(2+3j),'str',[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},None,True]
>>> l=[1,1,1,1]
>>> l
[1, 1, 1, 1]
>>> type(l)
<class 'list'>
>>> l=[1,2,3,4]
>>> m=[5,6,7]
>>> l+m
[1, 2, 3, 4, 5, 6, 7]
>>> m*3
[5, 6, 7, 5, 6, 7, 5, 6, 7]
>>> l
[1, 2, 3, 4]
>>> l[3]
4
>>> l[-3]
2
>>> l[-1]
4
>>> l[1:]
[2, 3, 4]
>>> l[:2]
[1, 2]
>>> l[::-1]
[4, 3, 2, 1]
