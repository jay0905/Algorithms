from collections import deque
import sys
sys = sys.stdin.readlines

n = int(input())
words = [input() for _ in range(n)]
different_words = []

for word in words:
    if not different_words:
        different_words.append(word)
    else:
        for different_word in different_words:
            if len(different_word) == len(word):
                two_words = different_word * 2
                if word in two_words:
                    break
        else:
            different_words.append(word)

print(len(different_words))
