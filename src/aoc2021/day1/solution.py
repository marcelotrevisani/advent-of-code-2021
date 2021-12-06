from pathlib import Path


def solve(input_list, slice_window=1):
    count = 0
    ref = sum(input_list[0:slice_window])
    for pos, num in enumerate(input_list[1:], start=1):
        num = sum(input_list[pos : pos + slice_window])
        if num > ref:
            count += 1
        ref = num
    return count


if __name__ == "__main__":
    input_file_path = Path(__file__).parent / "data" / "input1.txt"
    with open(input_file_path, "r") as input_file:
        all_input = [int(i) for i in input_file.readlines()]
        print(f"Problem 1: {solve(all_input)}")
        print(f"Problem 2: {solve(all_input, slice_window=3)}")
