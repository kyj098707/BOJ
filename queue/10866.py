from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
dq = deque()

for _ in range(n):
    command = input().rstrip()

    if command.split()[0] == "push_back":
        dq.append(command.split()[1])

    elif command.split()[0] == "push_front":
        dq.appendleft(command.split()[1])

    elif command.split()[0] == "pop_back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())

    elif command.split()[0] == "pop_front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())

    elif command.split()[0] == "size":
        print(len(dq))

    elif command.split()[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)

    elif command.split()[0] == "back":
        if len(dq) == 0:
            print(-1)

        else:
            print(dq[-1])

    elif command.split()[0] == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
