import sys

class circularQueue():

	def __init__(self, n):
		self.maxCount = n
		self.data = [''] * n
		self.count = 0
		self.front = -1
		self.rear = -1

	def size(self):
		return self.count

	def isEmpty(self):
		return self.count == 0

	def enqueue(self, item):
		if self.count == self.maxCount:
			raise IndexError('Queue Full')
		self.rear = (self.rear + 1) % self.maxCount
		self.data[self.rear] = item
		self.count += 1

	def dequeue(self):
		if self.isEmpty():
			raise IndexError('Queue Empty')
		self.front = (self.front + 1) % self.maxCount
		self.count -= 1
		return self.data[self.front]

n, k = map(int, sys.stdin.readline().strip().split())
circle = circularQueue(n)

for i in range(n):
	circle.enqueue(i+1)

outputs= "<"

while True:
	for i in range(k-1):
		circle.enqueue(circle.dequeue())
	outputs += str(circle.dequeue())
	if circle.isEmpty():
		break
	else:
		outputs += ", "

sys.stdout.write(outputs+">")
