def display(n):
    n+=10
    print("Inside :",n)

n=10
display(n)
print("Outside :",n)
print("--------------------------------------------------------")

def display():
    print("Inside :",n)
n=10
display()
print("Outside : ",n)
print("--------------------------------------------------------")


def display():
    n=10
    print("Inside :",n)
display()
print("Outside : ",n)
print("--------------------------------------------------------")


def display():
    global n
    n+=10
    print("Inside : ",n)
n=10
display()
print("Outside : ",n)
print("--------------------------------------------------------")

def display():
    global n
    n="PFS"
    print("Inside : ",n)
n="JFS"
display()
print("Outside : ",n)
print("--------------------------------------------------------")

def display():
    n="JFS"
    def update():
        nonlocal n
        n="PFS"
        print("Updated Course : ",n)
    update()
    print("Final Course : ", n)
display()



