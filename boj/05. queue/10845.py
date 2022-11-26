from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
dq = deque()

for _ in range(n):
    command = input().rstrip()

    if command == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif command == "size":
        print(len(dq))

    elif command == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif command == "pop":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif command == "back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
    else:
        dq.append(command.split()[-1])
