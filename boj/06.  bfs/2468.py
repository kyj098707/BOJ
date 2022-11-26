import sys

input = sys.stdin.readline

from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

area = []
n = int(input())

for _ in range(n):
    area.append(list(map(int, input().split())))


tmp_list = []
for i in range(0, 101):
    safe_area = []
    visit = [[0 for _ in range(n)] for __ in range(n)]
    Q = deque()
    for area_list in area:
        safe_area.append([int(x > i) for x in area_list])
    tmp = 0
    for x in range(n):
        for y in range(n):
            if safe_area[x][y] == 1 and (not visit[x][y]):
                Q.append((x, y))
                visit[x][y] = 1
                tmp += 1
                while len(Q):
                    cur_x = Q[0][0]
                    cur_y = Q[0][1]
                    Q.popleft()
                    for dir in range(4):
                        nx = cur_x + dx[dir]
                        ny = cur_y + dy[dir]

                        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                            continue
                        if visit[nx][ny] or safe_area[nx][ny] == 0:
                            continue

                        Q.append((nx, ny))
                        visit[nx][ny] = 1

    tmp_list.append(tmp)

print(max(tmp_list))
