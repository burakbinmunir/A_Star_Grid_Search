# A Star Pathfinding Algorithm Visualization

This Python script demonstrates the A* pathfinding algorithm in a grid-based environment using Tkinter for graphical representation.
<p align="center">
  <img src="https://github.com/burakbinmunir/A_Star_Grid_Search/assets/108978796/1a2cdb2e-7dbe-405e-a02e-8d3ea41ee78e" alt="Description of the image">
</p>

## Description

The script defines a class node to represent a node in the grid. A* algorithm is implemented to find the optimal path from a start node to a goal node, considering blocked nodes as obstacles.

## Requirements
- Python 3.x
- Tkinter (typically included with Python installations)

## Usage
- Open the script in a Python environment.
- Run the script in terminal `py a_star_visualization`
- The graphical user interface (GUI) will display a grid with blocked and unblocked cells.
- The A* algorithm will find the optimal path from the specified start node to the goal node.
- The GUI will highlight the path in green, and the total cost of the path will be displayed.

## Customization
- Modify the size variable to change the size of the grid.
- Adjust the start and goal node coordinates for different starting and ending positions.
- Block/unblock nodes by setting the blocked attribute in the initialize_grid function.

## Important Note

Ensure that Tkinter is installed, as the GUI relies on it for visualization.

