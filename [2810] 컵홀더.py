import sys
input = sys.stdin.readline

n = int(input())
seats = input().strip()
holder_seats = ""
FIRST = True

for seat in seats:
    if seat == "S":
        holder_seats += "*S"
    elif seat == "L":
        if FIRST:
            holder_seats += "*L"
            FIRST = False
        else:
            holder_seats += "L"
            FIRST = True
holder_seats += "*"

holder_cnt = 0
stack = []
for seat in holder_seats:
    if stack:
        if seat == "*":
            if stack[-1].isalpha():
                stack.pop()
                holder_cnt += 1
        else:
            if stack[-1] == "*":
                stack.pop()
                holder_cnt += 1
            else:
                stack.pop()
                stack.append(seat)
    else:
        stack.append(seat)

print(holder_cnt)
