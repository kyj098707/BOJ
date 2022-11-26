import sys

input = sys.stdin.readline

num = int(input())
room_list = []
for _ in range(num):
    room_list.append(tuple(map(int, input().split())))

room_list.sort(key=lambda x: (x[1], x[0]))


stack = [(0, 0)]
for room in room_list:
    cur_en = stack[-1][1]
    if room[0] >= cur_en:
        stack.append(room)

print(len(stack) - 1)
