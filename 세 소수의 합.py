def generate_prime_list(num):
    list = []

    for i in range(2, num):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            list.append(i)
            
    return list
        

def solution(n):
    prime_list = generate_prime_list(n)
    cnt = 0
    
    for i in range(len(prime_list)-2):
        for j in range(i+1, len(prime_list)-1):
            for k in range(j+1, len(prime_list)):
                if prime_list[i] + prime_list[j] + prime_list[k] == n:
                    cnt += 1
    return cnt
