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

reachable = 0
grid = [list(row) for row in input]

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
            reachable = reachable + 1

print(reachable)
