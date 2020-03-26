# 그냥 풀이
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
        
def solution(arr):
    while len(arr) > 1:
        one = arr.pop()
        two = arr.pop()
        arr.append(one * two // gcd(one, two))
        
    return arr[0]
    
# 내장함수 사용
from math import gcd

def lcm(x, y):
    return x * y // gcd(x, y)
        
def solution(arr):
    while len(arr) > 1:
        arr.append(lcm(arr.pop(), arr.pop()))
        
    return arr[0]
