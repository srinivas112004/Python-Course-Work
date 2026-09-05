with open('pfs-63.txt', 'r') as f:
    content = f.read()
    print(content)
    f.seek(0)
    print(f.readline())
    f.seek(0)
    print(f.readlines())

with open('pfs-63.txt', 'w+') as f:
    f.write("Hi Hello Wlelcome")
    f.seek(0)
    content = f.read()
    print(content)

with open('pfs-63.txt', 'a+') as f:
    
    f.write(" This is Python")
    f.seek(0)
    content = f.read()
    print(content)