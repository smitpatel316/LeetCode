# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return None
        self.helper(root, None)
        return root

    def helper(self, node, next_right):
        if not node:
            return
        if next_right:
            node.next = next_right
            self.helper(node.left, node.right)
            self.helper(node.right, next_right.left)
        else:
            self.helper(node.right, None)
            self.helper(node.left, node.right)


if __name__ == "__main__":
    t = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    r = Solution().connect(t)
    print(r)
