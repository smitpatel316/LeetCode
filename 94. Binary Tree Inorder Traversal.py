# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        else:
            return (
                self.inorderTraversal(root.left)
                + [root.val]
                + self.inorderTraversal(root.right)
            )
