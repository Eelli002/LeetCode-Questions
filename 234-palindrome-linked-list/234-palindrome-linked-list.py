# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
            
        start = 0
        end = len(arr)-1
        while start <= end:
            if arr[start] != arr[end]:
                return False
            start += 1
            end -= 1
        return True