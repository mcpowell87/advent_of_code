import time
from typing import List, Callable, Tuple, Optional
from copy import deepcopy

class Monkey():
    items: List[int] = []
    operation: Callable = None
    divisor: int = 0
    true_monkey: int = 0
    false_monkey: int = 0
    num_inspected = 0
    _boredom_divisor = 3

    def __init__(
            self,
            items: List[int],
            operation: Callable,
            divisor: int,
            true_monkey: int,
            false_monkey: int
        ):
        self.items = items
        self.operation = operation
        self.divisor = divisor
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

    def inspect_item(self, common_divisor: Optional[int] = None):
        """
        The monkey inspects the item, adds to worry value, and then gets bored
        """
        if self.items:
            # Monkey inspects the item
            self.num_inspected += 1
            # if the common divisor is set, apply it here
            # Worry is increased
            self.items[0] = self.operation(self.items[0])
            # Boredom sets in
            if not common_divisor:
                self.items[0] //= 3
            else:
                # This is to keep the numbers small, since all we care about is the 
                # num inspected count, not the value of the items
                self.items[0] %= common_divisor
    
    def throw_item(self) -> Tuple[int, int]:
        """
        Checks if the item worry score is divisble by divisor.  If true,
        pass the item to the true_monkey, otherwise false-monkey

        Returns:
            Tuple[int, int]: A tuple containing the item being thrown and the
            monkey being thrown to
        """
        item = self.items.pop(0)
        if item % self.divisor == 0:
            return (item, self.true_monkey)
        else:
            return (item, self.false_monkey)
    
    def catch_item(self, item: int):
        """
        Catches an item thrown to it and places at the end of the items list
        """
        self.items.append(item)

def play_monkey_in_the_middle(rounds: int, monkeys: List[Monkey], common_divisor: Optional[int] = None) -> List[int]: 
    """
    Plays x rounds of monkey in the middle.

    Args:
        rounds (int): The number of rounds to play
        include_boredom (bool, optional): Whether monkeys get bored. Defaults to False.
    
    Returns:
        List[int]: The list of items inspected by each monkey
    """
    for i in range(rounds):
        for monkey in monkeys:
            if not monkey.items:
                continue
            num_items = len(monkey.items)
            for _ in range(num_items):
                monkey.inspect_item(common_divisor)
                thrown_item, target_monkey = monkey.throw_item()
                monkeys[target_monkey].catch_item(thrown_item)
    return [monkey.num_inspected for monkey in monkeys]

def day11(monkeys: List[Monkey]):
    monkeys_p1 = deepcopy(monkeys)
    monkeys_p2 = deepcopy(monkeys)
    # Part 1
    num_inspected_p1 = play_monkey_in_the_middle(20, monkeys_p1)
    num_inspected_p1.sort(reverse=True)
    monkey_business_p1 = num_inspected_p1[0] * num_inspected_p1[1]
    print(f"The level of monkey business after 20 rounds is {monkey_business_p1}")

    # Part 2
    common_divisor = 1
    for monkey in monkeys:
        common_divisor *= monkey.divisor
    num_inspected_p2 = play_monkey_in_the_middle(10_000, monkeys_p2, common_divisor)
    num_inspected_p2.sort(reverse=True)
    monkey_business_p2 = num_inspected_p2[0] * num_inspected_p2[1]
    print(f"The level of monkey business after 10000 rounds is {monkey_business_p2}")

def load_input() -> List[Monkey]:
    """
    Yeah this could be more robust but it's an aoc problem
    """
    monkeys: List[Monkey] = []
    with open("input.txt") as file:
        lines = [line.strip() for line in file]
        i = 0
        while i < len(lines):
            line: str = lines[i]
            if line.__contains__("Monkey"):
                starting_items = [int(n) for n in lines[i + 1].split(":")[1].split(",")]
                operation: Callable = None
                operation_line = lines[i + 2].strip().split("=")[1].split()
                if operation_line[1] == "+":
                    operation = lambda x, y = int(operation_line[2]) : x + y
                elif operation_line[1] == "*":
                    if operation_line[2] == "old":
                        operation = lambda x : x * x
                    else:
                        operation = lambda x, y = int(operation_line[2]) : x * y
                divisor = int(lines[i + 3].strip().split()[-1])
                true_monkey = int(lines[i + 4].strip().split()[-1])
                false_monkey = int(lines[i + 5].strip().split()[-1])
                monkeys.append(Monkey(
                    items=starting_items,
                    operation=operation,
                    divisor=divisor,
                    true_monkey=true_monkey,
                    false_monkey=false_monkey
                ))
                i += 4 # skip the next 4 + 1 lines
            i += 1
    return monkeys

if __name__ == "__main__":
    start = time.perf_counter()
    day11(load_input())
    print(f"Ran in {(time.perf_counter() - start) * 1000} ms")