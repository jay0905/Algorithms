import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1]
DIVIDE = 1000000000

if n > 0:
    for i in range(2, n + 1):
        dp.append((dp[i - 1] + dp[i - 2]) % DIVIDE)

    print(1)
    print(dp[n])

elif n < 0:
    for i in range(2, abs(n) + 1):
        num = (dp[i - 2] - dp[i - 1])
        if num >= 0:
            dp.append(num % DIVIDE)
        else:
            dp.append(-(abs(num) % DIVIDE))

    if dp[-1] > 0:
        print(1)
    elif dp[-1] < 0:
        print(-1)
    else:
        print(0)
    print(abs(dp[-1]))

else:
    print(0)
    print(0)
