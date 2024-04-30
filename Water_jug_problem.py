from collections import deque

# Define a state class to represent the state of water in the jugs
class State:
    def __init__(self, jug_1, jug_2):
        self.jug_1 = jug_1
        self.jug_2 = jug_2

    def __eq__(self, other):
        return self.jug_1 == other.jug_1 and self.jug_2 == other.jug_2

    def __hash__(self):
        return hash((self.jug_1, self.jug_2))

    def __repr__(self):
        return f"({self.jug_1}, {self.jug_2})"

# Perform breadth-first search to find a sequence of actions leading to the desired state
def find_solution(capacity_jug_1, capacity_jug_2, target):
    start_state = State(0, 0)
    visited = set()
    queue = deque([(start_state, [])])

    while queue:
        current_state, actions = queue.popleft()
        if current_state.jug_2 == target or current_state.jug_1 == target:
            return actions

        visited.add(current_state)

        # Generate all possible next states from the current state
        next_states = []

        # Fill jug 1
        next_state = State(capacity_jug_1, current_state.jug_2)
        if next_state not in visited:
            next_states.append((next_state, actions + [f"({capacity_jug_1}, {current_state.jug_2})  Fill jug 1"]))

        # Fill jug 2
        next_state = State(current_state.jug_1, capacity_jug_2)
        if next_state not in visited:
            next_states.append((next_state, actions + [f'({current_state.jug_1}, {capacity_jug_2})  Fill jug 2']))

        # Empty jug 1
        next_state = State(0, current_state.jug_2)
        if next_state not in visited:
            next_states.append((next_state, actions + [f'(0, {current_state.jug_2})  Empty jug 1']))

        # Empty jug 2
        next_state = State(current_state.jug_1, 0)
        if next_state not in visited:
            next_states.append((next_state, actions + [f'({current_state.jug_1}, 0)  Empty jug 2']))

        # Pour water from jug 1 to jug 2
        pour_amount = min(current_state.jug_1, capacity_jug_2 - current_state.jug_2)
        next_state = State(current_state.jug_1 - pour_amount, current_state.jug_2 + pour_amount)
        if next_state not in visited:
            next_states.append((next_state, actions + [f'({current_state.jug_1 - pour_amount}, {current_state.jug_2 + pour_amount})  Pour from jug 1 to jug 2']))

        # Pour water from jug 2 to jug 1
        pour_amount = min(current_state.jug_2, capacity_jug_1 - current_state.jug_1)
        next_state = State(current_state.jug_1 + pour_amount, current_state.jug_2 - pour_amount)
        if next_state not in visited:
            next_states.append((next_state, actions + [f'({current_state.jug_1 + pour_amount}, {current_state.jug_2 - pour_amount})  Pour from jug 2 to jug 1']))

        queue.extend(next_states)

    return None

# Take user input for capacities and target amount
capacity_jug_1 = int(input("Enter the capacity of jug 1: "))
capacity_jug_2 = int(input("Enter the capacity of jug 2: "))
target = int(input("Enter the target amount: "))

# Find the sequence of actions to achieve the target amount
solution = find_solution(capacity_jug_1, capacity_jug_2, target)
if solution:
    print("Steps to achieve the target amount:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
