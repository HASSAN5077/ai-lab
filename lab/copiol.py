import heapq

def uniform_cost_search(start, goal, graph):
    frontier = [(0, start)]
    explored = set()
    while frontier:
        (cost, current_node) = heapq.heappop(frontier)
        if current_node == goal:
            return cost
        explored.add(current_node)
        for neighbor, neighbor_cost in graph[current_node].items():
            if neighbor not in explored:
                heapq.heappush(frontier, (cost + neighbor_cost, neighbor))
    return -1 # If goal is not reachable from start

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 3},
    'C': {'D': 2},
    'D': {}
}
start = 'A'
goal = 'D'
cost = uniform_cost_search(start, goal, graph)
print(cost) # Output: 4
