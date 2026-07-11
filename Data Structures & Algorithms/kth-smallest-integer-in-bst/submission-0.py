# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr=[]
        def collect_nodes(node):
            if not node:
                return
            
            self.arr.append(node.val)

            collect_nodes(node.left)
            collect_nodes(node.right)
        collect_nodes(root)
        return sorted(self.arr)[k-1]