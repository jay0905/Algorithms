import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
hear = set()
for _ in range(n):
    hear.add(input().strip())

see = set()
for _ in range(m):
    see.add(input().strip())

hear_see = list(hear & see)
hear_see.sort()

print(len(hear_see))
for person in hear_see:
    print(person)
