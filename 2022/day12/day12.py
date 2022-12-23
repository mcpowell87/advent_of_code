import time
from typing import List, Tuple
import heapq

move_map = "abcdefghijklmnopqrstuvwxyz"

directions = [
    (-1, 0), # Left
    (1, 0),  # Right
    (0, -1), # Down
    (0, 1)   # Up
]

def get_elevation(letter: str) -> int:
    """
    Helper to get the elevation of a particular position

    Args:
        letter (str): The letter at the position

    Returns:
        int: Elevation value
    """
    if letter == "S":
        letter = "a"
    elif letter == "E":
        letter = "z"
    return move_map.index(letter)

def get_neighbors(grid: List[List[int]], x: int, y: int) -> List[Tuple[int, int]]:
    """
    Gets a list of neighbors

    Args:
        grid (List[List[int]]): Grid
        x (int): X coordinate
        y (int): Y coordinate

    Returns:
        List[Tuple[int, int]]: Neighbors
    """
    neighbors: List[Tuple[int, int]] = []
    for direction in directions:
        new_x = x + direction[0]
        new_y = y + direction[1]
        if new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[x]):
            if get_elevation(grid[new_x][new_y]) <= get_elevation(grid[x][y]) + 1:
                neighbors.append((new_x, new_y))
    return neighbors

def get_dist(grid: List[List[int]], start_pos: Tuple[int, int], end_pos: Tuple[int, int]):
    """
    Gets the shortest path from start to end

    Args:
        grid (List[List[int]]): Grid
        start_pos (Tuple[int, int]): Starting position
        end_pos (Tuple[int, int]): Ending position

    Returns:
        _type_: The shortest number of steps to get to the end
    """
    visited = set()
    q = []
    heapq.heappush(q, (0, start_pos))
    while True:
        if not q:
            break
        dist, pos = heapq.heappop(q)
        if pos not in visited:
            visited.add(pos)
            if pos == end_pos:
                return dist
            neighbors = get_neighbors(grid, pos[0], pos[1])
            for x, y in neighbors:
                heapq.heappush(q, (dist + 1, (x, y)))

def get_start_end_points(grid: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Gets the start and end positions

    For part 1: The start position is the position with "S"
    For part 2: The start positions are any position with an elevation
    of "a"

    The end position is the position with "E"

    Args:
        grid (List[List[int]]): The grid

    Returns:
        List[Tuple[int, int]]: Returns a list of start and end positions, where
        the last element is the end position and all others are start positions.
        The very first index is the position with "S" for part 1, and all
        inbetween are positions that have an elevation of "a"
    """
    start_pos: Tuple[int, int] = None
    potential_start_pos: List[Tuple[int, int]] = []
    end_pos: Tuple[int, int] = None
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if col == "S":
                start_pos = (x, y)
            if col == "E":
                end_pos = (x, y)
            if col == "a":
                potential_start_pos.append((x, y))
    return [start_pos] + potential_start_pos + [end_pos]

def day12(grid: List[List[str]]):
    points = get_start_end_points(grid)
    end = points[-1]
    shortest_path = get_dist(grid, points[0], end)
    print(f"The fewest steps required to get the best signal is {shortest_path}")
    
    shortest_path_anywhere = float("inf")
    for starting_pos in points[0:len(points) - 1]:
        dist = get_dist(grid, starting_pos, end)
        if dist:
            shortest_path_anywhere = min(shortest_path_anywhere, dist)
    print(f"The fewest steps required to get the best signal from any position of elevation a is {shortest_path_anywhere}")


def load_input():
    grid: List[List[str]] = []
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            grid.append([char for char in line])
    return grid

if __name__ == "__main__":
    start = time.perf_counter()
    day12(load_input())
    print(f"Ran in {(time.perf_counter() - start) * 1000} ms")