import time
from typing import List

def day10(ops: List[int | None]):
    """
    Since register_history is a list containing the state of the register
    at the start of that cycle, we can shortcut and add two entries during addx
    operations.  This means that index 19 is the state of the register at the
    start of cycle 20
    """
    register_history: List[int] = [1]
    register = 1
    for op in ops:
        if op:
            register_history.extend([register, register + op])
            register += op
        else:
            register_history.append(register)
    signals = get_signal_strengths(20, 40, register_history)
    print(f"The sum of the signal strengths is {sum(signals)}")
    print("Rendered image:")
    render(register_history)

def get_signal_strengths(start: int, n: int, cycles: List[int]) -> List[int]:
    """
    Gets the signal strength starting at cycle <start> and every <n> cycles after

    Args:
        start (int): The cycle to begin at
        n (int): Jumps between cycles
        cycles (List[int]): Cycle history

    Returns:
        List[int]: List of signal strengths
    """
    signals: List[int] = []
    for i in range(start, len(cycles), n):
        signals.append(i * cycles[i-1])
    return signals

def render(cycles: List[int]):
    """
    Renders the CRT
    """
    crt_width = 40
    pixels = ["." for _ in range(240)]
    for cycle, register in enumerate(cycles):
        if (register == (cycle % crt_width) or
           register + 1 == (cycle % crt_width) or
           register - 1 == (cycle % crt_width)):
            pixels[cycle] = "#"
    start = 0
    end = 0
    for _ in range(6):
        start = start
        end = start + 40
        print(''.join(pixels[start:end]))
        start = end

def load_input() -> List[int | None]:
    """
    Loads input from the file.

    Since there are only two ops, we can simply the input by returning a list
    of numbers or none, instead of having to parse the op each time.
    """
    ops: List[int | None] = []
    with open("input.txt") as file:
        for line in file:
            _, *n = line.strip().split()
            ops.append(int(n[0]) if n else None)
    return ops

if __name__ == "__main__":
    start = time.perf_counter()
    day10(load_input())
    print(f"Ran in {(time.perf_counter() - start) * 1000} ms")