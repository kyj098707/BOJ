import sys

input = sys.stdin.readline

from collections import deque

num = int(input())

visit = [[0 for _ in range(num)] for __ in range(num)]
houses = []

for _ in range(num):
    houses.append(list(map(int, " ".join(input().rstrip()).split())))
Q = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
house_num = 0
cnt_list = []
for i in range(num):
    for j in range(num):
        if houses[i][j] == 1 and visit[i][j] != 1:
            house_num += 1
            Q.append((i, j))
            visit[i][j] = 1
            tmp = 1
            while len(Q):
                cur_x = Q[0][0]
                cur_y = Q[0][1]
                Q.popleft()
                for dir in range(4):
                    nx = cur_x + dx[dir]
                    ny = cur_y + dy[dir]

                    if nx < 0 or ny < 0 or nx >= num or ny >= num:
                        continue
                    if visit[nx][ny] or houses[nx][ny] == 0:
                        continue
                    visit[nx][ny] = 1
                    Q.append((nx, ny))
                    tmp += 1
            cnt_list.append(tmp)

print(house_num)

for cnt in sorted(cnt_list):
    print(cnt)
