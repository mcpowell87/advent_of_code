import time
from typing import List, Tuple, Set
from enum import Enum

class Direction(Enum):
    UP = (0, 1)
    DOWN = (0, -1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

def get_pos_diff(head: Tuple[int, int], tail: Tuple[int, int]) -> Tuple[int, int]:
    """
    Gets the net difference between the head and tail positions

    Args:
        head (Tuple[int, int]): Head position
        tail (Tuple[int, int]): Tail position

    Returns:
        Tuple[int, int]: Net diff
    """
    return tuple(map(lambda i, j: i - j, head, tail))

def add_pos(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> Tuple[int, int]:
    """
    Adds one position to another

    Args:
        pos1 (Tuple[int, int]): Pos to add to
        pos2 (Tuple[int, int]): Pos to add to pos1

    Returns:
        Tuple[int, int]: New pos
    """
    return tuple(map(lambda i, j: i + j, pos1, pos2))

def get_tail_position(current_h: Tuple[int, int], current_t: Tuple[int, int]) -> Tuple[int, int]:
    """
    Returns a new tail position after a move

    Args:
        current_h (Tuple[int, int]): The new head position
        current_t (Tuple[int, int]): The old tail position

    Returns:
        Tuple[int, int]: The new tail position
    """
    pos_diff = get_pos_diff(current_h, current_t)
    delta = (
                1 if pos_diff[0] >= 1 else -1 if pos_diff[0] <= -1 else 0,
                1 if pos_diff[1] >= 1 else -1 if pos_diff[1] <= -1 else 0
            )
    if abs(pos_diff[0]) > 1 or abs(pos_diff[1]) > 1:
        return add_pos(current_t, delta)
    return current_t

def day9(moves: List[Tuple[Direction, int]]):
    visited_p1: Set = set()
    visited_p2: Set = set()
    rope: List[Tuple[int, int]] = [(0,0) for _ in range(10)]
    visited_p1.add(rope[1])
    visited_p2.add(rope[-1])
    for direction, num_moves in moves:
        for _ in range(num_moves):
            rope[0] = add_pos(rope[0], direction.value)
            for i in range(1, len(rope)):
                rope[i] = get_tail_position(rope[i-1], rope[i])
            visited_p1.add(rope[1])
            visited_p2.add(rope[-1])
    print(f"The tail visits {len(visited_p1)} locations.")
    print(f"The 10 knot rope's tail visits {len(visited_p2)} locations")

def load_input() -> List[Tuple[Direction, int]]:
    moves: List[Tuple[Direction, int]] = []
    with open("input.txt") as file:
        for line in file:
            d, n = line.strip().split()
            if d == "D":
                moves.append((Direction.DOWN, int(n)))
            elif d == "U":
                moves.append((Direction.UP, int(n)))
            elif d == "L":
                moves.append((Direction.LEFT, int(n)))
            elif d == "R":
                moves.append((Direction.RIGHT, int(n)))
    return moves

if __name__ == "__main__":
    start = time.perf_counter()
    day9(load_input())
    print(f"Ran in {(time.perf_counter() - start) * 1000} ms")