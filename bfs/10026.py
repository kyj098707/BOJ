import sys
input = sys.stdin.readline

from collections import deque

num = int(input())
visit = [[0] * num for _ in range(num)]
visit_2 = [[0] * num for _ in range(num)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

grid = []
Q = deque()

rg_Q = deque()
for _ in range(num):
    grid.append(list(' '.join(input().rstrip()).split()))

cnt_1 = 0
for i in range(num):
    for j in range(num):
        cur_color = grid[i][j]
        if visit[i][j]:
            continue
        Q.append((i,j))
        while len(Q):
            cur_x = Q[0][0]
            cur_y = Q[0][1]
            Q.popleft()
            for dir in range(4):
                nx = cur_x + dx[dir]
                ny = cur_y + dy[dir]
                
                if nx < 0 or ny < 0 or nx >= num or ny >= num:
                    continue
                if visit[nx][ny]:
                    continue
                if  grid[nx][ny] != cur_color:
                    continue


                Q.append((nx,ny))
                visit[nx][ny] = 1
        cnt_1 += 1

cnt_2 = 0
for i in range(num):
    for j in range(num):
        cur_color = grid[i][j]
        if visit_2[i][j]:
            continue
        rg_Q.append((i,j))
        while len(rg_Q):
            cur_x = rg_Q[0][0]
            cur_y = rg_Q[0][1]
            rg_Q.popleft()
            for dir in range(4):
                nx = cur_x + dx[dir]
                ny = cur_y + dy[dir]
                
                if nx < 0 or ny < 0 or nx >= num or ny >= num:
                    continue
                if visit_2[nx][ny]:
                    continue
                if cur_color == 'B':
                    if cur_color != grid[nx][ny]:
                        continue
                if cur_color == 'G' or cur_color == 'R':
                    if grid[nx][ny] == 'B':
                        continue

                rg_Q.append((nx,ny))
                visit_2[nx][ny] = 1
        
        cnt_2 += 1

print(cnt_1, cnt_2)

    