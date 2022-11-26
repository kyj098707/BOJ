import sys

input = sys.stdin.readline
## 멀리서 다칠 때 + 1 , 가까이서 다치면 + cnt
stack = []

gualhos = input().rstrip()

total = 0
cnt = 0
for gualho in gualhos:
    if gualho == "(":
        cnt += 1
        stack.append("(")
    if gualho == ")" and stack[-1] == "(":

        cnt -= 1
        total = total + cnt
        stack.append(")")
    elif gualho == ")" and stack[-1] == ")":
        cnt -= 1
        total = total + 1
        stack.append(")")

print(total)
