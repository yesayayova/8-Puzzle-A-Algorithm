#mencari posisi suatu angka pada puxxle
def find_position(value, puzzle):
  for i in range(3):
    for j in range(3):
      if puzzle[i][j] == value:
  return i, j

#menghitung jarak manhattan dari semua posisi angka
def manhattan(puzzle, goal):
  manhattan_value = 0
  for row in range(3):
    for col in range(3):
      value = puzzle[row][col]
      x_puzzle, y_puzzle = find_position(value, puzzle)
      x_goal, y_goal = find_position(value, goal)
      manhattan_value += abs(x_puzzle-x_goal) + abs(y_puzzle-y_goal) #menjumlahkan semua nilai jarak manhattan dari setiap angka
  return manhattan_value
