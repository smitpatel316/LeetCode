# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged = None
        curr = merged
        while l1 or l2:
            if l1 and l2:
                if merged is None:
                    if l1.val < l2.val:
                        merged = ListNode(l1.val)
                        l1 = l1.next
                    else:
                        merged = ListNode(l2.val)
                        l2 = l2.next
                    curr = merged
                else:
                    if l1.val < l2.val:
                        curr.next = ListNode(l1.val)
                        l1 = l1.next
                    else:
                        curr.next = ListNode(l2.val)
                        l2 = l2.next
                    curr = curr.next
            elif l1 and not l2:
                if merged is None:
                    merged = ListNode(l1.val)
                    l1 = l1.next
                    curr = merged
                else:
                    curr.next = ListNode(l1.val)
                    l1 = l1.next
                    curr = curr.next
            elif l2 and not l1:
                if merged is None:
                    merged = ListNode(l2.val)
                    l2 = l2.next
                    curr = merged
                else:
                    curr.next = ListNode(l2.val)
                    l2 = l2.next
                    curr = curr.next
        return merged
