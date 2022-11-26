import sys

input = sys.stdin.readline

from collections import deque


dx = [1, 0, 0, -1, 0, 0]
dy = [0, 1, 0, 0, -1, 0]
dz = [0, 0, 1, 0, 0, -1]

while True:
    num_z, num_x, num_y = map(int, input().split())
    if num_z == 0 and num_x == 0 and num_y == 0:
        break
    visit = [[[0 for _ in range(num_y)] for __ in range(num_x)] for ___ in range(num_z)]
    building = []
    for _ in range(num_z):
        tmp = []
        for __ in range(num_x):
            tmp.append(" ".join(input().rstrip()).split())

        garbage = input().rstrip()
        building.append(tmp)

    Q = deque()
    result = 0

    for k in range(num_z):
        for i in range(num_x):
            for j in range(num_y):
                if building[k][i][j] == "S":
                    Q.append((k, i, j))
                    visit[k][i][j] = 1
                    while len(Q):
                        cur_z = Q[0][0]
                        cur_x = Q[0][1]
                        cur_y = Q[0][2]
                        Q.popleft()
                        for dir in range(6):
                            nz = cur_z + dz[dir]
                            nx = cur_x + dx[dir]
                            ny = cur_y + dy[dir]

                            if (
                                nz < 0
                                or nx < 0
                                or ny < 0
                                or nz >= num_z
                                or nx >= num_x
                                or ny >= num_y
                            ):
                                continue
                            if visit[nz][nx][ny] or building[nz][nx][ny] == "#":
                                continue
                            if building[nz][nx][ny] == "E":
                                print(
                                    f"Escaped in {visit[cur_z][cur_x][cur_y]} minute(s)."
                                )
                                result = 1
                            Q.append((nz, nx, ny))
                            visit[nz][nx][ny] = visit[cur_z][cur_x][cur_y] + 1
                    if result == 0:
                        print("Trapped!")
