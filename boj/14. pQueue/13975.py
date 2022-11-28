import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    num_list = list(map(int,input().split()))
    h = []
    for num in num_list:
        heapq.heappush(h, num)
    result = 0
    while len(h) > 1:
        a = heapq.heappop(h)
        b = heapq.heappop(h)
      
        total = a+b
        result += total
        heapq.heappush(h,total)
       
    print(result)