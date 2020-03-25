from collections import deque

def solution(numbers, target):
    queue = deque()
    queue.append(numbers[0])
    queue.append(-numbers[0])
    cnt = 2
    
    for i in range(1, len(numbers)):
        for _ in range(cnt):
            num = queue.popleft()
            queue.append(num + numbers[i])
            queue.append(num - numbers[i])
        
        cnt *= 2
    
    return queue.count(target)
            
        
        
        
