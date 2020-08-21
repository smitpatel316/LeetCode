# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs_helper(node, path, _sum):
            if not node:
                return 0
            counter = 0 if node.val != _sum else 1
            for i, val in enumerate(path):
                if val + node.val == _sum:
                    counter += 1
                path[i] = val + node.val

            path.append(node.val)

            return counter + dfs_helper(node.left, path[:], _sum) + dfs_helper(node.right, path[:], _sum)
        return dfs_helper(root, [], sum)
