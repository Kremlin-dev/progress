def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    """
    if not grid:
        return 0
    
    perimeter = 0
    
    # Iterate over each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the cell is land, add to the perimeter count
            if grid[i][j] == 1:
                # Check adjacent cells and add to perimeter count if they are water or out of bounds
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if i == len(grid)-1 or grid[i+1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                if j == len(grid[0])-1 or grid[i][j+1] == 0:
                    perimeter += 1
                    
    return perimeter
