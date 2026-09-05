# Pattern 1: Rectangle of Stars (10 x 5)
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

for i in range(10):
    for j in range(5):
        print("*", end=" ")
    print()


# Pattern 2: Square of Stars (5 x 5)
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

for row in range(5):
    for col in range(5):
        print("*", end=" ")
    print()


# Pattern 3: Row Number Pattern
# 0 0 0 0 0
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4

for row in range(5):
    for col in range(5):
        print(row, end=" ")
    print()


# Pattern 4: Square of '&'
# & & & & &
# & & & & &
# & & & & &
# & & & & &
# & & & & &

for row in range(5):
    for col in range(5):
        print("&", end=" ")
    print()


# Pattern 5: Row + Column Sum Pattern
# 0 1 2 3 4
# 1 2 3 4 5
# 2 3 4 5 6
# 3 4 5 6 7
# 4 5 6 7 8

for row in range(5):
    for col in range(5):
        print(row + col, end=" ")
    print()


# Pattern 6: Alternate Column Binary Pattern
# 0 1 0 1 0
# 0 1 0 1 0
# 0 1 0 1 0
# 0 1 0 1 0
# 0 1 0 1 0

for row in range(5):
    for col in range(5):
        if col % 2 == 0:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()


# Pattern 7: Alternate Column Binary Pattern (Same as Above)
# 0 1 0 1 0
# 0 1 0 1 0
# 0 1 0 1 0
# 0 1 0 1 0
# 0 1 0 1 0

for row in range(5):
    for col in range(5):
        if col % 2 == 0:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()


# Pattern 8: Checkerboard Binary Pattern
# 0 1 0 1 0
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1
# 0 1 0 1 0

for row in range(5):
    for col in range(5):
        if (row + col) % 2 == 0:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()


# Pattern 9: Left Half Pyramid
# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")
    print()


# Pattern 10: Inverted Left Half Pyramid
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()