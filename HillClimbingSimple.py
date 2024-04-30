from queue import PriorityQueue

def H(curr, goal):
    count = 0
    for i in range(0,9):
        if curr[i] != goal[i] and curr[i] != 0:
            count = count + 1
    return count

def generate_children(curr, h, goal):
    child = []
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
        new_h = H(new_curr, goal)
        if new_h < h:
            return child

    # Down
    if x < 2:
        new_curr = curr[:]
        new_curr[pos], new_curr[pos + 3] = new_curr[pos + 3], new_curr[pos]
        new_h = H(new_curr, goal)
        if new_h < h:
            return child

    # Left
    if y > 0:
        new_curr = curr[:]
        new_curr[pos], new_curr[pos - 1] = new_curr[pos - 1], new_curr[pos]
        new_h = H(new_curr, goal)
        if new_h < h:
            return child

    # Right
    if y < 2:
        new_curr = curr[:]
        new_curr[pos], new_curr[pos + 1] = new_curr[pos + 1], new_curr[pos]
        new_h = H(new_curr, goal)
        if new_h < h:
            return child

    return None

def bfs(initial, goal):
    heuristic = H(initial, goal)
    prev = None
    curr = initial
    path = [initial]
    while curr:
        if curr == goal:
            print("Solution Found")
            for p in path:
                for i in range(0, 8, 3):
                    print(p[i], " ", p[i+1], " ", p[i+2])
                print('----------')
            return
        
        child = generate_children(curr, heuristic, goal)
        prev = curr
        curr = child
        path = path + [child]

    print('Solution Not Found.')
    for p in path:
        if p:
            for i in range(0, 8, 3):
                print(p[i], " ", p[i+1], " ", p[i+2])
            print('----------')

initial = [2,0,3,1,8,4,7,6,5]
goal = [1,2,3,8,0,4,7,6,5]
bfs(initial, goal)