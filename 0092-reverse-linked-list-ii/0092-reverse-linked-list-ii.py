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
        
        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode
        
        # left만큼 노드 전진
        for i in range(left - 1):
            pre = pre.next
        
        # [left, right] nodes 역순 재배치
        reverse = None
        cur = pre.next
        for i in range(right - left + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next

        pre.next.next = cur
        pre.next = reverse

        return dummyNode.next
