import heapq

# Define the list of elements with priorities
elements = [(0, 'null', 'A'), (2, 'A', 'B'), (3, 'A', 'C'), (5, 'B', 'E'), (9, 'B', 'F')]

# Create an empty priority queue
priority_queue = []

# Populate the priority queue with elements
for element in elements:
    heapq.heappush(priority_queue, element)

# Retrieve and print elements in order of their priorities
while priority_queue:
    cost, parent, child = heapq.heappop(priority_queue)
    print(f"cost: {cost}, Parent: {parent}, Child: {child}")
