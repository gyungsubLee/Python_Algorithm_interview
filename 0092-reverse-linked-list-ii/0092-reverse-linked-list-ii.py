# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def toList(self,  head: Optional[ListNode])->List[int]:
        lst:List = []
        while head:
            lst.append(head.val)
            head = head.next
        return lst
    
    def swapInTwoPointer(self, left:int, right:int, lst:List[int])->List[int]:
        l,r = left-1, right-1
        while l < r:
            lst[l], lst[r] = lst[r], lst[l]
            l+=1
            r-=1
        return lst
    
    def toLinkedList(self, lst:List[int])->Optional[ListNode]:
        root = head = ListNode()
        for n in lst:
            head.next = ListNode(n)
            head = head.next
        return root.next
            
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # LinkedList -> List
        lst = self.toList(head)
        
        if len(lst) <2:
            return head
        
        return self.toLinkedList(self.swapInTwoPointer(left, right, lst))