import time

def firstUniqueSubstring(input: str, n: int) -> int:
    """
    This returns the number of characters that need to be processed
    before an n length substring of unique characters is found.

    Args:
        input (str): String to iterate
        n (int): Length of the unique substring

    Returns:
        int: The number of characters that need to be processed
    """
    left = 0
    right = 0
    seen = set()
    while right < len(input) and len(seen) < n:
        if input[right] not in seen:
            seen.add(input[right])
            right += 1
        else:
            seen.remove(input[left])
            left += 1
    return right

def day6(input: str):
    print(f"{firstUniqueSubstring(input, 4)} characters need to be processed before the first start-of-packet marker is detected.")
    print(f"{firstUniqueSubstring(input, 14)} characters need to be processed before the first start-of-message marker is detected.")

def load_input() -> str:
    with open("input.txt") as file:
        return file.readline().strip()

if __name__ == "__main__":
    start = time.perf_counter()
    day6(load_input())
    print(f"Ran in {(time.perf_counter() - start) * 1000} ms")