value_list = [0] * 2000010
cnt = 0

it = int(input())

num_list = list(map(int, input().split()))

total = int(input())

for num in num_list:
    if total / 2 == num:
        continue

    value_list[num] = value_list[num] + 1
    if value_list[total - num] == 1:
        cnt = cnt + 1

print(cnt)
