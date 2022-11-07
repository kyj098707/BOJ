import sys
from collections import deque

input = sys.stdin.readline

dq = deque()

n = int(input())

for i in range(1, n + 1):
    dq.append(i)

while len(dq) != 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])
