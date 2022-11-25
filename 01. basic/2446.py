n = int(input())

for i in range(n):
    blank = " " * (i)
    star = "*" * (2 * (n - i) - 1)
    print(blank + star)

for i in reversed(range(n - 1)):
    blank = " " * (i)
    star = "*" * (2 * (n - i) - 1)
    print(blank + star)
