tmp = 1
result_list = [0] * 10
for _ in range(3):
    tmp = tmp * int(input())

for n in str(tmp):
    n = int(n)
    result_list[n] = result_list[n] + 1

for result in result_list:
    print(result)
