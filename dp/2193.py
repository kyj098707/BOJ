D = [0 for _ in range(93)]
D[1] = 1
D[2] = 1
D[3] = D[1] + D[2]
for i in range(3, 92):
    D[i] = D[i - 1] + D[i - 2]

num = int((input()))
print(D[num])
