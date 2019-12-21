import sys

class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.size() == 0:
            return -1
        else:
            num = self.data.pop()
            return num

    def size(self):
        return len(self.data)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.size() == 0:
            return -1
        else:
            return self.data[-1]

n = int(input())
stack = Stack()

while n:
    input = sys.stdin.readline
    input = input().split()
    cmd = input[0]
    if cmd == 'push':
        stack.push(int(input[1]))
    elif cmd == 'pop':
        print(stack.pop())
    elif cmd == 'size':
        print(stack.size())
    elif cmd == 'empty':
        print(stack.empty())
    else:
        print(stack.top())
    n -= 1
