import sys

class Deque:

    def __init__(self):
        self.data = []

    def push_front(self, X):
        self.data.insert(0, X)

    def push_back(self, X):
        self.data.append(X)

    def pop_front(self):
        return self.data.pop(0) if not self.empty() else -1

    def pop_back(self):
        return self.data.pop() if not self.empty() else -1

    def size(self):
        return len(self.data)

    def empty(self):
        return 1 if self.size() == 0 else 0

    def front(self):
        return self.data[0] if not self.empty() else -1

    def back(self):
        return self.data[-1] if not self.empty() else -1

input = sys.stdin.readline
deque = Deque()

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == 'push_front':
        deque.push_front(cmd[1])
    elif cmd[0] == 'push_back':
        deque.push_back(cmd[1])
    elif cmd[0] == 'pop_front':
        print(deque.pop_front())
    elif cmd[0] == 'pop_back':
        print(deque.pop_back())
    elif cmd[0] == 'size':
        print(deque.size())
    elif cmd[0] == 'empty':
        print(deque.empty())
    elif cmd[0] == 'front':
        print(deque.front())
    elif cmd[0] == 'back':
        print(deque.back())
