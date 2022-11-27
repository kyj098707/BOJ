import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dic = dict()
for _ in range(n):
    site, password = input().split()
    dic[site] = password

for _ in range(k):
    print(dic[input().rstrip()])