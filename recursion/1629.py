import sys
input = sys.stdin.readline

def recursion(a,b,c):
    if b == 1:
        return a % c
    val = recursion(a,b//2,c)
    val = val * val % c
    if b % 2 == 0:
        return val
    return a * val % c

a,b,c = map(int, input().split())
print(recursion(a,b,c))