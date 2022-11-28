import sys
import heapq
input = sys.stdin.readline

n = int(input())
h = []

for _ in range(n):
    card_n = int(input())
    heapq.heappush(h,card_n)
result = 0
while len(h) >= 2:
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    shuffle = a+b
    result += shuffle
    heapq.heappush(h,shuffle)
    
print(result)