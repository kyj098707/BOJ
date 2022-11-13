import sys
input = sys.stdin.readline

from collections import deque

Q = deque()
dx = [1,0,-1,0]
dy = [0,1,0,-1]

num_x, num_y = map(int, input().split())
visit = [[0 for _ in range(num_y)] for __ in range(num_x)]
grid = []
if num_x == num_y == 1:
    print(1)
    exit()
for _ in range(num_x):
    grid.append(' '.join(input().rstrip()).split())

Q.append((0,0,0))
visit[0][0] = 1

while len(Q):
    cur_x = Q[0][0]
    cur_y = Q[0][1]
    crash_war = Q[0][2]
    Q.popleft()
    
    for dir in range(4):
        nx = cur_x + dx[dir]
        ny = cur_y + dy[dir]
        
        if nx < 0 or ny < 0 or nx >= num_x or ny >= num_y:
            continue
        if visit[nx][ny]:
            continue
        if grid[nx][ny] == '1' and crash_war :
            continue
        if nx == (num_x-1) and ny == (num_y - 1):
            print(visit[cur_x][cur_y] + 1)
            exit()
        visit[nx][ny] = 1
        if grid[nx][ny] == '1':
            Q.append((nx,ny,1))
        else:
            Q.append((nx,ny,crash_war))
        visit[nx][ny] = visit[cur_x][cur_y] + 1
        
       
print(-1)