result_list = []

for _ in range(5):
    result_list.append(int(input()))

result_list = sorted(result_list)
print(int(sum(result_list) / len(result_list)))
print(result_list[2])
