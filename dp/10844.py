D = [[0 for _ in range(10)] for _ in range(103)]

for i in range(1,10):
    D[1][i] = 1

for i in range(2,103):
    for k in range(10):
        if k == 0:
            D[i][k] = D[i-1][1]
            
        elif k == 9:
            D[i][k] = D[i-1][8]
            
        else:
            D[i][k] = D[i-1][k-1] + D[i-1][k+1]

        
    
print(sum(D[int(input())]) % 1000000000)