alpha_list = [0] * 26
input_str = input()

for c in input_str:
    alpha_list[ord(c) - ord("a")] = alpha_list[ord(c) - ord("a")] + 1

for result in alpha_list:
    print(result, end=" ")
