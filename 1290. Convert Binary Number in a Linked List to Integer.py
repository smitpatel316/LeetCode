# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0
        _bin = ""
        curr = head
        while curr:
            _bin += str(curr.val)
            curr = curr.next
        return int(_bin, 2)
