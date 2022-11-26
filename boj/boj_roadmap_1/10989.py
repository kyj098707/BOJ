import sys
input = sys.stdin.readline

visit = [0 for _ in range(10001)]

n = int(input())

for _ in range(n):
    visit[int(input())] += 1

for index in range(len(visit)):
    if visit[index] != 0 :
        for _ in range(visit[index]):
            print(index)