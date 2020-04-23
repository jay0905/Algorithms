출처: https://programmers.co.kr/learn/courses/30/lessons/17687

def convert(number, base):
    T = '0123456789ABCDEF'
    i, j = divmod(number, base)

    if i == 0:
        return T[j]
    else:
        return convert(i, base) + T[j]
    
def solution(n, t, m, p):
    digits = []
    number = 0
    
    while len(digits) < t * m:
        digits += list(convert(number, n))
        number += 1

    answer = ''
    for i in range(t):
        answer += digits[i * m + p - 1]

    return answer
