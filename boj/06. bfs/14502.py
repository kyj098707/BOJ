from collections import deque

num_x, num_y = map(int, input().split())
board = []

for _ in range(num_x):
    board.append(list(map(int,input().split())))
dx = [1,0,-1,0]
dy = [0,1,0,-1]
virus_cnt = []
def make_wall(k):
    virus = 0
    safe_area = 0
    if k == 3:
        Q = deque()
        visit = [[0 for _ in range(num_y)] for __ in range(num_x)]
        for a in range(num_x):
            for b in range(num_y):
                if board[a][b] == 2:
                    Q.append((a,b))
                    visit[a][b] = 1
                elif board[a][b] == 0:
                    safe_area += 1
    
        while Q:
            cur_x, cur_y = Q.popleft()
            for dir in range(4):
                nx = cur_x + dx[dir]
                ny = cur_y + dy[dir]

                if nx < 0 or ny < 0 or nx >= num_x or ny >= num_y:
                    continue
                if visit[nx][ny] or board[nx][ny] == 1:
                    continue
                Q.append((nx,ny))
                visit[nx][ny] = 1
                virus += 1
        virus_cnt.append(safe_area - virus)
        return
    
    for i in range(num_x):
        for j in range(num_y):
            if board[i][j] == 0:
                board[i][j] = 1
                make_wall(k+1)
                board[i][j] = 0

make_wall(0)
print(max(virus_cnt))