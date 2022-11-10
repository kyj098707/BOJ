import sys
from collections import deque

input = sys.stdin.readline

num_y, num_x = map(int, input().split())
visit = [[0] * num_y for _ in range(num_x)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

tomato_farm = []
Q = deque()
for _ in range(num_x):
    tomato_farm.append(list(map(int, input().split())))

for i in range(num_x):
    for j in range(num_y):
        if tomato_farm[i][j] == 1:
            Q.append((i, j))
            visit[i][j] = 1

while len(Q):
    cur_x = Q[0][0]
    cur_y = Q[0][1]
    Q.popleft()
    for dir in range(4):
        nx = cur_x + dx[dir]
        ny = cur_y + dy[dir]

        if nx < 0 or ny < 0 or nx >= num_x or ny >= num_y:
            continue
        if tomato_farm[nx][ny] == -1 or visit[nx][ny] != 0:
            continue
        Q.append((nx, ny))
        visit[nx][ny] = visit[cur_x][cur_y] + 1

mx = 0
result = 0
for i in range(num_x):
    for j in range(num_y):
        if visit[i][j] > mx:
            mx = visit[i][j]
        if visit[i][j] == 0 and tomato_farm[i][j] != -1:
            result = -1

if result == -1:
    print(result)
else:
    print(mx - 1)
