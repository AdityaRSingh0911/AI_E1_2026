from collections import deque

def bfs(graph, start):
    visited = set()         
    queue = deque([start])   
    
    visited.add(start)

    while queue:
        node = queue.popleft()   
        print(node, end=" ")

        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    'A': ['B', 'C','D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G','H','I'],
    'E': [],
    'H': [],
    'F': [],
    'I': ['L'],
    'G':['J','K'],
    'J': [],
    'K': [],
    'L': [],
}
bfs(graph, 'A')