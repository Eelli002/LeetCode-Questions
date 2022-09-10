# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None and list2 == None: return None
        elif list1 == None: return list2
        elif list2 == None: return list1
        else:
            if list1.val < list2.val:
                newList = ListNode(list1.val)
                list1 = list1.next
            else:
                newList = ListNode(list2.val)
                list2 = list2.next

            new_list_head = newList

            while list1 and list2:
                if list1.val < list2.val:
                    newList.next = ListNode(list1.val)
                    newList = newList.next
                    list1 = list1.next
                else:
                    newList.next = ListNode(list2.val)
                    newList = newList.next
                    list2 = list2.next

            if list1: newList.next = list1
            else: newList.next = list2

            return new_list_head