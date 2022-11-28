import sys
import heapq

input = sys.stdin.readline
n = int(input())
nums=[]
temps=[0]*(n+1)
for _ in range(n):
    deadline, value = map(int, input().split())
    nums.append((deadline,value))

nums = sorted(nums)
heaps=[]

for num in nums:
    heapq.heappush(heaps, num[1])
    if(num[0] < len(heaps)):
        heapq.heappop(heaps)
print(sum(heaps))