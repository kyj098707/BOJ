import sys

input = sys.stdin.readline
from collections import deque

# F최고층 S현재층 G목표층 U올라가는거 D내려가는거
F, S, G, U, D = map(int, input().split())
if S == G:
    print(0)
    exit()
visit = [0] * (F + 1)
dx = [U, D * -1]
Q = deque()
Q.append(S)
visit[S] = 1

while len(Q):
    cur_x = Q[0]
    Q.popleft()

    for dir in range(2):
        nx = cur_x + dx[dir]
        if nx <= 0 or nx > F:
            continue
        if visit[nx]:
            continue

        if nx == G:
            print(visit[cur_x])
            exit()
        visit[nx] = visit[cur_x] + 1
        Q.append(nx)

print("use the stairs")
