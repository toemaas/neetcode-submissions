# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in-order traversal gets us values in sorted order
        res = root.val
        cnt = k

        def dfs(node):
            if not node:
                return 0
            nonlocal res, cnt
            
            dfs(node.left)
            if cnt == 0:
                return res
            cnt -= 1
            if cnt == 0:
                res = node.val
            dfs(node.right)
        
        dfs(root)
        return res
