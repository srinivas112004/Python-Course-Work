Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('Built-in String Methods:')
Built-in String Methods:
s = 'Hare Krishna'
len(s)
12
ord('a')
97
ord('A')
65
chr(66)
'B'
chr(98)
'b'
min(s)
' '
max(s)
's'
sorted(s)
[' ', 'H', 'K', 'a', 'a', 'e', 'h', 'i', 'n', 'r', 'r', 's']
print('Case conversion methods:')
Case conversion methods:
s = 'Rupavani'
s
'Rupavani'
s.upper()
'RUPAVANI'
s.lower()
'rupavani'
s.title()
'Rupavani'
s.capitalize()
'Rupavani'
s = 'Dasari Rupavani'
s
'Dasari Rupavani'
s.upper()
'DASARI RUPAVANI'
s.lower()
'dasari rupavani'
s.title()
'Dasari Rupavani'
s.capitalize()
'Dasari rupavani'
s.swapcase()
'dASARI rUPAVANI'
print('Alignment and formating methods:')
Alignment and formating methods:
s = 'String is immutable'
s
'String is immutable'
s.center(40, '*')
'**********String is immutable***********'
c.ljust(40, '*')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    c.ljust(40, '*')
NameError: name 'c' is not defined
s.ljust(40, '*')
'String is immutable*********************'
s.rjust(40, '*')
'*********************String is immutable'
'7'.zfill(7)
'0000007'
'007'.zfill(2)
'007'
'007'.zfill(3)
'007'
print('Search and find methods:')
Search and find methods:

s = 'List is mutable'
s
'List is mutable'
s.fing('L')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    s.fing('L')
AttributeError: 'str' object has no attribute 'fing'. Did you mean: 'find'?
s.find('L')
0
s.find('s')
2
s.find('b')
12
s.find('z')
-1
s.rfind('s')
6
s.rfind('i')
5
s.rfind('z')
-1
s.index('s')
2
s.index('z')
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s.index('z')
ValueError: substring not found
s.count('s')
2
s.count('i')
2
s.count('z')
0
print('Replace and modify methods:')
Replace and modify methods:
s
'List is mutable'
s.replace('L', 'l')
'list is mutable'
s.replace('list', 'Tuple')
'List is mutable'
s
'List is mutable'
s.replace('List', 'Tuple')
'Tuple is mutable'
s.maketrans('aeiou', '12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
s.translate(s.maketrans('aeiou', '12345'))
'L3st 3s m5t1bl2'
s.translate(s.maketrans('aeiou', '*****'))
'L*st *s m*t*bl*'
print('Splitting and joining methods:')
Splitting and joining methods:
s
'List is mutable'
s.split()
['List', 'is', 'mutable']
s.split()
['List', 'is', 'mutable']
s
'List is mutable'
s.split(',')
['List is mutable']
'String-is-mutable'.split('-')
['String', 'is', 'mutable']
'List is mutable'.rsplit()
['List', 'is', 'mutable']
'List is mutable'.rsplit(' ', 1)
['List is', 'mutable']
'List is mutable'.split(' ', 1)
['List', 'is mutable']
>>> s = '''
... Python
... Programming
... Language
... '''
>>> s
'\nPython\nProgramming\nLanguage\n'
>>> s.splitlines()
['', 'Python', 'Programming', 'Language']
>>> ''.join(['', 'Python', 'Programming', 'Language'])
'PythonProgrammingLanguage'
>>> ' '.join(['', 'Python', 'Programming', 'Language'])
' Python Programming Language'
>>> '-'.join(['', 'Python', 'Programming', 'Language'])
'-Python-Programming-Language'
>>> s = 'Python-Programming-Language'.partition('-')
>>> s
('Python', '-', 'Programming-Language')
>>> 'Python.py'.partition('.')
('Python', '.', 'py')
>>> 'Python-Proogamming-Language'.rpartition('-')
('Python-Proogamming', '-', 'Language')
>>> 'Python.py.exe'.rpartition()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    'Python.py.exe'.rpartition()
TypeError: str.rpartition() takes exactly one argument (0 given)

>>> print('Whitespaces and trimming methods:')
Whitespaces and trimming methods:
>>> s = '         Hello          World           '
>>> s
'         Hello          World           '
>>> s.strip()
'Hello          World'
>>> s.lstrip()
'Hello          World           '
>>> s.rstrip()
'         Hello          World'
>>> print('Encoding and decoding:')
Encoding and decoding:
>>> b'Hello \xf0\x9f\x99\x82'.decode()
'Hello 🙂'
