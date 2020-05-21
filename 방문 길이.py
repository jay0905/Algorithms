# 출처: https://programmers.co.kr/learn/courses/30/lessons/49994

def movable(x, y):
    return -5 <= x <= 5 and -5 <= y <= 5 

def solution(dirs):
    answer = 0
    VISITED = []
    x, y = 0, 0

    for dir in dirs:
        if dir == "U":
            next_x, next_y = x, y + 1
        elif dir == "L":
            next_x, next_y = x - 1, y
        elif dir == "R":
            next_x, next_y = x + 1, y
        elif dir == "D":
            next_x, next_y = x, y - 1
            
        if movable(next_x, next_y):
            if [(x, y), (next_x, next_y)] not in VISITED and [(next_x, next_y), (x, y)] not in VISITED:
                answer += 1
                VISITED.append([(x, y), (next_x, next_y)])
            x, y = next_x, next_y

    print(VISITED)

    return answer
