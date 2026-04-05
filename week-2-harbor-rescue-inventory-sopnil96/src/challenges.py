"""Week 2 starter code for Harbor Rescue Inventory."""

from __future__ import annotations

def mission_snapshot(items: list[object]) -> tuple[object | None, object | None]:
    """Return the first and last items in the list."""
    if not items:
        return (None, None)
    return (items[0], items[-1])

def cargo_window(items: list[object], start: int, size: int) -> list[object]:
    """Return up to ``size`` items starting at index ``start``."""
    if start < 0 or start >= len(items) or size <= 0:
        return []
    return items[start : start + size]

def first_supply_index(items: list[object], target: object) -> int:
    """Return the index of the first occurrence of ``target``."""
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1

def supply_report(items: list[object], target: object) -> tuple[int, int]:
    """Return (count, first_index) for ``target`` in ``items``."""
    count = 0
    first_index = -1
    for i in range(len(items)):
        if items[i] == target:
            if first_index == -1:
                first_index = i
            count += 1
    return (count, first_index)

def priority_load(items: list[object], urgent_item: object) -> list[object]:
    """Return a new list with ``urgent_item`` added at the front."""
    # We create a new list so the original one doesn't change
    return [urgent_item] + items