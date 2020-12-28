# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode(-1)
        curr = head
        while l1 and l2:
            total = carry + l1.val + l2.val
            if total > 9:
                carry = 1
                total -= 10
            else:
                carry = 0
            curr.next = ListNode(total)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            total = carry + l1.val
            if total > 9:
                carry = 1
                total -= 10
            else:
                carry = 0
            curr.next = ListNode(total)
            curr = curr.next
            l1 = l1.next

        while l2:
            total = carry + l2.val
            if total > 9:
                carry = 1
                total -= 10
            else:
                carry = 0
            curr.next = ListNode(total)
            curr = curr.next
            l2 = l2.next
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next


def test_same_digits():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    added = Solution().addTwoNumbers(l1, l2)
    assert added.val == 7
    assert added.next.val == 0
    assert added.next.next.val == 8
    print("Test Same Digits: All Test Cases Passed")


def test_different_size():
    l1 = ListNode(1)

    l2 = ListNode(9)
    l2.next = ListNode(9)
    added = Solution().addTwoNumbers(l1, l2)
    while added is not None:
        print(added.val)
        added = added.next


if __name__ == "__main__":
    test_same_digits()
    test_different_size()
