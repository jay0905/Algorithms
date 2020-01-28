import sys
input = sys.stdin.readline

t = int(input())
d = [0]*101
d[1] = d[2] = d[3] = 1

def dp(n):
	if n > 5:
		for i in range(4, n+1):
			d[i] = d[i-3] + d[i-2]
	return d[n]

for i in range(t):
	n = int(input())
	print(dp(n))
