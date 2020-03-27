from itertools import permutations

def solution(numbers):
    permu_set = set()
    
    for i in range(1, len(numbers) + 1):
        permu = list(permutations(numbers, i))
        for p in permu:
            permu_set.add(int("".join(p)))
            
    permu_set -= set(range(0, 2))
    
    answer = 0
    for i in range(2, int(max(permu_set) ** 0.5) + 1):
        permu_set -= set(range(i * 2, max(permu_set) + 1, i))
            
    return len(permu_set)
