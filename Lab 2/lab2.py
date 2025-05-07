graph = {
    'a' : ['c'],
    'b' : ['c', 'e'],
    'c' : ['a', 'b', 'd', 'e'],
    'd' : ['e'],
    'e' : ['b', 'c'],
    'f' : []
}

for node , neighbours in graph.items():
    print(node,'->',neighbours)
   