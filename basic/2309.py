tiny_man_list = []

for _ in range(9):
    tiny_man_list.append(int(input()))

total_height = sum(tiny_man_list)

flag = False
for i in range(len(tiny_man_list) - 1):
    if flag:
        break
    for j in range(i + 1, len(tiny_man_list)):

        if tiny_man_list[i] + tiny_man_list[j] == total_height - 100:
            tmp_a = tiny_man_list[i]
            tmp_b = tiny_man_list[j]
            tiny_man_list.remove(tmp_a)
            tiny_man_list.remove(tmp_b)
            flag = True
            break

for result in sorted(tiny_man_list):
    print(result)
