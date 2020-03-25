def solution(n):
    n_one = bin(n).count('1')
    
    while True:
        n += 1
        
        if n_one == bin(n).count('1'):
            return n
