graph = {
    'A': ['B', 'E'],
    'B': ['F'],
    'C': ['G'],
    'D': ['E', 'H'],
    'E': ['A', 'D', 'H'],
    'F': ['B', 'G', 'I', 'J'],
    'G': ['C', 'F', 'J'],
    'H': ['D', 'E', 'I'],
    'I': ['F', 'H'],
    'J': ['F', 'G']
}

def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]
    
    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
            
            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
                
    return explored

print(bfs_connected_component(graph, 'A'))
