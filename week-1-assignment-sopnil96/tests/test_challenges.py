from __future__ import annotations

import pytest

from src.challenges import add, count_occurrences, is_even, last_index, linear_search


# -------------------------
# add
# -------------------------


def test_add_basic() -> None:
    assert add(2, 3) == 5


def test_add_with_zero() -> None:
    assert add(0, 0) == 0
    assert add(0, 7) == 7
    assert add(7, 0) == 7


def test_add_with_negatives() -> None:
    assert add(-1, 1) == 0
    assert add(-5, -6) == -11


# -------------------------
# is_even
# -------------------------


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, True),
        (1, False),
        (2, True),
        (7, False),
        (-4, True),
        (-3, False),
    ],
)
def test_is_even(n: int, expected: bool) -> None:
    assert is_even(n) is expected


# -------------------------
# linear_search
# -------------------------


def test_linear_search_found_middle() -> None:
    assert linear_search([10, 20, 30], 20) == 1


def test_linear_search_found_first() -> None:
    assert linear_search([99, 1, 2], 99) == 0


def test_linear_search_not_found() -> None:
    assert linear_search([1, 2, 3], 9) is None


def test_linear_search_empty() -> None:
    assert linear_search([], 1) is None


def test_linear_search_duplicates_returns_first() -> None:
    assert linear_search([5, 5, 5], 5) == 0
    assert linear_search([1, 2, 2, 2, 3], 2) == 1


def test_linear_search_non_int_types() -> None:
    assert linear_search(["a", "b", "c"], "c") == 2
    assert linear_search(["a", "b", "c"], "z") is None


# -------------------------
# count_occurrences
# -------------------------


def test_count_occurrences_basic() -> None:
    assert count_occurrences([1, 2, 2, 3], 2) == 2


def test_count_occurrences_empty() -> None:
    assert count_occurrences([], 7) == 0


def test_count_occurrences_not_present() -> None:
    assert count_occurrences([1, 2, 3], 9) == 0


def test_count_occurrences_strings() -> None:
    assert count_occurrences(["a", "b", "a", "a"], "a") == 3


def test_count_occurrences_generator() -> None:
    gen = (x % 3 for x in range(10))  # 0,1,2,0,1,2,0,1,2,0
    assert count_occurrences(gen, 0) == 4


# -------------------------
# last_index (stretch)
# -------------------------


def test_last_index_found_once() -> None:
    assert last_index([1, 2, 3], 2) == 1


def test_last_index_not_found() -> None:
    assert last_index([1, 2, 3], 9) is None


def test_last_index_empty() -> None:
    assert last_index([], 1) is None


def test_last_index_duplicates_returns_last() -> None:
    assert last_index([1, 2, 2, 2, 3], 2) == 3
    assert last_index([5, 5, 5], 5) == 2