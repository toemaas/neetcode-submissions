# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and q or p and not q:
                return False
            elif not p and not q:
                return True
                
            left = isSameTree(p.left, q.left)
            right = isSameTree(p.right, q.right)

            if p.val == q.val and left and right:
                return True
            return False

        res = False
        
        def traversal(r):
            nonlocal res
            if not r:
                return
            traversal(r.left)
            if r.val == subRoot.val:
                if isSameTree(r, subRoot):
                    res = True
            traversal(r.right)

        traversal(root)

        return res
        
        
