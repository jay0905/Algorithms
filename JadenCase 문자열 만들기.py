def solution(s):
    answer = ""
    
    for i in range(len(s)):
        if i == 0:
            if s[i].isalpha():
                answer += s[i].upper()
            else:
                answer += s[i]
        elif s[i - 1] == " " and s[i].isalpha():
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    
    return answer
    
