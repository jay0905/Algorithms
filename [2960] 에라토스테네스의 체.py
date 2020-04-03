import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
numbers = [True for _ in range(n + 1)]

def find_k(n, k, numbers):
    cnt = 0

    for i in range(2, n + 1):
        if numbers[i] == True:
            for j in range(i, n + 1, i):
                if numbers[j]== True:
                    numbers[j] = False
                    cnt += 1

                    if cnt == k:
                        return j

print(find_k(n, k, numbers))
