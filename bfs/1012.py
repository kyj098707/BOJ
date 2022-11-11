import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for _ in range(T):
    num_y, num_x, lettuce_num = map(int, input().split())
    lettuce_farm = [[0] * num_y for _ in range(num_x)]
    visit = [[0] * num_y for _ in range(num_x)]

    Q = deque()

    for _ in range(lettuce_num):
        j, i = map(int, input().split())

        lettuce_farm[i][j] = 1

    cnt = 0

    for i in range(num_x):
        for j in range(num_y):
            if lettuce_farm[i][j] == 1 and not visit[i][j]:
                cnt += 1
                Q.append((i, j))
                while len(Q):
                    cur_x = Q[0][0]
                    cur_y = Q[0][1]
                    Q.popleft()
                    for dir in range(4):
                        nx = cur_x + dx[dir]
                        ny = cur_y + dy[dir]

                        if nx >= num_x or nx < 0 or ny >= num_y or ny < 0:
                            continue
                        if visit[nx][ny] or lettuce_farm[nx][ny] == 0:
                            continue

                        Q.append((nx, ny))
                        visit[nx][ny] = 1
    print(cnt)
