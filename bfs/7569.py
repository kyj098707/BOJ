import sys

input = sys.stdin.readline
from collections import deque

dx = [1, 0, 0, -1, 0, 0]
dy = [0, 1, 0, 0, -1, 0]
dz = [0, 0, 1, 0, 0, -1]
num_y, num_x, num_z = map(int, input().split())
tomatoes = []
visit = [[[0 for _ in range(num_y)] for __ in range(num_x)] for ___ in range(num_z)]
for i in range(num_z):
    tmp_tomatoes = []
    for j in range(num_x):
        tmp_tomatoes.append(list(map(int, input().split())))
    tomatoes.append(tmp_tomatoes)

Q = deque()
for k in range(num_z):
    for i in range(num_x):
        for j in range(num_y):
            if tomatoes[k][i][j] == 1:
                Q.append((k, i, j))
                visit[k][i][j] = 1

while len(Q):
    cur_x = Q[0][1]
    cur_y = Q[0][2]
    cur_z = Q[0][0]

    Q.popleft()

    for dir in range(6):
        nx = cur_x + dx[dir]
        ny = cur_y + dy[dir]
        nz = cur_z + dz[dir]

        if nx < 0 or ny < 0 or nz < 0 or nx >= num_x or ny >= num_y or nz >= num_z:
            continue
        if visit[nz][nx][ny] or tomatoes[nz][nx][ny] != 0:
            continue

        Q.append((nz, nx, ny))

        visit[nz][nx][ny] = visit[cur_z][cur_x][cur_y] + 1

mx = 0
for k in range(num_z):
    for i in range(num_x):
        for j in range(num_y):

            mx = max(mx, visit[k][i][j])
            if visit[k][i][j] == 0 and tomatoes[k][i][j] != -1:
                print(-1)
                exit()

print(mx - 1)
