graph = {
    '1': ['2', '3', '4'],
    '2': ['1', '3', '4'],
    '3': ['1', '2', '4'],
    '4': ['1', '2', '3', '5'],
    '5': ['4', '6', '7', '8'],
    '6': ['5', '7', '8'],
    '7': ['5', '6', '8'],
    '8': ['5', '6', '7']
}

# part a
# from collections import deque

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

# print("BFS from '1':")
# bfs(graph, '1')

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

# print("All Paths from '1' to '6':")
# paths = find_all_paths(graph, '1', '6')
# for p in paths:
#     print(p)


# part c 

from collections import deque
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

print("Shortest Path from '1' to '6':", bfs_shortest_path(graph, '1', '6'))


