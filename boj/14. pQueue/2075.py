import sys
import heapq

input = sys.stdin.readline

n = int(input())
h = []
for i in range(n):
    tmp = list(map(int, input().split()))
    if i == 0:
        for t in tmp:
            heapq.heappush(h,t)
    else:
        for t in tmp:
            if t > h[0]:
                heapq.heappop(h)
                heapq.heappush(h,t)    
print(h[0])