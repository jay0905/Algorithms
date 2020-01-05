import sys, collections

n = int(sys.stdin.readline())
card = collections.deque(int(i+1) for i in range(n))

while len(card) > 1:
	card.popleft()
	card.append(card[0])
	card.popleft()

print(card[0])
