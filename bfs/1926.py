import sys
from collections import deque

input = sys.stdin.readline

paint = []

num_x, num_y = map(int, input().split())
visit = [[0] * num_y for i in range(num_x)]
for i in range(num_x):
    paint.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dq = deque()
fill_list = []
cnt = 0
for x in range(num_x):
    for y in range(num_y):
        if paint[x][y] == 0 or visit[x][y]:
            continue
        cnt += 1
        fill = 0
        dq.append((x, y))
        visit[x][y] = 1

        while len(dq) != 0:
            fill += 1
            cur_x = dq[0][0]
            cur_y = dq[0][1]
            dq.popleft()
            for dir in range(4):
                nx = cur_x + dx[dir]
                ny = cur_y + dy[dir]

                if nx < 0 or nx >= num_x or ny < 0 or ny >= num_y:
                    continue

                if visit[nx][ny] or paint[nx][ny] == 0:
                    continue

                dq.append((nx, ny))
                visit[nx][ny] = 1

        fill_list.append(fill)

print(cnt)
if not len(fill_list):
    print(0)
else:
    print(max(fill_list))
