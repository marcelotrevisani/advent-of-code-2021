import pytest

from src.aoc2021.day3.solution import solve1, solve2


@pytest.fixture
def input_example():
    return [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]


def test_solve1(input_example):
    assert solve1(input_example) == 198


def test_solve2(input_example):
    assert solve2(input_example) == 230
