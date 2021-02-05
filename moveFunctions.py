# Move the Puzzle-8 with input direction
def move_puzzle8(current, direction):
  x, y = find_position(0, current) # Find empty tile position

  # Move left piece of empty piece to empty piece
  if direction == 'left' and y != 0:
    current[x][y], current[x][y-1] = current[x][y-1], current[x][y]
  
  # Move upper piece of empty piece to empty piece
  elif direction == 'upper' and x != 0:
    current[x][y], current[x-1][y] = current[x-1][y], current[x][y]

  # Move right piece of empty piece to empty piece
  elif direction == 'right' and y != 2:
    current[x][y], current[x][y+1] = current[x][y+1], current[x][y]

  # Move bottom piece of empty piece to empty piece
  elif direction == 'bottom' and x != 2:
    current[x][y], current[x+1][y] = current[x+1][y], current[x][y]

  # If Puzzle-8 cannot move in the chosen direction, return boolean False
  else:
    return False
    
  return current
