graph = {
    'A': set(['B', 'E', 'C']),
    'B': set(['D', 'E']),
    'C': set([]),
    'D': set([]),
    'E': set([])
}

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

print(find_shortest_path(graph, 'A', 'E'))



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

graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'C', 'D']),
    'C': set(['A', 'B', 'D']),
    'D': set(['B', 'C', 'E']),
    'E': set(['D', 'F']),
    'F': set(['E', 'G']),
    'G': set(['F', 'H']),
    'H': set(['G', 'I']),
    'I': set(['H', 'J']),
    'J': set(['I', 'K']),
    'K': set(['J'])
}

print(list(all_paths_dfs(graph, 'A', 'D')))