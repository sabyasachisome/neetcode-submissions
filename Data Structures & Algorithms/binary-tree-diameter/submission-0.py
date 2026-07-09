# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter=0
        def dfs_depth(node):
            if node is None:
                return 0
            left_height= dfs_depth(node.left)
            right_height= dfs_depth(node.right)

            diameter= (left_height+right_height)
            self.max_diameter= max(diameter,self.max_diameter)

            return 1+max(left_height, right_height)
            
        dfs_depth(root)
        return self.max_diameter