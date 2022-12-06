import time
from typing import List, Tuple

def day4(assignment_pairs: List[List[Tuple[int, int]]]):
    """
    Part 1
    Prints the number of assignment pairs that contains a complete overlap 
    (where one time interval is contained completely within another).

    Part 2
    Prints the number of assignment pairs that contain at least a partial overlap.
    Args:
        assignment_pairs (List[Tuple[int, int]]): The assignment pairs
    """
    total_overlap_count = 0
    partial_overlap_count = 0
    for pair in assignment_pairs:
        # Part 1
        # Check if there is a total overlap
        if pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]:
            total_overlap_count += 1
        # Part 2
        # Check if there is a partial overlap, by chacking if the end time of
        # the first interval is after the start time of the second interval
        if pair[0][1] >= pair[1][0]:
            partial_overlap_count += 1
    print(f"There are {total_overlap_count} pairs that contain a complete overlap")
    print(f"There are {partial_overlap_count} pairs that contain a partial overlap")

def load_input() -> List[List[Tuple[int, int]]]:
    assignment_pairs: List[List[Tuple[int,int]]] = []
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            pairs = line.split(',')
            range1 = tuple([int(x) for x in pairs[0].split('-')])
            range2 = tuple([int(x) for x in pairs[1].split('-')])
            # Make sure the earliest interval is first
            if range1[0] < range2[0]:
                assignment_pairs.append([range1, range2])
            # If the start times are equal, sort by latest end time
            elif range1[0] == range2[0]:
                if range1[1] > range2[1]:
                    assignment_pairs.append([range1, range2])
                else:
                    assignment_pairs.append([range2, range1])
            else:
                assignment_pairs.append([range2, range1])
    return assignment_pairs

if __name__ == "__main__":
    start = time.perf_counter()
    day4(load_input())
    print(f"Ran in {(time.perf_counter() - start) * 1000} ms")