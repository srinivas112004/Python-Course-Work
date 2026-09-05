def retrivedata():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in data:
        yield i

reels = retrivedata()
while True:
    status = eval(input("Enter True or False :"))
    if status:
        print(next(reels))
    else:
        break


def even():
    i = 0
    while True:
        i += 2
        yield i

n = 50
res = even()
for i in range(n):
    print(next(res))


n = int(input())
gen = (x for x in range(1, n + 1) if n % x == 0)
for factor in gen:
    print(factor)


def Prime(n):
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            yield i

n = int(input())
for p in Prime(n):
    print(p)