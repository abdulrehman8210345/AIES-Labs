graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'E'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
}

from collections import deque

def bfs_shortest_path(graph, start, end):
    queue = deque()
    queue.append((start, [start]))
    visited = set([start])

    while queue:
        node, path = queue.popleft()
        if node == end:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

print("Shortest path from G to D:", bfs_shortest_path(graph, 'G', 'D'))
