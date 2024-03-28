def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Start DFS from node 'A'
dfs(graph, 'A')


# Alogorithm
'''
DFS(graph, start):
    Create an empty set called visited
    Call DFSRecursive(start, visited, graph)

DFSRecursive(node, visited, graph):
    Add node to visited set
    Process node (e.g., print it)

    For each neighbor of node:
        If neighbor is not in visited set:
            Recursively call DFSRecursive(neighbor, visited, graph)


'''