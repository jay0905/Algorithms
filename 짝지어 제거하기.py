def solution(s):
    stack = []
    
    for alphabet in s:
        if stack and alphabet == stack[-1]:
            stack.pop()
        else:
            stack.append(alphabet)
    
    if stack:
        return 0
    return 1
