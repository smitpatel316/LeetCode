# Definition for a binary tree node.
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def dfs(root, parent=None):
            if root:
                root.parent = parent
                dfs(root.left, root)
                dfs(root.right, root)

        dfs(root)

        q = deque([(target, 0)])
        visited = {target}
        while q:
            if q[0][1] == K:
                return [node.val for node, _ in q]
            node, distance = q.popleft()
            for _next in (node.left, node.right, node.parent):
                if _next and _next not in visited:
                    q.append((_next, distance + 1))
                    visited.add(_next)
        return []
