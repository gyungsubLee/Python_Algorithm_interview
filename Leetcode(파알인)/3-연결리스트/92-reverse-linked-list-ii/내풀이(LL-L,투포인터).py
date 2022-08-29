# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # LinkedList -> List
    def toList(self, head:ListNode)->ListNode:
        list:List = []
        node = head
        while node:
            list.append(node.val)
            node = node.next
        return list
    
    def swapInTwoPointer(self, left:int, right:int, lst:List)->List:
        # 투포인터 ->  스왑
        l, r = left-1, right-1
        while l < r:
            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r -= 1
            
        return lst
    
    def toLinkedList(self, list:List)->ListNode:
        # List -> LinkedList
        root = head = ListNode(0)
        for n in list:
            head.next = ListNode(n)
            head = head.next
        return root.next
        
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lst = self.toList(head)
        
        if len(lst) <2:
            return head
       
        return self.toLinkedList(self.swapInTwoPointer(left, right, lst))
         
        
            
        