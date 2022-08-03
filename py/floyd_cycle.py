from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next : Optional['ListNode'] = None


def has_cycle(head: Optional[ListNode]) -> bool:
    if not head:
        return False

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


def detect_cycle_start(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return False

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break

    if not fast or not fast.next:
        return None

    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return fast
