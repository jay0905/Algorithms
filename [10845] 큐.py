import sys

class Queue:

	def __init__(self):
		self.data = []

	def push(self, x):
		self.data.append(x)

	def pop(self):
		return self.data.pop(0) if self.size() != 0 else -1

	def size(self):
		return len(self.data)

	def empty(self):
		return 1 if self.size() == 0 else 0

	def front(self):
		return self.data[0] if self.size() != 0 else -1

	def back(self):
		return self.data[self.size()-1] if self.size() != 0 else -1

input = sys.stdin.readline
n = int(input())
q = Queue()

for i in range(n):
	cmd = input().split()
	if cmd[0] == 'push':
		q.push(cmd[1])
	elif cmd[0] == 'pop':
		print(q.pop())
	elif cmd[0] == 'size':
		print(q.size())
	elif cmd[0] == 'empty':
		print(q.empty())
	elif cmd[0] == 'front':
		print(q.front())
	elif cmd[0] == 'back':
		print(q.back())
