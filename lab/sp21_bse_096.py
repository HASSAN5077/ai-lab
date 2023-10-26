graph = {
    'A': [('B', 3), ('C', 10), ('F', 12)],
    'B': [('A', 3), ('D', 1), ('F', 12)],
    'C': [('A', 10), ('F', 12), ('G', 5)],
    'D': [('B', 1), ('E', 4), ('F', 7)],
    'E': [('D', 4), ('F', 6), ('G', 8)],
    'F': [('C', 12), ('D', 7), ('E', 6), ('G', 9)],
    'G': [('C', 5), ('E', 8), ('F', 9)]
}

visited = []
satartNode = 'A'
def bfs(graph,visited, start):
    queue = []
    queue.append('A')
    visited.append('A')
    while queue:
        node = queue.pop(0)
        print(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)


def dfs(graph, visited, node):
    visited.append(node)
    stack = []
    stack.append(node)
    while stack:
        n = stack[-1]
        print(n)
        stack.pop()
        for nei in graph[n]:
            if nei not in visited:
                stack.append(nei)
                visited.append(nei)





# bfs traversal
print("BFS Traversal")
bfs(graph,visited,satartNode)

visited.clear()

print("\n\nDFS Traversal")
#dfs traversal 
dfs(graph,visited,satartNode)