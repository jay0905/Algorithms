import sys
input = sys.stdin.readline

for _ in range(int(input())):
    alphabet_cnt = {}
    m = input().strip()
    length = len(m)

    for i, letter in enumerate(m):

        if letter not in alphabet_cnt:
            alphabet_cnt[letter] = 1
        else:
            alphabet_cnt[letter] += 1

        if alphabet_cnt[letter] == 3:
            if i == length - 1:
                print("FAKE")
                break
            if letter != m[i + 1]:
                print("FAKE")
                break
            else:
                alphabet_cnt[letter] = -1
    else:
        print("OK")
