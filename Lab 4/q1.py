# Question 1

graph = {
'1': set(['2', '4','3']),
'2': set(['1','3','4']),
'3': set(['1','2','4']),
'4': set(['1', '2','3','5']),
'5': set(['4', '6', '7','8']), 
'6': set(['5','7','8']), 
'7': set(['5', '6', '8']),
'8': set(['5', '6', '7']),
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
visited_task1 = dfs(graph, '1', [])
print("Part a")
print("Traversal path using DFS:", visited_task1)
print('')

# Part b

single_path_task2 = find_path(graph, '1', '6')
print("Part b")
print("Single path between 1 & 6:", single_path_task2)
print('')

# Part c
all_paths_task3 = list(all_paths_dfs(graph, '1', '6'))  # Convert generator to list
print("Part c")
print("All paths between 1 & 6:", all_paths_task3)
print('')

# Part d
shortest_path_task4 = find_shortest_path(graph, '1', '6')
print("Part d")
print("Shortest path between 1 & 6:", shortest_path_task4)
print('')