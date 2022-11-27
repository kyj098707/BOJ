import sys

input = sys.stdin.readline
n, m = map(int, input().split())

dic = dict()

for i in range(1, n + 1):
    dic[input().rstrip()] = str(i)

dic_2 = {v: k for k, v in dic.items()}
for _ in range(m):
    res = input().rstrip()
    if res.isdigit():
        print(dic_2[res])
    else:
        print(dic[res])
