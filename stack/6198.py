import sys
input = sys.stdin.readline

n = int(input())
rooftop_stack = [1000000001]
total = 0
cnt = 0
for _ in range(n):
    rooftop = int(input())

    while rooftop >= rooftop_stack[-1]:
        rooftop_stack.pop()
        cnt = cnt - 1
        #print(rooftop_stack)
    
    total = total + cnt
    rooftop_stack.append(rooftop)
    cnt = cnt + 1
print(total)
