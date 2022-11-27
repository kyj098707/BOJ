from collections import deque

a, b = map(int,input().split())

Q = deque()

Q.append((a,1))
while Q:
    cur_x, cur_cnt = Q.popleft()
    for dir in range(2):
        if dir == 0:
            nx = cur_x * 2
            ny = cur_cnt + 1
        if dir == 1:
            nx = cur_x * 10 + 1
            ny = cur_cnt + 1
        if nx > b:
            continue
        if nx == b:
            print(ny)
            quit()
        Q.append((nx,ny))
print(-1)