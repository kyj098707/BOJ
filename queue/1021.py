import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
dq = deque(range(1,n+1))
cnt = 0
find_nums = map(int, input().split())
for find_num in find_nums:
    flag = True
    while flag:

        if dq[0] == find_num:
            dq.popleft()
            flag = False
        else:
            if dq.index(find_num) >= len(dq)/2:
                dq.appendleft(dq.pop())
                
                cnt = cnt + 1
            else:
                dq.append(dq.popleft())
                
                cnt = cnt + 1
print(cnt)