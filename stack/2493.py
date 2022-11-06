import sys

input = sys.stdin.readline

stack = [[199999999, -1]]

_ = int(input())
result_list = []
top_list = list(map(int, input().split()))

for index, top in enumerate(top_list):
    while top > stack[-1][0]:
        stack.pop()
    result_list.append(stack[-1][1] + 1)
    stack.append([top, index])

for i in result_list:
    print(i, end=" ")
