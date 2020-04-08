import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

stack = []
o_cnt = 0
ioi_cnt = 0

for alphabet in s:
    if not stack:
        if alphabet == "I":
            stack.append(alphabet)
    else:
        if alphabet == "I":
            if stack[-1] == "O":
                stack.append(alphabet)
            else:
                if o_cnt >= n:
                    ioi_cnt += o_cnt - n + 1
                stack = ["I"]
                o_cnt = 0

        elif alphabet == "O":
            if stack[-1] == "I":
                stack.append(alphabet)
                o_cnt += 1
            else:
                o_cnt -= 1
                if o_cnt >= n:
                    ioi_cnt += o_cnt - n + 1
                stack = []
                o_cnt = 0

if stack:
    if stack[-1] == "O":
        o_cnt -= 1
        
    if o_cnt >= n:
        ioi_cnt += o_cnt - n + 1

print(ioi_cnt)
