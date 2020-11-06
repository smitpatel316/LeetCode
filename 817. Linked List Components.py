# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        if not head:
            return 0
        g = set(G)
        curr = head
        res = 0
        while curr:
            if curr.val in g and getattr(curr.next, "val", None) not in g:
                res += 1
            curr = curr.next
        return res
