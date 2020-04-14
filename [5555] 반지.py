import sys
sys = sys.stdin.readlines

target = input()
n = int(input())
rings = [input() for _ in range(n)]
answer = 0

for ring in rings:
    two_ring = ring * 2
    if target in two_ring:
        answer += 1

print(answer)
