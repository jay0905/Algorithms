import math

def solution(progresses, speeds):
    days = []
    answer = []
    
    for progress, speed in zip(progresses, speeds):
        days.append(math.ceil((100 - progress) / speed))

    maximum = days[0]
    day_cnt = 0
    for day in days:
        if day > maximum:
            maximum = day
            answer.append(day_cnt)
            day_cnt = 1
        else:                
            day_cnt += 1
    answer.append(day_cnt)
    
    return answer
    
