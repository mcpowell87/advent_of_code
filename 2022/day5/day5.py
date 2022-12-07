import time
from typing import Tuple, List

def day5(stacks: List[List[str]], instructions: List[Tuple[int, int, int]]):
    """
    Perform a series of instructions on 

    Args:
        stacks (List[List[str]]): The stack to perform operations on
        instructions (List[Tuple[int, int, int]]): The instruction set to follow
        which is in the format "move # from stack# to stack#"
    """
    stacks_p1 = [x[:] for x in stacks[:]]
    stacks_p2 = [x[:] for x in stacks[:]]
    for instruction in instructions:
        source_stack = instruction[1] - 1
        num_to_move = instruction[0]
        dest_stack = instruction[2] - 1
        p2_load = []
        for _ in range(num_to_move):
            # Part 1: Crates are moved one by one
            stacks_p1[dest_stack].append(stacks_p1[source_stack].pop())
            # Part 2: Multiple crates are moved at a time
            p2_load.insert(0, stacks_p2[source_stack].pop())
        stacks_p2[dest_stack].extend(p2_load)
    # Generate output
    output_p1: List[str] = []
    output_p2: List[str] = []
    for i in range(len(stacks)):
        output_p1.append(stacks_p1[i][-1])
        output_p2.append(stacks_p2[i][-1])
    print(f"The top most crates after the series of instructions for part 1 is {output_p1}")
    print(f"The top most crates after the series of instructions for part 2 is {output_p2}")

def load_stacks() -> List[List[str]]:
    stacks: List[List[str]] = []
    with open("input_stacks.txt") as file:
        for line in file:
            line = line.strip()
            stacks.append(line.split())
    return stacks

def load_instructions() -> List[Tuple[int, int, int]]:
    instructions: List[Tuple[int, int, int]] = []
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            parts = line.split()
            # Since format is 'move <int> from <int> to <int>, rather than 
            # parse the real text and intent, just assume <index 1> items will 
            # be moved from stack <index 3> to <index 5>.  This is AoC, not prod
            instructions.append((int(parts[1]), int(parts[3]), int(parts[5])))
    return instructions

if __name__ == "__main__":
    start = time.perf_counter()
    day5(load_stacks(), load_instructions())
    print(f"Ran in {(time.perf_counter() - start) * 1000} ms")