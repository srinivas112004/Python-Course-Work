Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#strings
s=""
s
''
s="Srinivas"
s+=" K"
s
'Srinivas K'
s*10
'Srinivas KSrinivas KSrinivas KSrinivas KSrinivas KSrinivas KSrinivas KSrinivas KSrinivas KSrinivas K'
s**2
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s**2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> "()"*10
'()()()()()()()()()()'
>>> s
'Srinivas K'
>>> s[0]
'S'
>>> s[1]
'r'
>>> s[2]
'i'
>>> s[::}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> s[::}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> s[::]
'Srinivas K'
>>> s[0:5]
'Srini'
>>> s[::-1]
'K savinirS'
>>> s[::2]
'Siia '
>>> #slicing s[start:end:step] defalut values start->0 end->len(s) and step->1
>>> "s" in s
True
>>> "Sru" in s
False
>>> "Sri" in s
True
>>> "Sri" not in s
False
