import sys

input = sys.stdin.readline

from collections import deque

num_x, num_y, k = map(int, input().split())

grid = [[0 for _ in range(num_y)] for __ in range(num_x)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for _ in range(k):
    y_1, x_1, y_2, x_2 = map(int, input().split())
    for i in range(x_1, x_2):
        for j in range(y_1, y_2):
            grid[i][j] = 1

Q = deque()
visit = [[0 for _ in range(num_y)] for __ in range(num_x)]
cnt = 0
cnt_list = []
for i in range(num_x):
    for j in range(num_y):
        tmp = 1
        if grid[i][j] == 0 and not visit[i][j]:
            Q.append((i, j))
            visit[i][j] = 1
            cnt += 1
            while len(Q):
                cur_x = Q[0][0]
                cur_y = Q[0][1]

                Q.popleft()
                for dir in range(4):
                    nx = cur_x + dx[dir]
                    ny = cur_y + dy[dir]

                    if nx < 0 or ny < 0 or nx >= num_x or ny >= num_y:
                        continue

                    if visit[nx][ny] or grid[nx][ny] == 1:
                        continue

                    visit[nx][ny] = 1
                    Q.append((nx, ny))
                    tmp += 1

            cnt_list.append(tmp)


print(cnt)
for result in sorted(cnt_list):
    print(result, end=" ")
