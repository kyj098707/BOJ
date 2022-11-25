n, m = map(int, input().split())
result = [0] * (m + 1)
tmp_list = sorted(list(map(int, input().split())))
num_list = []
tmp = 0
for num in tmp_list:
    if tmp == num:
        continue
    tmp = num
    num_list.append(num)


def func(k):
    if k == m:
        for i in range(m):
            print(result[i], end=" ")
        print()
        return
    for i in range(len(num_list)):
        result[k] = num_list[i]
        func(k + 1)


func(0)
