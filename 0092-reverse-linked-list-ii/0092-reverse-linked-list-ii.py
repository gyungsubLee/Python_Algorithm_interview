# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self,  head: Optional[ListNode], left:int, right:int)->List[int]:
        # 예외처리
        if left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        for i in range(left - 1):
            pre = pre.next
            
        rev = None
        cur = pre.next
        for i in range(right - left + 1):
            cur.next, rev, cur = rev, cur, cur.next
        
        pre.next.next = cur
        pre.next = rev
        
        return dummy.next