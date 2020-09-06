# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.pindex = 0

    def helper(self, start, end, preorder, imap) -> TreeNode:
        if start > end:
            return None

        root = TreeNode(preorder[self.pindex])
        self.pindex += 1
        index = imap.get(root.val)
        root.left = self.helper(start, index - 1, preorder, imap)
        root.right = self.helper(index + 1, end, preorder, imap)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        imap = {value: index for (index, value) in enumerate(inorder)}
        return self.helper(0, len(inorder) - 1, preorder, imap)


if __name__ == "__main__":

    def inorder_print(root):
        if root is not None:
            inorder_print(root.left)
            print(root.val)
            inorder_print(root.right)

    root2 = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    inorder_print(root2)
