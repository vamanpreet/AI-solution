# from collections import deque

# # Function to find the position of the empty tile (0) in the puzzle
# def find_empty(puzzle):
#     for i in range(3):
#         for j in range(3):
#             if puzzle[i][j] == 0:
#                 return i, j

# # Function to generate possible moves from a given puzzle state
# def generate_moves(puzzle):
#     i, j = find_empty(puzzle)
#     moves = []

#     # Move Up
#     if i > 0:
#         new_puzzle = [row[:] for row in puzzle]
#         new_puzzle[i][j], new_puzzle[i - 1][j] = new_puzzle[i - 1][j], new_puzzle[i][j]
#         moves.append(new_puzzle)

#     # Move Down
#     if i < 2:
#         new_puzzle = [row[:] for row in puzzle]
#         new_puzzle[i][j], new_puzzle[i + 1][j] = new_puzzle[i + 1][j], new_puzzle[i][j]
#         moves.append(new_puzzle)

#     # Move Left
#     if j > 0:
#         new_puzzle = [row[:] for row in puzzle]
#         new_puzzle[i][j], new_puzzle[i][j - 1] = new_puzzle[i][j - 1], new_puzzle[i][j]
#         moves.append(new_puzzle)

#     # Move Right
#     if j < 2:
#         new_puzzle = [row[:] for row in puzzle]
#         new_puzzle[i][j], new_puzzle[i][j + 1] = new_puzzle[i][j + 1], new_puzzle[i][j]
#         moves.append(new_puzzle)

#     return moves

# # Breadth-first search algorithm to solve the puzzle
# def bfs(initial, goal):
#     queue = deque([(initial, [])])
#     visited = set()

#     while queue:
#         current, path = queue.popleft()
#         if current == goal:
#             return path

#         visited.add(tuple(map(tuple, current)))

#         for move in generate_moves(current):
#             if tuple(map(tuple, move)) not in visited:
#                 queue.append((move, path + [move]))

#     return None

# # Initial and goal states
# initial = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
# goal = [[2, 8, 1], [0, 4, 3], [7, 6, 5]]

# # Solve the puzzle
# solution = bfs(initial, goal)

# if solution:
#     print("Solution found!")
#     print("Number of moves:", len(solution) - 1)
#     for i, step in enumerate(solution):
#         print("Step", i, ":")
#         for row in step:
#             print(row)
#         print()
# else:
#     print("No solution found.")



# Python3 program to print the path from root 
# node to destination node for N*N-1 puzzle 
# algorithm using Branch and Bound
# The solution assumes that instance of 
# puzzle is solvable

# Importing copy for deepcopy function
import copy

# # Importing the heap functions from python 
# # library for Priority Queue
# from heapq import heappush, heappop
from collections import deque

# # This variable can be changed to change
# # the program from 8 puzzle(n=3) to 15 
# # puzzle(n=4) to 24 puzzle(n=5)...
# n = 3

# bottom, left, top, right
row = [ 1, 0, -1, 0 ]
col = [ 0, -1, 0, 1 ]

# # A class for Priority Queue
# class priorityQueue:
	
# 	# Constructor to initialize a
# 	# Priority Queue
# 	def __init__(self):
# 		self.heap = []

# 	# Inserts a new key 'k'
# 	def push(self, k):
# 		heappush(self.heap, k)

# 	# Method to remove minimum element 
# 	# from Priority Queue
# 	def pop(self):
# 		return heappop(self.heap)

# 	# Method to know if the Queue is empty
# 	def empty(self):
# 		if not self.heap:
# 			return True
# 		else:
# 			return False

# Node structure
class node:
	
	def __init__(self, parent, mat, empty_tile_pos, level):
					
		# Stores the parent node of the 
		# current node helps in tracing 
		# path when the answer is found
		self.parent = parent

		# Stores the matrix
		self.mat = mat

		# Stores the position at which the
		# empty space tile exists in the matrix
		self.empty_tile_pos = empty_tile_pos

		# Stores the number of moves so far
		self.level = level

# # Function to calculate the number of 
# # misplaced tiles ie. number of non-blank
# # tiles not in their goal position
# def calculateCost(mat, final) -> int:
	
# 	count = 0
# 	for i in range(n):
# 		for j in range(n):
# 			if ((mat[i][j]) and
# 				(mat[i][j] != final[i][j])):
# 				count += 1
				
# 	return count

def newNode(mat, empty_tile_pos, new_empty_tile_pos,
			level, parent, final) -> node:
				
	# Copy data from parent matrix to current matrix
	new_mat = copy.deepcopy(mat)

	# Move tile by 1 position
	x1 = empty_tile_pos[0]
	y1 = empty_tile_pos[1]
	x2 = new_empty_tile_pos[0]
	y2 = new_empty_tile_pos[1]
	new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]


	new_node = node(parent, new_mat, new_empty_tile_pos, level)
	return new_node

# Function to print the N x N matrix
def printMatrix(mat):
	
	for i in range(3):
		for j in range(3):
			print("%d " % (mat[i][j]), end = " ")
			
		print()

# # Function to check if (x, y) is a valid
# # matrix coordinate
def isSafe(x, y):
	
	return x >= 0 and x < 3 and y >= 0 and y < 3

# # Print path from root node to destination node
def printPath(root):
	
	if root == None:
		return
	
	printPath(root.parent)
	printMatrix(root.mat)
	print()

# # Function to solve N*N - 1 puzzle algorithm
# # using Branch and Bound. empty_tile_pos is
# # the blank tile position in the initial state.
def solve(initial, empty_tile_pos, final):
	
	# Create a priority queue to store live
	# nodes of search tree
	q = deque()

	# Create the root node
	root = node(None, initial, 
				empty_tile_pos, 0)

	# Add root to list of live nodes
	q.append(root)

	# Finds a live node with least cost,
	# add its children to list of live 
	# nodes and finally deletes it from 
	# the list.
	while q:

		# Find a live node with least estimated
		# cost and delete it from the list of 
		# live nodes
		curr = q.popleft()
			
			# Print the path from root to
			# destination;
		if(curr == final):
			printPath(curr)
			return

		# Generate all possible children
		for i in range(4):
			new_tile_pos = [
				curr.empty_tile_pos[0] + row[i],
				curr.empty_tile_pos[1] + col[i], ]
				
			if isSafe(new_tile_pos[0], new_tile_pos[1]):
				
				# Create a child node
				child = newNode(curr.mat,
								curr.empty_tile_pos,
								new_tile_pos,
								curr.level + 1,
								curr, final,)

				# Add child to list of live nodes
				q.append(child)

# # Driver Code

# # Initial configuration
# # Value 0 is used for empty space
initial = [ [ 1, 2, 3 ], 
			[ 5, 6, 0 ], 
			[ 7, 8, 4 ] ]

# # Solvable Final configuration
# # Value 0 is used for empty space
final = [ [ 1, 2, 3 ], 
		[ 5, 8, 6 ], 
		[ 0, 7, 4 ] ]

# # Blank tile coordinates in 
# # initial configuration
empty_tile_pos = [ 1, 2 ]

# # Function call to solve the puzzle
solve(initial, empty_tile_pos, final)



# from collections import deque


# # Function to get the possible moves for a given state
# def get_moves(state):
#     moves = []
#     empty_index = state.index(0)
#     row, col = divmod(empty_index, 3) # Get row and column of the empty tile
    
#     # Check possible moves: up, down, left, right
#     if row > 0:
#         moves.append((empty_index - 3, 'Up'))
#     if row < 2:
#         moves.append((empty_index + 3, 'Down'))
#     if col > 0:
#         moves.append((empty_index - 1, 'Left'))
#     if col < 2:
#         moves.append((empty_index + 1, 'Right'))
    
#     return moves

# # Function to apply a move to a state
# def apply_move(state, move):
#     new_state = state
#     empty_index, _ = move
#     new_state[state.index(0)], new_state[empty_index] = new_state[empty_index], new_state[state.index(0)]
#     return new_state

# # Function to perform breadth-first search
# def bfs(start_state):
#     visited = set()
#     queue = deque([(start_state, [])])
    
#     while queue:
#         state, path = queue.popleft()
#         visited.add(state)
        
#         if state == goal_state:
#             return path
        
#         for move in get_moves(state):
#             new_state = apply_move(state, move)
#             if new_state not in visited:
#                 queue.append((new_state, path + new_state))
#                 visited.add(new_state)
    
#     return None

# # Example usage
# initial_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]  # Initial state, 0 represents the empty tile
# # Define the goal state
# goal_state = [[2, 8, 1], [0, 4, 3], [7, 6, 5]]
# solution = bfs(initial_state)

# if solution:
#     print("Solution found in", len(solution))
#     for move in solution:
#         print(move)
# else:
#     print("No solution found.")



# from collections import deque
# import copy

# # Function to get the possible moves for a given state
# def get_moves(state):
#     moves = []
#     empty_row, empty_col = next((i, row.index(0)) for i, row in enumerate(state) if 0 in row)  # Get row and column of the empty tile
    
#     # Check possible moves: up, down, left, right
#     if empty_row > 0:
#         moves.append(((empty_row - 1, empty_col), 'Up'))
#     if empty_row < 2:
#         moves.append(((empty_row + 1, empty_col), 'Down'))
#     if empty_col > 0:
#         moves.append(((empty_row, empty_col - 1), 'Left'))
#     if empty_col < 2:
#         moves.append(((empty_row, empty_col + 1), 'Right'))
    
#     return moves

# # Function to apply a move to a state
# def apply_move(state, move):
#     new_state = copy.deepcopy(state)  # Create a deep copy of the state
#     (empty_row, empty_col), (new_row, new_col) = move
#     new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
#     return new_state

# # Function to perform breadth-first search
# def bfs(start_state, goal_state):
#     visited = set()
#     queue = deque([(start_state, [])])
    
#     while queue:
#         state, path = queue.popleft()
#         visited.add(tuple(map(tuple, state)))
        
#         if state == goal_state:
#             return path
        
#         for move in get_moves(state):
#             new_state = apply_move(state, move[0])
#             if tuple(map(tuple, new_state)) not in visited:
#                 queue.append((new_state, path + [move[1]]))
#                 visited.add(tuple(map(tuple, new_state)))
    
#     return None

# # Function to print the matrix
# def print_matrix(matrix):
#     for row in matrix:
#         print(*row)
#     print()

# # Example usage
# initial_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]  # Initial state, 0 represents the empty tile
# goal_state = [[2, 8, 1], [0, 4, 3], [7, 6, 5]]  # Define the goal state

# solution = bfs(initial_state, goal_state)

# if solution:
#     print("Solution found in", len(solution), "moves:")
#     current_state = initial_state
#     print("Initial State:")
#     print_matrix(current_state)
#     for move in solution:
#         new_state = apply_move(current_state, move[0])
#         print("Move", move[1] + ":")
#         print_matrix(new_state)
#         current_state = new_state
# else:
#     print("No solution found.")
