# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoList(self, l1: ListNode, l2:ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoList(l1.next, l2)
        
        return l1 or l2
        
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        
        # 런너를 사용하여 중간 노드 찾기
        half, fast, slow = None, head, head
        while fast and fast.next:
            half = slow
            fast = fast.next.next
            slow = slow.next
        half.next = None
        
        # 분할 재귀호출
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        
        return self.mergeTwoList(l1, l2)