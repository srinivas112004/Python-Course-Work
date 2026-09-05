def display(n):
    n += 10
    print("Inside: ", n)

n = 10
display(n)
print("Outside: ", n)

def display(n):
    n += 10.9
    print("Inside: ", n)

n = 10.5
display(n)
print("Outside: ", n)

def display(n):
    n += ' Krishna'
    print("Inside: ", n)

n = 'Hare'
display(n)
print("Outside: ", n)

def display(n):
    n += (1, 2, 3, 4)
    print("Inside: ", n)

n = (1, 2, 3)
display(n)
print("Outside: ", n)

def display(n):
    n = False
    print("Inside: ", n)

n = True
display(n)
print("Outside: ", n)

def display(n):
    n.append(10)
    print("Inside: ", n)

n = [1, 2, 3, 4, 5]
display(n)
print("Outside: ", n)

def display(n):
    n.add(10)
    print("Inside: ", n)

n = {1, 2, 3}
display(n)
print("Outside: ", n)

def display(n):
    n[5] = 8
    print("Inside: ", n)

n = {1: 2, 3: 4}
display(n)
print("Outside: ", n)