'''
All path from source to targer
modified dfs

DFS(graph, visited, path, current, target):
    if current == target:
        print(path)
        return
    
    visited[current] = True
    path.append(current)

    for each neighbor in graph[current]:
        if not visited[neighbor]:
            DFS(graph, visited, path, neighbor, target)
    
    path.pop()
    visited[current] = False



'''


def dfs(graph, visited, path, current, target):
    if current == target:
        print(path)
        return
    
    visited[current] = True
    path.append(current)

    for neighbor in graph[current]:
        if not visited[neighbor]:
            dfs(graph, visited, path, neighbor, target)
    
    path.pop()
    visited[current] = False

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
visited = {node: False for node in graph}
path = []
dfs(graph, visited, path, 'A', 'F')
