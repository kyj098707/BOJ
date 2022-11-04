alpha_list = [0] * 30
alpha_list2 = [0] * 30

alpha_1 = input()
alpha_2 = input()
cnt = 0
for c in alpha_1:
    num_c = ord(c) - ord('a')
    alpha_list[num_c] = alpha_list[num_c] + 1


for c in alpha_2:
    num_c = ord(c) - ord('a')
    alpha_list2[num_c] = alpha_list2[num_c] + 1 

for c_1,c_2 in zip(alpha_list,alpha_list2):
    cnt = abs(c_1 - c_2) + cnt

print(cnt)