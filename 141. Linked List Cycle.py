# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = []
        curr = head
        if head == None:
            return False
        while curr != None:
            if curr in seen:
                return True
            else:
                seen.append(curr)
                curr = curr.next
        return False
