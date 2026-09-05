#List comprehension
res=[i for i in range(1,11)]
print(res)

n=12
res=[i for i in range(1,n+1) if n%i==0]
print(res)

r=[12,23,45,687,34,123,34,12,43,90]
res=[i if i%2==0 else 0 for i in r]
print(res)

r=[[12,23,45],[687,34,123],[34,43,90]]
res=[j for i in r for j in i if j%2==0]
print(res)

res=[[j for j in range(1,4)] for i in range(3) ]
print(res)

#Set comprehension
res={i for i in range(1,11)}
print(res)

n=12
res={i for i in range(1,n+1) if n%i==0}
print(res)

r=[12,23,45,687,34,123,34,12,43,90]
res={i if i%2==0 else 0 for i in r}
print(res)

r=[[12,23,45],[687,34,123],[34,43,90]]
res={j for i in r for j in i if j%2==0}
print(res)

l=[int(input(f"Enter the number -{i+1}:")) for i in range(10)]
print(l)

names=[input(f"Enter the student name -{i+1}:") for i in range(10)]
print(names)

# Dictionary comprehension
names={input("Enter the student name :"):float(input("Enter the Student Marks :")) for i in range(5)}
print(names)
res={i:i*i for i in range(1,6)}
print(res)