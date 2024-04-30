import copy

class BlockWorld:
    def __init__(self, initial_state, final_state):
        self.initial_state = initial_state
        self.final_state = final_state

    def generate_children(self, curr_state):
        children = []
        # Iterate over each stack (list) in the current state
        for i, stack in enumerate(curr_state):
            # Check if the stack is not empty
            if stack:  
                # Iterate over each stack (list) again to find other stacks to move blocks to
                for j in range(len(curr_state)):
                    # Ensure we're not moving blocks from and to the same stack
                    if i != j:
                        # Create a deep copy of the current state to avoid modifying it directly
                        new_state = copy.deepcopy(curr_state)
                        # Move the top block from stack i to stack j
                        new_state[j].append(new_state[i].pop())
                        # Add the resulting state to the list of children
                        children.append(new_state)
        return children

    def search(self):
        if self.initial_state == self.final_state:
            print("Initial State is Final State. No Need to Search.")
            return

        visited = set()
        stack = [(self.initial_state, [])]  
        while stack:
            state, path = stack.pop()
            if state == self.final_state:
                print("Solution found")
                for i in path:
                    print(i)
                return

            visited.add(tuple(map(tuple, state)))  
            children = self.generate_children(state)
            for child in children:
                if tuple(map(tuple, child)) not in visited:
                    stack.append((child, path + [child]))

        print("Solution not found.")

# Test the BlockWorld class
initial_state = [['A'], ['B', 'C'], []]
final_state = [['A', 'B', 'C'], [], []]

print("Initial State:", initial_state)

block_world = BlockWorld(initial_state, final_state)
block_world.search()
