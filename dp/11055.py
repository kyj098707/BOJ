num = int(input())
num_list = list(map(int, input().split()))

D = [0 for _ in range(1003)]
D[0] = num_list[0]
mx = D[0]
for i in range(1,num):
    D[i] = num_list[i]
    for j in range(i):
        if num_list[i] <= num_list[j]:
            continue
        D[i] = max(D[i], D[j] + num_list[i])
    mx = max(mx,D[i])

print(mx)