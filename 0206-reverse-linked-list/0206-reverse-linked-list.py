# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        def reverse(node:ListNode, rev:ListNode=None):
            if not node:
                return rev
            next, node.next = node.next, rev
            return reverse(next, node)
        return reverse(head)
            
            
        