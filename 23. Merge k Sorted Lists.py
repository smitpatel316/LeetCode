# Definition for singly-linked list.
from typing import List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def __init__(self):
        self.heap = []

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        self.populate_heap(lists)
        head = ListNode()
        curr = head
        while self.heap:
            (val, index) = heapq.heappop(self.heap)
            curr.next = ListNode(val)
            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(self.heap, (lists[index].val, index))
            curr = curr.next
        return head.next

    def populate_heap(self, lists):
        for i, linked_list in enumerate(lists):
            if linked_list:
                heapq.heappush(self.heap, (linked_list.val, i))


if __name__ == "__main__":
    lls = [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6)),
    ]
    ll = Solution().mergeKLists(lls)
    while ll:
        print(ll)
        ll = ll.next
