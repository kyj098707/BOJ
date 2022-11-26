n = int(input())

for i in range(n):
    blank = " " * i
    star = "*" * (n - i)
    print(blank + star)
