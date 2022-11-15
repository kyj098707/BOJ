import sys

input = sys.stdin.readline

num = int(input())

calender = []

for _ in range(num):
    st_mon, st_date, en_mon, en_date = map(int, input().split())
    calender.append((st_mon, st_date, en_mon, en_date))

calender.sort(key=lambda x: (x[2], x[3], x[0], x[1]))

## 3월 1일부터 11월 30일 까지
stack = [(0, 0, 3, 1)]
for date in calender:
    st_mon = date[0]
    st_date = date[1]
    if st_mon > stack[-1][-2] or (st_mon == stack[-1][-2] and st_date > stack[-1][-1]):
        continue
    while date[0] < stack[-1][0] or (
        date[0] == stack[-1][0] and date[1] <= stack[-1][1]
    ):
        stack.pop()
    stack.append((stack[-1][-2], stack[-1][-1], date[2], date[3]))
while 11 < stack[-1][0]:
    stack.pop()

print(calender)
print(stack)

if stack[-1][2] <= 11:
    print(0)
else:
    print(len(stack) - 1)
