import sys

input = sys.stdin.readline

num = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.sort()
B_list.sort(reverse=True)
total = 0
for i in range(num):
    total += A_list[i] * B_list[i]

print(total)
