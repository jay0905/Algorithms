def solution(monster, S1, S2, S3):
    monster = [m-1 for m in monster]
    
    answer = 0
    
    for i in range(1, S1+1):
        for j in range(1, S2+1):
            for k in range(1, S3+1):
                if i + j + k in monster:
                    answer += 1
    
    answer /= S1*S2*S3
    
    return int((1 - answer) * 1000)
