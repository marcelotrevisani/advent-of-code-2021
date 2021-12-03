from dataclasses import dataclass
from pathlib import Path


class Tree:
    def __init__(self):
        self.root = Node("")

    def add_num(self, num: str):
        current_node = self.root
        for i in num.strip():
            if i == "0":
                if current_node.zero is None:
                    current_node.zero = Node("0", 1)
                else:
                    current_node.zero.weight += 1
                current_node = current_node.zero
            elif i == "1":
                if current_node.one is None:
                    current_node.one = Node("1", 1)
                else:
                    current_node.one.weight += 1
                current_node = current_node.one

    def get_most_common(self):
        return self.__generic_common(True)

    def get_least_common(self):
        return self.__generic_common(False)

    def __generic_common(self, most_common):
        current_node = self.root
        result = ""
        while True:
            result += current_node.value
            if current_node.zero is None and current_node.one is None:
                break
            if current_node.zero is None or current_node.one is None:
                current_node = current_node.zero or current_node.one
            elif current_node.zero >= current_node.one:
                current_node = current_node.zero if most_common else current_node.one
            else:
                current_node = current_node.one if most_common else current_node.zero
        return result


@dataclass
class Node:
    value: str
    weight: int = 1
    zero: "Node" = None
    one: "Node" = None

    def __ge__(self, other: "Node"):
        return self.weight > other.weight or self.weight == other.weight and self.value == 0


def solve2(input_list):
    tree = Tree()
    for line in input_list:
        tree.add_num(line)

    oxigen = int(tree.get_most_common(), 2)
    co2 = int(tree.get_least_common(), 2)
    return oxigen * co2


def solve1(input_list):
    count_0 = [0] * len(input_list[0].strip())
    for line in input_list:
        for pos, digit in enumerate(line.strip()):
            if digit == "0":
                count_0[pos] += 1

    gamma = epsilon = ""
    for i in count_0:
        if i > len(input_list) // 2:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    return int(gamma, 2) * int(epsilon, 2)


if __name__ == "__main__":
    with open(Path(__file__).parent / "data" / "input.txt", "r") as input_file:
        all_lines = input_file.readlines()
        print(f"Problem 1: {solve1(all_lines)}")
        print(f"Problem 2: {solve2(all_lines)}")
