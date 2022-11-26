odd_list = []
for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        odd_list.append(num)

if len(odd_list) == 0:
    print(-1)
else:
    print(sum(odd_list))
    print(min(odd_list))
