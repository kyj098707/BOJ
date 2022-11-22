num = int(input())
num_list = list(map(int, input().split()))

D = [1 for _ in range(1003)]
mx = 1
for i in range(1,num):
    for j in range(i):
        if num_list[i] <= num_list[j]:
            continue
        D[i] = max(D[i], D[j] + 1)
    mx = max(D[i], mx)

print(mx)