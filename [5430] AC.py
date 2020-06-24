from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    numbers = deque(input()[1:-2].split(","))
    REVERSED = False

    for current in p:
        if current == 'R':
            REVERSED = True if REVERSED == False else False
        if current == 'D':
            if n != 0 and numbers:
                if REVERSED:
                    numbers.pop()
                else:
                    numbers.popleft()
            else:
                print("error")
                break
    else:
        if REVERSED:
            numbers.reverse()

        answer = "["
        for num in numbers:
            answer += num
            answer += ","

        if answer[-1] == ",":
            answer = answer[:-1]

        answer += "]"
        print(answer)
