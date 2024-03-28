from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)

# Example graph represented as an adjacency list
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

# Start BFS from node 'A'
bfs(graph, 'A')

#Algorithm

'''
BFS(graph, start):
    Create an empty set called visited
    Create an empty queue called queue
    Add start node to the queue

    While queue is not empty:
        Dequeue a node from the queue
        If node has not been visited:
            Mark node as visited
            Process node (e.g., print it)
            Enqueue all unvisited neighbors of node



'''