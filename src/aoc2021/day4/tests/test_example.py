from pathlib import Path

import pytest

from src.aoc2021.day4.solution import parse_input, solve1, solve2


@pytest.fixture
def input_example():
    return Path(__file__).parent / "example.txt"


def test_problem1(input_example):
    assert solve1(*parse_input(input_example)) == 4512


def test_problem2(input_example):
    assert solve2(*parse_input(input_example)) == 1924
