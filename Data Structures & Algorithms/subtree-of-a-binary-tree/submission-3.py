# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        
        if not root:
            return False
        
        if self.check_sametree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

        
        
    def check_sametree(self, tree1_node, tree2_node):
        if not tree1_node and not tree2_node:
            return True
        
        if tree1_node and tree2_node and tree1_node.val==tree2_node.val:
            return self.check_sametree(tree1_node.left, tree2_node.left) and self.check_sametree(tree1_node.right, tree2_node.right)
        
        return False