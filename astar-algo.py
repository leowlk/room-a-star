from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import numpy as np

# Clean data
arr = np.loadtxt("data/roomU_raster_matrix.txt")
arr = np.around(arr, 2)
arr = arr + 1.35
arr = np.rint(arr)
# print(arr)

arr.tolist()

grid = Grid(matrix = arr)
start = grid.node(0, 0)
end = grid.node(0, 20)

finder = AStarFinder(diagonal_movement = DiagonalMovement.always)
path, runs = finder.find_path(start, end, grid)

print('operations:', runs, 'path length:', len(path))
print(grid.grid_str(path=path, start=start, end=end))
print('Path:', path)