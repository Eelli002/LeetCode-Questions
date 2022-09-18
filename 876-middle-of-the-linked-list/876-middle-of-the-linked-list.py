# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def Length(node):
            if not node: return 0
            length = 1
            while node.next:
                node = node.next
                length += 1
            return length
        
        length = Length(head)
        print(length)
        midpoint = length // 2
        for i in range(midpoint):
            head = head.next
        return head
        