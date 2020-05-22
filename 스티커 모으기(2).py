# 출처: https://programmers.co.kr/learn/courses/30/lessons/12971#

def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    
    dp1 = [0] * len(sticker)

    dp1[0] = sticker[0]
    dp1[1] = dp1[0]
    for i in range(2, len(sticker) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

    value1 = max(dp1)

    dp2 = [0] * len(sticker)

    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    value2 = max(dp2)

    answer = max(value1, value2)
    return answer
