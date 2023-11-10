import random
import tkinter as tk

# Class to represent a node in the grid
class node:
    x = -1
    y = -1
    g = -1
    h = -1
    f = -1
    visited = False
    blocked = False
    parent = None
    
    def __init__(self):
        x = -1
        y = -1
        g = -1
        h = -1
        f = -1
        visited = False
        blocked = False
        parent = None

# Function to calculate the Euclidean distance between two nodes
ecludian_distance = lambda x1, y1, x2, y2 : ((x2-x1)**2 + (y2-y1)**2)**0.5

# Function to display the grid on the terminal
def display_grid (grid, size):
    for _ in range(size):
        for __ in range(size):
            print(f"""({grid[_][__].x} , {grid[_][__].y}), g = {grid[_][__].g}, h = {grid[_][__].h}, f = {grid[_][__].f}""")
        

# Function to initialize the grid with nodes
def initialize_grid( size , goal):
    grid = [[0 for x in range(size)] for y in range(size)]
    for _ in range(size):
        for __ in range(size):
            n = node()
            n.x = _
            n.y = __
            n.g = 1
            n.h = ecludian_distance(_, __, goal.x, goal.y) # Use Euclidean distance as the heuristic
            grid[_][__] = n
    return grid

# Function to sort the open list based on `f` value
def sort_open_list(open_list):
    for _ in range(len(open_list)):
        for __ in range(len(open_list)):
            if open_list[_].f < open_list[__].f:
                temp = open_list[_]
                open_list[_] = open_list[__]
                open_list[__] = temp
    return open_list

# Function to extract the path from the closed list
def extract_path(closed_list):
    path = []
    current = closed_list[-1]  
    while current is not None:
        path.append(current)
        current = current.parent
    return path[::-1]  

# Function to run the A* algorithm
def a_star(start, grid, size, goal):
    open_list = []
    open_list.append(grid[start.x][start.y])
    closed_list = []
    
    # Check if the goal or start is blocked
    if grid[goal.x][goal.y].blocked == True or grid[start.x][start.y].blocked == True:
        return None , None
    
    g_t = 0 # Total cost from start to current node
    goal_found = False
    while open_list and goal_found == False:
        open_list = sort_open_list(open_list)
        current = open_list[0]
        
        if current.visited == False:
            current.visited = True            
        
            g_t += current.g
            
            # Check if the goal is reached 
            if current.x == goal.x and current.y == goal.y:
                goal_found = True
                closed_list.append(current)
                path = extract_path(closed_list)
                cost = 0
                for _ in range(len(path)):
                    cost += path[_].g
                return path , cost
            
            
            if current.x - 1 >= 0 and current.x - 1 < size  and current.y >= 0 and current.y < size and grid[current.x - 1][current.y].visited == False and grid[current.x - 1][current.y].blocked == False:
                grid[current.x - 1][current.y].f = g_t + grid[current.x - 1][current.y].h
                grid[current.x - 1][current.y].parent = current
                
                # Check if the node is already in the open list
                if  grid[current.x - 1][current.y] not in open_list: 
                    open_list.append(grid[current.x - 1][current.y])
                
            if current.x + 1 >= 0 and current.x + 1 < size and current.y + 1 >= 0 and current.y + 1 < size and grid[current.x + 1][current.y + 1].visited == False and grid[current.x + 1][current.y + 1].blocked == False:
                grid[current.x + 1][current.y + 1].f = g_t + grid[current.x + 1][current.y + 1].h
                grid[current.x + 1][current.y + 1].parent = current
                if grid[current.x + 1][current.y + 1] not in open_list:
                    open_list.append(grid[current.x + 1][current.y + 1])
                
            if current.x + 1 >= 0 and  current.x + 1 < size and current.y >= 0 and current.y < size and grid[current.x + 1][current.y].visited == False and grid[current.x + 1][current.y].blocked == False:
                grid[current.x + 1][current.y].f = g_t + grid[current.x + 1][current.y].h
                grid[current.x + 1][current.y].parent = current
                if grid[current.x + 1][current.y] not in open_list:
                    open_list.append(grid[current.x + 1][current.y])
                
            if current.x >= 0 and current.x < size and current.y + 1 >= 0 and current.y + 1 < size and grid[current.x][current.y + 1].visited == False and grid[current.x][current.y + 1].blocked == False:
                grid[current.x][current.y + 1].f = g_t + grid[current.x][current.y + 1].h
                grid[current.x][current.y + 1].parent = current
                if grid[current.x][current.y + 1] not in open_list:
                    open_list.append(grid[current.x][current.y + 1])
                
            if current.x - 1 >= 0 and  current.x - 1 < size and current.y + 1 >= 0 and current.y + 1 < size and grid[current.x - 1][current.y + 1].visited == False and grid[current.x - 1][current.y + 1].blocked == False:
                grid[current.x - 1][current.y + 1].f = g_t + grid[current.x - 1][current.y + 1].h
                grid[current.x - 1][current.y + 1].parent = current
                if grid[current.x - 1][current.y + 1] not in open_list:
                    open_list.append(grid[current.x - 1][current.y + 1])
                
            if current.x + 1 >= 0 and current.x + 1 < size and current.y - 1 >= 0 and current.y - 1 < size and grid[current.x + 1][current.y - 1].visited == False and grid[current.x + 1][current.y - 1].blocked == False:
                grid[current.x + 1][current.y - 1].f = g_t + grid[current.x + 1][current.y - 1].h
                grid[current.x + 1][current.y - 1].parent = current
                if grid[current.x + 1][current.y - 1] not in open_list:
                    open_list.append(grid[current.x + 1][current.y - 1])
                
            if current.x >= 0 and current.x < size and current.y - 1 >= 0 and current.y - 1 < size and grid[current.x][current.y - 1].visited == False and grid[current.x][current.y - 1].blocked == False:
                grid[current.x][current.y - 1].f = g_t + grid[current.x][current.y - 1].h
                grid[current.x][current.y - 1].parent = current
                if grid[current.x][current.y - 1] not in open_list:
                    open_list.append(grid[current.x][current.y - 1])
                
            if current.x - 1 >= 0 and current.x - 1 < size and current.y - 1 >= 0 and current.y - 1 < size and grid[current.x - 1][current.y - 1].visited == False and grid[current.x - 1][current.y - 1].blocked == False:
                grid[current.x - 1][current.y - 1].f = g_t + grid[current.x - 1][current.y - 1].h
                grid[current.x - 1][current.y - 1].parent = current
                if grid[current.x - 1][current.y - 1] not in open_list:
                    open_list.append(grid[current.x - 1][current.y - 1])
                
            
            open_list.remove(current)
            closed_list.append(current)
    
    return None , None        

# Function to draw the grid on the GUI
def draw_grid(canvas, grid, size, path):
    cell_size = 30  # Width and height of a cell
    for i in range(size):
        for j in range(size):
            color = 'black' if grid[i][j].blocked else 'white'
            canvas.create_rectangle(j*cell_size, i*cell_size, (j+1)*cell_size, (i+1)*cell_size, fill=color, outline='black')
            if grid[i][j] in path:
                canvas.create_oval(j*cell_size+5, i*cell_size+5, (j+1)*cell_size-5, (i+1)*cell_size-5, fill='green')  # Highlight path in green
    canvas.pack()


# Function to run the A* algorithm and update the GUI
def run_a_star():
    size = 10 # Size of the grid
    
    # Create the goal node
    g_x = 9 
    g_y = 9
    goal = node()
    goal.x = g_x
    goal.y = g_y
    
    grid = initialize_grid(size=size, goal=goal)
    goal = grid[g_x][g_y]
    
    start = node()
    start.x = 2
    start.y = 4
    
    # Block some random nodes
    
    # grid[5][5].blocked = True
    grid[3][3].blocked = True
    grid[4][4].blocked = True
    grid[2][2].blocked = True
    
    grid[5][0].blocked = True
    grid[5][1].blocked = True
    grid[5][2].blocked = True
    grid[5][3].blocked = True
    grid[5][4].blocked = True
    grid[5][5].blocked = True
    grid[5][6].blocked = True
    grid[5][7].blocked = True
    # grid[5][8].blocked = True
    # grid[5][9].blocked = True
    
    
    path , cost = a_star(start, grid, size, goal)
    
    if path is None:
        print("No path found")
        return
    
    
    window = tk.Tk()
    canvas = tk.Canvas(window, width=size*30, height=size*30)

    # Draw the grid with highlighted path
    draw_grid(canvas, grid, size, path)

    # Add a label to display the cost
    cost_label = tk.Label(window, text=f"Total Cost: {cost}")
    cost_label.pack()

    window.mainloop()

run_a_star()
