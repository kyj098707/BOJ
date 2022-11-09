import sys
input = sys.stdin.readline

T = int(input())
good_word = ['A','B']
cnt = 0
for i in range(T):
    stack = ['1']

    word = input().rstrip()

    for w in word:
        if (w == good_word[0] and stack[-1] == good_word[0]) or (w == good_word[1] and stack[-1] == good_word[1]):
            stack.pop()
        else:
            stack.append(w)

    if len(stack) == 1:
        cnt += 1
    
print(cnt)