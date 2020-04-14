출처: https://programmers.co.kr/learn/courses/30/lessons/60058

def is_correct(s):
    stack = []

    for bracket in s:
        if bracket == "(":
            stack.append(bracket)
        else:
            if not stack:
                return False

            stack.pop()

    return False if stack else True

def split_string(s):
    left = right = 0

    for idx, bracket in enumerate(s):
        if bracket == "(":
            left += 1
        else:
            right += 1

        if left == right:
            break

    u = s[:idx + 1]
    v = s[idx + 1:]

    return u, v

def solution(p):
    if p == "" or is_correct(p):
        return p

    u, v = split_string(p)

    if is_correct(u):
        string = solution(v)
        return u + string
    else:
        t = "("
        t += solution(v)
        t += ")"

        u2 = u[1:-1]

        answer = ""
        for bracket in u2:
            if bracket == "(":
                answer += ")"
            else:
                answer += "("

        t += answer
        return t
