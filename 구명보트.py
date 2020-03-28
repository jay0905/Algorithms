def solution(people, limit):
    people.sort(reverse = True)
    cnt = 0
    
    for person in people:
        if person + people[-1] <= limit:
            people.pop()
        cnt += 1
        
    return cnt
