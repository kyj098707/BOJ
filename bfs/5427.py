import sys

input = sys.stdin.readline

from collections import deque

T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(T):
    result = 0
    num_y, num_x = map(int, input().split())
    visit = [[10000010] * num_y for i in range(num_x)]

    building = []
    Q = deque()
    for __ in range(num_x):
        building.append((" ".join(input())).split())

    for i in range(num_x):
        for j in range(num_y):
            if building[i][j] == "*":
                Q.append((i, j))
                visit[i][j] = 0

    while len(Q):
        cur_x = Q[0][0]
        cur_y = Q[0][1]
        Q.popleft()

        for dir in range(4):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]

            if nx < 0 or ny < 0 or nx >= num_x or ny >= num_y:
                continue
            if visit[nx][ny] != 10000010 or building[nx][ny] == "#":
                continue

            visit[nx][ny] = visit[cur_x][cur_y] + 1
            Q.append((nx, ny))

    for i in range(num_x):
        for j in range(num_y):
            if building[i][j] == "@":
                Q.append((i, j))
                visit[i][j] = 0

    while len(Q):
        cur_x = Q[0][0]
        cur_y = Q[0][1]
        Q.popleft()

        for dir in range(4):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]

            if nx < 0 or ny < 0 or nx >= num_x or ny >= num_y:

                print(visit[cur_x][cur_y] + 1)
                Q.clear()
                result = 1
                break

            if (visit[nx][ny] <= visit[cur_x][cur_y] + 1) or building[nx][ny] == "#":
                continue

            Q.append((nx, ny))
            visit[nx][ny] = visit[cur_x][cur_y] + 1

    if result == 0:
        print("IMPOSSIBLE")
