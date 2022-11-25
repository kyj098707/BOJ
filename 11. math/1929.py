def isprime(n):
    if n == 1:
        return 0
    for i in range(2, n + 1):
        if i * i > n:
            return 1
        if n % i == 0:
            return 0


a, b = map(int, input().split())
for num in range(a, b + 1):
    if isprime(num):
        print(num)
