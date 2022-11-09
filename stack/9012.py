import sys
input = sys.stdin.readline

T = int(input())
gualho_list = ['(',')']
for _ in range(T):
    stack = [0]
    gualhos = input().rstrip()

    for gualho in gualhos:
        if (stack[-1] == gualho_list[0] and gualho == gualho_list[1]):
            stack.pop()
        else:
            stack.append(gualho)
    
    if len(stack) == 1:
        print("YES")
    else:
        print("NO")