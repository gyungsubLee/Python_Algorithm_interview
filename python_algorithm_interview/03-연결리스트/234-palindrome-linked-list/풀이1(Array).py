# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q:List = []
        
        if not head:
            return False
        
        node = head
        while node:
            q.append(node.val)
            node = node.next
            
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        return True
        
        