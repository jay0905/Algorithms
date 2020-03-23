from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    location_list = deque(False for _ in range(len(priorities)))
    location_list[location] = True
    cnt = 0
    
    while priorities:
        m = max(priorities)
        
        if priorities[0] < m:
            priorities.append(priorities.popleft())
            location_list.append(location_list.popleft())
        else:
            cnt += 1
            
            if location_list[0] == True:
                return cnt
            else:
                priorities.popleft()
                location_list.popleft()
