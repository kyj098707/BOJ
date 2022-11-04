n = int(input())

for i in range(n):
    blank = " " * (n - 1 - i)
    star = "*" * (2 * i + 1)
    print(blank + star)
