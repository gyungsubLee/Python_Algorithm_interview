# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # 풀이 1-1
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # T: O(n), M: O(1)
        prev, curr = None, head
        while curr:
            next, curr.next = curr.next, prev
            prev, curr = curr, next
        return prev

    # 풀이 1-2
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
        while head:
            rev, rev.next, head = head, rev, head.next
        return rev