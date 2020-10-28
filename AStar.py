def aStar(rubik):
    goal     = [[0, 1 ,2],
               [3, 4, 5],
               [6, 7, 8]]
    current  = rubik
    explored = [current]
    
    while True:
        #jika goal-state ditemukan
        if current == goal:
            return 1
            break
        
        frontier = []
        frontier_cost = []
        explored.append(current)

        if (right(current) is not False) and (right(current) not in explored):
            x = right(current)
            frontier.append(x)
            frontier_cost.append(heuristik(x))

        if (left(current) is not False) and (left(current) not in explored):
            x = left(current)
            frontier.append(x)
            frontier_cost.append(heuristik(x))

        if (top(current) is not False) and (top(current) not in explored):
            x = top(current)
            frontier.append(x)
            frontier_cost.append(heuristik(x))

        if (bottom(current) is not False) and (bottom(current) not in explored):
            x = bottom(current)
            frontier.append(x)
            frontier_cost.append(heuristik(x))
            
        #jika goal-state tidak ditemukan
        if len(frontier) == 0:
            #print("Not Found")
            return 0
            break
        
        #mencari suksesor dengan nilai heuristik terkecil
        index = 0
        for i in range(len(frontier)):
            if frontier_cost[index] > frontier_cost[i]:
                index = i
                
        current = frontier[index]
        
 #=======================================================
 #Berbagai fungsi perpindahan angka dalam puzzle
 #=======================================================
 
 def right(x):
    y = []
    for i in range(3):
        y.append(x[i].copy())
            
    col , row = position(y)
    if row == 2:
        return False
    
    temp = y[col][row]
    y[col][row] = y[col][row+1]
    y[col][row+1] = temp
    
    return y

def left(x):
    y = []
    for i in range(3):
        y.append(x[i].copy())
            
    col , row = position(y)
    if row == 0:
        return False
    
    temp = y[col][row]
    y[col][row] = y[col][row-1]
    y[col][row-1] = temp
    
    return y

def top(x):
    y = []
    for i in range(3):
        y.append(x[i].copy())
            
    col , row = position(y)
    if col == 0:
        return False
    
    temp = y[col][row]
    y[col][row] = y[col-1][row]
    y[col-1][row] = temp
    
    return y

def bottom(x):
    y = []
    for i in range(3):
        y.append(x[i].copy())
            
    col , row = position(y)
    if col == 2:
        return False
    
    temp = y[col][row]
    y[col][row] = y[col+1][row]
    y[col+1][row] = temp
    
    return y

#================================================
#Fungsi untuk menentukan posisi angka 0
#================================================

def position(value):
    for i in range(3):
        for j in range(3):
            if value[i][j] == 0:
                  return i, j
                  
#================================================
#Fungsi heuristik pada setiap state
#================================================
def heuristik(curr):
    x = 0
    for i in range(3):
        for j in range(3):
                x += density(curr, i, j)
    return x
    
def density(curr, y, x):
    value = curr[y][x]
    goal  = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]]
    for i in range(3):
        for j in range(3):
            if goal[i][j] == value:
                return abs(i-y)+abs(j-x)

#============================================================
#Fungsi untuk membuat kondisi awal dari n langkah scr random
#============================================================

from random import randint

def random(rubik, n):
    for i in range(n):
        x = randint(0, 3)
        if (x == 0) and (left(rubik) is not False):
            rubik = left(rubik)
        elif (x == 1) and (right(rubik) is not False):
            rubik = right(rubik)
        elif (x == 2) and (top(rubik) is not False):
            rubik = top(rubik)
        elif (x == 3) and (bottom(rubik) is not False):
            rubik = bottom(rubik)      
        
    return rubik
        
