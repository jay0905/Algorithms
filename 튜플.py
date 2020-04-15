출처: https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    s = s[1:-1]
    set_list = []

    idx = 0
    while idx < len(s):
        if s[idx] == "{":
            my_set = set()
        elif s[idx].isdigit():
            num = ""
            while s[idx].isdigit():
                num += s[idx]
                idx += 1
            my_set.add(int(num))
            idx -= 1
        elif s[idx] == "}":
            set_list.append(my_set)
        
        idx += 1

    set_list.sort(key=lambda x:len(x))

    answer = []
    for i in range(len(set_list)):
        if i == 0:
            answer += set_list[i]
        else:
            answer += set_list[i] - set_list[i - 1]
    
    return answer
        
