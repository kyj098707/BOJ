import sys

input = sys.stdin.readline

k, n = map(int, input().split())

dic = dict()
for _ in range(n):
    stu_num = input().rstrip()
    if dic.get(stu_num) == None:
        dic[stu_num] = 1
    else:
        del dic[stu_num]
        dic[stu_num] = 1
cnt = 0
for stu, times in dic.items():
    if times > 1:
        continue
    print(stu)
    cnt += 1
    if cnt == k:
        break
