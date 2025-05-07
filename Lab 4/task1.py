graph1={
'A':['B','E','C'],
'B':['D','E'],
'C':[],
'D':[],
'E':[]
}
def dfs(graph, node, visited):
  if node not in visited:
    visited. append (node)
    for n in graph[node]:
        dfs(graph,n, visited)
  return visited
visited = dfs(graph1, 'A', [])
print(visited)