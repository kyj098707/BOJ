

n = int(input())

num_list = list(map(int,input().split()))

trg_n = int(input())
trg_list = list(map(int,input().split()))

num_list.sort()

def bs(st,en,val):

    while (st<=en):
        mid = (st+en)//2
        if num_list[mid] == val:
            return 1
        if num_list[mid] > val:
            en = mid-1
        if num_list[mid] < val:
            st = mid+1
    return 0

for trg in trg_list:
    print(bs(0,n-1,trg))

