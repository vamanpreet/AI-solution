import copy
from collections import deque

class BlockWorld:
    def __init__(self, initial_state, final_state):
        self.initial_state = initial_state
        self.final_state = final_state

    def generate_children(self, curr_state):
        children = []
        for i, stack in enumerate(curr_state):
            if stack:  
                for j in range(len(curr_state)):
                    if i != j:
                        new_state = copy.deepcopy(curr_state)
                        new_state[j].append(new_state[i].pop())
                        children.append(new_state)
        return children

    def search(self):
        if self.initial_state == self.final_state:
            print("Initial State is Final State. No Need to Search.")
            return

        visited = set()
        queue = deque([(self.initial_state, [])])  # (State, Path from Initial State to this State)
        while queue:
            state, path = queue.popleft()
            if state == self.final_state:
                print("Solution found")
                for i in path:
                    print(i)
                return

            visited.add(tuple(map(tuple, state)))       # Convert state to tuple to make it hashable 
            children = self.generate_children(state)
            for child in children:
                if tuple(map(tuple, child)) not in visited:
                    queue.append((child, path + [child]))

        print("Solution not found.")

# Test the BlockWorld class
initial_state = [['A'], ['B', 'C'], []]
final_state = [['A', 'B', 'C'], [], []]

print("Initial State:", initial_state)

block_world = BlockWorld(initial_state, final_state)
block_world.search()
