import sys
input = sys.stdin.readline

n = int(input().strip())
an = list(map(int, input().strip().split()))
a, b, c, d = map(int, input().strip().split())

maxv = -sys.maxsize -1
minv = sys.maxsize

def cal(num, idx, add, sub, mul, div):
    global n, maxv, minv
    if idx == n:
        maxv = max(maxv, num)
        minv = min(minv, num)
        return
    else:
        if add:
            cal(num + an[idx], idx+1, add-1, sub, mul, div)
        if sub:
            cal(num - an[idx], idx+1, add, sub-1, mul, div)
        if mul:
            cal(num * an[idx], idx+1, add, sub, mul-1, div)
        if div:
            cal(int(num / an[idx]), idx+1, add, sub, mul, div-1)

cal(an[0], 1, a, b, c, d)
print(maxv)
print(minv)
