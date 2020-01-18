import sys
input = sys.stdin.readline

n = int(input())
numN = list(map(int, input().strip().split()))
m = int(input())
numM = list(map(int, input().strip().split()))

def BinarySearch(target, list):
    lower = 0
    upper = len(list) - 1
    while lower <= upper:
        mid = (lower + upper) // 2
        if list[mid] < target:
            lower = mid + 1
        elif list[mid] > target:
            upper = mid - 1
        else:
            return True
    return False

numN.sort()
for i in range(m):
    if BinarySearch(numM[i], numN):
        print(1)
    else:
        print(0)
