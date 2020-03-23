def solution(clothes):
    clothes_dict = dict()
    
    for cloth in clothes:
        if cloth[1] not in clothes_dict:
            clothes_dict[cloth[1]] = 1
        else:
            clothes_dict[cloth[1]] += 1
    
    answer = 1
    for value in clothes_dict.values():
        answer *= (value + 1)
        
    return answer - 1
