import sys
from collections import deque


input = sys.stdin.readline

num_x, num_y = map(int, input().split())
maze = []
visit = [[99999] * num_y for _ in range(num_x)]
j_visit = [[-1] * num_y for _ in range(num_x)]
result = 0
for _ in range(num_x):
    maze.append(list(" ".join(input().rstrip()).split(" ")))

Q = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
j_pos = ""
for i in range(num_x):
    for j in range(num_y):
        if maze[i][j] == "F":
            visit = [[-1] * num_y for _ in range(num_x)]
            Q.append((i, j))
            visit[i][j] = 0

        if maze[i][j] == "J":
            j_pos = (i, j)

while len(Q):
    cur_x = Q[0][0]
    cur_y = Q[0][1]
    Q.popleft()

    for dir in range(4):
        nx = dx[dir] + cur_x
        ny = dy[dir] + cur_y

        if nx < 0 or ny < 0 or nx >= num_x or ny >= num_y:
            continue

        if visit[nx][ny] >= 0 or maze[nx][ny] == "#":
            continue

        Q.append((nx, ny))
        visit[nx][ny] = visit[cur_x][cur_y] + 1

JQ = deque()
JQ.append(j_pos)
j_visit[j_pos[0]][j_pos[1]] = 0

while len(JQ):
    cur_x = JQ[0][0]
    cur_y = JQ[0][1]

    JQ.popleft()

    for dir in range(4):
        nx = cur_x + dx[dir]
        ny = cur_y + dy[dir]

        if nx < 0 or ny < 0 or nx >= num_x or ny >= num_y:
            print(j_visit[cur_x][cur_y] + 1)
            result = 1
            exit()
        if j_visit[nx][ny] >= 0 or maze[nx][ny] == "#":
            continue
        j_visit[nx][ny] = j_visit[cur_x][cur_y] + 1
        if j_visit[nx][ny] >= visit[nx][ny]:
            continue
        JQ.append((nx, ny))
        if nx == 0 or nx == num_x - 1 or ny == 0 or ny == num_y - 1:
            result = 1


if result == 0:
    print("IMPOSSIBLE")
