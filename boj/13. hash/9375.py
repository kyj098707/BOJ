import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    dic = dict()
    val_list = []
    for __ in range(n):
        ___, pos = input().split()
        if dic.get(pos) == None:
            dic[pos] = 1
        else:
            dic[pos] += 1

        val_list = [v for v in dic.values()]
    if len(val_list) == 1:
        print(val_list[0])
    else:

        total = 1
        for val in val_list:
            total *= val + 1

        print(total - 1)
