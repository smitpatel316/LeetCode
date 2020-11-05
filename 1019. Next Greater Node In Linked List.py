# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return []
        _len = 0
        curr = head
        while curr:
            _len += 1
            curr = curr.next
        res = [0] * _len
        curr = head
        stack = []
        i = 0
        while curr:
            if not stack:
                stack.append([curr.val, i])
            else:
                while stack and stack[-1][0] < curr.val:
                    val, index = stack.pop()
                    res[index] = curr.val
                stack.append([curr.val, i])
            i += 1
            curr = curr.next
        return res
