# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode(0)
        
        while list1 and list2:
            if list1.val <= list2.val:
                head.next = ListNode(list1.val)
                list1, head = list1.next, head.next
            else:
                head.next = ListNode(list2.val)
                list2, head = list2.next, head.next
            
        if list1:
            head.next = list1
        if list2:
            head.next = list2
        
        return dummy.next
                
                
            