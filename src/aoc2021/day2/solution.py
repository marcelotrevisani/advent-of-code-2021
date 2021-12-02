import re
from pathlib import Path

RE_DIRECTION = re.compile(r"(\w+)\s+(\d+)")


def solve1(input_list):
    horizontal_pos = 0
    depth = 0
    for direction in input_list:
        values = RE_DIRECTION.match(direction)
        if not values:
            continue
        mov, num = values.groups()
        num = int(num)
        match mov.lower():
            case "forward":
                horizontal_pos += num
            case "down":
                depth += num
            case "up":
                depth -= num
    return depth * horizontal_pos


def solve2(input_list):
    aim = 0
    horizontal = 0
    depth = 0
    for direction in input_list:
        values = RE_DIRECTION.match(direction)
        if not values:
            continue
        mov, num = values.groups()
        num = int(num)
        match mov.lower():
            case "forward":
                if aim == 0:
                    horizontal += num
                else:
                    horizontal += num
                    depth += num * aim
            case "down":
                aim += num
            case "up":
                aim -= num
    return horizontal * depth


if __name__ == "__main__":
    with open(Path(__file__).parent / "data" / "input.txt") as input_file:
        all_lines = input_file.readlines()
        print(f"Problem 1: {solve1(all_lines)}")
        print(f"Problem 2: {solve2(all_lines)}")