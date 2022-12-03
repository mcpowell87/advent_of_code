from typing import List
import re
import heapq
import time

def day1():
    """
    Prints out the top 3 elves carrying the most calories as well as their
    collective total calorie count.

    Implemented using a max heap.
    """
    heap = []
    inventory = open("input.txt", "r")

    cur_elf = 1
    cur_total = 0
    # Parses through the input and creates a max heap with the results
    for item in inventory:
        # Strips whitespace characters
        item = re.sub(r'\s+', '', item)
        if item and item.isnumeric():
            cur_total += int(item)
        else:
            heapq.heappush(heap, (-cur_total, cur_elf))
            cur_elf += 1
            cur_total = 0
    # Add the last trailing elf, if there is one
    if cur_total > 0:
        heapq.heappush(heap, (-cur_total, cur_elf))

    print("The top 3 elves calorie counts are as follows:")
    total_calories = 0
    for i in range(3):
        elf = heapq.heappop(heap)
        total_calories += -elf[0]
        print(f"Elf {elf[1]} - {-elf[0]} calories")
    print(f"Between the three of them, they have {total_calories} calories")

if __name__ == "__main__":
    start = time.perf_counter()
    day1()
    print(f"Ran in {(time.perf_counter() - start) * 1000} ms")