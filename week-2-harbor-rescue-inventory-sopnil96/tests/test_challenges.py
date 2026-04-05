"""Week 2 starter code for Harbor Rescue Inventory."""

from __future__ import annotations

def mission_snapshot(items: list[object]) -> tuple[object | None, object | None]:
    """Return the first and last items in the list."""
    # If the list is empty, return (None, None)
    if not items:
        return (None, None)
    # Return a tuple of the first and last element
    return (items[0], items[-1])

def cargo_window(items: list[object], start: int, size: int) -> list[object]:
    """Return up to ``size`` items starting at index ``start``."""
    # If the start index is negative or beyond the list length, return empty
    if start < 0 or start >= len(items):
        return []
    # Return the slice from start to start + size
    return items[start : start + size]

def first_supply_index(items: list[object], target: object) -> int:
    """Return the index of the first occurrence of ``target``."""
    # Standard search: returns index if found, else -1
    try:
        return items.index(target)
    except ValueError:
        return -1

def supply_report(items: list[object], target: object) -> tuple[int, int]:
    """Return (count, first_index) for ``target`` in ``items``."""
    count = 0
    first_index = -1
    
    for i in range(len(items)):
        if items[i] == target:
            if first_index == -1:
                # Capture only the first time we see it
                first_index = i
            count += 1
            
    return (count, first_index)

def priority_load(items: list[object], urgent_item: object) -> list[object]:
    """Return a new list with ``urgent_item`` added at the front."""
    # STRETCH CHALLENGE: Do not mutate the original input list.
    # We create a brand new list with the item at index 0.
    return [urgent_item] + items