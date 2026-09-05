from re import Pattern
import re
# fullname=input("Enter the full name :")
# pattern=r'^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$'
# res=re.fullmatch(pattern,fullname)
# print("Valid full name" if res else "invalid full name")

# email=input("Enter the email : ")
# pattern=r'^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$'
# res=re.fullmatch(pattern,email)
# print("Valid email" if res else "invlaid email")


# phone_no=input("Enter the Phone number : ")
# pattern=r'^(?:\+91|0)?[6-9]\d{9}$'
# res=re.fullmatch(pattern,phone_no)
# print("Valid phone number" if res else "invlaid  phone number")


import re

# password = input("Enter your password: ")

# pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@$!%?&])[A-Za-z0-9@$!%?&]{8,}$'

# res = re.fullmatch(pattern, password)

# print("Valid password" if res else "Invalid password")

# username=input()
# Pattern=r'^[A-Za-z0-9]{5,15}'
# res=re.fullmatch(Pattern,username)
# print("Valid Username" if res else "Invalid Username")

adhar=input()
Pattern=r'\d{4} \d{4} \d{4}'
res=re.fullmatch(Pattern,adhar)
print("Valid adhar" if res else "Invalid adhar")

