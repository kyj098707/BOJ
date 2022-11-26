import sys

input = sys.stdin.readline
from collections import deque

m_x = [1, 0, -1, 0]
m_y = [0, 1, 0, -1]

h_x = [2, 1, -1, -2, -2, -1, 1, 2]
h_y = [1, 2, 2, 1, -1, -2, -2, -1]
### 3차원 배열을 만들어서 접근 하면 좋을 듯
k = int(input())
num_y, num_x = map(int, input().split())

visit = [[[0 for _ in range(k + 1)] for __ in range(num_y)] for ___ in range(num_x)]
grid = []
for _ in range(num_x):
    grid.append(list(map(int, input().split())))
if num_y == num_x == 1:
    print(0)
    quit()
Q = deque()

Q.append((0, 0, 0))
visit[0][0][0] = 1

while Q:
    cur_x, cur_y, horse_num = Q.popleft()

    for dir in range(4):
        nx = cur_x + m_x[dir]
        ny = cur_y + m_y[dir]

        if nx < 0 or ny < 0 or nx >= num_x or ny >= num_y:
            continue
        if visit[nx][ny][horse_num] or grid[nx][ny] == 1:
            continue

        if nx == num_x - 1 and ny == num_y - 1:
            print(visit[cur_x][cur_y][horse_num])
            quit()

        Q.append((nx, ny, horse_num))
        visit[nx][ny][horse_num] = visit[cur_x][cur_y][horse_num] + 1

    if horse_num + 1 <= k:
        for dir in range(8):
            nx = cur_x + h_x[dir]
            ny = cur_y + h_y[dir]
            n_horse = horse_num + 1

            if nx < 0 or ny < 0 or nx >= num_x or ny >= num_y:
                continue
            if visit[nx][ny][n_horse] or grid[nx][ny] == 1:
                continue

            if nx == num_x - 1 and ny == num_y - 1:
                print(visit[cur_x][cur_y][horse_num])

                quit()

            visit[nx][ny][n_horse] = visit[cur_x][cur_y][horse_num] + 1

            Q.append((nx, ny, n_horse))

print(-1)
