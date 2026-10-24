# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root, maxPast):
            if not root:
                return

            if root.val >= maxPast:
                self.res += 1
                maxPast = root.val

            dfs(root.left, maxPast)
            dfs(root.right, maxPast)


        dfs(root, -100)
        return self.res