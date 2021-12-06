from pathlib import Path
from typing import Optional

import numpy as np
from numpy import ndarray


def parse_input(file_path):
    with open(file_path, "r") as input_file:
        numbers_draw = np.loadtxt(input_file, dtype=int, delimiter=",", max_rows=1)
        all_boards = np.loadtxt(input_file, dtype=int, skiprows=1)
        all_boards = all_boards.reshape((all_boards.shape[0] // 5, 5, 5))
        return numbers_draw, all_boards


def get_sum_board_winner_value(
    board_flag, all_boards, axis=0, ref_winners=None
) -> Optional[ndarray]:
    result = None
    for dimension in range(all_boards.shape[0]):
        if dimension in ref_winners:
            continue
        one_dimension_flag = board_flag[dimension, :, :]
        winner = np.all(one_dimension_flag, axis=axis)
        if np.any(winner):
            ref_winners.add(dimension)
            dimension_board = all_boards[dimension, :, :]
            result = result or np.sum(
                dimension_board[np.where(one_dimension_flag == False)]
            )
    return result


def solve1(numbers_draw, all_boards):
    return generic_solver(numbers_draw, all_boards, 1)[0]


def generic_solver(numbers_draw, all_boards, stop_winner=None):
    board_flag = np.full(all_boards.shape, False, dtype=bool)
    result_values = []
    winner_boards = set()
    for i in numbers_draw:
        positions = np.where(all_boards == i)
        board_flag[positions] = True
        if winner_value := (
            get_sum_board_winner_value(
                board_flag, all_boards, axis=0, ref_winners=winner_boards
            )
            or get_sum_board_winner_value(
                board_flag, all_boards, axis=1, ref_winners=winner_boards
            )
        ):
            result_values.append(winner_value * i)
            if len(result_values) == stop_winner:
                return result_values
    return result_values


def solve2(numbers_draw, all_boards):
    return generic_solver(numbers_draw, all_boards)[-1]


if __name__ == "__main__":
    numbers_draw, all_boards = parse_input(Path(__file__).parent / "data" / "input.txt")
    print(f"Problem 1: {solve1(numbers_draw, all_boards)}")
    print(f"Problem 2: {solve2(numbers_draw, all_boards)}")
