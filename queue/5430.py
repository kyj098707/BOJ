import sys
from collections import deque

input = sys.stdin.readline

dq = deque()

T = int(input())

for _ in range(T):
    is_forward = True
    command = input().rstrip()
    num = int(input())
    result = ''
    dq = input().rstrip()[1:-1].split(',')
    
    if num == 0:
        dq = []
    else :
        dq = deque(dq)
    
    
    
    for c in command:
        if c == 'R':
            is_forward = not is_forward
        elif c == 'D':
            if len(dq) == 0:
                result = 'error'
                break
            else:
                if is_forward:
                    dq.popleft()
                else:
                    dq.pop()
    
    if result == 'error':
        print(result)
    else:
        if not is_forward:
            dq.reverse()
        print('['+','.join(dq)+']')