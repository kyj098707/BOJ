def isprime(n):
    if n == 1:
        return 0
    for i in range(2, n + 1):
        if i * i > n:
            return 1
        if n % i == 0:
            return 0


n = int(input())
num_list = list(map(int, input().split()))
sum = 0
for num in num_list:
    sum += isprime(num)

print(sum)
