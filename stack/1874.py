import sys

input = sys.stdin.readline

n = int(input())
values = list(range(1, n + 1))
stack = [0]
cnt = 0
flag = True
available = True
result = []
target_vals = []
for _ in range(n):
    target_vals.append(int(input()))
count = 0
while flag:

    target_val = target_vals[count]
    count = count + 1

    if stack[-1] > target_val:
        print("No")
        flag = False
        available = False
    elif stack[-1] == target_val:
        result.append("-")
        stack.pop()
        if cnt == n and stack[-1] == 0:
            flag = False

    else:
        while stack[-1] != target_val:
            result.append("+")
            stack.append(values[cnt])
            cnt = cnt + 1
        result.append("-")
        stack.pop()

        if cnt == n and stack[-1] == 0:
            flag = False

if available:
    for res in result:
        print(res)
