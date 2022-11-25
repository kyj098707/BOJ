n = int(input())

for i in range(n):
    blank = " " * (n - 1 - i)
    star = "*" * (2 * i + 1)
    print(blank + star)
for i in range(n - 1):
    blank = " " * (i + 1)
    star = "*" * (2 * (n - i - 2) + 1)
    print(blank + star)
