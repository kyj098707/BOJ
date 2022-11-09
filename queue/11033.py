import sys
from collections import deque

iput = sys.stdin.readline
dq = deque()

n, l = map(int, input().split())

num_list = list(map(int, input().split()))

for index, num in enumerate(num_list):
    while dq and dq[-1][0] > num:
        dq.pop()
    while dq and dq[0][1] < index - l + 1:
        dq.popleft()

    dq.append([num, index])
    print(dq[0][0], end=" ")
