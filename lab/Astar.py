
import heapq
class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
        self.priority = cost + heuristic

    def __lt__(self, other):
        return self.priority < other.priority

def a_star_search(graph, start, goal, heuristic):
    open_set = []
    closed_set = set()

    start_node = Node(start, None, 0, heuristic[start])
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal:
            path = []
            cost = current_node.cost
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return [path[::-1], cost]

        if current_node.state in closed_set:
            continue

        closed_set.add(current_node.state)

        for neighbor, cost in graph[current_node.state]:
            if neighbor not in closed_set:
                neighbor_node = Node(neighbor, current_node, current_node.cost + cost, heuristic[neighbor])
                heapq.heappush(open_set, neighbor_node)

    return []

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('E', 5), ('F', 6)],
    'C': [('A', 3), ('D', 2), ('E', 4)],
    'D': [('C', 2), ('E', 3), ('F', 2)],
    'E': [('B', 5), ('C', 4), ('D', 3)],
    'F': [('B', 6), ('D', 2)]
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 5,
    'F': 0
}

start = 'A'
goal = 'F'

result = a_star_search(graph, start, goal, heuristic)

print(result[0], " cost is: " , result[1])