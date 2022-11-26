n = int(input())

for i in range(n):
    star = "*" * (2 * (n - i) - 1)
    blank = " " * i
    print(blank + star)
