import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                
    return distances
    
    
    
# Example Graph
graph = 
{
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('E', 5)],
    'D': [('E', 3)],
    'E': []
}
    
print(dijlstra(graph, 'A'))