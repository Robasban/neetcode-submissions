# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        minHeap = []
        heapq.heapify(minHeap)

        def dfs(root):
            if not root:
                return
            
            heapq.heappush(minHeap, -root.val)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
            
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return -minHeap[0]