"""
Week 1 — Intro Challenges

Rules:
- Implement the functions below.
- Do NOT change function names or parameters (tests depend on them).
- Keep solutions readable and simple.
- Stdlib only.

Tip:
Run tests from repo root:
    pytest -q
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from typing import Optional, TypeVar

T = TypeVar("T")


def add(a: int, b: int) -> int:
    """
    Return the sum of two integers.

    Examples:
        add(2, 3) -> 5
        add(-1, 1) -> 0

    Complexity:
        Time: O(1)
        Space: O(1)
    """
    # TODO: implement
    raise NotImplementedError


def is_even(n: int) -> bool:
    """
    Return True if n is even, otherwise False.

    Notes:
    - Works for negative numbers too (Python's % handles this nicely).

    Examples:
        is_even(0) -> True
        is_even(7) -> False
        is_even(-4) -> True

    Complexity:
        Time: O(1)
        Space: O(1)
    """
    # TODO: implement
    raise NotImplementedError


def linear_search(nums: Sequence[T], target: T) -> Optional[int]:
    """
    Return the FIRST index where target appears in nums, or None if not found.

    Examples:
        linear_search([10, 20, 30], 20) -> 1
        linear_search([1, 2, 3], 9) -> None
        linear_search([5, 5, 5], 5) -> 0

    Edge cases:
    - empty list/sequence
    - duplicates (must return first match)
    - target not present

    Complexity:
        Time: O(n) worst-case
        Space: O(1)
    """
    # TODO: implement
    raise NotImplementedError


def count_occurrences(items: Iterable[T], target: T) -> int:
    """
    Count how many times target appears in items.

    Examples:
        count_occurrences([1, 2, 2, 3], 2) -> 2
        count_occurrences([], 7) -> 0

    Notes:
    - items is an Iterable: it might be a list, tuple, set, generator, etc.

    Complexity:
        Time: O(n)
        Space: O(1)
    """
    # TODO: implement
    raise NotImplementedError


# Stretch (optional)
def last_index(nums: Sequence[T], target: T) -> Optional[int]:
    """
    Return the LAST index where target appears in nums, or None if not found.

    Examples:
        last_index([1, 2, 2, 3], 2) -> 2
        last_index([1, 2, 3], 9) -> None
        last_index([], 1) -> None

    Complexity:
        Time: O(n)
        Space: O(1)
    """
    # TODO: implement
    raise NotImplementedError