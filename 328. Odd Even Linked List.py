# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        odd_head = head
        even_head = head.next

        prev_odd = None

        curr_odd = odd_head
        curr_even = even_head

        on_odd = True
        curr = head
        while curr.next is not None:
            if on_odd:
                curr.next = curr.next.next
                prev_odd = curr_odd
                curr_odd = curr.next
                on_odd = False
                curr = curr_even
            else:
                curr.next = curr.next.next
                curr_even = curr.next
                on_odd = True
                curr = curr_odd

        if prev_odd.next is not None:
            prev_odd.next.next = even_head
        else:
            prev_odd.next = even_head
        return odd_head


if __name__ == "__main__":

    def list_ll(arr):
        head = ListNode(arr[0])
        curr = head
        for i in range(1, len(arr)):
            curr.next = ListNode(arr[i])
            curr = curr.next
        return head

    list_a = [1, 2, 3, 4, 5, 6, 7, 8]
    new_ll = Solution().oddEvenList(list_ll(list_a))
    while new_ll is not None:
        print(new_ll.val)
        new_ll = new_ll.next
