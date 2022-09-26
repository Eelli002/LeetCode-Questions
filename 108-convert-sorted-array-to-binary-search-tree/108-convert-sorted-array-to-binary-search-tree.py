# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def BST(l, r):
            print(l, r)
            if l > r: return None
            mp = (l+r) // 2
            
            print(nums[mp])
            
            root = TreeNode(nums[mp])
            root.left = BST(l, mp-1)
            root.right = BST(mp+1, r)
            return root
        return BST(0, len(nums)-1)