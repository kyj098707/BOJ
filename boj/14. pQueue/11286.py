import sys
import heapq
input = sys.stdin.readline


n = int(input())
h = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if not h:
            print(0)
        else:
            print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h,(abs(num),num))

