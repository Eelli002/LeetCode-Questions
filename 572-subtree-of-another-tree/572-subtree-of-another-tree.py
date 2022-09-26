# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Is_Same(self, r, sr):
            if not r and not sr: return True
            if not r or not sr or r.val != sr.val: return False
            return (self.Is_Same(r.left, sr.left) and self.Is_Same(r.right, sr.right))
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: 
            return False
                
        if root.val == subRoot.val and self.Is_Same(root, subRoot): 
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)