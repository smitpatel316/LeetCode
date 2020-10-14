# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if head.next is None:
            return head
        mid = head
        ahead = head.next
        while ahead and ahead.next:
            mid = mid.next
            ahead = ahead.next.next
        prev = mid
        if mid:
            mid = mid.next
        prev.next = None
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(mid)
        new_head = ListNode(0)
        curr = new_head
        while left_sorted and right_sorted:
            _next = ListNode()
            if left_sorted.val < right_sorted.val:
                _next.val = left_sorted.val
                left_sorted = left_sorted.next
            else:
                _next.val = right_sorted.val
                right_sorted = right_sorted.next
            curr.next = _next
            curr = curr.next
        while left_sorted:
            curr.next = ListNode(left_sorted.val)
            left_sorted = left_sorted.next
            curr = curr.next
        while right_sorted:
            curr.next = ListNode(right_sorted.val)
            right_sorted = right_sorted.next
            curr = curr.next
        return new_head.next
