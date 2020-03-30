출처: https://programmers.co.kr/learn/courses/30/lessons/12987

def solution(A, B):
    A.sort()
    B.sort()
    result = 0
    last = 0
    
    for i in range(len(A)):
        for j in range(last, len(B)):
            if A[i] < B[j]:
                result += 1
                last = j + 1
                break
    
    return result
