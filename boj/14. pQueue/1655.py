import heapq
import sys
input = sys.stdin.readline

n = int(input())
r_h = []
l_h = []
for _ in range(n):
    num = int(input())

    if len(r_h) == len(l_h):
        heapq.heappush(r_h,-1 * num)
    else:
        heapq.heappush(l_h,num)
    if r_h and l_h and r_h[0] * -1 > l_h[0]:
        r = heapq.heappop(r_h) * -1
        l = heapq.heappop(l_h)

        heapq.heappush(r_h,-l)
        heapq.heappush(l_h,r)
    
    print(r_h[0] * -1)