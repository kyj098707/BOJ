n = int(input())

for i in range(n):
    star = "*" * (i + 1)
    blank = " " * (2 * (n - i - 1))
    print(star + blank + star)

for i in reversed(range(n - 1)):
    star = "*" * (i + 1)
    blank = " " * (2 * (n - i - 1))
    print(star + blank + star)
