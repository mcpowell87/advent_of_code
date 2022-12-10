import time
from typing import List, Tuple

def is_visible_in_row(tree_height: int, row: List[int]) -> bool:
    """
    Returns True there is a sight line to a particular tree down a specific row

    Args:
        coord (int): The height of the tree
        row (List[int]): The row being looked down

    Returns:
        bool: True if visible
    """
    for tree in row:
        if tree >= tree_height:
            return False
    return True

def view_distance(tree_height: int, row: List[int]) -> int:
    """
    Returns the view distance given a row

    Args:
        tree_height (int): The tree height at the location of viewing
        row (List[int]): The row being looked down

    Returns:
        int: The number of trees visible
    """
    distance = 0
    for tree in row:
        distance += 1
        if tree >= tree_height:
            return distance
    return distance

def day8(tree_grid: List[List[int]]):
    # Found this fancy way to rotate a grid, since navigating across rows is
    # easier than navigating down columns.
    tree_grid_rotated = list(zip(*tree_grid))

    num_visible = 0
    view_score = 0
    for x in range(len(tree_grid[0])):
        for y in range(len(tree_grid)):
            height = tree_grid[x][y]
            # Part 1
            # Look down each row until y and see if there are any larger trees
            # in front of it.  If not, it's visible.
            if (is_visible_in_row(height, tree_grid[x][:y]) or
                is_visible_in_row(height, tree_grid[x][y + 1:]) or
                is_visible_in_row(height, tree_grid_rotated[y][:x]) or
                is_visible_in_row(height, tree_grid_rotated[y][x + 1:])):
                num_visible += 1
            # Part 2
            # For each tree, look in each direction and print out the score
            # (distance) you can see, multiply and that's the score.
            cur_score = (view_distance(height, tree_grid[x][:y][::-1]) *
                view_distance(height, tree_grid[x][y + 1:]) *
                view_distance(height, tree_grid_rotated[y][:x][::-1]) *
                view_distance(height, tree_grid_rotated[y][x + 1:]))
            view_score = max(cur_score, view_score)
    
    print(f"The number of trees visible from the outside are {num_visible}")
    print(f"The highest scenic score possible is {view_score}")

def load_input():
    tree_grid: List[List[int]] = []
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            tree_grid.append([int(x) for x in line])
    return tree_grid

if __name__ == "__main__":
    start = time.perf_counter()
    day8(load_input())
    print(f"Ran in {(time.perf_counter() - start) * 1000} ms")