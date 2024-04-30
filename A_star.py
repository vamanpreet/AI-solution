from queue import PriorityQueue

def H(curr, goal):
    count = 0
    for i in range(0,9):
        if curr[i] == goal[i] and curr[i] != 0:
            count = count + 1
    return count

def generate_children(curr):
    children = []
    pos = 0
    for i in range(0,9):
        if curr[i] == 0:
            pos = i
            break
    x = pos//3
    y = pos%3
    
    
    # Up
    if x > 0:
        new_curr = curr[:]
        new_curr[pos], new_curr[pos - 3] = new_curr[pos - 3], new_curr[pos]
        children.append(new_curr)

    # Down
    if x < 2:
        new_curr = curr[:]
        new_curr[pos], new_curr[pos + 3] = new_curr[pos + 3], new_curr[pos]
        children.append(new_curr)

    # Left
    if y > 0:
        new_curr = curr[:]
        new_curr[pos], new_curr[pos - 1] = new_curr[pos - 1], new_curr[pos]
        children.append(new_curr)

    # Right
    if y < 2:
        new_curr = curr[:]
        new_curr[pos], new_curr[pos + 1] = new_curr[pos + 1], new_curr[pos]
        children.append(new_curr)

    return children

def bfs(initial, goal):
    open_list = PriorityQueue()
    closed_list = set()
    cost = H(initial, goal)
    open_list.put((-cost,0, initial, [initial]))  # cost=h(n) + g(n), g(n), node, path
    while not open_list.empty():
        cost, gn, state, path = open_list.get()
        print(-cost)
        if state == goal:
            print("Solution Found")
            for p in path:
                for i in range(0, 8, 3):
                    print(p[i], " ", p[i+1], " ", p[i+2])
                print('----------')
            return

        if tuple(state) not in closed_list:
            closed_list.add(tuple(state))
        
        children = generate_children(state)
        for child in children:
            if tuple(child) not in closed_list:
                new_cost = H(child, goal)+gn
                open_list.put((-new_cost, gn+1, child, path + [child]))

    print('Solution Not Found.')

initial = [2,0,3,1,8,4,7,6,5]
goal = [1,2,3,8,0,4,7,6,5]
bfs(initial, goal)