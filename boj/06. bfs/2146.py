import sys

input = sys.stdin.readline

from collections import deque

n = int(input())
visit = [[0 for _ in range(n)] for __ in range(n)]
grid = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    grid.append(list(map(int, input().split())))

Q = deque()
island_number = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] != 0 and not visit[i][j]:
            island_number += 1
            grid[i][j] = island_number
            Q.append((i, j))
            while len(Q):
                cur_x, cur_y = Q.popleft()
                for dir in range(4):
                    nx = cur_x + dx[dir]
                    ny = cur_y + dy[dir]

                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    if grid[nx][ny] == 0 or visit[nx][ny]:
                        continue

                    visit[nx][ny] = 1
                    grid[nx][ny] = island_number
                    Q.append((nx, ny))


Q = deque()
result = 9999
for num in range(island_number):
    visit = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == num + 1:
                Q.append((i, j))
                visit[i][j] = 1

    while len(Q):
        cur_x, cur_y = Q.popleft()

        for dir in range(4):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if grid[nx][ny] == num + 1:
                continue
            if visit[nx][ny]:
                continue
            if grid[nx][ny] != 0:
                result = min(visit[cur_x][cur_y] - 1, result)

            visit[nx][ny] = visit[cur_x][cur_y] + 1
            Q.append((nx, ny))
print(result)
