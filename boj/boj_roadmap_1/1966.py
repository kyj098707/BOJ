from collections import deque

T = int(input())


for _ in range(T):
    importance = [0 for __ in range(11)]
    Q = deque()
    n, m = map(int,input().split())
    num_list = list(map(int,input().split()))
    for i in range(n):
        if i == m:
            Q.append((num_list[i],1))
        else:
            Q.append((num_list[i],0))
        importance[num_list[i]] += 1
    cnt = 0
    while Q:
        if max(importance[Q[0][0]+1:]) > 0:
            Q.append(Q.popleft())
        else:
            cnt += 1
            if Q[0][1] == 1:
                
                print(cnt)
                break
            importance[Q.popleft()[0]] -= 1 
