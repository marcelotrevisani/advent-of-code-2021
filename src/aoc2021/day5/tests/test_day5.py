from pathlib import Path

import pytest

from src.aoc2021.day5.solution import read_input, clean_input, solve1, solve2


@pytest.fixture
def example_input():
    return Path(__file__).parent / "example.txt"


def test_parse_input(example_input):
    assert read_input(example_input) == [
        (0, 9, 5, 9),
        (8, 0, 0, 8),
        (9, 4, 3, 4),
        (2, 2, 2, 1),
        (7, 0, 7, 4),
        (6, 4, 2, 0),
        (0, 9, 2, 9),
        (3, 4, 1, 4),
        (0, 0, 8, 8),
        (5, 5, 8, 2),
    ]


def test_clean_input(example_input):
    lines = read_input(example_input)
    assert clean_input(lines) == [
        (0, 9, 5, 9),
        (9, 4, 3, 4),
        (2, 2, 2, 1),
        (7, 0, 7, 4),
        (0, 9, 2, 9),
        (3, 4, 1, 4),
    ]

def test_example_solve1(example_input):
    assert solve1(clean_input(read_input(example_input))) == 5


def test_example_solve2(example_input):
    assert solve2(read_input(example_input)) == 12
