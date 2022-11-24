n = int(input())
num_list = sorted(list(map(int, input().split())))

trg_n = int(input())
trg_list = list(map(int,input().split()))

def find_lower_bound(trg):
    st = 0
    en = n
    
    while st < en:
        mid = (st+en)//2
        if num_list[mid] >= trg:
            en = mid
        else:
            st = mid+1

    return st

def find_upper_bound(trg):
    st = 0
    en = n
    
    while st < en:
        mid = (st+en)//2
        if num_list[mid] > trg:
            en = mid
        else:
            st = mid+1
    return st

for trg in trg_list:
    print(find_upper_bound(trg) - find_lower_bound(trg), end = ' ')