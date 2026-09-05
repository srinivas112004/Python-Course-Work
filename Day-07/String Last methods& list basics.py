Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
c="string.py"
>>> c.startswith("s")
True
>>> c.endswith(".py")
True
>>> c.islower()
True
>>> c.isupper()
False
>>> c.istitle()
False
>>> "Titel".istitle()
True
>>> " ".isspace()
True
>>> "my_var".isidentifier()
True
>>> c.isalpha()
False
>>> c.isalnum()
False
>>> "hello12".isalnum()
True
>>> lst=[1,2,3,4]
>>> lst.insert(0,6)
>>> lst
[6, 1, 2, 3, 4]
>>> sorted(lst)
[1, 2, 3, 4, 6]
>>> sorted(lst,reverse=True)
[6, 4, 3, 2, 1]
>>> lst.extend(lst)
>>> lst
[6, 1, 2, 3, 4, 6, 1, 2, 3, 4]
>>> lst.append(lst)
>>> lst
[6, 1, 2, 3, 4, 6, 1, 2, 3, 4, [...]]
[6, 1, 2, 3, 4, 6, 1, 2, 3, 4, [...]]
[6, 1, 2, 3, 4, 6, 1, 2, 3, 4, [Ellipsis]]
lst.pop()
[6, 1, 2, 3, 4, 6, 1, 2, 3, 4]
for i in range(5):
    lst.pop()

4
3
2
1
6
lst
[6, 1, 2, 3, 4]
lst.reverse()
lst
[4, 3, 2, 1, 6]
type(lst)==list
True
#List Operations
l=[1,2,3,4]
m=[5,6,7,8]
l+m
[1, 2, 3, 4, 5, 6, 7, 8]
l[1]
2
l
[1, 2, 3, 4]
l[::-1]
[4, 3, 2, 1]
l[-1]
4
l[3]
4
