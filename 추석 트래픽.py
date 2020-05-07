# 출처: https://programmers.co.kr/learn/courses/30/lessons/17676

def solution(lines):
    times = []

    for line in lines:
        infos = line.split()
        end = infos[1].split(":")
        end_sec = float(end[0]) * 3600 + float(end[1]) * 60 + float(end[2])
        t = float(infos[2][:-1])
        start_sec = round(end_sec - t + 0.001, 3)

        if start_sec < 0:
            start_sec = 0.0

        times.append([start_sec, end_sec])

    candidates = []
    for i, time in enumerate(times):
        sec_start = time[0]
        sec_end = round(time[0] + 0.999, 3)
        cnt = 1

        for j, other_time in enumerate(times):
            if i == j:
                continue

            if (sec_start <= other_time[0] and sec_end >= other_time[0]) or (sec_start <= other_time[1] and sec_end >= other_time[0]):
                cnt += 1

        candidates.append(cnt)

        sec_start = time[1]
        sec_end = round(time[1] + 0.999, 3)
        cnt = 1

        for j, other_time in enumerate(times):
            if i == j:
                continue

            if (sec_start <= other_time[0] and sec_end >= other_time[0]) or (sec_start <= other_time[1] and sec_end >= other_time[0]):
                cnt += 1

        candidates.append(cnt)

    answer = max(candidates)
    return answer
