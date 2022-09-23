# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        
        def Depth(root):
            nonlocal max_diameter
            if not root: return -1
            
            r_depth = Depth(root.right)
            l_depth = Depth(root.left)
    
            root_height = max(r_depth, l_depth) + 1
            root_diameter = r_depth + l_depth + 2
            max_diameter = max(root_diameter, max_diameter)
                
            return root_height
        
        Depth(root)
        
        return max_diameter