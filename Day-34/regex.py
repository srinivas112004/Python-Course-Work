from re import Pattern
import re

# pattern =r'[a-z]'
# text='codegnan'

# res=re.match(pattern,text)

# print(res.group() if res else "Pattern not found")



# pattern =r'[0-9]'
# text='codegnan2026'

# res=re.search(pattern,text)

# print(res.group() if res else "Pattern not found")



# pattern =r'[0-9]'
# text='codegnan 2026 python version 3.14'

# res=re.findall(pattern,text)

# print(res)


# pattern =r'[0-9]'
# text='codegnan 2026 python version 3.14'

# res=re.finditer(pattern,text)

# for i in res:
#     print(i.group(),i.start())


# pattern =r'[0-9]{10}'
# text='6301548779'

# res=re.fullmatch(pattern,text)

# print(res.group() if res else "Pattern not found")

# pattern =r'[,(#]'
# text='Java,Python(html#css'

# res=re.split(pattern,text)

# print(res)

# pattern =r'[a-z]'
# text='Python version 3.14 , batch-63'

# res=re.sub(pattern,"*",text)

# print(res)

# pattern =r'e.t'
# text='e@t eaat eat eet ect Egfhject hgjeokl'

# res=re.findall(pattern,text)

# print(res)


# pattern =r'^(91)'
# text='919876543210'

# res=re.findall(pattern,text)

# print(res)


# pattern =r'0$'
# text='919876543210'

# res=re.findall(pattern,text)

# print(res)

# pattern=r'to*'
# text='to tdfghjk too tooo tooooooo'
# res=re.findall(pattern,text)

# print(res)


# pattern=r'to+'
# text='to tdfghjk too tooo tooooooo'
# res=re.findall(pattern,text)

# print(res)



# pattern=r'91|0'
# text='05678'

# res=re.findall(pattern,text)

# print(res)



pattern=r'[aeiouAEIOU]'
text='codegnan programming'

res=re.findall(pattern,text)

print(res)