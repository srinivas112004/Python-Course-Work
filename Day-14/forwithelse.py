for i in range(1,10):
    if i==15:
        break
    print(i,end=" ")
else:
    print("End of th Loop")
    

pin=1234
for _ in range(5):
    epin=int(input("Enter the Pin : "))
    if pin==epin:
        print("Phone Unlocked")
        break
    else:
        print("Invalid Pin")
else:
    print("Try again after 30 sec..")

n=int(input("Enter the number : "))
print("Factors  :",end=" ")
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")

n=int(input("Enter a number: "))
if n<=1:
    print("Not a Prime")
else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print("Not a prime")
            break  
    else:
        print("Prime Number ")

d={}
t=0
while True:
    prod=input("Enter Product : ")
    if prod=="exit" or prod=="Exit":
        break
    else:
        price=float(input("Enter Price : "))
        d[prod]=price
        t+=price
print(d)
print("Bill : ",t)

i=0
while i<=10:
    i+=1
    if i==15:
        break
    print(i)
else:
    print("End of the loop")