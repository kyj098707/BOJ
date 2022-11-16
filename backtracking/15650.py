n, m = map(int, input().split())
num_list = [0] * (n+1)
is_used = [0] * (n+1)
def func(k):
    if k == m:
        for i in range(m):
            print(num_list[i], end = ' ')
        print()
        return
    if k == 0 :
        st = 1
    else:
        st = num_list[k] + 1
    
    
    for i in range(st,n+1):
        if is_used[i] == 1:
            continue
        num_list[k] = i
        is_used[i] = 1
        func(k+1)
        is_used[i] = 0

func(0)