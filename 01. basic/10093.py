a, b = map(int, input().split())

if abs(a - b) <= 1:
    print(0)
elif b > a:
    print(b - a - 1)
    for result in range(a + 1, b - 1):
        print(result, end=" ")

    print(b - 1)
else:
    print(a - b - 1)
    for result in range(b + 1, a - 1):
        print(result, end=" ")

    print(a - 1)
