graph = {
    'A': ['B', 'C', 'D'], 
    'B': ['A', 'E'], 
    'C': ['A', 'F'], 
    'D': ['A', 'E', 'G'], 
    'E': ['D', 'B', 'G'], 
    'F': ['C', 'G'], 
    'G': ['F', 'E', 'D'],  
}

# part a 

from collections import deque

# def bfs(graph, start):
#     queue = deque([start])
#     visited = set([start])

#     while queue:
#         node = queue.popleft()
#         print(node, end=" ")

#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(neighbor)

# print("BFS from 'A':")
# bfs(graph, 'A')


# part b 

# def find_all_paths(graph, start, end, path=[]):
#     path = path + [start]

#     if start == end:
#         return [path]

#     all_paths = []

#     for neighbor in graph[start]:
#         if neighbor not in path:
#             new_paths = find_all_paths(graph, neighbor, end, path)
#             for p in new_paths:
#                 all_paths.append(p)

#     return all_paths

# print("All Paths from 'A' to 'G':")
# paths = find_all_paths(graph, 'A', 'G')
# for p in paths:
#     print(p)


# part c 

def bfs_shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        node, path = queue.popleft()
        if node == end:
            return path  

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

print("Shortest Path from 'A' to 'G':", bfs_shortest_path(graph, 'A', 'G'))


