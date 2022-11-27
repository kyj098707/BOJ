import sys

input = sys.stdin.readline

T, m = map(int, input().split())

dic = dict()
dic_2 = dict()
for _ in range(T):
    group = input().rstrip()
    dic[group] = []
    n = int(input())
    for __ in range(n):
        p = input().rstrip()
        dic[group].append(p)
        dic_2[p] = group

for _ in range(m):
    p = input().rstrip()
    opt = int(input())

    if opt == 1:
        print(dic_2[p])
    else:
        for member in sorted(dic[p]):
            print(member)
