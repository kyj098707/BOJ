import sys

input = sys.stdin.readline

stack = [199999999]
result_list = []
top_list = list(map(int, input().split()))

for top in top_list():
    while top > stack[-1]:
        stack.pop()
    result_list.append(len(stack) - 1)

print(result_list)
