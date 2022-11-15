import sys

input = sys.stdin.readline

from collections import deque

MAX_LEN = 200010

n, k = map(int, input().split())
Q = deque()
if n == k:
    print(0)
    quit()

visit = [0] * MAX_LEN
dx = [1, -1]

Q.append(n)
visit[n] = 1

while Q:
    cur_x = Q.popleft()

    if 2 * cur_x < MAX_LEN and visit[2 * cur_x] == 0:
        visit[2 * cur_x] = visit[cur_x]
        Q.appendleft(2 * cur_x)

    for dir in range(2):
        nx = cur_x + dx[dir]

        if nx < 0 or nx >= MAX_LEN or visit[nx] != 0:
            continue
        visit[nx] = visit[cur_x] + 1
        Q.append(nx)


print(visit[k] - 1)
