input = open("2025/day4/input.txt", "r", encoding="utf-8").read().splitlines()

def is_roll_at_pos(grid: list[list], row: int, cell: int):
    if not 0 <= row < len(grid):
        return False
    elif not 0 <= cell < len(grid[row]):
        return False
    
    content = grid[row][cell]
    
    if content == "@":
        return True
    return False

def remove_rolls_from_grid(grid: list[list]) -> int | list[list]:
    removed = 0
    
    for r_index, row in enumerate(grid):
        for c_index, cell in enumerate(row):
            if not cell == "@":
                continue
        
            adjacent = [
                is_roll_at_pos(grid, r_index-1, c_index-1),
                is_roll_at_pos(grid, r_index, c_index-1),
                is_roll_at_pos(grid, r_index+1, c_index-1),
                is_roll_at_pos(grid, r_index-1, c_index+1),
                is_roll_at_pos(grid, r_index, c_index+1),
                is_roll_at_pos(grid, r_index+1, c_index+1),
                is_roll_at_pos(grid, r_index-1, c_index),
                is_roll_at_pos(grid, r_index+1, c_index),
            ]
        
            if sum(adjacent) < 4:
                grid[r_index][c_index] = "."
                removed = removed + 1
    
    return removed, grid

removed = 0
n_removed = 1
grid = [list(row) for row in input]

while n_removed > 0:
    n_removed, grid = remove_rolls_from_grid(grid)
    removed = n_removed + removed
    pass

print(removed)
