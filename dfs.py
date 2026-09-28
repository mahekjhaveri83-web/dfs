graph = {
    'A' : ['B','H'],
    'B' : ['C','E'],
    'C' : ['D'],
    'D' : [],
    'E' : ['F','G'],
    'F' : [],
    'G' : [],
    'H' : ['I','J'],
    'I' : [],
    'J' : ['K'],
    'K' : []
    }

stack = []
visited = []
start = 'A'
stack.append(start)

while stack:
    node = stack.pop()
    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)
