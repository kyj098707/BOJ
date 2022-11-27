import sys
input = sys.stdin.readline
dic = dict()
n = int(input())
for _ in range(n):
    p, info = input().split()
    dic[p] = info

person_list = []
for i in dic:
    if dic[i] == 'enter':
        person_list.append(i)
person_list.sort(reverse=True)
for p in person_list:
    print(p)