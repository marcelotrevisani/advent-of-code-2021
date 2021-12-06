import re
from pathlib import Path

import numpy as np


def read_input(file_path):
    with open(file_path, "r") as input_file:
        content = input_file.read()
        all_input = re.findall(r"(\d+),(\d+)\s+->\s+(\d+),(\d+)", content, re.MULTILINE)
        return [tuple(map(int, line)) for line in all_input]


def clean_input(all_input):
    result = []
    for x1, y1, x2, y2 in all_input:
        if x1 == x2 or y1 == y2:
            result.append((x1, y1, x2, y2))
    return result


def solve1(all_input):
    all_input = np.array(all_input, dtype=int)
    max_values = np.max(all_input, axis=0)
    x_max = max(max_values[0], max_values[2])
    y_max = max(max_values[1], max_values[3])
    grid_points = np.zeros((x_max+1, y_max+1), dtype=int)
    for x1, y1, x2, y2 in all_input:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                grid_points[x1, y] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                grid_points[x, y1] += 1
        else:
            for i in range(max(x1, x2) + 1 - min(x1, x2)):
                xi = i if x1 < x2 else -i
                yi = i if y1 < y2 else -i
                grid_points[x1 + xi, y1 + yi] += 1
    return grid_points[grid_points >= 2].size


def solve2(all_input):
    return solve1(all_input)


if __name__ == "__main__":
    file_path = Path(__file__).parent / "data" / "input.txt"
    all_input = read_input(file_path)
    input_problem1 = clean_input(all_input)
    print(f"Problem 1: {solve1(input_problem1)}")
    print(f"Problem 2: {solve2(all_input)}")
