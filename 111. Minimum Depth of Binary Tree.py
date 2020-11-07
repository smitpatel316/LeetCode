from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque([[root, 1]])
        while q:
            node, depth = q.popleft()
            if node.left is None and node.right is None:
                return depth
            if node.left:
                q.append([node.left, depth + 1])
            if node.right:
                q.append([node.right, depth + 1])
        return 0
