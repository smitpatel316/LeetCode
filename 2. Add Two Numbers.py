# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        ptr = head
        curr1, curr2 = l1, l2
        while curr1 is not None and curr2 is not None:
            temp_sum = curr1.val + curr2.val
            new_node = None
            if temp_sum >= 10:
                new_node = ListNode(temp_sum - 10)
                if curr1.next is not None:
                    curr1.next.val += 1
                elif curr2.next is not None:
                    curr2.next.val += 1
                else:
                    curr1.next = ListNode(1)
            else:
                new_node = ListNode(temp_sum)

            if head is None:
                head = new_node
                ptr = head
            else:
                ptr.next = new_node
                ptr = ptr.next
            curr1 = curr1.next
            curr2 = curr2.next

        while curr1 is not None:
            new_node = None
            if curr1.val >= 10:
                new_node = ListNode(curr1.val - 10)
                if curr1.next is None:
                    curr1.next = ListNode(1)
                else:
                    curr1.next.val += 1
            else:
                new_node = ListNode(curr1.val)
            if head is None:
                head = new_node
                ptr = head
            else:
                ptr.next = new_node
                ptr = ptr.next
            curr1 = curr1.next

        while curr2 is not None:
            new_node = None
            if curr2.val >= 10:
                new_node = ListNode(curr2.val - 10)
                if curr2.next is None:
                    curr2.next = ListNode(1)
                else:
                    curr2.next.val += 1
            else:
                new_node = ListNode(curr2.val)
            if head is None:
                head = new_node
                ptr = head
            else:
                ptr.next = new_node
                ptr = ptr.next
            curr2 = curr2.next
        return head


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
