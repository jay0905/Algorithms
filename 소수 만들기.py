from itertools import combinations

def solution(nums):
    combis = list(combinations(nums, 3))
    cnt = 0
    
    for combi in combis:
        for i in range(2, sum(combi)):
            if sum(combi) % i == 0:
                break
        else:
            cnt += 1
    
    return cnt
