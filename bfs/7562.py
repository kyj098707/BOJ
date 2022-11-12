import sys

input = sys.stdin.readline

from collections import deque

T = int(input())
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, 2, 1, -1, -2]
for _ in range(T):
    Q = deque()
    n = int(input())
    visit = [[0 for _ in range(n)] for __ in range(n)]

    x, y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    if target_x == x and target_y == y:
        print(0)
        continue
    Q.append((x, y))
    visit[x][y] = 1
    while len(Q):
        cur_x = Q[0][0]
        cur_y = Q[0][1]
        Q.popleft()
        for dir in range(8):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visit[nx][ny]:
                continue
            if nx == target_x and ny == target_y:
                print(visit[cur_x][cur_y])
                Q.clear()
                break

            visit[nx][ny] = visit[cur_x][cur_y] + 1
            Q.append((nx, ny))
