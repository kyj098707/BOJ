import sys

input = sys.stdin.readline

num = int(input())
rope_list = []
for _ in range(num):
    rope_list.append(int(input()))

rope_list.sort()
mx = 0
for i, rope in enumerate(rope_list):
    mx = max(mx, rope * (num - i))

print(mx)
