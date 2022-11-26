n = int(input())

word_list = []

for _ in range(n):
    word_list.append(input())

word_list.sort(key=lambda x: (len(x), x))

tmp = ""
for result in word_list:
    if tmp == result:
        continue
    tmp = result
    print(result)
