# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # hashmap, where level is the key, value is value
        # traverse, keeping track of level
        # left to right, inorder traversal
        hm = {}
        def traversal(root: Optional[TreeNode], level: int):
            if not root:
                return
            if level not in hm:
                hm[level] = [root.val]
            else:
                hm[level].append(root.val)
            traversal(root.left, level + 1)
            traversal(root.right, level + 1)
        res = []
        traversal(root, 0)
        for sublist in hm:
            res.append(hm[sublist])
        return res