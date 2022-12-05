import time
from typing import Tuple, List, Set

priorities = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def day3(backpacks: List[Tuple[str, str]]):
    """
    Part 1:
    Prints out the sum of priorities of items that appear in both compartments
    of the backpack.

    Part 2:
    Prints out the sum of priorities for items that appear in the badge groups
    of three.
    Args:
        backpacks (List[Tuple[str, str]]): List of backpacks with their contents
    """
    # Part 1
    priority_score = 0
    for backpack in backpacks:
        dupes = set()
        compartment1 = backpack[0]
        compartment2 = backpack[1]
        for item in compartment1:
            if item in compartment2 and item not in dupes:
                dupes.add(item)
                priority_score += priorities.index(item)
    print(f"The sum of the priorites of items that appear in both compartments is {priority_score}")

    # Part 2
    badge_score = 0
    badge_group: List[Set[str]] = []
    for i, backpack in enumerate(backpacks):
        badge_group.append(set(list(backpack[0]) + list(backpack[1])))
        if (i + 1) % 3 == 0:
            dupes = badge_group[0].intersection(badge_group[1]).intersection(badge_group[2])
            badge_score += sum([priorities.index(x) for x in dupes])
            badge_group = []
    print(f"The sum of the priorites of items in the badge groups is {badge_score}")

def load_input() -> List[Tuple[str, str]]:
    """
    Loads the input file and returns the contents of each backpack
    split into the two separate compartments

    Returns:
        List[Tuple[str, str]]: List of items in each backpack split into
        two sections
    """
    backpacks: List[Tuple[str, str]] = []
    with open("input.txt", "r") as input_file:
        for line in input_file:
            line = line.strip()
            mid = len(line) // 2
            backpacks.append((line[0:mid], line[mid:])) # end 1 before to prevent capturing newlines
    return backpacks


if __name__ == "__main__":
    start = time.perf_counter()
    day3(load_input())
    print(f"Ran in {(time.perf_counter() - start) * 1000} ms")
