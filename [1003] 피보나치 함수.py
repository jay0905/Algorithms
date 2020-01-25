import sys
input = sys.stdin.readline

t = int(input())
f0 = [1, 0]  # f0[n] 은 fibonacci(n)에서 0이 출력된 횟수
f1 = [0, 1]

def cal(n):
	length = len(f0)
	if n >= length:
		for i in range(length, n+1):
			f0.append(f0[i-1] + f0[i-2])
			f1.append(f1[i-1] + f1[i-2])
	print(f0[n], f1[n])

for i in range(t):
	n = int(input())
	cal(n)
