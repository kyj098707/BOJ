import sys

input = sys.stdin.readline

n = int(input())

num_list = list(map(int, input().split()))

stack = [[-1, 1000001]]
result = [0] * n

for index, num in enumerate(num_list):
    while stack[-1][1] < num:
        result[stack[-1][0]] = num
        stack.pop()
    stack.append([index, num])


for i in stack[1:]:
    result[i[0]] = -1

for res in result:

    print(res, end=" ")
