# 출처: https://programmers.co.kr/learn/courses/30/lessons/17678

from collections import deque

def time_str(time):
    hour = ''
    minutes = ''

    if time[0] < 10:
        hour = "0" + str(time[0])
    else:
        hour = str(time[0])

    if time[1] < 10:
        minutes = "0" + str(time[1])
    else:
        minutes = str(time[1])

    return hour + ":" + minutes

def solution(n, t, m, timetable):
    timetable = [[int(time[:2]), int(time[3:5])] for time in timetable]
    timetable.sort(key=lambda x: (x[0], x[1]))
    timetable = deque(timetable)
    depart_time = [9, 0]

    for i in range(1, n):

        pop_cnt = 0
        
        while pop_cnt < m:
            SMALLER = False
            if timetable:
                if timetable[0][0] == depart_time[0]:
                    if timetable[0][1] <= depart_time[1]:
                        SMALLER = True
                elif timetable[0][0] < depart_time[0]:
                    SMALLER = True
                    
                if SMALLER:
                    timetable.popleft()
                    pop_cnt += 1
                else:
                    break

        depart_time[1] += t

        if depart_time[1] >= 60:
            depart_time[0] += 1
            depart_time[1] -= 60

    answer = ''
    if len(timetable) < m:
        return time_str(depart_time)
    
    else:
        cnt = 0

        for time in timetable:
            if time[0] == depart_time[0]:
                if time[1] <= depart_time[1]:
                    cnt += 1
            else:
                if time[0] < depart_time[0]:
                    cnt += 1
                
            if cnt == m:
                if time[1] == 0:
                    time[0] -= 1
                    time[1] = 59
                else:
                    time[1] -= 1

                return time_str(time)

        return time_str(depart_time)
