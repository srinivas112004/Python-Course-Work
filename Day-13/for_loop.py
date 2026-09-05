"""s="Python Programming"
for i in range(len(s)):
    if s[i] in "aeiouAEIOU":
        print(i,s[i])
"""
"""lst=[1,2,3,4,5,6,7]
s=0
for i in range(len(lst)):
    if lst[i]%2==0:
        s=s+i
        print(i,lst[i])
print(s)

import sys
n=int(sys.stdin.readline())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"Factorial of {n} is {fact}")"""


"""n=int(input("Enter the Number of students:"))
d={}
for i in range(n):
    name=input("Enter the Name : ")
    marks=float(input("Enter the Marks : "))
    d[name]=marks
max_marks=max(d.values())
min_marks=min(d.values())
for k , v in d.items():
    if v==max_marks:
        print(k,v)
    if v==min_marks:
        print(k,v)"""


n=int(input("Enter the no of products"))
lst=[]
for i in range(n):
    n=input("enter the product name : ")
    p=float(input("Enter the price :"))
    q=int(input("Enter the Quantity"))
    lst.append({"name":n,"price":p,"quantity":q})
print(lst)
s=0
for i in range(len(lst)):
    s=s+(lst[i]["price"]*lst[i]["quantity"])
print(f"Total Bill : ",s)







