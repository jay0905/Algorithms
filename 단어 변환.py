# 출처: https://programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def changeable(current, next):
    cnt = 0
    
    for current_alphabet, next_alphabet in zip(current, next):
        if current_alphabet != next_alphabet:
            cnt += 1

    return True if cnt == 1 else False

def solution(begin, target, words):
    answer = 0
    USED = set()
    queue = deque([begin])
    second_queue = []
    
    while queue:
        
        current = queue.popleft()
        USED.add(current)

        if current == target:
            return answer

        for word in words:
            if changeable(current, word) and word not in USED:
                second_queue.append(word)

        if not queue:
            queue = deque(second_queue)
            second_queue = []
            answer += 1
        
    return 0
