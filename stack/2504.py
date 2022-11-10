import sys

input = sys.stdin.readline

gualhos = input().rstrip()
stack = [0]
result = 0
total = 1
# 괄호안에 들어 간 값들은 모두 연산 후 곱해주어야 함

operation_mode = 0
for i in range(len(gualhos)):
    if gualhos[i] == "(":
        total *= 2
        stack.append(gualhos[i])
    elif gualhos[i] == "[":
        total *= 3
        stack.append(gualhos[i])
    elif gualhos[i] == ")" and stack[-1] == "(":
        if gualhos[i - 1] == "(":
            result = result + total
        total //= 2
        stack.pop()
    elif gualhos[i] == "]" and stack[-1] == "[":
        if gualhos[i - 1] == "[":
            result = result + total
        total //= 3
        stack.pop()
    else:
        stack.append(gualhos[i])

if len(stack) != 1:
    print(0)
else:
    print(result)
