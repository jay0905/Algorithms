# 출처: https://programmers.co.kr/learn/courses/30/lessons/49995

def solution(cookie):
    max_value = 0

    for i in range(len(cookie) - 1):
        front_value, front_idx = cookie[i], i
        back_value, back_idx = cookie[i + 1], i + 1

        while True:
            if front_value == back_value and front_value > max_value:
                max_value = front_value

            if front_value < back_value and front_idx > 0:
                front_idx -= 1
                front_value += cookie[front_idx]
            elif front_value >= back_value and back_idx < len(cookie) - 1:
                back_idx += 1
                back_value += cookie[back_idx]
            else:
                break
                
    answer = max_value    
    return answer
