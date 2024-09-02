import numpy as np
import random
def combine_and_shift_left(row):
    new_row = [i for i in row if i != 0]  # Filter out zeros
    i = 0
    while i < len(new_row)-1:  # Combine adjacent equal non-zero elements
        if new_row[i] == new_row[i+1]:
            new_row[i] *= 2
            del new_row[i+1]  # Remove the combined element
            new_row.append(0)  # Append a zero at the end
        i += 1
    return new_row + [0] * (len(row) - len(new_row))  # Fill the rest with zeros
def shift_left(grid):
    for i in range(len(grid)):
        grid[i] = combine_and_shift_left(grid[i])
    insert_random(grid)
    return grid

def combine_and_shift_right(row):
    return combine_and_shift_left(row[::-1])[::-1]  # Reverse, combine and shift left, then reverse back

def shift_right(grid):
    for i in range(len(grid)):
        grid[i] = combine_and_shift_right(grid[i])
    insert_random(grid)
    return grid

def shift_up(grid):
    grid = np.transpose(grid)  # Transpose to treat columns as rows
    grid = shift_left(grid)  # Shift left (which is actually up due to transpose)
    grid = np.transpose(grid)  # Transpose back
    return grid

def shift_down(grid):
    grid = np.transpose(grid)  # Transpose to treat columns as rows
    grid = shift_right(grid)  # Shift right (which is actually down due to transpose)
    grid = np.transpose(grid)  # Transpose back
    return grid

def insert_random(grid):
    empty_spots = [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == 0]
    if empty_spots:
        i, j = random.choice(empty_spots)
        grid[i][j] = random.choice([2, 4])


grid = np.array([
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
], dtype=int)

# Randomly place two '2's or '4's on the grid
for _ in range(2):
    empty_spots = [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == 0]
    if empty_spots:
        i, j = random.choice(empty_spots)
        grid[i][j] = random.choice([2, 4])


print("Original grid:")
print(grid)
def is_game_over(grid):
    for row in grid:
        if 0 in row:
            return False
    return True
def is_game_won(grid):
    for row in grid:
        if 2048 in row:
            return True
    return False

while True:

    if is_game_over(grid):
        print("Game Over! ")
        break
    if is_game_won(grid):
        print("YOU WON! ")
        break
    choice = int(input("Please enter the shift operation you want to perform:\n1. Left\n2. Right\n3. Up\n4. Down\n"))

    if choice == 1:
        print("Performing left operation")
        new_grid = shift_left(grid)
        print(new_grid)
    elif choice == 2:
        print("Performing right operation")
        new_grid = shift_right(grid)
        print(new_grid)
    elif choice == 3:
        print("Performing up operation")
        new_grid = shift_up(grid)
        print(new_grid)
    elif choice == 4:
        print("Performing down operation")
        new_grid = shift_down(grid)
        print(new_grid)
    else:
        print("Invalid choice")
        new_grid = grid

print("\nGrid after operation:")
print(new_grid)