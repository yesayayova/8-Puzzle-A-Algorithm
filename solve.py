# Check Puzzle-8 inputted exist in the state
def is_contain(puzzle, state):
  for item in state:
    if puzzle.tolist() == item[0].tolist():
      return True
 return False

def solve(puzzle, goal):
 # Initializing state to save nodes has been generated
 # Storage format: Tuple (puzzle, id_node, id_parent, g(n), h(n))
 state = [(puzzle, 0, -1, 0, 0)]

 # Create list visited to collect id_node of nodes has been visited
 visited = []

 # Save g(n) (Cost of n from the initial puzzle-8)
 # Save h(n) (Cost of going from n to a goal node)
 gn, hn = 0, 0

 # Initializing id_curr, current state
 id_curr, current = 0, puzzle.copy()

 # Create id_node, id_parent
 id_node, id_parent = 1, 0
 k = 0
 while True:
  # List id_curr to list visited
  visited.append(id_curr)

 # Return state and visited if the puzzle-8 solvable
 if current.tolist() == goal.tolist():
  result = bestpathing(state, goal)
  for i in range(len(result)):
    for j in range(3):
      print(result[i][j].tolist())
    print()
  break

 # Initializing frontier to collect all children states from current state
 # Storage format: Tuple (puzzle, id_node, id_parent, g(n), h(n))
 frontier = []

 # Update g(n) value
 gn = int(state[id_curr][3]) + 1

 # Generate successor from the current state
 for direction in ['left', 'upper', 'right', 'bottom']:
  move = move_puzzle8(current.copy(), direction)
  if (type(move) != bool) and (is_contain(move, state) == False):
    hn = manhattan(move, goal) # Calculate Manhattan distance
    frontier.append((move, id_node, id_curr, gn, hn))
    id_node += 1 # Increment id_node

 # Merge list state and frontier
 state = state + frontier

 # Create cost to calculate all f(n) of unvisited nodes
 unvisited = [item[1] for item in state if item[1] not in visited]
 cost = [item[3]+item[4] for item in state if item[1] not in visited]

 # Find index of minimum value f(n) from list cost
 winning_curr = int(unvisited[cost.index(min(cost))])

 # Update id_curr, id_parent, current state
 current = state[winning_curr][0]
 id_curr = state[winning_curr][1]
 id_parent = state[winning_curr][2]

 # Return False, False if the puzzle-8 unsolvable
 if (len(state)-1) == len(visited):
  return False, False

def bestpathing(state, goal):
 result, id_node = [], None
 for item in state:
  if item[0].tolist() == goal.tolist():
    id_node = int(item[1])
  break
 while id_node != -1:
  result.append(state[id_node][0])
  id_node = state[id_node][2]
 return result[::-1]
