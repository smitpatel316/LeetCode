# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        curr = head
        ahead = head.next
        while curr and ahead and ahead.next:
            if curr == ahead:
                return True
            curr = curr.next
            ahead = ahead.next.next
        return False
