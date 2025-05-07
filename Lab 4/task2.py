graph = {
    'A': set(['B', 'E', 'C']),
    'B': set(['D', 'E']),
    'C': set([]),
    'D': set([]),
    'E': set([])
}

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

print(find_path(graph, 'A', 'E'))