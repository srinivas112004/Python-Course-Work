base_case=True
def func():
    if base_case:
        return
    func()

func()

def display(n):
    if n > 10:
        return
    print(n, end=' ')
    display(n + 1)

display(1)


def display(n):
    if n > 10:
        return
    display(n + 1)
    print(n, end=' ')

display(1)


def displaysum(n):
    if n == 0:
        return 0
    return n + displaysum(n - 1)

print(displaysum(8))


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(3))


def display(s, n):
    if n == len(s):
        return
    print(s[n])
    display(s, n + 1)

display("Python Programming", 0)


def display(s, n):
    if n == len(s):
        return
    display(s, n + 1)
    print(s[n])

display("Python Programming", 0)


def display(s, n, res):
    if n == len(s):
        return
    res += s[n]
    print(res)
    display(s, n + 1, res)

display("Python Programming", 0, "")


def display(s, inp, n):
    if n > len(s) - inp:
        return
    print(s[n:n + inp])
    display(s, inp, n + 1)

inp = int(input())
display("Python", inp, 0)


def disp(n):
    if n <= 0:
        return
    disp(n // 10)
    print(n % 10)

disp(987654)


def disp(n):
    if n <= 0:
        return 0
    return n % 10 + disp(n // 10)

print(disp(987654))

def countdigits(n,count):
    if n<=0:
        return count
    count+=1
    return countdigits(n//10,count)
print(countdigits(1234,0))