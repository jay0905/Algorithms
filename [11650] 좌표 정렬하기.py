import sys, collections
input = sys.stdin.readline

n = int(input())
dots = [[int(x) for x in input().split()] for y in range(n)]
dots.sort(key=lambda x:(x[0], x[1]))

for dot in dots:
    print(dot[0], dot[1])
