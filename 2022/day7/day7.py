import time
from typing import List, Union

class File:
    def __init__(self, name: str, size: int = 0):
        self.name = name
        self.size = size

class Folder:
    def __init__(self, name: str, parent: "Folder" = None):
        self.name: str = name
        self.children: List[Union[File, Folder]] = []
        self.parent: Folder = parent
    
def get_sizes(root: Folder, sizes: List[int]) -> int:
    """
    Prints the total file size of the directory as well as recursively
    include total file sizes for each directory below

    Args:
        root (Folder): Root folder to return size for
        sizes (List[int]): List of sizes for each child directory

    Returns:
        int: The total size for this directory and all subdirectories
    """
    size = 0
    for c in root.children:
        if isinstance(c, File):
            size += c.size
        else:
            size += get_sizes(c, sizes)
    sizes.append(size)
    return size

def day7(commands: List[str]):
    total_disk_space = 70_000_000
    free_space_required_for_update = 30_000_000
    root = generate_folder_tree(commands)
    sizes = []
    total_used = get_sizes(root, sizes)
    sizes.sort()
    valid_sizes_sum = sum([size if size <= 100_000 else 0 for size in sizes])
    # Part 1
    print(f"The sum of the total sizes of directories under 100,000 is {valid_sizes_sum}")
    # Part 2
    remaining_space = total_disk_space - total_used
    space_needed = free_space_required_for_update - remaining_space
    print(f"Remaining space is {remaining_space}, so we need to free up {space_needed} space to update.")
    for size in sizes:
        if size >= space_needed:
            print(f"The size of the smallest directory needed to be deleted is {size}")
            break

def generate_folder_tree(commands: List[str]) -> Folder:
    root = Folder("/")
    cwd = root
    for command in commands:
        parts = command.split()
        # Check if it's a user command
        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[2] == "..":
                    cwd = cwd.parent
                else:
                    for f in cwd.children:
                        if isinstance(f, Folder) and f.name == parts[2]:
                            cwd = f
                            break
            elif parts[1] == "ls":
                continue
        elif parts[0] == "dir":
            cwd.children.append(Folder(parts[1], cwd))
        else:
            cwd.children.append(File(parts[1], int(parts[0])))
    return root

def load_input() -> List[str]:
    with open("input.txt") as file:
        return [l.strip() for l in file]

if __name__ == "__main__":
    start = time.perf_counter()
    day7(load_input())
    print(f"Ran in {(time.perf_counter() - start) * 1000} ms")