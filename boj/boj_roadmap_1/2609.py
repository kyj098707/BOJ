a, b = map(int, input().split())
result1 = 0

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        result1 = i

print(result1)
print((a // result1) * (b // result1) * result1)
