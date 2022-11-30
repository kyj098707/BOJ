from collections import deque

adj = [[] for _ in range(1002)]
vis = [0 for _ in range(1002)]
n, m = map(int, input().split())

for _ in range(m):
    a, b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

num = 0
Q =deque()
for i in range(1,n+1):
    if vis[i]:
        continue
    vis[i] = 1
    Q.append(i)

    num += 1

    while Q:
        cur_n = Q.popleft()
        for n in adj[cur_n]:
            if vis[n]:
                continue
            Q.append(n)
            vis[n] = 1

print(num)