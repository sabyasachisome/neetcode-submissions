# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p and q and p.val==q.val:
            left_status= self.isSameTree(p.left, q.left)
            right_status= self.isSameTree(p.right, q.right)
            return (left_status and right_status)
        else:
            return False