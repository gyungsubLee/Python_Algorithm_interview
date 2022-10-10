# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head):
        # T: O(n), M: O(n)
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next= node.next
            node.next = prev
            return reverse(next, node)
        return reverse(head)


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(2)
l.next.next.next = ListNode(1)
print(Solution().reverseList(l))