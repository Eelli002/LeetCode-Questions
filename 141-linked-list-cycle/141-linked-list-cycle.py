# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None: return False
        dictionary = {}
        while head != None:
            if head in dictionary: return True
            dictionary[head] = 1
            head = head.next
        return False