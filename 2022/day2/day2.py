import time
from typing import List, Tuple
from enum import Enum

class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Result(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6

movemap = {
    "A": Move.ROCK,
    "B": Move.PAPER,
    "C": Move.SCISSORS,
    "X": Move.ROCK,
    "Y": Move.PAPER,
    "Z": Move.SCISSORS
}

resultmap = {
    "X": Result.LOSE,
    "Y": Result.DRAW,
    "Z": Result.WIN
}

def get_score_p1(p1_move: Move, p2_move: Move) -> int:
    """
    Returns the score of the round the perspective of p1_move

    Args:
        p1_move (Move): Player 1's move
        p2_move (Move): Player 2's move

    Returns:
        int: The score of this round
    """
    if p1_move == p2_move:
        return p1_move.value + Result.DRAW.value
    if p1_move == Move.ROCK:
        return p1_move.value + (Result.WIN.value if p2_move == Move.SCISSORS else Result.LOSE.value)
    if p1_move == Move.PAPER:
        return p1_move.value + (Result.WIN.value if p2_move == Move.ROCK else Result.LOSE.value)
    if p1_move == Move.SCISSORS:
        return p1_move.value + (Result.WIN.value if p2_move == Move.PAPER else Result.LOSE.value)
    return 0

def get_score_p2(move: Move, result: Result) -> int:
    """
    Returns the score of a round given a move and a round result

    Args:
        move (Move): The move to play against
        result (Result): The end result of the round

    Returns:
        int: The score of this round
    """
    score = 0
    if result == Result.DRAW:
        score = move.value
    elif move == Move.ROCK:
        score = Move.PAPER.value if result == result.WIN else Move.SCISSORS.value
    elif move == Move.PAPER:
        score = Move.SCISSORS.value if result == result.WIN else Move.ROCK.value
    else:
        score = Move.ROCK.value if result == result.WIN else Move.PAPER.value
    return score + result.value


def day2(movelist: List[Tuple[str, str]]):
    """
    Prints the score if you follow the stratey guide (input)
    """
    score_p1 = 0
    score_p2 = 0
    for round in movelist:
        score_p1 += get_score_p1(movemap[round[1]], movemap[round[0]])
        score_p2 += get_score_p2(movemap[round[0]], resultmap[round[1]])
    print (f"The score achieved with the strategy guide in part 1 is {score_p1}")
    print (f"The score achieved with the strategy guide in part 2 is {score_p2}")


def load_input() -> List[Tuple[str, str]]:
    """
    Loads the input file and transforms it to a list of tuples, where
    the first element is the first play, and the second is the second play

    Returns:
        List[Tuple[str, str]]: List of plays in the strategy guide
    """
    input = open("input.txt", "r")
    plays: List[Tuple[str, str]] = []

    for line in input:
        play = line.split()
        if len(play) < 2:
            # line is invalid, skip
            continue
        plays.append((play[0], play[1]))
    return plays

if __name__ == "__main__":
    start = time.perf_counter()
    day2(load_input())
    print(f"Ran in {(time.perf_counter() - start) * 1000} ms")
