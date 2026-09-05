# Pattern 1: Center Aligned Half Pyramid
#
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *

n = int(input())

for i in range(n):
    for j in range(n, i, -1):
        print(" ", end=" ")
    for k in range(i + 1):
        print("*", end=" ")
    print()


# Pattern 2: Inverted Center Aligned Half Pyramid
#
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *

n = int(input())

for i in range(n, 0, -1):
    for j in range(n, i, -1):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()


# Pattern 3: Hollow Square
#
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n - 1 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# Pattern 4: Hollow Square with Plus (+)
#
# * * * * *
# *   *   *
# * * * * *
# *   *   *
# * * * * *

n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n - 1 or j == n - 1 or i == n // 2 or j == n // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# Pattern 5: X Pattern
#
# *       *
#   *   *
#     *
#   *   *
# *       *

n = int(input())

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# Pattern 6: Letter A

n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or j == n - 1 or i == n // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# Pattern 7: Letter B

n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or j == n - 1 or i == n // 2 or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# Pattern 8: Letter C

n = int(input())

for i in range(n):
    if i == 0 or i == n - 1:
        print("*  " * n)
    else:
        print("*")
    print()


# Pattern 9: Letter D

n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n - 1 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# Pattern 10: Letter E

n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n // 2 or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# Pattern 11: Letter F

n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# Pattern 12: Letter G

n = int(input())
m = n // 2

for i in range(n):
    for j in range(n):
        if (
            i == 0 or
            j == 0 or
            (i == n - 1 and j <= m) or
            (j == m and i >= m) or
            (i == m and j >= m) or
            (j == n - 1 and i >= m)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# Pattern 13: Letter H

n = int(input())

for i in range(n):
    for j in range(n):
        if j == 0 or i == n // 2 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# Pattern 14: Letter I

n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or j == n // 2 or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# Pattern 15: Letter J

n = int(input())
m = n // 2

for i in range(n):
    for j in range(n):
        if i == 0 or j == n // 2 or (i == n - 1 and j <= m):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# Pattern 16: Letter K

n = int(input())
m = n // 2

for i in range(n):
    for j in range(n):
        if (
            j == 0 or
            (i == m and j <= m - 1) or
            (i + j == n - 1 and i <= m) or
            (i == j and i >= m)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# Pattern 17: Letter L

n = int(input())

for i in range(n):
    for j in range(n):
        if j == 0 or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# Pattern 18: Letter M

n = int(input())
m = n // 2

for i in range(n):
    for j in range(n):
        if (
            j == 0 or
            j == n - 1 or
            (i + j == n - 1 and i <= m) or
            (i == j and i <= m)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()