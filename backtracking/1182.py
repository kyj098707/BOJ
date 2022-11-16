n, s = map(int, input().split())

num_list = list(map(int,input().split()))


cnt = 0
def func(k,total):
    global cnt
    if k == n:
        if total == s:
            cnt += 1
        return
    
    func(k+1, total+num_list[k])
    func(k+1, total)

func(0,0)
if s == 0:
    print(cnt - 1)
else:
    print(cnt)
