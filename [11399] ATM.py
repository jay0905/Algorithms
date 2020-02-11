import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().strip().split()))

p.sort()

watingTime = 0
sumTime = 0

for i in range(n):
    watingTime += p[i]
    sumTime += watingTime     

print(sumTime)
