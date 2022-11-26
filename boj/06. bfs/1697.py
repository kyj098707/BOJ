import sys
from collections import deque


n, k = map(int, input().split())
if n == k:
    print(0)
    exit()
visit = [0] * 222222


Q = deque()
Q.append(n)
dx = [-1, 1]
while len(Q):
    cur_pos = Q[0]
    Q.popleft()
    for dir in range(3):
        if dir == 2:
            nx = cur_pos * 2
        else:
            nx = cur_pos + dx[dir]

        if nx < 0 or nx >= 222222:
            continue
        if visit[nx]:
            continue
        if nx == k:
            print(visit[cur_pos] + 1)
            exit()

        visit[nx] = visit[cur_pos] + 1
        Q.append(nx)
