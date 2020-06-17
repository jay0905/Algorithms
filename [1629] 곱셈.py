import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def solve(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b % 2 == 1:
        return solve(a, b - 1) * a
    elif b % 2 == 0:
        x = solve(a, b // 2) % c
        return (x ** 2) % c

print(solve(a, b) % c)
