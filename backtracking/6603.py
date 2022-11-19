import sys
input = sys.stdin.readline

result = [0] * 6
num_list = []

def func(k,st):
    if k == 6:
        for i in range(6):
            print(result[i], end = " ")
        print()
        return
    
    for i in range(st,len(num_list)):
        
        result[k] = num_list[i]
        st = i+1
        func(k+1,i+1)

while True:
    num_list = list(map(int,input().split()))
    if num_list == [0]:
        break
    num_list = num_list[1:]
    num_list.sort()
    func(0,0)
    print()
