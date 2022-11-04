import math

room_number = int(input())
num_list = [0] * 10

for num in str(room_number):
    num_list[int(num)] = num_list[int(num)] + 1

tmp = math.ceil((num_list[6] + num_list[9]) / 2)

num_list[6], num_list[9] = tmp, tmp

print(max(num_list))
