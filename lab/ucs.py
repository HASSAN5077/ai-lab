import heapq

def uniform_cosst_search(graph,start, goal):
    visisted = set()
    queue = [(0, start)]
    parent = {}
    cost = {node: float('inf') for node in graph}
    cost[start] = 0

    while queue:
        cur_cost, cur_node = heapq.heappop(queue)

        if(cur_node in visisted):
            continue

        visisted.add(cur_node)

        if(cur_node == goal):
            path = []
            while cur_node is not None:
                path.append(cur_node)
                cur_node = parent.get(cur_node)

            return [path[::-1],cur_cost]
        
        for neighbor, edge_cost in graph[cur_node]:
            new_cost = cost[cur_node] + edge_cost
            if new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = cur_node
                heapq.heappush(queue, (new_cost, neighbor))
    return []



graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('E', 5), ('F', 6)],
    'C': [('A', 3), ('D', 2), ('E', 4)],
    'D': [('C', 2), ('E', 3), ('F', 2)],
    'E': [('B', 5), ('C', 4), ('D', 3)],
    'F': [('B', 6), ('D', 2)]
}


start = 'A'
goal = 'F'

ans = uniform_cosst_search(graph,start,goal)

print(ans[0] , "and he cost is: " , ans[1])

