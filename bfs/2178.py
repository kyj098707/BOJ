import sys
from collections import deque

input = sys.stdin.readline

num_x, num_y = map(int, input().split())
maze = []
visit = [[0] * num_y for _ in range(num_x)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

Q = deque()

for _ in range(num_x):
    maze.append(list(map(int, " ".join(input().rstrip()).split(" "))))

Q.append((0, 0))
mx = 0
cnt = 0

while len(Q):
    cur_x = Q[0][0]
    cur_y = Q[0][1]
    Q.popleft()
    for dir in range(4):
        nx = cur_x + dx[dir]
        ny = cur_y + dy[dir]

        if nx >= num_x or ny >= num_y or nx < 0 or ny < 0:
            continue

        if visit[nx][ny] or maze[nx][ny] != 1:
            continue

        Q.append((nx, ny))
        visit[nx][ny] = visit[cur_x][cur_y] + 1
        cnt += 1

print(visit[num_x - 1][num_y - 1] + 1)
