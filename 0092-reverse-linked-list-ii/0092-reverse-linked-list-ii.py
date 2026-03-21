# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        curr = head
        prev = None
        idx = 1
        
        while idx < left:
            prev = curr
            curr = curr.next
            idx += 1
        
        conn_node = prev
        tail = curr
        
        while idx <= right:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            idx += 1
        
        if conn_node:
            conn_node.next = prev
        else:
            head = prev
        
        tail.next = curr
        
        return head