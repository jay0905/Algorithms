from collections import Counter
import sys

input = sys.stdin.readline

def mean(n, numbers):
    return round(sum(numbers) / n)

def median(n, numbers):
    return numbers[n // 2]

def mode(n, numbers):
    numbers_counter = Counter(numbers).most_common()
    if n > 1:
        if numbers_counter[0][1] == numbers_counter[1][1]:
            return numbers_counter[1][0]
    return numbers_counter[0][0]

def min_max(n, numbers):
    return numbers[-1] - numbers[0]

n = int(input())
numbers = [int(input()) for _ in range(n)]
numbers.sort()

print(mean(n, numbers))
print(median(n, numbers))
print(mode(n, numbers))
print(min_max(n, numbers))
