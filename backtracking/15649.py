import sys
input = sys.stdin.readline

n, m = map(int,input().split())
is_used = [0] * (n+1)
num_list = [0] * (n+1)

def func(k):
    if k == m:
        for i in range(m):
            print(num_list[i],end=' ')
        print()
            
    else:
        for i in range(1,n+1):
            if is_used[i] == 0:
                num_list[k] = i
                is_used[i] = 1
                func(k+1)  
                is_used[i] = 0

func(0)