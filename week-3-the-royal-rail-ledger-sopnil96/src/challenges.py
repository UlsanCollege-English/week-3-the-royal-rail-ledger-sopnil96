from __future__ import annotations

"""Week 3 homework: The Royal Rail Ledger.

Implement the required functions below.
Use stdlib only.
"""

class SLLNode:
    """Node for a singly linked list."""
    def __init__(self, value: int, next: SLLNode | None = None) -> None:
        self.value = value
        self.next = next


class SinglyLinkedList:
    """Simple singly linked list with a head reference."""
    def __init__(self) -> None:
        self.head: SLLNode | None = None


class DLLNode:
    """Node for a doubly linked list."""
    def __init__(
        self,
        value: int,
        prev: DLLNode | None = None,
        next: DLLNode | None = None,
    ) -> None:
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    """Simple doubly linked list with head and tail references."""
    def __init__(self) -> None:
        self.head: DLLNode | None = None
        self.tail: DLLNode | None = None


def build_sll_from_list(values: list[int]) -> SinglyLinkedList:
    """Build and return a singly linked list from a Python list."""
    sll = SinglyLinkedList()
    if not values:
        return sll

    sll.head = SLLNode(values[0])
    current = sll.head
    for value in values[1:]:
        current.next = SLLNode(value)
        current = current.next

    return sll


def sll_to_list(sll: SinglyLinkedList) -> list[int]:
    """Return all values from a singly linked list as a Python list."""
    result = []
    current = sll.head
    while current is not None:
        result.append(current.value)
        current = current.next
    return result


def find_first_repeat_sll(sll: SinglyLinkedList) -> int | None:
    """Return the first repeated value seen from left to right.
    Return None if no value repeats.
    """
    seen = set()
    current = sll.head
    while current is not None:
        if current.value in seen:
            return current.value
        seen.add(current.value)
        current = current.next
    return None


def remove_all_from_dll(dll: DoublyLinkedList, target: int) -> None:
    """Remove all nodes whose value equals target.
    Update dll.head and dll.tail correctly.
    """
    current = dll.head
    while current is not None:
        next_node = current.next  # Save before potentially removing
        
        if current.value == target:
            # Patch the previous node's next pointer
            if current.prev is not None:
                current.prev.next = current.next
            else:
                # This node was the head
                dll.head = current.next

            # Patch the next node's prev pointer
            if current.next is not None:
                current.next.prev = current.prev
            else:
                # This node was the tail
                dll.tail = current.prev

        current = next_node


def is_train_palindrome(dll: DoublyLinkedList) -> bool:
    """Stretch: return True if the DLL reads the same forward and backward."""
    if dll.head is None:
        return True

    left = dll.head
    right = dll.tail

    while left is not None and right is not None:
        if left.value != right.value:
            return False
            
        # Stop when the two pointers meet or cross
        if left is right:
            break
        left = left.next
        if left is right:
            break
        right = right.prev

    return True