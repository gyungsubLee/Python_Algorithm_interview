# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst:List = []
        
        node = head
        while node:
            lst.append(node.val)
            node = node.next
        
        lst.sort()
        
        node = head
        for i in range(len(lst)):
            node.val = lst[i]
            node = node.next
        
        return head
        
        