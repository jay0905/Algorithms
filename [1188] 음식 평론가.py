import sys
input = sys.stdin.readline

def gcd(n, m):
    if n % m == 0:
        return m
    return gcd(m, n % m)

n, m = map(int, input().strip().split())
print(m - gcd(n, m))
