from collections import deque
n, m = map(int,input().split())
visit = [100002 for _ in range(200006)]

if n >= m :
    print(n - m)
    print(1)
    quit()

Q = deque()

Q.append(n)
visit[n] = 0
result_1 = 0
result_2 = 0
while Q:
    cur_x = Q.popleft()
    for dir in range(3):
        if dir == 0:
            nx = cur_x + 1
        elif dir == 1:
            nx = cur_x - 1
        else:
            nx = cur_x * 2

        if nx > 200004 or nx < 0:
            continue
        if visit[nx] <= visit[cur_x]:
            continue
        if nx == m:
            result_2 += 1
            result_1 = visit[cur_x] + 1
        Q.append(nx)
        visit[nx] = visit[cur_x] + 1

print(result_1)
print(result_2)