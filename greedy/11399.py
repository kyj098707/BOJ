import sys

input = sys.stdin.readline

n = int(input())

num_list = list(map(int, input().split()))

total = 0
for i, num in enumerate(sorted(num_list)):
    total += num * (n - i)

print(total)
