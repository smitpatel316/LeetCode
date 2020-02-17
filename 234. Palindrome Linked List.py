# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        second_head = slow.next
        slow.next = None
        prev = None
        curr = second_head
        ahead = curr.next

        while curr is not None:
            curr.next = prev
            prev = curr
            curr = ahead
            if ahead is not None:
                ahead = ahead.next

        second_head.next = None

        right = prev
        left = head
        while right is not None:
            if left.val != right.val:
                return False
            right = right.next
            left = left.next
        return True
