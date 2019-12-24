import sys
input = sys.stdin.readline

n = int(input())
inputs = list(map(int, input().split()))
stack = [0]
outputs = [-1 for _ in range(n)]

for i in range(1, n):
    # stack을 pop하는 반복문
    while stack and inputs[stack[-1]] < inputs[i]:
        outputs[stack[-1]] = inputs[i]
        stack.pop()
    stack.append(i)
    i += 1

for i in outputs:
    print(i, end=' ')
