from collections import deque

num_x, num_y = map(int, input().split())

board = []

for _ in range(num_x):
    board.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

Q = deque()
cnt = 0
while True:
    visit = [[0 for _ in range(num_y)] for __ in range(num_x)]
    Q.append((0, 0))
    while Q:
        cur_x, cur_y = Q.popleft()
        for dir in range(4):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]

            if nx < 0 or ny < 0 or nx >= num_x or ny >= num_y:
                continue

            if board[nx][ny] == 0 and visit[nx][ny]:
                continue

            if board[nx][ny] == 1:
                visit[nx][ny] += 1
                continue

            visit[nx][ny] = 1
            Q.append((nx, ny))
    isEmpty = True
    for i in range(num_x):
        for j in range(num_y):
            if visit[i][j] >= 2:
                isEmpty = False
                board[i][j] = 0
    if isEmpty:
        break
    cnt += 1

print(cnt)
