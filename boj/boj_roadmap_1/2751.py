import sys

input = sys.stdin.readline

# python 정렬은 n logn
n = int(input())
num_list = []
for _ in range(n):
    num_list.append(int(input()))

for num in sorted(num_list):
    print(num)
