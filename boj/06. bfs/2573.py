import sys

input = sys.stdin.readline

from collections import deque

num_x, num_y = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

grid = []
for _ in range(num_x):
    grid.append(list(map(int, input().split())))
cnt = 0
while True:
    Q = deque()
    visit = [[0 for _ in range(num_y)] for __ in range(num_x)]
    for i in range(num_x):
        for j in range(num_y):
            if grid[i][j] == 0 and not visit[i][j]:
                Q.append((i, j))
                visit[i][j] = 1
                while len(Q):
                    cur_x, cur_y = Q.popleft()

                    for dir in range(4):
                        nx = cur_x + dx[dir]
                        ny = cur_y + dy[dir]

                        if nx < 0 or ny < 0 or nx >= num_x or ny >= num_y:
                            continue
                        if visit[nx][ny]:
                            continue
                        if grid[nx][ny] != 0:
                            if grid[nx][ny] > 0:
                                grid[nx][ny] -= 1
                                if grid[nx][ny] == 0:
                                    visit[nx][ny] = 1

                            continue

                        visit[nx][ny] = 1
                        Q.append((nx, ny))

    Q = deque()
    visit = [[0 for _ in range(num_y)] for __ in range(num_x)]

    tmp = 0
    for i in range(num_x):
        for j in range(num_y):
            if grid[i][j] != 0 and not visit[i][j]:
                tmp += 1
                Q.append((i, j))
                while len(Q):
                    cur_x, cur_y = Q.popleft()
                    for dir in range(4):
                        nx = cur_x + dx[dir]
                        ny = cur_y + dy[dir]

                        if nx < 0 or ny < 0 or nx >= num_x or ny >= num_y:
                            continue
                        if grid[nx][ny] == 0 or visit[nx][ny] != 0:
                            continue

                        visit[nx][ny] = 1
                        Q.append((nx, ny))
    cnt += 1

    if tmp >= 2:
        break

    if tmp == 0:
        print(0)
        quit()
print(cnt)
