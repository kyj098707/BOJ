import sys
input = sys.stdin.readline

spot_list = []
n = int(input())

for _ in range(n):
    x,y = map(int,input().split())
    spot_list.append((x,y))

spot_list.sort(key= lambda x:(x[0],x[1]))

for spot in spot_list:
    print(spot[0], spot[1])