import pytest

from src.aoc2021.day2.solution import solve1, solve2


@pytest.fixture
def input_example():
    return ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def test_example_input_problem1(input_example):
    assert solve1(input_example) == 150


def test_example_input_problem2(input_example):
    assert solve2(input_example) == 900
