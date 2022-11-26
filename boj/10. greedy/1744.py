import sys

input = sys.stdin.readline
# 1은 곱하면 무조건 손해, 0은 음수가 곱해주기 x 홀수이면 가장 절대값이 낮은 음수와 곱해줌
num = int(input())
p_value_list = []  # 양수 리스트
n_value_list = []  # 음수 리스트
have_zero = False

for _ in range(num):
    value = int(input())
    if num == 1:
        print(value)
        quit()

    if value > 0:
        p_value_list.append(value)
    elif value < 0:
        n_value_list.append(value)
    else:
        have_zero = True
total = 0
p_value_num = len(p_value_list)
n_value_num = len(n_value_list)

sorted_p_value_list = sorted(p_value_list)
sorted_n_value_list = sorted(n_value_list)

for i in range(p_value_num - 1, -1, -2):
    if i == 0:
        total += sorted_p_value_list[i]
    else:
        if sorted_p_value_list[i] == 1 or sorted_p_value_list[i - 1] == 1:
            total += sorted_p_value_list[i] + sorted_p_value_list[i - 1]
        else:
            total += sorted_p_value_list[i] * sorted_p_value_list[i - 1]

for i in range(0, n_value_num, 2):
    if i == n_value_num - 1:
        if not have_zero:
            total += sorted_n_value_list[i]
    else:
        total += sorted_n_value_list[i] * sorted_n_value_list[i + 1]

print(total)
