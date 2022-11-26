from collections import deque

n, k = map(int, input().split())
if n == k:
    print(0)
    print(k)
    quit()
path_arr = []
visit = [0] * 100001
track = [0] * 100001
Q = deque()
Q.append(n)
visit[n] = 1
dx = [-1, 1]
while Q:
    cur_x = Q.popleft()
    for dir in range(3):
        if dir == 2:
            nx = cur_x * 2
        else:
            nx = cur_x + dx[dir]

        if nx < 0 or nx > 100000:
            continue
        if visit[nx]:
            continue
        if nx == k:
            print(visit[cur_x])
            x = cur_x
            for _ in range(visit[cur_x]):
                path_arr.append(x)
                x = track[x]
            for i in path_arr[::-1]:
                print(i, end=" ")
            print(k)
            quit()
        visit[nx] = visit[cur_x] + 1
        Q.append(nx)
        track[nx] = cur_x
