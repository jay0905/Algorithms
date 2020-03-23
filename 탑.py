def solution(heights):
    stack = []
    answer = [0 for _ in range(len(heights))]
    
    for i, height in enumerate(heights):
        while stack and height >= stack[-1][0]:
            stack.pop()
        
        if stack:
            answer[i] = stack[-1][1]

        stack.append((height, i+1))
        
    return answer
