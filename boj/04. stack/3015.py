import sys

input = sys.stdin.readline

n = int(input())
stack = [[2**31 + 1, 0]]
total = 0
for _ in range(n):
    num = int(input())
    cnt = 1
    if num < stack[-1][0]:
        if len(stack) != 1:
            total = total + 1

    else:
        while num >= stack[-1][0]:

            if num == stack[-1][0]:
                cnt = stack[-1][1]
                total = total + cnt
                stack.pop()
                cnt = cnt + 1
            else:
                total = total + stack[-1][1]
                stack.pop()
        if len(stack) != 1:
            total = total + 1

    stack.append([num, cnt])


print(total)
