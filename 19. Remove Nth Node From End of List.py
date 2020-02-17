# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        behind = head
        ahead = head
        for i in range(n):
            ahead = ahead.next

        if not ahead:
            return behind.next

        while ahead.next:
            behind = behind.next
            ahead = ahead.next

        behind.next = behind.next.next
        return head