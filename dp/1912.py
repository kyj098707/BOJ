num = int(input())
num_list = list(map(int, input().split()))
D = [-1001] * 100003
mx = -1001
for i in range(num):
    if num_list[i] < 0:
        mx = max(D[i], mx)
    D[i+1] = D[i] + num_list[i]
    if D[i+1] <= num_list[i]:
        D[i+1] = num_list[i]
    if i == num-1:
        mx = max(D[i+1], mx)

print(mx)