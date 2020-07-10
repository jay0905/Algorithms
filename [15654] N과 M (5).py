import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
permu = list(permutations(nums, m))

for p in permu:
    for num in p:
        print(num, end=' ')
    print()
