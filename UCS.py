from queue import PriorityQueue

edges = {
    'S': {'A': 1, 'B': 4},
    'A': {'B': 2, 'S': 1, 'C': 5, 'D': 12},
    'C': {'B': 2, 'A': 5, 'D': 3},
    'D': {'A': 12, 'C': 3},
    'B': {'A': 2, 'C': 2, 'S': 4}
}

def ucs(start, goal, edges):
    open_list = PriorityQueue()
    open_list.put((0, start, []))      # cost, node, path

    closed_list = set()

    while open_list:
        cost, node, path = open_list.get()
        if node == goal:
            return [cost, path + [node]]
        
        if node not in closed_list:
            closed_list.add(node)
        
        for neighbour, edgeCost in edges.get(node, {}).items():
            if neighbour not in closed_list:
                totalcost = edgeCost + cost
                open_list.put((totalcost, neighbour, path + [node]))
    
    return None


start_node = 'S'
goal_node = 'D'
cost, path = ucs(start_node, goal_node, edges)
if path:
    print("Path found:", path, "with cost of ", cost)
    cost=0
else:
    print("No path found.")