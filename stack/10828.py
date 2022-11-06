import sys

input = sys.stdin.readline

num = int(input())
stack = []

for _ in range(num):
    command = input().rstrip()

    if command == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()

    elif command == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif command == "size":
        print(len(stack))

    elif command == "empty":
        if len(stack):
            print(0)
        else:
            print(1)

    else:
        stack.append(command.split()[-1])
