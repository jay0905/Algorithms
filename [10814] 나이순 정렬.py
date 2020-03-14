import sys, collections
input = sys.stdin.readline

n = int(input())

members = [[x for x in input().strip().split()] for y in range(n)]
members.sort(key=lambda x:int(x[0]))

for member in members:
    print(member[0], member[1])
