# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        prev = None
        curr = head
        ahead = curr.next
        while curr != None:
            curr.next = prev
            prev = curr
            curr = ahead
            if ahead != None:
                ahead = ahead.next
        return prev
