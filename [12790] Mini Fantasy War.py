import sys
input = sys.stdin.readline

HP = 0
MP = 1
ATTACK = 2
SHILED = 3

for _ in range(int(input())):
    nums = list(map(int, input().split()))
    power_sum = 0

    if nums[HP] + nums[HP + 4] < 1:
        power_sum += 1
    else:
        power_sum += nums[HP] + nums[HP + 4]

    if nums[MP] + nums[MP + 4] < 1:
        power_sum += 5 * 1
    else:
        power_sum += 5 * (nums[MP] + nums[MP + 4])

    if nums[ATTACK] + nums[ATTACK + 4] > 0:
        power_sum += 2 * (nums[ATTACK] + nums[ATTACK + 4])

    power_sum += 2 * (nums[SHILED] + nums[SHILED + 4])

    print(power_sum)
