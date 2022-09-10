# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list_head = ListNode()
        new_list_tail = new_list_head
        
        while list1 and list2:
            if list1.val < list2.val:
                new_list_tail.next = list1
                list1 = list1.next
            else:
                new_list_tail.next = list2
                list2 = list2.next
            new_list_tail = new_list_tail.next
            
        if list1:
            new_list_tail.next = list1
            new_list_tail = new_list_tail.next
        elif list2:
            new_list_tail.next = list2
            new_list_tail = new_list_tail.next
        new_list_head = new_list_head.next
        return new_list_head
            