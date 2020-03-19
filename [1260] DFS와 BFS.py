from collections import deque
import sys
input = sys.stdin.readline

def dfs(current_node, matrix, DFS_VISITED):
    DFS_VISITED.append(current_node)

    for search_node in range(len(matrix[current_node])):
        if matrix[current_node][search_node] and search_node not in DFS_VISITED:
            dfs(search_node, matrix, DFS_VISITED)

    return DFS_VISITED


def bfs(matrix, v):
    queue = deque([v])
    BFS_VISITED = [v]

    while queue:
        current_node = queue.popleft()

        for search_node in range(len(matrix[current_node])):
            if matrix[current_node][search_node] and search_node not in BFS_VISITED:
                BFS_VISITED.append(search_node)
                queue.append(search_node)

    return BFS_VISITED


if __name__ == "__main__":
    n, m, v = map(int, input().strip().split())
    matrix = [[0] * (n + 1) for _ in range(n + 1)]
    FIRST_FLAG = True

    for _ in range(m):
        connected = list(map(int, input().strip().split()))
        matrix[connected[0]][connected[1]] = 1
        matrix[connected[1]][connected[0]] = 1

    print(*dfs(v, matrix, []))
    print(*bfs(matrix, v))
