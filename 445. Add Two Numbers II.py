# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = []
        s2 = []

        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next

        head = ListNode()
        total = 0
        while s1 or s2:
            if s1:
                total += s1.pop()
            if s2:
                total += s2.pop()
            head.val = total % 10
            _head = ListNode(total // 10)
            _head.next = head
            head = _head
            total //= 10
        return head.next if head.val == 0 else head


if __name__ == "__main__":
    l_1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
    l_2 = ListNode(5, ListNode(6, ListNode(4)))
    added = Solution().addTwoNumbers(l_1, l_2)
    while added:
        print(added.val)
        added = added.next
