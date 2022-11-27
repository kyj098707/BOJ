input_str = input()

dic = dict()

for i in range(len(input_str)):
    for j in range(i+1,len(input_str)+1):
        dic[input_str[i:j]] = 1
print(sum([v for v in dic.values()]))
    

