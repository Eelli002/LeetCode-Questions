# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def Get_Tail(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head
        while head:
            tail = head
            head = head.next
        return tail
        
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        reversed_head = ListNode(None)
        reversed_pointer = reversed_head
        list_pointer = head
        tail = self.Get_Tail(head)
        while head.next:
            while list_pointer.next != tail:
                list_pointer = list_pointer.next
            reversed_pointer.next = tail
            reversed_pointer = reversed_pointer.next
            tail = list_pointer
            tail.next = None
            list_pointer = head
        
        reversed_pointer.next = head
        reversed_head = reversed_head.next
        return reversed_head