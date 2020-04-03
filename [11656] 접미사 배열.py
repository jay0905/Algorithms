import sys
input = sys.stdin.readline

s = input().strip()
suffixes = []

for i in range(len(s)):
    suffixes.append(s[i:])

suffixes.sort()

for suffix in suffixes:
    print(suffix)
