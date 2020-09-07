# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def __str__(self):
        return f"{self.val}"


class Solution:
    def flatten(self, head: "Node") -> "Node":
        if head is None:
            return None
        return self.flatten_helper(head)[0]

    def flatten_helper(self, head: "Node"):
        if not head:
            return None
        else:
            curr = head
            prev = None
            while curr is not None:
                if curr.child is not None:
                    flattened_child, tail = self.flatten_helper(curr.child)
                    _next = curr.next
                    curr.next = flattened_child
                    if flattened_child is not None:
                        flattened_child.prev = curr
                    if tail is not None:
                        tail.next = _next
                    if _next is not None:
                        _next.prev = tail

                    curr.child = None
                prev = curr
                curr = curr.next
            return head, prev


if __name__ == "__main__":
    list_1 = [1, 2, 3, 4, 5, 6]
    list_2 = [7, 8, 9, 10]
    list_3 = [11, 12]

    def generate(lista):
        h = Node(lista[0])
        curr = h
        for i in range(1, len(lista)):
            n = Node(lista[i])
            curr.next = n
            n.prev = curr
            curr = curr.next
        return h

    list_1 = generate(list_1)
    list_2 = generate(list_2)
    list_3 = generate(list_3)
    list_1.next.next.child = list_2
    list_2.next.child = list_3

    head = Solution().flatten(list_1)

    while head is not None:
        print(head.val)
        head = head.next
