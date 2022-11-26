import sys
input = sys.stdin.readline

n = int(input())
spot_list = []

for _ in range(n):
    x,y = map(int,input().split())
    spot_list.append((x,y))

spot_list.sort(key=lambda x :(x[1],x[0]))

for spot in spot_list:
    print(spot[0], spot[1])

