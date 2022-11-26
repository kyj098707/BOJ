def solution(k, score):
    answer = []
    stack = []
    for i in range(len(score)):
        
        stack.append(score[i])
        stack.sort(reverse=True)
        while len(stack) > k:
            stack.pop()
        answer.append(stack[-1])
    return answer