graph_2 = {
'A': set(['B', 'C','D']),
'B': set(['A','E']),
'C': set(['A','F']),
'D': set(['A', 'E','G']),
'E': set(['B', 'D', 'G']), 
'F': set(['C','G']), 
'G': set(['D', 'E', 'F'])
}

def dfs(graph, node, visited):
  if node not in visited:
    visited. append (node)
    for n in graph[node]:
        dfs(graph,n, visited)
  return visited

def find_path(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None

def find_shortest_path(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def all_paths_dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    visited.add(start)
    path = path + [start]
    if start == goal:
        yield path
    else:
        for next_vertex in graph[start] - visited:
            yield from all_paths_dfs(graph, next_vertex, goal, visited, path)
    visited.remove(start)

# Part a
visited_task1 = dfs(graph_2, 'A', [])
print("Part a")
print("Traversal path using DFS:", visited_task1)
print('')

# Part b
single_path_task2 = find_path(graph_2, 'A', 'G')
print("Part b")
print("Single path between A & G:", single_path_task2)
print('')

# Part c
all_paths_task3 = list(all_paths_dfs(graph_2, 'A', 'G'))  # Convert generator to list
print("Part c")
print("All paths between A & G:", all_paths_task3)
print('')
# Part d
shortest_path_task4 = find_shortest_path(graph_2, 'A', 'G')
print("Part d")
print("Shortest path between A & G:", shortest_path_task4)
print('')