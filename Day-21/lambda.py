from functools import reduce

greater = lambda x, y: x if x > y else y
print(greater(2, 4))

greet = lambda name: f"Hello {name}"
print(greet("Ram"))

ev_od = lambda n: "Even" if n % 2 == 0 else "Odd"
print(ev_od(4))

avg = lambda a, b, c: (a + b + c) / 3
print(avg(1, 2, 3))

gst = lambda price: price + price * 0.18
print(gst(1000))

prices = [10, 20, 30, 40]
print(list(map(lambda p: p + p * 0.18, prices)))

names = ["c", "java", "python", "gO", "flutter"]
print(list(map(lambda name: name.title(), names)))

prices = [10, 20, 30, 40]
print(list(map(lambda p: p - p * 0.30, prices)))

print(list(filter(lambda p: p > 10, prices)))
print(list(filter(lambda n: len(n) > 5, names)))

print(reduce(lambda acc, p: acc + p, prices))

print(reduce(lambda res, n: res + " " + n, names))

products = {
    "sugar": 60,
    "salt": 50,
    "eggs": 120,
    "Cooking oil": 120,
    "bread": 45
}

print(dict(sorted(products.items(), key=lambda i: i[1])))

