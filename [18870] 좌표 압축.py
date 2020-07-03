import sys
input = sys.stdin.readline

n = int(input())
locations = list(map(int, input().split()))
sorted_locations = sorted(locations)

compressed = {}
compressed_num = 0

for num in sorted_locations:
    if num not in compressed:
        compressed[num] = compressed_num
        compressed_num += 1

for location in locations:
    print(compressed[location], end=" ")
