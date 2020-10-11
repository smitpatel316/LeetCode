from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.root = root
        self.items = deque([])
        self.inorder(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.items.popleft()

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.items) > 0

    def inorder(self, root):
        if not root:
            return
        if root.left:
            self.inorder(root.left)
        self.items.append(root.val)
        if root.right:
            self.inorder(root.right)


if __name__ == "__main__":
    t = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
    obj = BSTIterator(t)
    print(obj.items)
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
