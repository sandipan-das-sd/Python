def dfs(graph, cur, visited, rec_stack):
    visited[cur] = True
    rec_stack[cur] = True #rec_stack is used to keep track of the visited elements
    
    for neighbor in graph[cur]:
        if not visited[neighbor]:
            if dfs(graph, neighbor, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True
    
    rec_stack[cur] = False
    return False

def is_cyclic(graph, vertices):
    visited = [False] * vertices
    rec_stack = [False] * vertices
    
    for i in range(vertices):
        if not visited[i]:
            if dfs(graph, i, visited, rec_stack):
                return True
    return False

# Example usage:
graph = {
    0: [1],
    1: [2],
    2: [3],
    3: [1]
}
vertices = 4

if is_cyclic(graph, vertices):
    print("Cycle exists in the graph.")
else:
    print("No cycle exists in the graph.")
