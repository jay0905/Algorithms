from collections import deque
import sys
input = sys.stdin.readline

def bfs(queue, visited):
    queue.append((n, 0))
    visited.add(n)

    while queue:
        current, cnt = queue.popleft()

        if current == k:
            return cnt

        cnt += 1

        for x in (current - 1, current + 1, current * 2):
            if 0 <= x <= MAXSIZE and x not in visited:
                queue.append((x, cnt))
                visited.add(x)


if __name__ == "__main__":
    n, k = map(int, input().strip().split())
    queue = deque()
    visited = set()
    MAXSIZE = 100000

    print(bfs(queue, visited))
