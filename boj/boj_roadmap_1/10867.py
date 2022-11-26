visit = [0 for _ in range(2006)]

n = int(input())
num_list = list(map(int, input().split()))

for num in num_list:
    visit[num + 1000] = 1

for i in range(2006):
    if visit[i] != 0:
        print(i - 1000, end=" ")
