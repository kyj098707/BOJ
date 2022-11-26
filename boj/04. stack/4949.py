import sys

input = sys.stdin.readline


gualho_list = ["[", "]", "(", ")"]
while True:
    stack = [0]
    sentence = input().rstrip()
    if sentence == ".":
        break
    for word in sentence:
        if word in gualho_list:
            if (stack[-1] == gualho_list[0] and word == gualho_list[1]) or (
                stack[-1] == gualho_list[2] and word == gualho_list[3]
            ):
                stack.pop()
            else:
                stack.append(word)

    if len(stack) == 1:
        print("yes")
    else:
        print("no")
