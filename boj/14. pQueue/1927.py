import heapq
import sys
input = sys.stdin.readline

n = int(input())

h = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h,num)

