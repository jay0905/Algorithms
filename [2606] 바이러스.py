from collections import deque
import sys
input = sys.stdin.readline

computer = int(input())
pair = int(input())

matrix = [[0] * (computer + 1) for _ in range(computer + 1)]
for _ in range(pair):
    connected = list(map(int, input().strip().split()))
    matrix[connected[0]][connected[1]] = 1
    matrix[connected[1]][connected[0]] = 1

VIRUS_START = 1


def bfs(start):
    queue = deque([start])
    VISITED = [start]
    answer = 0
    while queue:
        current_node = queue.popleft()
        for search_node in range(len(matrix[current_node])):
            if matrix[current_node][search_node] and search_node not in VISITED:
                VISITED.append(search_node)
                queue.append(search_node)
                answer += 1
    return answer


print(bfs(VIRUS_START))
